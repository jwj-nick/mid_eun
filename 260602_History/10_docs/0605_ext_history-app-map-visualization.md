# History App — Map Visualization Strategy
> Claude Code reference doc | history-app project

---

## 1. 에피소드 유형 분류 (4 Types)

| Type | 레이블 | 예시 | 핵심 표현 |
|------|--------|------|-----------|
| **A** | 영토/세력권 | 몽골제국 최대 영토, 로마 제국 | 면적 채색 + 경계 변화 |
| **B** | 전쟁/전투 | 임진왜란 진격로, 노르망디 | 루트 애니메이션 + 마커 |
| **C** | 교역/이동 | 실크로드, 대항해시대 | 선 경로 + 흐름 표현 |
| **D** | 문화/종교 전파 | 불교 전파, 이슬람 확산 | 확산 애니메이션 |

---

## 2. 기술 스택 선택 기준

### Type A, B → **Mapbox GL JS** (권장)
- 벡터 렌더링 → 확대해도 선명
- 커스텀 스타일로 고지도 질감 구현 가능
- 3D 지형 표현 (산악 전투 등)
- 스타일 JSON으로 시대감 있는 배경 제작 가능

### Type C, D → **Leaflet.js + D3.js**
- D3 흐름 애니메이션 강점 (force, path animation)
- 교역량·전파 속도를 데이터 시각화로 표현
- 경량, 오픈소스

---

## 3. 공통 아키텍처

```
┌─────────────────────────────────┐
│  에피소드 데이터 (JSON)           │  ← 에피소드별 교체 대상
├─────────────────────────────────┤
│  지도 엔진 레이어                 │  ← Mapbox or Leaflet (Type별 고정)
├─────────────────────────────────┤
│  GeoJSON 영토 데이터              │  ← Natural Earth + 시대별 커스텀
├─────────────────────────────────┤
│  타임라인 슬라이더 UI             │  ← 공통 컴포넌트 (재사용)
├─────────────────────────────────┤
│  Claude API (해설 생성)           │  ← 마커/영역 클릭 시 동적 생성
└─────────────────────────────────┘
```

**원칙: 엔진·UI는 고정, 데이터(JSON)만 에피소드별 교체**

---

## 4. 에피소드 데이터 구조 (JSON 스키마 제안)

```json
{
  "episode": {
    "id": "mongol-empire-peak",
    "type": "A",
    "title": "몽골 제국의 최대 강역 (1279)",
    "period": { "start": 1206, "end": 1368 },
    "engine": "mapbox"
  },
  "timeline": [
    {
      "year": 1206,
      "label": "칭기즈칸 즉위",
      "territories": ["mongolia"],
      "events": [
        { "lat": 47.9, "lng": 106.9, "label": "쿠릴타이 개최" }
      ]
    },
    {
      "year": 1279,
      "label": "최대 강역",
      "territories": ["mongolia", "china", "persia", "russia-steppe"],
      "events": []
    }
  ],
  "colorMap": {
    "mongolia": "#C0392B",
    "china": "#E74C3C"
  }
}
```

---

## 5. 지도 데이터 소스

| 소스 | 용도 | 비용 | 비고 |
|------|------|------|------|
| [Natural Earth](https://www.naturalearthdata.com/) | 국경 shapefile → GeoJSON 변환 | 무료 | 해상도 1:10m 권장 |
| [Geacron](http://geacron.com/) | 연도별 영토 데이터 API | 유료 | 완성도 높음 |
| [David Rumsey Map Collection](https://www.davidrumsey.com/) | 고지도 타일 (WMTS) | 무료 | 배경 타일용 |
| Wikipedia/Wikimedia | SVG 역사 지도 | 무료 | 제한적 |

---

## 6. 시각 품질 3요소

1. **배경 타일**
   - Mapbox 커스텀 스타일 (고지도 질감)
   - Stamen Watercolor (수채화풍, 고대 에피소드)
   - David Rumsey WMTS 타일

2. **영토 색상 팔레트**
   - 시대별 제국마다 고유 컬러 시스템 사전 정의
   - 투명도(opacity) 0.6~0.8로 지형 보이게 유지

3. **전환 애니메이션**
   - 연도 슬라이더 드래그 → 영토 부드럽게 morph
   - Mapbox: `setPaintProperty` + CSS transition
   - Leaflet: layer swap + fade

---

## 7. Mapbox 기본 구현 패턴 (Type A)

```javascript
// 영토 레이어 추가
map.addLayer({
  id: 'territory-fill',
  type: 'fill',
  source: {
    type: 'geojson',
    data: historicalGeoJSON  // 연도별 GeoJSON
  },
  paint: {
    'fill-color': ['get', 'color'],  // feature.properties.color
    'fill-opacity': 0.65
  }
});

// 타임라인 슬라이더 연동
slider.addEventListener('input', (e) => {
  const year = parseInt(e.target.value);
  const data = getGeoJSONByYear(year);  // 에피소드 JSON에서 로드
  map.getSource('territory-fill').setData(data);
});
```

---

## 8. Claude API 연동 패턴

```javascript
// 마커 클릭 → Claude 해설 생성
marker.on('click', async (feature) => {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 300,
      messages: [{
        role: 'user',
        content: `중학생 대상으로 "${feature.label}" 사건을 3문장으로 설명해줘. 연도: ${feature.year}`
      }]
    })
  });
  const data = await res.json();
  showPopup(feature, data.content[0].text);
});
```

---

## 9. 개발 우선순위 제안

```
Phase 1: Type A 단일 에피소드 (영토)
  → Mapbox + GeoJSON + 슬라이더 기본 동작 확인

Phase 2: Claude API 팝업 해설 연동

Phase 3: Type B 전투/전쟁 루트 추가

Phase 4: 에피소드 JSON 스키마 확정 후 시리즈화
```

---

*생성: Claude Sonnet (claude.ai) | 프로젝트: history-app*

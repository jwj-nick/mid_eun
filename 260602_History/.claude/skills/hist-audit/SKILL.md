---
name: hist-audit
description: 완성된 에피소드를 다중 페르소나로 감수하고 위반을 수정한다. 역사학자(사실)·교사(수위·톤·중1 눈높이)·균형심판(탈서구중심·논쟁 균형)·편집자(APP_PRINCIPLES·접근성) 관점으로 점검. 호출 예시 — "/hist-audit ww2", "제국주의 감수".
allowed-tools: Read, Write, Edit, Bash, WebSearch, Agent
metadata:
  project: 260602_History
  stage: 5 감수
  ssot: APP_PRINCIPLES.md, 00_project_hub/plan/260603_history_hub_master_plan.md
  status: seed
---

# hist-audit — 다중 페르소나 감수 (단계 5)

배포 전 품질 게이트. math-story-telling의 se-audit-* 통합판. 4개 페르소나(병렬 Agent 가능).

> **범위 = 에피소드(`30_content/<slug>/episode.json`).** 인물 도감(people) 페이지는 이 스킬이 아니라 **`hist-person` + `10_docs/PEOPLE_GUIDE.md` §4 인물 audit 체크리스트**로 감수한다.

## 입력
- `30_content/<slug>/episode.json` + `50_app/<slug>/index.html` + `20_research/<slug>/`

## 페르소나 점검
1. **역사학자** — 날짜·인명·인과 정확성, 단정 vs 추정 표기. 리서치 출처와 대조.
2. **교사(중1)** — 어휘·문장 길이·잔혹/정치 수위, 어려운 말 풀이 여부, 흥미 유지.
3. **균형심판** — 탈서구중심(비서구·약소국 자리 있나), 논쟁 균형("이런 시각도"), "그때의 생각" 렌즈 적절성, 인물 영웅화 금지.
4. **편집자** — APP_PRINCIPLES(여는 장면·빈칸·톤), 접근성(대비·터치타깃·모바일), 영상 링크 정책(video/search), 인용 출처·저작권.

## 동작
- 각 페르소나가 위반 목록 작성 → 심각도 분류 → **데이터(episode.json) 수정** → 재빌드 → 재확인. (앱 직접수정 아닌 데이터 수정 우선)

## 출력
- `20_research/<slug>/audit.md` (발견·수정 내역) + 수정 반영된 episode.json/앱

## 블록별 점검 (누적)
- **S0 서사·정서 레이어**: 미스터리 훅이 **사실을 왜곡·과장(낚시)하지 않나**? 편지/단서 프롬프트가 감정·상상 영역이라 사실 단정 없나? 또래 묘사가 **확인된 인물 또는 일반화된 또래**이고 날조·영웅화 아닌가? 탐정 프레이밍이 가벼움으로 비극의 무게를 해치지 않나?
- **quiz**: 정답(`answer` 인덱스) 정확? 보기·해설 사실/수위 OK? 오답도 모욕적이지 않게? 정답 강요 톤 아님?
- **notes-export**: 인쇄/복사 동작, 빈 메모 안내, 로컬 저장(개인정보 외부전송 없음) 확인.
- **map**: **실제 지도(Leaflet+OSM)** — 마커 좌표·라벨 정확? caption에 "현재 지도 위 표시" 명시(옛 국경 오해 방지)? 팝업 동작? 지리 단정 회피?
- **voice** (S3): `imagined:false`면 인용·출처 정확한가(날조 아님)? `imagined:true`면 배지로 '상상'임이 분명하고 source에 근거가 있나? 1인칭 내용이 사실을 왜곡하지 않나? 중1 수위 OK?
- **chart** (S4): 수치·연도 출처 있나(불확실하면 '대략값' 표기)? 막대 비율이 값과 맞나? `relatable` 비유가 과장 아닌가? 축/단위 오해 없나?
- **compare** (S5): 각 상태(state) 내용이 사실 정확? 단계 순서·연도 맞나? `img` 있으면 PD/CC·출처 표기? 비교가 한쪽을 부당하게 미화/폄하하지 않나?
- **choice** (S7): 선택지가 균형 잡혔나(어느 쪽도 단정·폄하 X)? 해설이 사실 기반이고 역사 왜곡 없나? 중1에게 과한 도덕 압박 아닌가? `after`가 '정답 없음'을 분명히 하나?
- **image** (S1): 라이선스 **PD 또는 명확한 CC**인가(출처·라이선스 표기 확인)? alt 텍스트 있나(접근성)? caption이 지도 내용을 과장·왜곡하지 않나? `src`가 `img/` 상대경로이고 자산이 `30_content/<slug>/img/`에 실재하나(빌드 복사 확인)? hotspot 좌표가 엉뚱한 곳 아닌가?

## 품질 게이트 (통과해야 배포)
- [ ] 사실 오류 0 (또는 정정 완료)
- [ ] 수위·톤 중1 적합
- [ ] 비서구 관점·논쟁 균형 확인
- [ ] **각 섹션 대표 이미지 ≥2 (건물·명화·기념물·아이콘·상징; map/battlemap/chart 제외)** — 부족 시 hist-visuals 보강
- [ ] APP_PRINCIPLES·접근성·링크정책 통과
- [ ] (해당 시) quiz 정답·해설 정확, notes-export 동작

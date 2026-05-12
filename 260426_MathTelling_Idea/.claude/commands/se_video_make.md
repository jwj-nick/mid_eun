# /se_video_make — MathTelling 영상 제작 파이프라인

수학 개념 설명 영상(MP4, 1280×720)을 처음부터 끝까지 만든다.
**나레이션 스크립트 → TTS 오디오 → GSAP 애니메이션 HTML → HyperFrames 렌더 → FFmpeg 합성**

---

## 인수 파싱

`$ARGUMENTS` 형식: `unit=## concept=slug person=이름 duration=초`

예시:
- `/se_video_make unit=01 concept=sieve person=에라토스테네스 duration=30`
- `/se_video_make unit=03 concept=balance_scale person=알콰리즈미 duration=40`
- `/se_video_make` (인수 없으면 STAGE 1에서 사용자에게 확인)

`resume=stageN` 인수가 있으면 Stage N 이전을 건너뛰고 기존 파일에서 이어 시작한다.

---

## 사전 확인

실행 전 아래를 체크한다. 실패 시 해당 줄에 설치 방법을 알려주고 중단한다.

```powershell
ffmpeg -version 2>&1 | Select-String "ffmpeg version"
python -m edge_tts --version 2>&1 | Select-Object -First 1
hyperframes --version 2>&1 | Select-Object -First 1
```

---

## STAGE 1 — 개념 선택

`unit`과 `concept`이 인수에 있으면 건너뛴다.

없으면:
1. `20_research/02_R2-people-map.md`를 읽어 인물-단원 매핑을 표시한다.
2. 사용자에게 다음 4가지를 확인한다:
   - 단원 번호 (예: 01)
   - 개념 슬러그 (아래 표 참조)
   - 인물명
   - 목표 영상 길이 (초)

**Visual Type 표** (concept → 시각 유형 → 템플릿):

| concept 슬러그 | visual_type | 설명 |
|---|---|---|
| sieve | number-grid | 숫자 그리드, 합성수 제거 |
| prime_factorization | number-grid | 소인수분해 트리 |
| number_line | number-line | 수직선 위 양수/음수 이동 |
| balance_scale | balance-scale | 양팔 저울 이항 시각화 |
| coordinate | coordinate-plane | 좌표축과 점/선 등장 |
| proportional | coordinate-plane | y=ax 그래프 |
| inversely_proportional | coordinate-plane | y=a/x 쌍곡선 |
| bar_chart | bar-chart | 막대/코크스콤 차트 |
| geometry | geometry-sketch | 점→선→각→도형 |

매핑이 불명확하면 사용자에게 확인한다.

출력 디렉토리를 설정한다:
`OUTDIR = c:\Kids\30_MiddleSchool\260426_MathTelling_Idea\90_video\unit{unit}\{concept}`

OUTDIR 디렉토리를 생성한다 (없으면).

---

## STAGE 2 — 나레이션 스크립트 작성

목표 파일: `{OUTDIR}/narration.txt`

### 스크립트 분량 기준
한국어 TTS 기준 분당 약 300자 → 목표 길이(초) × 5자
예: 30초 영상 → 약 150자 (문장 부호 포함)

### 구조 (5단계)
1. **도입** (1~2문장): 인물 등장, 시대·장소
2. **문제 제기** (1~2문장): 이 인물이 왜 이 개념이 필요했나
3. **발견의 순간** (2~3문장): 핵심 아이디어 — **애니메이션과 동기화되는 부분**
4. **개념 설명** (1~2문장): 수학적 내용을 이야기 언어로
5. **마무리** (1문장): 현대적 연결 또는 인물의 메시지

### 참조 문서
스크립트 작성 전 읽을 파일:
- `20_research/02_R2-people-map.md` — 해당 인물 섹션
- `50_stories/unit{unit}_{단원명}/unit{unit}.md` — 기존 이야기 (있으면)
- `10_docs/01_learner-profile.md` — 딸의 눈높이 확인

스크립트를 `{OUTDIR}/narration.txt`에 저장한다.

**사용자에게 검토를 요청한다. 승인 후 Stage 3으로 진행한다.**

---

## STAGE 3 — TTS 오디오 생성

```powershell
python -m edge_tts `
  --voice ko-KR-SunHiNeural `
  --file "{OUTDIR}\narration.txt" `
  --write-media "{OUTDIR}\narration.mp3"
```

생성 후 실제 오디오 길이를 측정한다:
```powershell
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "{OUTDIR}\narration.mp3"
```

이 값을 `AUDIO_DURATION`으로 저장한다. 이후 모든 단계는 이 값을 기준으로 한다.

목표 길이와 ±3초 이상 차이 나면:
- 너무 길면: 스크립트를 줄여 Stage 2부터 재실행
- 너무 짧으면: 스크립트에 설명 추가 후 Stage 2부터 재실행

---

## STAGE 4 — 시각적 컴포지션 HTML 작성

목표 파일: `{OUTDIR}/index.html`

### 4A: 템플릿 로드
`90_video/_templates/{visual_type}.html`을 읽는다.

### 4B: 플레이스홀더 교체

| 플레이스홀더 | 교체 내용 |
|---|---|
| `{{TITLE}}` | 개념 제목 (예: "에라토스테네스의 체") |
| `{{SUBTITLE}}` | 인물·시대 한 줄 |
| `{{DURATION}}` | AUDIO_DURATION 값 (반올림 정수 + 1) |
| `{{COMPOSER_ID}}` | concept 슬러그 |
| `{{DATA_SECTION}}` | 개념별 DOM 요소 (숫자, 라벨 등) |
| `{{TIMELINE_SECTION}}` | GSAP 타임라인 코드 |

### 4C: 타임라인 동기화

narration.txt를 문단별로 나누고 각 문단이 시작하는 시각(초)을 추정한다.

추정 공식: `문단 시작 시각 = 이전 문단들 문자 수 합계 / 총 문자 수 × AUDIO_DURATION`

이 타이밍을 기준으로 GSAP `tl.to()` 절대 시간값을 결정한다.

**모든 유형에 적용되는 필수 패턴**:
```javascript
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
tl.from('#root', { opacity: 0, duration: 0.5 }, 0);
// ... (유형별 코드)
window.__timelines['{{COMPOSER_ID}}'] = tl;
```

**`tl.call()`은 사용하지 않는다** — HyperFrames가 seek 시 콜백을 발동하지 않음.
텍스트 교체는 항상 여러 div를 미리 만들고 opacity로 전환한다.

### 4D: 파일 저장

완성된 HTML을 `{OUTDIR}/index.html`에 저장한다.

HyperFrames 루트 요소 확인:
```html
<div id="root"
  data-composition-id="{{COMPOSER_ID}}"
  data-start="0"
  data-duration="{{DURATION}}"
  data-width="1280"
  data-height="720">
```

---

## STAGE 5 — HyperFrames 렌더링

```powershell
hyperframes render "{OUTDIR}" -o "{OUTDIR}\raw.mp4" -f 24 -q standard
```

완료 확인:
```powershell
Test-Path "{OUTDIR}\raw.mp4"
```

**실패 시 체크리스트**:
- `data-composition-id` 값이 `window.__timelines[키]`와 일치하는가
- `data-duration`이 숫자(문자열 아님)인가
- GSAP CDN 스크립트 태그가 있는가
- `window.__timelines` 등록이 스크립트 최하단에 있는가

---

## STAGE 6 — FFmpeg 오디오 합성

```powershell
ffmpeg -y `
  -i "{OUTDIR}\raw.mp4" `
  -i "{OUTDIR}\narration.mp3" `
  -map 0:v -map 1:a `
  -c:v copy -c:a aac `
  -shortest `
  "{OUTDIR}\final.mp4"
```

완료 확인:
```powershell
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "{OUTDIR}\final.mp4"
```

---

## 완료 보고

다음 내용을 출력한다:

```
[se_video_make 완료]
단원: unit{unit} · {concept}
인물: {person}
영상 길이: {AUDIO_DURATION}초
출력: {OUTDIR}\final.mp4

권장 다음 작업:
- final.mp4 재생 → 나레이션과 애니메이션 동기화 확인
- 수정 필요 시: narration.txt 편집 후 /se_video_make resume=stage3
- 완성 시 worklog에 결과 기록
```

---

## 에러 핸들링 요약

| 증상 | 원인 | 조치 |
|---|---|---|
| edge-tts 오류 | 미설치 또는 네트워크 | `python -m pip install edge-tts` |
| HyperFrames exit code 9 | 정상 종료 (exit code 9 = 완료를 의미) | `Test-Path raw.mp4`로 파일 존재 확인 |
| 오디오 없는 MP4 | FFmpeg map 오류 | `ffprobe final.mp4`로 Audio stream 확인 |
| 한글 폰트 깨짐 | 폰트 미매핑 | `index.html`에 Noto Sans KR CDN 링크 확인 |
| 영상이 너무 빨리 끝남 | GSAP 타이밍이 AUDIO_DURATION보다 짧음 | `data-duration` 값 증가 후 Stage 5 재실행 |

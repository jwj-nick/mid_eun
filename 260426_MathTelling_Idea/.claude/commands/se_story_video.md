# /se_story_video — Story 영상 제작 파이프라인

> 단원별 Story 영상(50초, 1280×720, MP4)을 처음부터 끝까지 만든다.
> 인물 서사 중심 5장면 구조. 마스터 템플릿 + 단원 데이터 주입 방식.
> 기존 `se_video_make`는 Concept 영상용. 이 스킬은 Story 영상 전용.

---

## 인수 파싱

`$ARGUMENTS` 형식: `unit=NN` (필수)

예시:
- `/se_story_video unit=01`
- `/se_story_video unit=07`
- `/se_story_video unit=01 resume=stage4` (Stage 4부터 이어 진행)

---

## 사전 확인

```bash
ffmpeg -version 2>&1 | head -1
python -m edge_tts --version 2>&1 | head -1
hyperframes --version 2>&1 | head -2
```

모두 설치되어 있어야 진행. 없는 경우 안내 후 중단.

참조 문서 (선행 읽기):
- `90_video/_docs/STORY_VIDEO_GUIDE.md` — 단일 진실 원본
- `90_video/_templates/story-master.html` — 마스터 템플릿
- `90_video/_assets/palettes.css` — 단원별 컬러

---

## STAGE 1 — 단원 정보 수집

`unit` 인수에서 단원 번호를 받아 다음을 수집한다.

1. `50_units/NN_단원명/story.html` — 인물·시대·서사 흐름 확인
2. `50_units/NN_단원명/story/unitNN.md` — 인물 원문 텍스트
3. `20_research/02_R2-people-map.md` — R2 인물 자료 (해당 인물 섹션)
4. `10_docs/01_learner-profile.md` — 학습자 톤 확인
5. `90_video/_docs/STORY_VIDEO_GUIDE.md` — 표준 명세

산출물:
```
OUTDIR = 90_video/unitNN/
```

OUTDIR 디렉토리 생성 (없으면).

---

## STAGE 2 — 스토리보드 작성

목표 파일: `{OUTDIR}/storyboard.md`

### 작성 형식

```markdown
# Unit NN — 인물명 Story 영상 스토리보드

## 메타
- 인물: {인물명}
- 시대·장소: {시대 + 도시/지역}
- 단원: Unit NN — {단원명}
- 톤 키워드: {팔레트 톤 — STORY_VIDEO_GUIDE.md §4.3}
- 목표 길이: 50초

## Scene 1 (0~5s) 타이틀
- 텍스트: {인물명} / {시대·장소} / Unit NN — {단원명}
- 시각: 정적 배경 + 페이드 인
- 나레이션 (20~25자): "..."

## Scene 2 (5~15s) 인물 등장
- 헤드라인: {1줄 인물 한 마디}
- 본문: {2~3줄 인물 소개}
- 심볼: {symbol.svg} (이유: ...)
- 나레이션 (45~55자): "..."

## Scene 3 (15~32s) 결정적 순간
- 키워드: {핵심 한 단어/구절}
- 메타포 SVG: {symbol.svg}
- 설명: {1~2줄 발견·문제}
- 나레이션 (80~90자): "..."

## Scene 4 (32~45s) 수학과의 연결
- 헤드라인: {예: "오늘 우리는..."}
- 다이어그램 SVG: {symbol.svg}
- 설명: {수학 연결}
- 나레이션 (60~70자): "..."

## Scene 5 (45~50s) 마무리
- 한 문장: "이 단원에서, 그를 만나봅시다"
- 나레이션 (20~25자): "..."

## 총 분량
- 합계 글자수: 약 245자 (한국어 TTS 5자/초 × 50초 = 250자 ± 20)
```

---

## STAGE 3 — Narration 추출

스토리보드의 5개 나레이션을 줄 단위로 모아 `{OUTDIR}/narration.txt`에 저장.
빈 줄로 장면 구분 (TTS는 빈 줄에서 자연스럽게 호흡).

```
{S1 narration}

{S2 narration}

{S3 narration}

{S4 narration}

{S5 narration}
```

---

## STAGE 4 — TTS 오디오 생성

```bash
python -m edge_tts \
  --voice ko-KR-SunHiNeural \
  --file "{OUTDIR}/narration.txt" \
  --write-media "{OUTDIR}/narration.mp3"
```

길이 측정:
```bash
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "{OUTDIR}/narration.mp3"
```

`AUDIO_DURATION` 변수에 저장. 45~55초 범위 확인.
범위 밖이면 STAGE 2로 돌아가 스토리보드 분량 조정.

---

## STAGE 5 — 시각 컴포지션

목표 파일: `{OUTDIR}/index.html`

### 5A: 마스터 템플릿 로드

`90_video/_templates/story-master.html` 읽기.

### 5B: 단원별 placeholder 교체

| placeholder | 값 |
|---|---|
| `{{UNIT_NN}}` | `unit-NN` (예: `unit-01`) |
| `{{COMPOSITION_ID}}` | `story-unitNN` |
| `{{DURATION}}` | `Math.ceil(AUDIO_DURATION) + 1` |
| `{{PERSON}}` | 인물명 |
| `{{ERA}}` | 시대 + 장소 |
| `{{UNIT_TITLE}}` | `Unit NN — 단원명` |
| `{{S2_HEAD}}` | 스토리보드 S2 헤드 |
| `{{S2_BODY}}` | 스토리보드 S2 본문 |
| `{{S2_SYMBOL}}` | 해당 SVG 인라인 (`90_video/_assets/symbols/*.svg` 내용 그대로 삽입) |
| `{{S3_KEYWORD}}` | S3 키워드 |
| `{{S3_TEXT}}` | S3 설명 |
| `{{S3_METAPHOR}}` | SVG 인라인 |
| `{{S4_HEAD}}` | S4 헤드 |
| `{{S4_TEXT}}` | S4 본문 |
| `{{S4_DIAGRAM}}` | SVG 인라인 |
| `{{S5_TEXT}}` | S5 마무리 한 문장 |

### 5C: palettes.css 경로 확인

`<link rel="stylesheet" href="../_assets/palettes.css">` 가 unitNN/ 위치에서 정상 해상되는지 확인.

### 5D: 타이밍 미세 조정 (선택)

`AUDIO_DURATION` 이 50초가 아니면 마스터 템플릿의 `T = {...}` 객체와 fade 시간을 비례 스케일링.

기본 권장: 마스터 그대로 사용. 길이 차이 ±5초까지는 보정 없이 OK.

---

## STAGE 6 — HyperFrames 렌더

```bash
hyperframes render "{OUTDIR}" -o "{OUTDIR}/raw.mp4" -f 24 -q standard
```

확인:
```bash
test -f "{OUTDIR}/raw.mp4" && echo "raw.mp4 OK"
```

**실패 시 체크리스트**:
- `data-composition-id` ↔ `window.__timelines[키]` 일치
- `data-duration` 숫자 (문자열 아님)
- GSAP CDN 로드 확인
- palettes.css 경로 정상

---

## STAGE 7 — FFmpeg 합성

```bash
ffmpeg -y \
  -i "{OUTDIR}/raw.mp4" \
  -i "{OUTDIR}/narration.mp3" \
  -map 0:v -map 1:a \
  -c:v copy -c:a aac \
  -shortest \
  "{OUTDIR}/final.mp4"
```

확인:
```bash
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "{OUTDIR}/final.mp4"
```

---

## STAGE 8 — Poster 추출 (선택)

```bash
ffmpeg -y -i "{OUTDIR}/final.mp4" -ss 00:00:02 -vframes 1 -q:v 2 "{OUTDIR}/poster.jpg"
```

---

## 완료 보고

```
[se_story_video 완료]
단원: Unit NN — {단원명}
인물: {인물명}
영상 길이: {AUDIO_DURATION}초
출력: {OUTDIR}/final.mp4

권장 다음 작업:
- final.mp4 재생 → 톤·동기 확인
- 수정 시 narration.txt 편집 후 resume=stage4
- story.html 임베드: ../50_units/NN_단원명/story.html 상단 <video> 추가
```

---

## 에러 핸들링

| 증상 | 원인 | 조치 |
|---|---|---|
| edge-tts 실패 | 네트워크/SSL | `pip install --upgrade edge-tts` |
| AUDIO_DURATION ≠ 50±5 | 스크립트 분량 부적합 | STAGE 2로 돌아가 글자수 조정 |
| HyperFrames exit 9 | 정상 종료 의미 | `test -f raw.mp4` 로 확인 |
| 한글 폰트 깨짐 | Noto Sans KR CDN 미로드 | 폰트 preconnect 확인 |
| 영상-음성 sync 어긋남 | data-duration 부정확 | AUDIO_DURATION 재측정 후 보정 |

---

## 변경 이력

- v1.0 (2026-05-14): 초안 (chatlog 260514_story_video_plan.md Round 1~4 기반)

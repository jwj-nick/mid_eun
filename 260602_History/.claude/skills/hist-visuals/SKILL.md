---
name: hist-visuals
description: 에피소드 섹션에 그 시대의 대표 이미지(건물·명화·기념물·문화아이콘·상징)를 ≥2점 보강한다. Commons(PD/CC) 격리 소싱 → 전점 Read 검수 → episode.json image 배열 패치 → 빌드·게이트·배포. 호출 예시 — "/hist-visuals exploration", "라틴아메리카 시각자료 보강".
allowed-tools: Read, Write, Edit, Bash
metadata:
  project: 260602_History
  stage: 4.5 비주얼 보강 (빌드와 배포 사이)
  ssot: 00_project_hub/plan/0614_plan_visual_enrichment_all.md
  status: active
---

# hist-visuals — 대표 이미지 보강

## 표준 (불변)
- **모든 섹션에 대표 이미지 ≥ 2점.** = 건물·마스터피스(명화/조각)·기념비·문화 아이콘·상징물.
- 카운트: `image`(단일=1/배열=개수) + `oldmap`(=1)만. `map`/`battlemap`/`chart`는 제외(공간·데이터).
- 자산: **PD 또는 명확한 CC만**, 출처·라이선스 caption + alt. **전점 Read 검수**(검색 1위 신뢰 금지). 손그림·AI생성·API키 금지. 포스터/책표지/현대화폐/로고 = 저작권 제외. 현역 정치인 영웅샷·잔혹묘사 회피.

## 입력
- `30_content/<slug>/episode.json`, 계획 쇼핑리스트(`0614_plan_visual_enrichment_all.md` §2)
- 현황 실측: `python 40_build/_audit_visuals.py` → `_visual_audit.txt`(섹션별 대표이미지 수·부족분)

## 동작 (허브 1배치 = 1커밋)
1. **현황 측정:** _audit_visuals.py로 부족 섹션 확인.
2. **소싱(네트워크 단독 명령):** Commons API(urllib) — `generator=search&gsrnamespace=6` 또는 정확 `titles=File:...`. 라이선스 화이트리스트(public domain/cc0/cc by/cc-by[-sa]) + 이미지 확장자(jpg/png) 필터. `iiurlwidth`로 썸네일(SVG→PNG). **429 빈발: time.sleep(4~10), 정확 파일명 우선, 허브 단위 1스크립트.** 후보는 `_stage_<hub>/`에.
   - ⚠️ 네트워크는 **단독·최소** 명령(빌드·python 묶지 말 것 — ask-list 승인대기 hang). PYTHONIOENCODING=utf-8. heredoc 금지(Write로 임시 .py 작성→실행→rm).
3. **검수:** 후보 전점 **Read 도구 시각 확인**. 엉뚱본/저해상/책스캔/화폐·로고/중복 탈락. 필요시 PIL 크롭(여백·비율).
4. **패치:** 채택본 `30_content/<slug>/img/`에 의미있는 이름으로 복사 → episode.json:
   - 단일 image → 배열 승격(`aslist`), `order`에 `image:0`/`image:1` 토큰 삽입(헬퍼 `after(order,anchor,[...])`).
   - 각 image: `src`(img/ 상대), `caption`(내용+출처+라이선스), `alt`, 선택 `credit`/`license`.
   - JSON 라운드트립: `json.dumps(doc, ensure_ascii=False, indent=1)`.
5. **빌드·게이트:** `python 40_build/build.py <slug>` → G0 빌드 · G1 node --check(엔진 변경 시) · **G2 이미지 ref 실재 + 라이선스 표기(jpg/png 정규식)** · G3 배포 후 라이브 200·신자산 substring(`?cb=`·유한루프·sleep12).
6. **배포·커밋:** `50_app/<slug>` → `$DEPLOY/history/<slug>` 복사. **소스/배포 repo 각각 자기 cwd에서 push**(한 명령에 묶으면 이중푸시·소스누락 버그). 허브 단위 커밋.
7. **갱신:** 계획 §6 진행기록 + 메모리.

## 임시 스크립트 위생
- `_fetch_*.py`·`_audit_*.py`·`_patch_*.py`·`_stage_*/` 는 작업용 → 완료 후 정리. episode.json·img·앱만 커밋.

## 품질 게이트 (배포 전)
- [ ] 각 보강 섹션 대표이미지 ≥2 (실측 재확인)
- [ ] 전 신규 이미지 Read 검수 통과(주제 일치·해상도·비참혹)
- [ ] 라이선스 PD/CC + 출처 caption + alt
- [ ] G0~G3 통과, 양 repo push 확인(멱등 프로브)

## 견본
- latin-america(0614): civilizations 4유적·colonial 포토시·independence 산토도밍고. 패턴 표준.

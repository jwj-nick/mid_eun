<!-- 00_project_hub/plan/0618_plan_visual_upgrade.md -->
# PLAN — 전체 페이지 시각효과 업그레이드 (엔진 1곳 → 모든 페이지) ★

> Nick 지시: "전체 페이지 시각효과 업그레이드 계획 세우고 자율진행."
> 핵심 전략: 모든 에피소드가 **공유 엔진** `40_build/templates/episode.html` 하나를 쓰므로, **엔진의 시각 레이어만 손보면 14개 SPA·90+ 섹션 전부에 일괄 적용**된다. 콘텐츠(JSON)는 건드리지 않음.

## 1. 원칙
- **기능 보존 0 리스크**: 전부 *추가형*(additive) CSS/JS. 기존 블록 렌더·이벤트·Leaflet·라이트박스 로직 불변. `node --check`로 JS 검증.
- **접근성**: 모든 모션은 `@media (prefers-reduced-motion: no-preference)` 안에만 → 멀미·저사양 사용자 보호.
- **은은하게**: 학습 앱이므로 화려함보다 '읽는 흐름을 돕는' 미세 모션·깊이감. 과하면 가독성 해침.

## 2. 적용할 효과 (엔진)
**모션 (reduced-motion 가드):**
1. **스크롤 리빌** — `.wrap`/`.home-wrap`의 각 블록이 뷰포트 진입 시 fade+상승(IntersectionObserver, 1회). 섹션이 '차례로 펼쳐지는' 느낌.
2. **차트 바 성장** — 막대가 0→목표 너비로 1초 동안 차오름(해당 블록 리빌 시 발동).
3. **히어로 진입** — 섹션 전환마다 제목·키커·시대뱃지가 살짝 떠오름(섹션마다 재생).
4. **퀴즈 정답 팝** — 정답 선택 시 미세 스케일 팝.
**정적 폴리시 (모션 무관):**
5. 이미지 호버 줌(`.imgbox:hover img` scale 1.04, overflow clip).
6. 카드형 블록(why·chart·compare·choice) 호버 시 그림자 상승.
7. spark 블록 미세 골드 글로우, 히어로 상단 하이라이트 셰이딩, h2 블록 점 글로우.

## 3. 구현 위치 (엔진 1파일)
- `</style>` 직전: §2 CSS 블록 추가.
- `vfx(container)` 함수 신설(IntersectionObserver 리빌 + 차트 바 애니메이션, reduced-motion·미지원 가드) → `render()`·`renderHome()`·`renderNotes()` 끝에서 호출.
- 손작성 랜딩 3종(history `/index.html`, tracks `/index.html`, finance `/index.html`)은 이미 호버/트랜지션 보유 → 가벼운 동일 톤 리빌만 선택 적용(여력 시).

## 4. 검증 + 배포 (자율)
- V1: 엔진 `<script>` 추출 `node --check` 통과.
- V2: 대표 1개(tracks/finance/wisdom) 빌드 후 HTML에 vfx/CSS 주입 확인 + 차트/리빌 마크업 점검.
- **재빌드 = 전 슬러그**(엔진 바뀌면 모든 산출 HTML 변경): ww2·imperialism·powers·exploration·renaissance·revolutions·coldwar·globalization·new-order·north-america·latin-america·figures·tracks/sci-tech·tracks/finance/{history,people,empire,wisdom}.
- **배포**: `deploy.py <slug>`(shutil 멱등·백그라운드). ⚠️ americas는 deploy 경로가 `history/americas/<na|la>` 중첩 → 슬러그→목적지 매핑 스크립트(`_deploy_all.py`)로 처리. 배포 repo 1커밋+푸시.
- **G3**: 변경 표식(예: `cbar` transition CSS 또는 `IntersectionObserver`) 라이브 substring 매칭 샘플 폴(finite·캐시버스트).
- people 도감(`build_people.py`, 별도 템플릿)은 이번 범위 밖(에피소드 엔진과 무관) — 필요 시 후속.

## 5. 롤백
- 엔진 변경이 전부 additive·가드라 문제 시 §2 블록 + vfx 호출만 제거하면 원복. 콘텐츠 영향 0.

## 6. Nick 코멘트
- (여기에)

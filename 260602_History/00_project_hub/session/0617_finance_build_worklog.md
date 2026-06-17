<!-- 00_project_hub/session/0617_finance_build_worklog.md -->
# WORKLOG — tracks/finance 제작 (★ 압축 생존용 단일 진실)

> 이 파일을 먼저 읽으면 어느 NCC 세션이든 "여기서 이어서" 가능.
> 계획 SSOT = `plan/0617_plan_track_finance.md`. 스키마 = `10_docs/EPISODE_SCHEMA.md`. 프로토콜 = `CLAUDE.md`. 스킬 = `tracks-write`(호기심 엔진 탑재).

## 🎯 목표
경제·금융 통사 SPA `/history/tracks/finance/` (10정거장, 호기심 엔진, 고등/일반). sci-tech 인프라 전부 재사용, 신규 엔진 0.

## ✅ Nick 확정 (0617)
통합 tracks/finance / 고등·일반(생활 hook) / 10정거장(S7=제국 화폐타락 강화) / 호기심 엔진 tracks-write 승격 / 자율진행.

## ⚠️ 안전 (금융 특수)
투자 권유·특정 상품/코인 추천 **절대 금지**(교육·역사만). 시장 vs 규제 양면. 암호화폐 투기 경고.

## 🚧 RESUME HERE
- **F1 ✅** 호기심 엔진 tracks-write 승격.
- **다음 = F2** `30_content/tracks/finance/episode.json` 10정거장 텍스트(hook+spark+why+cards+chart+timeline+connect+links+quiz+reflect, 이미지는 F4). 빌드 검증.
- 이후 F3 링크 200검증 → F4 이미지 ≥2(소싱+Read검수) → F5 빌드·자율감수 → F6 deploy.py(백그라운드)+G3+tracks랜딩 finance카드 활성+허브카드 → F7 SSOT.
- 빌드 `PYTHONIOENCODING=utf-8 python 40_build/build.py tracks/finance`. 배포 `python 40_build/deploy.py tracks/finance`(★백그라운드, 셸 cp 금지).

## 📋 정거장 (10)
0 money(돈) · 1 commerce(상업혁명·복식부기) · 2 stocks(주식·첫거품) · 3 banks(은행·없던돈) · 4 depression(대공황1929) · 5 dollar(달러시대) · 6 credit(신용·카드) · 7 inflation★(제국 화폐타락: 로마·명·스페인·바이마르) · 8 crisis-2008 · 9 digital-money(코인).

## 🔁 재사용 자산 (sci-tech서 검증)
stock_exchange·euro_tower(globalization), lehman(new-order). 신규 소싱: 로마 데나리우스·튤립버블·영란은행·1929군중·브레튼우즈·신용카드·바이마르지폐·비트코인 등.

## 🚀 확장 (EXPANSION) — 단일 SPA → 4부작 허브
> 계획 SSOT = `plan/0617_plan_finance_expansion.md`. 구조: `tracks/finance/`=랜딩 + history(기존)·people·empire·wisdom.
> 빌드 `build.py tracks/finance/<ep>` · 배포 `deploy.py tracks/finance/<ep>`(백그라운드) · 랜딩=손작성(`40_build/landing/finance_index.html`).

### RESUME (확장) — ✅ 전부 완료 (0618)
- **X0~X4 ✅ 완료·라이브.** `tracks/finance` = 4부작 허브(랜딩 + history10·people7·empire7·wisdom7 = 31정거장). deploy.py tracks/finance 52/52 OK. tracks 랜딩 finance 카드 4부작 갱신·배포.
- 이미지: people 12(charles_v로 fuggerei 대체)·empire 13(bank_of_england/eccles 재사용)·wisdom 2(stock_exchange/market 재사용)+차트. 전점 Read 검수, 라이선스 파일 일치로 정정.
- 링크 60개 중 2개 404 교정(런던시티→시티_오브_런던, AI에너지→Environmental_impact_of_AI). 자율감수: 이미지 0누락·퀴즈정답 정합·投資조언0 disclaimer·반유대 음모론 deepdive 확인.
- 남은 것: (선택) Nick 리뷰 후 톤/내용 조정. 다음 분야 트랙=예술·문화·체육.

### 로그 (확장, 최신 위)
- 0618 X2~X4: empire(돈의수도·런던·금고·선물·★연준·★페트로달러·AI에너지) + wisdom(편지·자본주의·★복리·삶의복리투자·주식지식·마음가짐·돈을아는어른) 작성·빌드·배포. 이미지 batch2~4 소싱(charles_v·nixon·연준·금괴·포트녹스·유전·데이터센터 등 전점 Read검수), 링크 60검증(2교정), 자율감수 통과. 허브 전체 deploy 52/52. SSOT(ROADMAP·PROGRESS) 갱신.
- 0617 X1: people episode.json 7섹션(메디치·푸거·★유대인과돈[음모론 해체 deepdive+quiz2]·로스차일드[워털루 신화 해체]·J.P.모건[1907→연준]·연준의장들[볼커 인플레 차트]·버핏[복리]). build OK(85256자). 이미지 13 fetch 중.
- 0617 X0: 통사 10정거장 → `tracks/finance/history/`로 이동(slug·brand·foot·hub 메타 패치). 랜딩(`finance_index.html`, 자녀 편지+4카드) 작성·50_app staging. history 배포 DEPLOY_OK 21/21. 기존 SPA는 허브 URL에 임시 잔존(X4에서 랜딩으로 교체).

## 📝 로그 (통사, 최신 위)
- 0617 #3: ★F4~F7 완료·라이브. 이미지 20점(재사용3+신규17, 전점 Read검수, 남부연합지폐·PDF문서 오선정 2 교정), 자율감수 통과(투자권유0·암호화폐 경고·양면). deploy.py 배포(21/21)·G3 PASS, tracks 랜딩 금융 카드 활성+허브 카드 2트랙 반영, SERIES_ROADMAP/PROGRESS/메모리 갱신. **tracks/finance 완료.** https://jwj-nick.github.io/history/tracks/finance/
- 0617 #2: F2 완료 — episode.json 10정거장(돈·상업혁명·주식·은행·대공황·달러·신용·★제국화폐타락·2008·코인). 호기심 엔진 spark·mind 10/10, 차트 2(대공황 실업률·로마 데나리우스 은함량), 링크 30, 용어 18. 빌드 OK(89006자). 이미지=F4. 다음=F3 링크 200검증(튤립 url 오타 의심→교정 예정).
- 0617 #1: F1 — 호기심 엔진 tracks-write 승격(전 분야 트랙 표준, spark/wonder-first/mind-bender/장치≥3 게이트). 계획 plan/0617. 다음=F2.

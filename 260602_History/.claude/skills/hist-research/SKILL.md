---
name: hist-research
description: 한 에피소드의 사실·인물·인용·영상 자료를 병렬로 리서치하고 출처와 함께 정리한다. 날짜·인명 팩트체크, 비서구·약소국 관점 보강, 논쟁 균형 가이드, 인물 자료, 저작권 안전 인용, 유튜브 실제 영상(한·영) 큐레이션을 수행. 호출 예시 — "/hist-research imperialism", "제국주의 리서치".
allowed-tools: Read, Write, WebSearch, WebFetch, Agent, Glob
metadata:
  project: 260602_History
  stage: 2 리서치·팩트체크
  ssot: 00_project_hub/plan/260603_history_hub_master_plan.md
  status: seed
---

# hist-research — 리서치·팩트체크 (단계 2)

Ep01에서 검증한 **3-에이전트 병렬 패턴**을 표준화. 결과는 항상 **출처(채널/URL/기관)** 와 함께.

## 입력
- `10_docs/content-map_<slug>.md` (단계 1 산출) — 리서치 To-Do

## 동작 (병렬 Agent)
> ⚠️ **실전 교훈(Ep02)**: 리서치 에이전트는 **반드시 한 메시지 안에서 동시에** 발사하고, 직후 "몇 개가 실제로 돌아왔는지" 개수를 검증한다. (Ep02에서 3개 의도→1개만 발사된 사고. 누락 시 즉시 재발사.)

1. **팩트체크 에이전트** — 날짜·인명·지명 검증/정정, 안네식 정정사항 플래그. (중1 교과서 기준)
2. **관점·균형 에이전트** — 비서구·약소국·식민지 관점 보강 자료, 논쟁 주제(예: 원폭·책임·냉전 잔혹사) **균형 서술 가이드**, "그때의 생각"(당시 상식 vs 현재) 대비 포인트.
3. **인물·인용 에이전트** — "꼭 알아야 할 인물" 핵심 사실 + 빛과 그림자 + **저작권 안전 짧은 인용**(출처·날짜).
4. **유튜브 큐레이션 에이전트** — 한국어(EBS·사피엔스·최태성·KBS 등) + 외국(Crash Course·TED-Ed·Simple History 등) **실재 확인된** 영상. 고신뢰=video, 불확실=search 폴백.
5. **이미지·자산 에이전트 (S1+ 블록용)** — image/compare 블록이 쓸 **공개도메인(PD-old) 또는 명확한 CC** 자료. Wikimedia Commons 파일 페이지에서 ① 정확한 라이선스(PD/CC BY-SA…) ② 저자 ③ `upload.wikimedia.org` **직접 URL** ④ 내용·언어를 확인해 기록. 실전 교훈: 검색어만으론 부족 → **파일 페이지를 WebFetch로 검증하고, 실물을 curl로 받아 임베드 적합성(벡터/raster·viewBox·언어·범례)까지 확인**. 못 구하면 폴백(map 대체) 보고. map용 좌표·출처도 여기서.

> 영상 링크는 죽은 링크 방지를 위해 **확인된 것만 video, 나머지는 검색어(search)** 로 표기(스키마 정책).

## 출력
- `20_research/<slug>/facts.md` · `perspective.md` · `people.md` · `videos.md` (모두 출처 포함)

## 품질 게이트
- [ ] 모든 날짜·인명에 출처 / 정정사항 별도 표시
- [ ] 비서구 관점·논쟁 균형 가이드 포함
- [ ] 인용문 저작권 안전 + 출처
- [ ] 영상 video/search 분류 + 길이·언어

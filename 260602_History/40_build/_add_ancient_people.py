# -*- coding: utf-8 -*-
# Append ancient/medieval world-history figures to people.json (v3). Idempotent by slug.
import json, io, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "30_content/people/people.json"
data = json.loads(P.read_text(encoding="utf-8"))
people = data["people"] if isinstance(data, dict) and "people" in data else data

def wiki(ko, en, britID=None, native_label=None, native_url=None):
    L=[{"label":"위키백과 (한국어)","url":"https://ko.wikipedia.org/wiki/"+ko,"lang":"ko","type":"wiki"},
       {"label":"Wikipedia (English)","url":"https://en.wikipedia.org/wiki/"+en,"lang":"en","type":"wiki"}]
    if native_label and native_url:
        L.append({"label":native_label,"url":native_url,"lang":"x","type":"wiki"})
    if britID:
        L.append({"label":"Encyclopædia Britannica","url":"https://www.britannica.com/biography/"+britID,"lang":"en","type":"encyclopedia"})
    return L

NEW = [
{
 "slug":"confucius","face":"☯️",
 "names":{"native":"孔子 (공자)","roman":"Confucius / Kongzi","pronun_ko":"쿵쯔(공자)","en":"Confucius","ko":"공자","alias":"공구(孔丘)"},
 "nationality":"중국 (춘추시대 노나라)","lifespan":"BC551~BC479",
 "oneLine":"어진 마음과 도리로 어지러운 세상을 바로잡으려 한 동아시아의 스승",
 "bio":[
  "춘추시대의 혼란기, 노나라의 가난한 집안에서 태어났어요. 벼슬에서 자기 뜻을 펼치려 여러 나라를 떠돌았지만 끝내 등용되지 못했고 — 대신 제자를 가르치는 데 평생을 바쳤죠. 그가 죽은 뒤 제자들이 그의 말을 모은 《논어》가, 2500년 동안 동아시아 사람들의 마음을 이끌었어요.",
  "그의 가르침의 핵심은 ‘인(仁, 어짊)’과 ‘예(禮, 도리)’예요 — 각자가 제자리에서 사람다운 도리를 다하면 어지러운 세상도 바로 선다는 것이죠. ‘내가 원하지 않는 것을 남에게 행하지 말라’는 그의 말은, 같은 시대 다른 문명도 도달한 ‘황금률’과 통해요. 그의 유교는 한나라 때 국교가 되어 중국·한국·일본·베트남을 묶는 가장 큰 사상이 됐어요."
 ],
 "personTimeline":[{"yr":"BC551","t":"노나라에서 출생"},{"yr":"BC500경","t":"여러 나라를 떠돌며 도(道)를 펴려 함"},{"yr":"BC479","t":"사망 — 제자들이 《논어》를 엮음"},{"yr":"BC136경","t":"(후대) 한 무제가 유교를 국교화"}],
 "lightShadow":"그의 가르침은 ‘조화와 도리’의 빛과, ‘신분·위계 질서를 정당화한다’는 비판의 그림자를 함께 지녀요. 같은 사상이 시대에 따라 안정의 힘도, 변화를 막는 굴레도 됐죠.",
 "portrait":{"src":"img/confucius.jpg","alt":"동아시아의 스승 공자의 전통 초상","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":""},
 "links":wiki("공자","Confucius","Confucius"),
 "related":[{"ep":"axial-age","section":"china-sages","label":"중국 — 공자와 제자백가","epLabel":"축의 시대"},{"ep":"eastern-empires","section":"han","label":"유교를 국교로 — 한나라","epLabel":"고대 동방 제국"}],
 "reflect":"‘내가 원하지 않는 것을 남에게 하지 말라’ — 2500년 전 공자의 이 말이 지금 너의 하루에도 쓸모가 있을지 생각해 보세요.",
 "quickCard":{"era":"춘추시대 (BC551~479)","keywords":["인(仁)과 예(禮)","《논어》","유교의 시작"],"oneQuestion":"세상을 바꾸는 건 ‘강한 법’일까, ‘사람의 도리’일까?"},
 "whyHere":"‘축의 시대’ 중국의 사상을 대표하는 인물이에요. 그리스의 소크라테스, 인도의 붓다와 거의 같은 시기에 — 그는 ‘어지러운 세상을 어떻게 살 것인가’를 물었죠. 그의 답(인·예)은 동아시아 2천 년의 바탕이 됐고, 한국사의 유교적 전통과도 직접 닿아 있어요.",
 "quotes":[{"text":"배우고 때로 익히면 또한 기쁘지 아니한가.","note":"《논어》 첫 구절 — 배움의 즐거움","grade":"직접"},{"text":"내가 원하지 않는 것을 남에게 행하지 말라.","note":"《논어》 — ‘황금률’의 동양판","grade":"직접"}],
 "figuresLink":"confucius-socrates"
},
{
 "slug":"socrates","face":"🏛️",
 "names":{"native":"Σωκράτης","roman":"Socrates","pronun_ko":"소크라테스","en":"Socrates","ko":"소크라테스","alias":""},
 "nationality":"고대 그리스 (아테네)","lifespan":"BC470경~BC399",
 "oneLine":"스스로 묻고 따지는 삶을 일깨운 서양 철학의 아버지",
 "bio":[
  "아테네의 평범한 집안에서 태어나 책 한 권 남기지 않았지만, 인류의 생각하는 방식을 바꿔 놓았어요. 그는 광장에서 사람들에게 끝없이 물었죠 — ‘정의가 무엇인가? 당신은 그걸 정말 안다고 할 수 있는가?’ 답을 주는 대신 질문으로 상대 스스로 ‘안다는 착각’을 깨닫게 하는 ‘산파술’이었어요.",
  "그는 ‘나는 내가 모른다는 것을 안다’며 무지의 자각이 지혜의 출발이라 했어요. 하지만 그의 집요한 질문은 권력자들을 불편하게 했고 — ‘청년을 타락시키고 신을 모독했다’는 죄로 사형(독배)당했죠. 죽음 앞에서도 ‘검토되지 않는 삶은 살 가치가 없다’며 신념을 굽히지 않았어요. 그의 제자 플라톤, 그 제자 아리스토텔레스로 서양 철학이 이어집니다."
 ],
 "personTimeline":[{"yr":"BC470경","t":"아테네에서 출생"},{"yr":"BC430경~","t":"광장에서 ‘묻는 철학’을 펼침"},{"yr":"BC399","t":"재판 끝에 독배를 들고 죽음"}],
 "lightShadow":"‘묻고 의심하는 정신’을 인류에 선물했지만, 그 질문 때문에 사형당했어요 — 새로운 생각이 늘 환영받는 건 아니라는 걸 보여 주죠. 또 그를 ‘아는’ 것이 거의 제자 플라톤의 기록을 통해서라, ‘진짜 소크라테스’가 어디까지인지도 흥미로운 물음이에요.",
 "portrait":{"src":"img/socrates.jpg","alt":"고대 철학자 소크라테스의 대리석 흉상","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":""},
 "links":wiki("소크라테스","Socrates","Socrates"),
 "related":[{"ep":"greece","section":"philosophy","label":"철학의 탄생 — 소크라테스","epLabel":"그리스"},{"ep":"axial-age","section":"greece-reason","label":"그리스 — 이성으로 묻다","epLabel":"축의 시대"}],
 "reflect":"‘당연하게 여겨지는 것에 의문을 던지는 일’은 왜 불편하면서도 중요할까요? 너가 ‘정말 그럴까?’ 하고 따져 보고 싶은 ‘당연한 것’은?",
 "quickCard":{"era":"고전기 아테네 (BC470~399)","keywords":["산파술(묻는 철학)","무지의 자각","검토하는 삶"],"oneQuestion":"‘안다’는 것과 ‘안다고 믿는 것’은 어떻게 다를까?"},
 "whyHere":"‘축의 시대’ 그리스를 대표하는 인물이에요. 같은 시기 중국의 공자, 인도의 붓다와 함께 — 그는 ‘신화가 아니라 이성으로 따지는’ 길을 열었죠. 오늘날 과학과 비판적 사고의 뿌리가 그의 ‘묻는 태도’에 닿아 있어요.",
 "quotes":[{"text":"검토되지 않는 삶은 살 가치가 없다.","note":"재판에서 한 말로 전해짐(플라톤 《소크라테스의 변명》)","grade":"전언"},{"text":"나는 내가 아무것도 모른다는 것을 안다.","note":"그의 지혜관을 요약하는 말","grade":"요지"}],
 "figuresLink":"confucius-socrates"
},
{
 "slug":"alexander","face":"⚔️",
 "names":{"native":"Ἀλέξανδρος","roman":"Alexander the Great","pronun_ko":"알렉산드로스","en":"Alexander_the_Great","ko":"알렉산드로스 대왕","alias":"알렉산더 대왕"},
 "nationality":"고대 마케도니아","lifespan":"BC356~BC323",
 "oneLine":"13년 만에 세 대륙을 정복하고 동서를 섞은 32세의 정복자",
 "bio":[
  "그리스 북쪽 마케도니아의 왕자로 태어나, 어린 시절 철학자 아리스토텔레스에게 배웠어요. 스무 살에 왕이 되자마자 동방 원정에 나서 — 당시 세계 최강 페르시아 제국을 무너뜨리고, 이집트를 거쳐 인도 북서부까지 진군했죠. 단 13년 만에 유럽·아시아·아프리카에 걸친 대제국을 세운 거예요.",
  "그가 남긴 가장 큰 유산은 영토가 아니라 ‘헬레니즘’ — 그리스 문화가 동방까지 퍼져 동서양이 융합된 새 문명이에요. 그리스어가 공용어가 되고, 그리스 조각이 멀리 간다라 불상에까지 영향을 줬죠. 하지만 BC323년 바빌론에서 32세에 갑자기 죽으면서, 거대한 제국은 부하 장군들에 의해 셋으로 갈라졌어요."
 ],
 "personTimeline":[{"yr":"BC356","t":"마케도니아에서 출생(스승 아리스토텔레스)"},{"yr":"BC336","t":"20세에 왕위 — 동방 원정 시작"},{"yr":"BC331","t":"페르시아 제국 정복"},{"yr":"BC326","t":"인도 북서부(인더스)까지 진군"},{"yr":"BC323","t":"바빌론에서 32세에 사망"}],
 "lightShadow":"동서 문명을 섞은 ‘연결자’이자, 수많은 도시를 파괴한 ‘정복자’예요. 그의 정복은 폭력이었지만 헬레니즘이라는 융합 문명을 낳았죠 — 역사의 빛과 그늘이 한 몸에 있는 인물이에요.",
 "portrait":{"src":"img/alexander.jpg","alt":"이소스 전투에서 돌격하는 알렉산드로스를 그린 고대 모자이크","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":""},
 "links":wiki("알렉산드로스_3세","Alexander_the_Great","Alexander-the-Great"),
 "related":[{"ep":"greece","section":"alexander","label":"알렉산드로스와 헬레니즘","epLabel":"그리스"}],
 "reflect":"알렉산드로스의 정복은 ‘폭력’이었지만 ‘문명의 융합(헬레니즘)’을 낳았어요. 이런 사건을 ‘좋았다/나빴다’로 단순히 말할 수 있을까요?",
 "quickCard":{"era":"헬레니즘의 시작 (BC356~323)","keywords":["페르시아 정복","헬레니즘(동서 융합)","32세 요절"],"oneQuestion":"한 사람의 정복이 ‘문명의 만남’을 가져왔다면, 그를 어떻게 평가해야 할까?"},
 "whyHere":"그리스 문명을 동방 끝까지 퍼뜨려 ‘헬레니즘’ 시대를 연 인물이에요. 같은 ‘고대 동방 제국’ 편의 진시황과 견주면 — 비슷한 시기, 동서에서 ‘정복과 통합’을 이룬 두 군주를 나란히 볼 수 있죠.",
 "quotes":[{"text":"나에게는 정복할 세계가 더 이상 없구나.","note":"후대에 그에게 붙은 유명한 말(출처 불확실)","grade":"전언"}],
 "figuresLink":"alexander-qin"
},
{
 "slug":"qin-shi-huang","face":"🐲",
 "names":{"native":"秦始皇","roman":"Qin Shi Huang","pronun_ko":"친스황(진시황)","en":"Qin_Shi_Huang","ko":"진시황","alias":"시황제·영정(嬴政)"},
 "nationality":"중국 (진나라)","lifespan":"BC259~BC210",
 "oneLine":"천하를 처음 통일하고 스스로 ‘첫 황제’가 된 사람",
 "bio":[
  "수백 년간 갈라져 싸우던 중국을, 진(秦)나라 왕 영정이 차례로 정복해 BC221년 처음으로 통일했어요. 그는 스스로를 ‘첫 번째 황제’ 시황제(始皇帝)라 칭하고, 법가 사상을 바탕으로 강력한 중앙집권을 폈죠. 무엇보다 문자·도량형·화폐·수레바퀴 폭을 전부 통일해 — 넓은 천하를 하나의 기준으로 묶었어요(이 ‘표준화’가 이후 2천 년 중국의 바탕이 됩니다).",
  "북방을 막으려 만리장성을 잇고, 자기 무덤에 흙 군대(병마용)를 묻었어요. 하지만 그의 통치는 가혹했죠 — 사상을 통제하려 책을 불태우고 학자를 묻었으며(분서갱유), 영생을 찾아 헤매다 49세에 죽었어요. 가혹한 진나라는 그가 죽자마자 반란 속에 단 15년 만에 무너졌죠. ‘위대한 통일’과 ‘가혹한 단명’이 한데 있는 황제예요."
 ],
 "personTimeline":[{"yr":"BC259","t":"진나라 왕족으로 출생"},{"yr":"BC221","t":"천하 통일 — ‘시황제’ 칭함"},{"yr":"BC213경","t":"분서갱유(사상 탄압)"},{"yr":"BC210","t":"순행 중 사망 — 진 곧 붕괴"}],
 "lightShadow":"중국을 하나로 묶은 ‘통일의 위업’과, 백성을 가혹하게 동원하고 사상을 탄압한 ‘폭군’의 두 얼굴을 함께 봐야 해요. 통일·만리장성·병마용 모두 위업이자 백성의 고통이었죠.",
 "portrait":{"src":"img/qin-shi-huang.jpg","alt":"중국 첫 황제 진시황을 그린 전통 초상화","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":""},
 "links":wiki("진_시황제","Qin_Shi_Huang","Qin-Shi-Huang"),
 "related":[{"ep":"eastern-empires","section":"qin","label":"천하를 통일하다 — 진시황","epLabel":"고대 동방 제국"}],
 "reflect":"진시황은 ‘위대한 황제’와 ‘가혹한 폭군’ 중 어느 쪽으로 기억해야 할까요? 아니면 둘 다일까요? 위업과 희생을 함께 본다는 건 어떤 의미일까요?",
 "quickCard":{"era":"중국 최초 통일 (BC259~210)","keywords":["천하 통일","문자·도량형 표준화","만리장성·병마용·분서갱유"],"oneQuestion":"큰 것을 ‘이루는 힘’과 그것을 ‘오래 유지하는 힘’은 같을까, 다를까?"},
 "whyHere":"중국을 처음 통일한 인물이에요. 거의 같은 시기 서방을 정복한 알렉산드로스와 견주면 — ‘정복’과 ‘통합’의 동서 두 길을 비교해 볼 수 있죠. 그가 세운 ‘표준화된 중앙집권’은 한국사(한자 문화권)에도 닿아요.",
 "quotes":[{"text":"천하의 무기를 거두어 녹이고, 한 가지 문자로 천하를 적게 하라.","note":"통일 정책을 전하는 《사기》의 기록 취지","grade":"요지"}],
 "figuresLink":"alexander-qin"
},
{
 "slug":"ashoka","face":"🦁",
 "names":{"native":"अशोक","roman":"Ashoka","pronun_ko":"아쇼카(아소카)","en":"Ashoka","ko":"아소카","alias":"아육왕(阿育王)"},
 "nationality":"고대 인도 (마우리아 제국)","lifespan":"BC304경~BC232",
 "oneLine":"정복을 뉘우치고 비폭력을 돌에 새긴, 거의 유일한 정복 군주",
 "bio":[
  "인도 최초의 통일 제국 마우리아의 왕으로, 동부의 칼링가를 정복하며 인도 대부분을 손에 넣었어요. 그런데 그 전쟁의 참상(수십만 명의 죽음)에 깊이 충격받아 — 이긴 자리에서 오히려 무너졌죠. 그는 불교에 귀의해 ‘다시는 칼로 정복하지 않겠다’ 결심하고, 통치 방식을 완전히 바꿨어요.",
  "그는 ‘다르마(법·도리)’에 따른 통치를 내걸고 생명 존중·관용·복지를 강조했으며, 이를 새긴 돌기둥(석주)과 바위 칙령을 제국 곳곳에 세웠어요(우리가 아소카를 아는 건 이 비문 덕이에요). 또 불교를 적극 후원해 스리랑카·중앙아시아로 전파했는데 — 이것이 훗날 불교가 동아시아(중국·한국·일본)까지 퍼지는 출발점이 됐죠. 그의 사자 석주는 오늘날 인도의 국가 상징이에요."
 ],
 "personTimeline":[{"yr":"BC268경","t":"마우리아 제국 왕위에 오름"},{"yr":"BC261경","t":"칼링가 정복 — 참상에 회한, 불교 귀의"},{"yr":"BC250경","t":"다르마 칙령(석주)을 전국에 세움 · 불교 전파"},{"yr":"BC232경","t":"사망"}],
 "lightShadow":"‘승리를 뉘우친 왕’이라는 드문 빛을 지녔지만, 그의 통치도 완전무결하진 않았고 마우리아는 그의 사후 빠르게 쇠퇴했어요. 그래도 ‘무력이 아닌 도리로 다스린다’는 이상은 인류 정신사의 인상적인 장면이에요.",
 "portrait":{"src":"img/ashoka.jpg","alt":"아소카 석주 꼭대기의 네 마리 사자 주두(인도의 국가 상징)","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":"아소카의 동시대 초상은 전하지 않아, 그의 상징인 사자 주두로 대신함"},
 "links":wiki("아소카","Ashoka","Ashoka"),
 "related":[{"ep":"eastern-empires","section":"maurya","label":"뉘우친 정복자 — 아소카","epLabel":"고대 동방 제국"}],
 "reflect":"대부분의 정복자가 승리를 기념비에 새길 때, 아소카는 ‘후회’를 새겼어요. ‘힘으로 이기는 것’과 ‘사람의 마음을 얻는 것’은 어떻게 다를까요?",
 "quickCard":{"era":"마우리아 전성기 (BC3세기)","keywords":["칼링가 전쟁의 회한","불교 귀의·전파","다르마(도리)의 통치"],"oneQuestion":"‘이긴 자’가 그 승리를 뉘우칠 수 있다면, 진짜 강함이란 무엇일까?"},
 "whyHere":"불교를 동아시아로 퍼뜨린 출발점이자 ‘비폭력 통치’의 상징이에요. 로마의 콘스탄티누스(기독교를 품은 황제)와 견주면 — ‘종교를 국가의 중심에 들인 두 군주’를 동서에서 나란히 볼 수 있죠. 한국사의 불교 전래와도 닿아요.",
 "quotes":[{"text":"모든 사람은 나의 자식이다.","note":"아소카 석주 칙령에 새겨진 통치 이념","grade":"직접"}],
 "figuresLink":"ashoka-constantine"
},
{
 "slug":"constantine","face":"✝️",
 "names":{"native":"Flavius Constantinus","roman":"Constantine the Great","pronun_ko":"콘스탄티누스","en":"Constantine_the_Great","ko":"콘스탄티누스","alias":"콘스탄티누스 1세·대제"},
 "nationality":"로마 제국","lifespan":"272경~337",
 "oneLine":"기독교를 품어 로마와 결합시키고 ‘새 로마’를 세운 황제",
 "bio":[
  "혼란하던 로마 제국의 권력 다툼에서 승리해 황제가 됐어요. 그의 가장 큰 결정은 — 300년간 박해받던 기독교를 공인한 것이에요(밀라노 칙령, 313). 전설에 따르면 결전을 앞두고 ‘이 표식으로 이기리라’는 십자가 환상을 보았다고 전해지죠. 이로써 변방의 박해받던 종교가 로마 제국의 합법 종교가 됐고, 4세기 말 국교로 이어졌어요.",
  "그는 또 제국의 동쪽에 ‘새 로마’ 콘스탄티노플(지금의 이스탄불)을 세웠어요 — 훗날 천 년을 더 이어 갈 동로마(비잔틴) 제국의 수도가 되죠. 기독교와 로마를 결합시킨 그의 선택은, 서로마가 멸망한 뒤에도 기독교가 유럽을 천 년간 지배할 기반을 놓았어요. 유럽 문명의 방향을 결정한 황제예요."
 ],
 "personTimeline":[{"yr":"272경","t":"출생"},{"yr":"312","t":"밀비우스 다리 전투 승리(십자가 환상 전설)"},{"yr":"313","t":"밀라노 칙령 — 기독교 공인"},{"yr":"330","t":"콘스탄티노플 건설(‘새 로마’)"},{"yr":"337","t":"사망(임종 직전 세례)"}],
 "lightShadow":"기독교에 자유를 준 ‘관용의 빛’과, 종교를 권력 통합의 도구로 쓴 ‘정치적 계산’의 그림자를 함께 봐야 해요. 권력 다툼에서 가족까지 제거한 냉혹함도 있었죠.",
 "portrait":{"src":"img/constantine.jpg","alt":"로마 황제 콘스탄티누스의 거대한 대리석 두상","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":""},
 "links":wiki("콘스탄티누스_1세","Constantine_the_Great","Constantine-I-Roman-emperor"),
 "related":[{"ep":"rome","section":"christianity","label":"변방의 종교, 제국을 얻다","epLabel":"로마"}],
 "reflect":"콘스탄티누스의 기독교 공인은 ‘신앙의 자유’였을까요, ‘권력의 계산’이었을까요? 한 결정에 두 동기가 섞여 있을 때 우리는 그것을 어떻게 봐야 할까요?",
 "quickCard":{"era":"로마 후기 (272~337)","keywords":["밀라노 칙령(기독교 공인)","콘스탄티노플 건설","로마와 기독교의 결합"],"oneQuestion":"한 통치자의 종교 선택이, 천 년 뒤 세계를 바꿀 수 있을까?"},
 "whyHere":"기독교를 로마 제국의 중심에 들여 유럽 문명의 방향을 바꾼 황제예요. 인도의 아소카(불교를 품은 왕)와 견주면 — ‘종교를 국가와 결합시킨 두 군주’의 동서 짝을 볼 수 있죠.",
 "quotes":[{"text":"이 표식으로 너는 이기리라.","note":"전투 전 보았다는 십자가 환상의 전설(라틴어 ‘In hoc signo vinces’)","grade":"전언"}],
 "figuresLink":"ashoka-constantine"
},
{
 "slug":"genghis-khan","face":"🏹",
 "names":{"native":"Чингис хаан","roman":"Genghis Khan","pronun_ko":"칭기스 칸(칭기즈칸)","en":"Genghis_Khan","ko":"칭기즈칸","alias":"테무진(鐵木眞)"},
 "nationality":"몽골 제국","lifespan":"1162경~1227",
 "oneLine":"흩어진 초원의 부족을 통일해 인류 최대 제국을 세운 정복자",
 "bio":[
  "어린 시절 아버지를 잃고 노예처럼 쫓기던 초원의 소년 테무진은, 자라서 흩어진 몽골 부족을 모두 통일하고 1206년 ‘칭기즈칸(위대한 군주)’으로 추대됐어요. 그가 이끈 기마 군대는 놀라운 속도로 — 동쪽 중국에서 서쪽 유럽 문턱까지 — 인류 역사상 가장 넓은 제국을 정복했죠.",
  "그의 정복은 잔혹했지만(저항한 도시는 학살), 동시에 정복지의 기술자·상인·종교를 보호하고 혈통이 아닌 능력으로 사람을 등용했어요. 역참(통신망)으로 거대한 제국을 묶어 동서 교류를 폭발시켰죠(팍스 몽골리카). 그는 ‘파괴자’이자 ‘연결자’라는 두 얼굴로 기억돼요. 고려는 이 거대한 폭풍에 맞서 40년을 항쟁했어요."
 ],
 "personTimeline":[{"yr":"1162경","t":"초원에서 테무진으로 출생"},{"yr":"1206","t":"몽골 통일 — ‘칭기즈칸’ 추대"},{"yr":"1219~","t":"중앙아시아·페르시아 원정"},{"yr":"1227","t":"원정 중 사망 — 제국은 후예들이 확장"}],
 "lightShadow":"‘잔혹한 파괴자’이자 ‘동서를 잇고 능력을 중시한 연결자’ — 어느 한쪽만 보면 그를 오해해요. 역사 속 정복이 ‘파괴’와 ‘새 질서’를 동시에 가져온다는 걸 가장 극적으로 보여 주는 인물이죠.",
 "portrait":{"src":"img/genghis-khan.jpg","alt":"흰옷을 입은 노년의 칭기즈칸을 그린 원나라 시대 초상화","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":""},
 "links":wiki("칭기즈_칸","Genghis_Khan","Genghis-Khan"),
 "related":[{"ep":"eurasia","section":"mongol","label":"몽골의 폭풍 — 칭기즈칸","epLabel":"유라시아를 잇다"},{"ep":"korea/goryeo","section":"mongol","label":"몽골 40년 항쟁(고려)","epLabel":"한국사 고려"}],
 "reflect":"칭기즈칸은 ‘파괴자’이자 ‘연결자’였어요. 한 인물을 ‘좋다/나쁘다’ 한쪽으로만 보면 진실을 놓치죠. 역사 인물을 ‘두 얼굴’로 함께 보는 건 왜 중요할까요?",
 "quickCard":{"era":"몽골 제국 (1162경~1227)","keywords":["몽골 통일","인류 최대 제국","파괴와 연결의 두 얼굴"],"oneQuestion":"세계를 하나로 묶은 힘이 폭력이었다면, 그 통합을 어떻게 평가해야 할까?"},
 "whyHere":"인류 최대 제국을 세워 동서를 하나로 묶은 인물이에요. 로마의 카이사르(제국을 연 정복자)와 견주면 — 천 년의 거리를 두고 ‘제국을 만든 두 정복자’를 나란히 볼 수 있죠. 고려의 몽골 항쟁(한국사)과도 직접 닿아요.",
 "quotes":[{"text":"하늘에 해가 하나이듯, 땅에는 한 명의 주인이 있어야 한다.","note":"그의 세계관을 전하는 말(《몽골비사》 등)","grade":"요지"}],
 "figuresLink":"genghis-caesar"
},
{
 "slug":"caesar","face":"🏛️",
 "names":{"native":"Gaius Iulius Caesar","roman":"Julius Caesar","pronun_ko":"율리우스 카이사르","en":"Julius_Caesar","ko":"율리우스 카이사르","alias":"시저"},
 "nationality":"로마 공화정","lifespan":"BC100~BC44",
 "oneLine":"공화정을 끝내고 ‘황제’의 대명사가 된 정복자",
 "bio":[
  "로마 공화정 말기, 뛰어난 군인이자 정치가로 갈리아(지금의 프랑스)를 정복해 명성과 군대를 얻었어요. BC49년, 그는 군대를 이끌고 본국 경계인 루비콘강을 ‘주사위는 던져졌다’며 건너 내전을 일으키고 권력을 장악했죠. 빈부 격차와 분열로 이미 곪아 있던 500년 공화정은, 그렇게 사실상 막을 내렸어요.",
  "그는 사실상 1인 지배자가 됐지만 — ‘공화정을 죽이고 왕이 되려 한다’고 본 원로원 의원들에게 BC44년 암살당했어요. 하지만 그의 죽음으로도 공화정은 되살아나지 못했고, 그의 양아들 옥타비아누스가 ‘황제’의 시대를 열죠. ‘카이사르’라는 그의 이름은 훗날 황제를 뜻하는 말이 됐어요 — 독일의 ‘카이저’, 러시아의 ‘차르’가 모두 여기서 왔죠."
 ],
 "personTimeline":[{"yr":"BC100","t":"로마에서 출생"},{"yr":"BC58~50","t":"갈리아 정복 — 명성과 군대를 얻음"},{"yr":"BC49","t":"루비콘강을 건너 내전 — ‘주사위는 던져졌다’"},{"yr":"BC44","t":"원로원에서 암살됨"}],
 "lightShadow":"‘유능한 개혁가’이자 ‘공화정을 끝낸 야심가’의 두 얼굴. 그를 ‘영웅’으로 볼지 ‘공화정의 파괴자’로 볼지는 2천 년째 논쟁거리예요 — ‘제도가 시대를 못 따라갈 때 강한 개인이 그 틈을 파고든다’는 패턴의 상징이죠.",
 "portrait":{"src":"img/caesar.jpg","alt":"로마 정치가 율리우스 카이사르의 대리석 흉상","source":"Wikimedia Commons","license":"퍼블릭 도메인","note":""},
 "links":wiki("율리우스_카이사르","Julius_Caesar","Julius-Caesar-Roman-ruler"),
 "related":[{"ep":"rome","section":"crisis","label":"공화정의 위기 — 카이사르","epLabel":"로마"}],
 "reflect":"로마 공화정은 ‘외부의 적’이 아니라 ‘내부의 분열’ 때문에 무너졌고, 그 틈을 카이사르가 파고들었어요. ‘제도가 시대를 못 따라갈 때’ 어떤 일이 벌어질까요?",
 "quickCard":{"era":"로마 공화정 말기 (BC100~44)","keywords":["갈리아 정복","루비콘강·내전","공화정의 종말"],"oneQuestion":"한 사람이 ‘유능한 개혁가’이면서 동시에 ‘체제의 파괴자’일 수 있을까?"},
 "whyHere":"500년 로마 공화정을 끝내고 제정의 길을 연 인물이에요. 천 년 뒤 인류 최대 제국을 세운 칭기즈칸과 견주면 — 시대도 무대도 다른 ‘제국을 만든 두 정복자’를 나란히 볼 수 있죠.",
 "quotes":[{"text":"주사위는 던져졌다.","note":"루비콘강을 건너며 한 말로 전해짐","grade":"전언"},{"text":"왔노라, 보았노라, 이겼노라.","note":"신속한 승리를 전한 그의 보고(‘Veni, vidi, vici’)","grade":"직접"}],
 "figuresLink":"genghis-caesar"
}
]

existing = {p["slug"] for p in people}
added = 0
for n in NEW:
    if n["slug"] in existing:
        # replace
        for i,p in enumerate(people):
            if p["slug"]==n["slug"]: people[i]=n
    else:
        people.append(n); added += 1
P.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print("ADDED %d, total %d" % (added, len(people)))

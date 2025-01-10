from bs4 import BeautifulSoup

# Пример HTML-кода (замените на свой)
html_content = """
<tr>
<td>一</td>
<td>One</td>
<td>いち<br>ichi</td>
<td>ひと(つ)<br>hito(tsu)</td>
<td>一人<br>hitori<br>(one person, alone)</td>
</tr>
<tr>
<td>二</td>
<td>Two</td>
<td>に<br>ni</td>
<td>ふた(つ)<br>futa(tsu)</td>
<td>二人<br>futari<br>(two people)</td>
</tr>
<tr>
<td>三</td>
<td>Three</td>
<td>さん<br>san</td>
<td>み(っつ)<br>mi(ttsu)</td>
<td>三日<br>mikka<br>(3rd day of the month)</td>
</tr>
<tr>
<td>四</td>
<td>Four</td>
<td>し<br>shi</td>
<td>よ(っつ), よん<br>yo(ttsu), yon</td>
<td>四日<br>yokka<br>(4th day of the month)</td>
</tr>
<tr>
<td>五</td>
<td>Five</td>
<td>ご<br>go</td>
<td>いつ(つ)<br>itsu(tsu)</td>
<td>五日<br>itsuka<br>(5th day of the month)</td>
</tr>
<tr>
<td>六</td>
<td>Six</td>
<td>ろく<br>roku</td>
<td>む(っつ)、むい<br>mu(ttsu), mui</td>
<td>六日<br>muika<br>(6th day of the month)</td>
</tr>
<tr>
<td>七</td>
<td>Seven</td>
<td>しち<br>shichi</td>
<td>なな(つ), なな<br>nana(tsu), nana</td>
<td>七日<br>nanoka<br>(7th day of the month)</td>
</tr>
<tr>
<td>八</td>
<td>Eight</td>
<td>はち<br>hachi</td>
<td>や(っつ), よう<br>ya(ttsu), you</td>
<td>八日<br>youka<br>(8th day of the month)</td>
</tr>
<tr>
<td>九</td>
<td>Nine</td>
<td>きゅう, く<br>kyuu, ku</td>
<td>ここの(つ)<br>kokono(tsu)</td>
<td>九日<br>kokonoka<br>(9th day of the month)</td>
</tr>
<tr>
<td>十</td>
<td>Ten</td>
<td>じゅう<br>juu</td>
<td>とう, とお<br>tou, too</td>
<td>十日<br>tooka<br>(10th day of the month)</td>
</tr>
<tr>
<td>百</td>
<td>Hundred</td>
<td>ひゃく<br>hyaku</td>
<td>—</td>
<td>百円<br>hyakuen<br>(100 yen)</td>
</tr>
<tr>
<td>五</td>
<td>Five</td>
<td>ご<br>go</td>
<td>いつ(つ)<br>itsu(tsu)</td>
<td>五日<br>itsuka<br>(5th day of the month)</td>
</tr>
<tr>
<td>千</td>
<td>Thousand</td>
<td>せん<br>sen</td>
<td>ち<br>chi</td>
<td>千円、千葉県<br>senen, chibaken<br>(1,000 yen), (Chiba prefecture)</td>
</tr>
<tr>
<td>万</td>
<td>Ten thousand</td>
<td>まん<br>man</td>
<td>—</td>
<td>一万円、万年筆<br>ichimanen, mannenpitsu<br>(10,000 yen), (fountain pen)</td>
</tr>
<tr>
<td>億</td>
<td>Hundred-million</td>
<td>おく<br>oku</td>
<td>ー</td>
<td>一億円<br>ichiokuen<br>(100,000,000 yen)</td>
</tr>
</tbody>
</table>
<p> </p>
<p> </p>
<h3>Kanji related to Time </h3>
<table>
<colgroup> <col width="12%"> <col width="15%"> <col width="20%"> <col width="20%"> <col width="33%"> </colgroup>
<thead>
<tr>
<th>Kanji</th>
<th>Meaning</th>
<th>Onyomi</th>
<th>Kunyomi</th>
<th>Vocabulary</th>
</tr>
</thead>
<tbody>
<tr>
<td>日</td>
<td>Day, sun</td>
<td>にち, じつ<br>nichi, jitsu</td>
<td>ひ, か<br>hi, ka</td>
<td>日曜日、休日<br>nichiyoubi, kyuujitsu<br>(Sunday), (holiday)</td>
</tr>
<tr>
<td>週</td>
<td>Week</td>
<td>しゅう<br>shuu</td>
<td>—</td>
<td>来週、週末<br>raishuu, shuumatsu<br>(next week), (weekend)</td>
</tr>
<tr>
<td>月</td>
<td>Month, moon</td>
<td>げつ, がつ<br>getsu, gatsu</td>
<td>つき<br>tsuki</td>
<td>月、月曜日<br>tsuki, getsuyoubi<br>(moon), (Monday)</td>
</tr>
<tr>
<td>年</td>
<td>Year</td>
<td>ねん<br>nen</td>
<td>とし<br>toshi</td>
<td>今年、去年<br>kotoshi, kyonen<br>(this year), (last year)</td>
</tr>
<tr>
<td>時</td>
<td>Time, hour</td>
<td>じ<br>ji</td>
<td>とき<br>toki</td>
<td>何時、時々<br>nanji, tokidoki<br>(what time), (sometimes)</td>
</tr>
<tr>
<td>間</td>
<td>Interval</td>
<td>かん<br>kan</td>
<td>あいだ, ま<br>aida, ma</td>
<td>時間<br>jikan<br>(time)</td>
</tr>
<tr>
<td>分</td>
<td>Minute, part, understand</td>
<td>ぶん, ふん, ぶ<br>bun, fun, bu</td>
<td>わ(かる)<br>wa(karu)</td>
<td>２分、 自分、 分かる<br>nifun, jibun, wakaru<br>(two minutes), (oneself), (to understand)</td>
</tr>
<tr>
<td>午</td>
<td>Noon</td>
<td>ご<br>go</td>
<td>ご</td>
<td>午前<br>gozen<br>(morning, A.M.)</td>
</tr>
<tr>
<td>前</td>
<td>Before</td>
<td>ぜん<br>zen</td>
<td>まえ<br>mae</td>
<td>前回、駅前<br>zenkai, ekimae<br>(last time), (front of the station)</td>
</tr>
<tr>
<td>後</td>
<td>After</td>
<td>ご, こう<br>go, kou</td>
<td>あと, うし<br>ato, ushi</td>
<td>後で、後ろ<br>atode, ushiro<br>(after), (behind)</td>
</tr>
<tr>
<td>今</td>
<td>Now</td>
<td>こん<br>kon</td>
<td>いま<br>ima</td>
<td>今回、今<br>konkai, ima<br>(this time), (now)</td>
</tr>
<tr>
<td>先</td>
<td>Previous</td>
<td>せん<br>sen</td>
<td>さき<br>saki</td>
<td>先週、先生<br>senshuu, sensei<br>(last week), (teacher)</td>
</tr>
<tr>
<td>来</td>
<td>Next, come</td>
<td>らい<br>rai</td>
<td>く(る)<br>ku(ru)</td>
<td>来月、来る<br>raigetsu, kuru<br>(next month), (to come)</td>
</tr>
<tr>
<td>毎</td>
<td>Every</td>
<td>まい<br>mai</td>
<td>ごと<br>goto</td>
<td>毎日<br>mainichi<br>(every day)</td>
</tr>
</tbody>
</table>
<p> </p>
<p> </p>
<h3>Kanji related to People, Places, &amp; Things</h3>
<table>
<colgroup> <col width="12%"> <col width="15%"> <col width="20%"> <col width="20%"> <col width="33%"> </colgroup>
<thead>
<tr>
<th>Kanji</th>
<th>Meaning</th>
<th>Onyomi</th>
<th>Kunyomi</th>
<th>Vocabulary</th>
</tr>
</thead>
<tbody>
<tr>
<td>人</td>
<td>Person</td>
<td>じん, にん<br>jin, nin</td>
<td>ひと<br>hito</td>
<td>アメリカ人、外人<br>amerikajin, gaijin<br>(American person), (foreigner)</td>
</tr>
<tr>
<td>男</td>
<td>Man</td>
<td>だん, なん<br>dan, nan</td>
<td>おとこ<br>otoko</td>
<td>男の子、男性<br>otokonoko, dansei<br>(boy), (male)</td>
</tr>
<tr>
<td>女</td>
<td>Woman</td>
<td>じょ<br>jo</td>
<td>おんな<br>onna</td>
<td>女の子、女性<br>onnanoko, josei<br>(girl), (female)</td>
</tr>
<tr>
<td>子</td>
<td>Child</td>
<td>し<br>shi</td>
<td>こ<br>ko</td>
<td>子供、菓子屋<br>kodomo, kashiya<br>(child), (kashiya)</td>
</tr>
<tr>
<td>母</td>
<td>Mother</td>
<td>ぼ<br>bo</td>
<td>はは<br>haha</td>
<td>母<br>haha<br>(mother)</td>
</tr>
<tr>
<td>父</td>
<td>Father</td>
<td>ふ<br>fu</td>
<td>ちち<br>chichi</td>
<td>父<br>chichi<br>(father)</td>
</tr>
<tr>
<td>友</td>
<td>Friend</td>
<td>ゆう<br>yuu</td>
<td>とも<br>tomo</td>
<td>友達<br>tomodachi<br>(friend)</td>
</tr>
<tr>
<td>本</td>
<td>Book, Origin</td>
<td>ほん<br>hon</td>
<td>もと<br>moto</td>
<td>日本、本当<br>nihon, hontou<br>(Japan), (reality)</td>
</tr>
<tr>
<td>気</td>
<td>Spirit</td>
<td>き<br>ki</td>
<td>—</td>
<td>元気<br>genki<br>(lively, fine)</td>
</tr>
<tr>
<td>生</td>
<td>Life</td>
<td>せい, しょう<br>sei, shou</td>
<td>い(きる), う(まれる)<br>i(kiru), u(mareru)</td>
<td>生徒、生きる<br>seito, ikiru<br>(pupil), (to live)</td>
</tr>
<tr>
<td>車</td>
<td>Car</td>
<td>しゃ<br>sha</td>
<td>くるま<br>kuruma</td>
<td>車、電車<br>kuruma, densha<br>(car), (train)</td>
</tr>
<tr>
<td>語</td>
<td>Language</td>
<td>ご<br>go</td>
<td>かた(る)<br>kata(ru)</td>
<td>英語、日本語<br>eigo, nihongo<br>(English), (Japanese)</td>
</tr>
<tr>
<td>耳</td>
<td>Ear</td>
<td>じ<br>ji</td>
<td>みみ<br>mimi</td>
<td>耳<br>mimi<br>(ear)</td>
</tr>
<tr>
<td>手</td>
<td>Hand</td>
<td>しゅ<br>shu</td>
<td>て<br>te</td>
<td>手紙、選手<br>tegami, senshu<br>(letter), (athlete)</td>
</tr>
<tr>
<td>足</td>
<td>Foot</td>
<td>そく<br>soku</td>
<td>あし、た(す)<br>ashi, ta(su)</td>
<td>足<br>ashi<br>(foot)</td>
</tr>
<tr>
<td>目</td>
<td>Eye</td>
<td>もく<br>moku</td>
<td>め<br>me</td>
<td>目<br>me<br>(eye)</td>
</tr>
<tr>
<td>口</td>
<td>Mouth</td>
<td>こう<br>kou</td>
<td>くち<br>kuchi</td>
<td>入り口<br>iriguchi<br>(entrance)</td>
</tr>
<tr>
<td>店</td>
<td>Shop</td>
<td>てん<br>ten</td>
<td>みせ<br>mise</td>
<td>喫茶店<br>kissaten<br>(coffee shop)</td>
</tr>
<tr>
<td>駅</td>
<td>Station</td>
<td>えき<br>eki</td>
<td>—</td>
<td>駅弁<br>ekiben<br>(station bento)</td>
</tr>
<tr>
<td>道</td>
<td>Street</td>
<td>どう<br>dou</td>
<td>みち<br>michi</td>
<td>道、道具<br>michi, dougu<br>(road), (tool)</td>
</tr>
<tr>
<td>国</td>
<td>Country</td>
<td>こく<br>koku</td>
<td>くに<br>kuni</td>
<td>国、外国<br>kuni, gaikoku<br>(country), (foreign)</td>
</tr>
<tr>
<td>学</td>
<td>Study</td>
<td>がく<br>gaku</td>
<td>まな(ぶ)<br>mana(bu)</td>
<td>大学、学ぶ<br>daigaku, manabu<br>(university), (to learn)</td>
</tr>
<tr>
<td>校</td>
<td>School</td>
<td>こう<br>kou</td>
<td>—</td>
<td>学校<br>gakkou<br>(school)</td>
</tr>
<tr>
<td>名</td>
<td>Name</td>
<td>めい, みょう<br>mei, myou</td>
<td>な<br>na</td>
<td>名前<br>namae<br>(name)</td>
</tr>
<tr>
<td>円</td>
<td>Yen, circle</td>
<td>えん<br>en</td>
<td>まる(い)<br>maru(i)</td>
<td>円い<br>marui<br>(round)</td>
</tr>
<tr>
<td>半</td>
<td>Half</td>
<td>はん<br>han</td>
<td>なか(ば)<br>naka(ba)</td>
<td>半分<br>hanbun<br>(half)</td>
</tr>
<tr>
<td>全</td>
<td>All</td>
<td>ぜん<br>zen</td>
<td>まった(く), すべて<br>matta(ku), sube(te)</td>
<td>全然、全く<br>zenzen, mattaku<br>(completely, not at all), (really)</td>
</tr>
<tr>
<td>何</td>
<td>What</td>
<td>か<br>ka</td>
<td>なん, なに<br>nan, nani</td>
<td>何、何日<br>nani, nannichi<br>(what), (what day)</td>
</tr>
</tbody>
</table>
<p> </p>
<p> </p>
<h3>Kanji related to Nature &amp; Directions</h3>
<table>
<colgroup> <col width="12%"> <col width="15%"> <col width="20%"> <col width="20%"> <col width="33%"> </colgroup>
<thead>
<tr>
<th>Kanji</th>
<th>Meaning</th>
<th>Onyomi</th>
<th>Kunyomi</th>
<th>Vocabulary</th>
</tr>
</thead>
<tbody>
<tr>
<td>火</td>
<td>Fire</td>
<td>か<br>ka</td>
<td>ひ<br>hi</td>
<td>火、火曜日<br>hi, kayoubi<br>(fire), (Tuesday)</td>
</tr>
<tr>
<td>水</td>
<td>Water</td>
<td>すい<br>sui</td>
<td>みず<br>mizu</td>
<td>水、水曜日<br>mizu, suiyoubi<br>(water), (Wednesday)</td>
</tr>
<tr>
<td>木</td>
<td>Tree</td>
<td>もく<br>moku</td>
<td>き<br>ki</td>
<td>木、木曜日<br>ki, mokuyoubi<br>(tree), (Thursday)</td>
</tr>
<tr>
<td>金</td>
<td>Money, gold</td>
<td>きん<br>kin</td>
<td>かね<br>kane</td>
<td>金、金曜日<br>kane, kinyoubi<br>(money), (Friday)</td>
</tr>
<tr>
<td>土</td>
<td>Earth</td>
<td>ど, to</td>
<td>つち<br>tsuchi</td>
<td>土地、土曜日<br>tochi, doyoubi<br>(land), (Saturday)</td>
</tr>
<tr>
<td>海</td>
<td>Sea</td>
<td>かい<br>kai</td>
<td>うみ<br>umi</td>
<td>海、海外<br>umi, kaigai<br>(sea), (overseas)</td>
</tr>
<tr>
<td>川</td>
<td>River</td>
<td>せん<br>sen</td>
<td>かわ<br>kawa</td>
<td>川<br>kawa<br>(river)</td>
</tr>
<tr>
<td>山</td>
<td>Mountain</td>
<td>さん<br>san</td>
<td>やま<br>yama</td>
<td>山、富士山<br>yama, fujisan<br>(mountain), (Mt Fuji)</td>
</tr>
<tr>
<td>花</td>
<td>Flower</td>
<td>か<br>ka</td>
<td>はな<br>hana</td>
<td>花火、花粉症<br>hanabi, kafunshou<br>(fireworks), (hay fever)</td>
</tr>
<tr>
<td>天</td>
<td>Heaven</td>
<td>てん<br>ten</td>
<td>あめ, あま<br>ame, ama</td>
<td>天気<br>tenki<br>(weather)</td>
</tr>
<tr>
<td>空</td>
<td>Sky, empty</td>
<td>くう<br>kuu</td>
<td>そら, あける<br>sora, a(keru)</td>
<td>空、空港<br>sora, kuukou<br>(sky), (airport)</td>
</tr>
<tr>
<td>晴</td>
<td>Sunny</td>
<td>せい<br>sei</td>
<td>は(れ)<br>ha(re)</td>
<td>晴れ<br>hare<br>(sunny)</td>
</tr>
<tr>
<td>雨</td>
<td>Rain</td>
<td>う<br>u</td>
<td>あめ<br>ame</td>
<td>雨<br>ame<br>(rain)</td>
</tr>
<tr>
<td>雪</td>
<td>Snow</td>
<td>せつ<br>setsu</td>
<td>ゆき<br>yuki</td>
<td>雪<br>yuki<br>(snow)</td>
</tr>
<tr>
<td>雲</td>
<td>Cloud</td>
<td>うん<br>un</td>
<td>くも<br>kumo</td>
<td>曇り<br>kumori<br>(cloudy)</td>
</tr>
<tr>
<td>風</td>
<td>Wind</td>
<td>ふう<br>fuu</td>
<td>かぜ<br>kaze</td>
<td>風、台風<br>kaze, taifuu<br>(wind), (taiphoon)</td>
</tr>
<tr>
<td>電</td>
<td>Electricity</td>
<td>でん<br>den</td>
<td>—</td>
<td>電気<br>denki<br>(electricity)</td>
</tr>
<tr>
<td>外</td>
<td>Outside</td>
<td>がい<br>gai</td>
<td>そと,はず(れる)<br>soto, hazu(reru)</td>
<td>外、外国<br>soto, gaikoku<br>(outside), (foreign country)</td>
</tr>
<tr>
<td>内</td>
<td>Inside</td>
<td>ない<br>nai</td>
<td>うち<br>uchi</td>
<td>内、車内<br>uchi, shanai<br>(inside), (inside the car/train)</td>
</tr>
<tr>
<td>上</td>
<td>Above</td>
<td>じょう<br>jou</td>
<td>うえ, あ(げる)<br>ue, a(geru)</td>
<td>上、上手<br>ue, jouzu<br>(above), (good at)</td>
</tr>
<tr>
<td>下</td>
<td>Below</td>
<td>か, げ<br>ka, ge</td>
<td>した、く(だる)<br>shita, ku(daru)</td>
<td>下、下さい<br>shita, kudasai<br>(below), (please)</td>
</tr>
<tr>
<td>右</td>
<td>Right</td>
<td>ゆう<br>yuu</td>
<td>みぎ<br>migi</td>
<td>右<br>migi<br>(right)</td>
</tr>
<tr>
<td>左</td>
<td>Left</td>
<td>さ<br>sa</td>
<td>ひだり<br>hidari</td>
<td>左<br>hidari<br>(left)</td>
</tr>
<tr>
<td>中</td>
<td>Middle</td>
<td>ちゅう, じゅう<br>chuu, juu</td>
<td>なか<br>naka</td>
<td>中、中学校<br>naka, chuugakkou<br>(middle, in), (junior high school)</td>
</tr>
<tr>
<td>北</td>
<td>North</td>
<td>ほく</td>
<td>きた<br>kita</td>
<td>北<br>kita<br>(north)</td>
</tr>
<tr>
<td>西</td>
<td>West</td>
<td>せい, さい<br>sei, sai</td>
<td>にし<br>nishi</td>
<td>西<br>nishi<br>(west)</td>
</tr>
<tr>
<td>東</td>
<td>East</td>
<td>とう<br>tou</td>
<td>ひがし<br>higashi</td>
<td>東、東京<br>higashi, toukyou<br>(East), (Tokyo)</td>
</tr>
<tr>
<td>南</td>
<td>South</td>
<td>なん<br>nan</td>
<td>みなみ<br>minami</td>
<td>南<br>minami<br>(south)</td>
</tr>
</tbody>
</table>
<p> </p>
<p> </p>
<h3>Kanji related to Verbs</h3>
<table>
<colgroup> <col width="12%"> <col width="15%"> <col width="20%"> <col width="20%"> <col width="33%"> </colgroup>
<thead>
<tr>
<th>Kanji</th>
<th>Meaning</th>
<th>Onyomi</th>
<th>Kunyomi</th>
<th>Vocabulary</th>
</tr>
</thead>
<tbody>
<tr>
<td>見</td>
<td>See</td>
<td>けん<br>ken</td>
<td>み(る)<br>mi(ru)</td>
<td>見る、見せる<br>miru, miseru<br>(to see), (to show)</td>
</tr>
<tr>
<td>聞</td>
<td>Hear</td>
<td>もん, ぶん<br>mon, bun</td>
<td>き(く)<br>ki(ku)</td>
<td>聞く<br>kiku<br>(to listen, to hear)</td>
</tr>
<tr>
<td>書</td>
<td>Write</td>
<td>しょ<br>jo</td>
<td>か(く)<br>ka(ku)</td>
<td>書く、辞書<br>kaku, jisho<br>(to write), (dictionary)</td>
</tr>
<tr>
<td>言</td>
<td>Say</td>
<td>げん<br>gen</td>
<td>い(う)<br>i(u)</td>
<td>言う<br>iu<br>(to say)</td>
</tr>
<tr>
<td>話</td>
<td>Talk</td>
<td>わ<br>wa</td>
<td>はなし, はな(す)<br>hanashi, hana(su)</td>
<td>話す、電話<br>hanasu, denwa<br>(to talk), (telephone)</td>
</tr>
<tr>
<td>読</td>
<td>Read</td>
<td>どく<br>doku</td>
<td>よ(む)<br>yo(mu)</td>
<td>読む<br>yomu<br>(to read)</td>
</tr>
<tr>
<td>行</td>
<td>Go</td>
<td>こう<br>kou</td>
<td>い(く), おこな(う)<br>i(ku), okona(u)</td>
<td>行く、銀行<br>iku, ginkou<br>(to go), (bank)</td>
</tr>
<tr>
<td>買</td>
<td>Buy</td>
<td>ばい<br>bai</td>
<td>か(う)<br>ka(u)</td>
<td>買う、買い物<br>kau, kaimono<br>(to buy), (shopping)</td>
</tr>
<tr>
<td>出</td>
<td>Exit</td>
<td>しゅつ<br>shuu</td>
<td>で(る), だ(す)<br>de(ru), da(su)</td>
<td>出る、出口<br>deru, deguchi<br>(to exit), (exit)</td>
</tr>
<tr>
<td>入</td>
<td>Enter, put in</td>
<td>にゅう<br>nyuu</td>
<td>はい(る), い(れる)<br>hai(ru), i(reru)</td>
<td>入る、立ち入り禁止<br>(to enter), (no entry)</td>
</tr>
<tr>
<td>食</td>
<td>Eat</td>
<td>しょく<br>shoku</td>
<td>た(べる)<br>ta(beru)</td>
<td>食べる、食事<br>taberu, shokuji<br>(to eat), (meal)</td>
</tr>
<tr>
<td>飲</td>
<td>Drink</td>
<td>いん<br>in</td>
<td>の(む)<br>no(mu)</td>
<td>飲む、飲み物<br>nomu, nomimono<br>(to drink), (beverage)</td>
</tr>
<tr>
<td>休</td>
<td>Rest</td>
<td>きゅう<br>kyuu</td>
<td>やす(む), やす(み)<br>yasu(mu), yasu(mi)</td>
<td>休む、休日<br>yasumu, kyuujitsu<br>(to rest), (holiday)</td>
</tr>
<tr>
<td>会</td>
<td>Meet</td>
<td>かい<br>kai</td>
<td>あ(う)<br>a(u)</td>
<td>会う、会社<br>au, kaisha<br>(to meet), (company)</td>
</tr>
</tbody>
</table>
<p> </p>
<p> </p>
<h3>Kanji related to Adjectives</h3>
<table>
<colgroup> <col width="12%"> <col width="15%"> <col width="20%"> <col width="20%"> <col width="33%"> </colgroup>
<thead>
<tr>
<th>Kanji</th>
<th>Meaning</th>
<th>Onyomi</th>
<th>Kunyomi</th>
<th>Vocabulary</th>
</tr>
</thead>
<tbody>
<tr>
<td>多</td>
<td>A lot</td>
<td>た<br>ta</td>
<td>おお(い)<br>oo(i)</td>
<td>多い、多分<br>ooi, tabun<br>(many), (probably)</td>
</tr>
<tr>
<td>少</td>
<td>A little</td>
<td>しょう<br>shou</td>
<td>すこ(し), すく(ない)<br>suko(shi), suku(nai)</td>
<td>少し<br>sukoshi<br>(a little)</td>
</tr>
<tr>
<td>古</td>
<td>Old</td>
<td>こ<br>ko</td>
<td>ふる(い)<br>furu(i)</td>
<td>古い<br>furui<br>(old)</td>
</tr>
<tr>
<td>新</td>
<td>New</td>
<td>しん<br>shin</td>
<td>あたら(しい)<br>atara(shii)</td>
<td>新しい、新聞<br>atarashii, shinbun<br>(new), (newspaper)</td>
</tr>
<tr>
<td>大</td>
<td>Big</td>
<td>だい, たい<br>dai, tai</td>
<td>おお(きい)<br>oo(kii)</td>
<td>大きい、大変<br>ookii, taihen<br>(big), (very, terribly)</td>
</tr>
<tr>
<td>小</td>
<td>Small</td>
<td>しょう<br>shou</td>
<td>ちい(さい)、こ<br>chii(sai), ko</td>
<td>小さい<br>chiisai<br>(small)</td>
</tr>
<tr>
<td>長</td>
<td>Long, leader</td>
<td>ちょう<br>chou</td>
<td>なが(い)<br>naga(i)</td>
<td>長い、部長<br>nagai, buchou<br>(long), (manager)</td>
</tr>
<tr>
<td>短</td>
<td>Short</td>
<td>たん<br>tan</td>
<td>みじか(い)<br>mijika(i)</td>
<td>短い<br>mijikai<br>(short)</td>
</tr>
<tr>
<td>遠</td>
<td>Far</td>
<td>えん<br>en</td>
<td>とお(い)<br>too(i)</td>
<td>遠い<br>tooi<br>(far)</td>
</tr>
<tr>
<td>近</td>
<td>Near</td>
<td>きん, こん<br>kin, kon</td>
<td>ちか(い)<br>chika(i)</td>
<td>近い、近く<br>chikai, chikaku<br>(close), (near)</td>
</tr>
<tr>
<td>白</td>
<td>White</td>
<td>はく<br>haku</td>
<td>しろ, しろ(い)<br>shiro, shiro(i)</td>
<td>白い、面白い<br>shiroi, omoshiroi<br>(white), (interesting)</td>
</tr>
<tr>
<td>黒</td>
<td>Black</td>
<td>こく<br>koku</td>
<td>くろ、くろ(い)<br>kuro, kuro(i)</td>
<td>黒、真っ黒<br>kuro, makkuro<br>(black), (pitch black)</td>
</tr>
<tr>
<td>高</td>
<td>Expensive, high</td>
<td>こう<br>kou</td>
<td>たか(い)<br>taka(i)</td>
<td>高い<br>takai<br>(expensive, tall)</td>
</tr>
<tr>
<td>安</td>
<td>Cheap, safety</td>
<td>あん<br>an</td>
<td>やす(い)<br>yasu(i)</td>
<td>安い、安心<br>yasui, anshin<br>(cheap), (relief)</td>
</tr>
"""

# Парсим HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Ищем все строки таблицы
rows = soup.find_all('tr')

# Извлечение кандзи и каны
kanjis = []
for row in rows:
    columns = row.find_all('td')  # Находим все ячейки в строке
    if len(columns) >= 2:  # Проверяем, что ячеек достаточно
        kanji = columns[0].get_text(strip=True)
        onyomi = columns[2].get_text(strip=True)
        kunyuomi = columns[3].get_text(strip=True)
        kanjis.append((kanji, onyomi, kunyuomi))

# Сохранение в файл
with open('kanji_yomi.txt', 'w', encoding='utf-8') as file:
    for kanji, onyomi, kunyuomi in kanjis:
        file.write(f"{kanji}\t{onyomi}\t{kunyuomi}\n")

print("Данные сохранены в файл kanji_yomi.txt")
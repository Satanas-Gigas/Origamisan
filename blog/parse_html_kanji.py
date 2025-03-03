from bs4 import BeautifulSoup

# Пример HTML-кода (замените на свой)
html_content = """
<tr>
<td style="text-align:center;" valign="top" width="20">5B89</td>
<td style="text-align:center;" valign="top" width="30"><a title="安" href="https://nihongoichiban.com/2011/04/09/%e5%ae%89/" target="_blank">安</a></td>
<td valign="top" width="200">AN</td>
<td valign="top" width="200">yasu(i)</td>
<td valign="top" width="200">peace, cheap, safety</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E00</td>
<td style="text-align:center;" valign="top" width="30"><a title="一" href="https://nihongoichiban.com/2011/03/21/%e4%b8%80/" target="_blank">一</a></td>
<td valign="top" width="200">ICHI, ITSU</td>
<td valign="top" width="200">hito(tsu), hito-</td>
<td valign="top" width="200">one</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">98F2</td>
<td style="text-align:center;" valign="top" width="30"><a title="飲" href="https://nihongoichiban.com/2011/04/09/%e9%a3%b2/" target="_blank">飲</a></td>
<td valign="top" width="200">IN</td>
<td valign="top" width="200">no(mu)</td>
<td valign="top" width="200">to drink</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">53F3</td>
<td style="text-align:center;" valign="top" width="30"><a title="右" href="https://nihongoichiban.com/2011/04/09/%e5%8f%b3/" target="_blank">右</a></td>
<td valign="top" width="200">U, YUU</td>
<td valign="top" width="200">migi</td>
<td valign="top" width="200">right</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">96E8</td>
<td style="text-align:center;" valign="top" width="30"><a title="雨" href="https://nihongoichiban.com/2011/03/26/%e9%9b%a8/" target="_blank">雨</a></td>
<td valign="top" width="200">U</td>
<td valign="top" width="200">ame</td>
<td valign="top" width="200">rain</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">99C5</td>
<td style="text-align:center;" valign="top" width="30"><a title="駅" href="https://nihongoichiban.com/2011/04/09/%e9%a7%85/" target="_blank">駅</a></td>
<td valign="top" width="200">EKI</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">station</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5186</td>
<td style="text-align:center;" valign="top" width="30"><a title="円" href="https://nihongoichiban.com/2011/03/21/86/" target="_blank">円</a></td>
<td valign="top" width="200">EN</td>
<td valign="top" width="200">maru(i)</td>
<td valign="top" width="200">circle, Yen, round</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">706B</td>
<td style="text-align:center;" valign="top" width="30"><a title="火" href="https://nihongoichiban.com/2011/03/24/%e7%81%ab/" target="_blank">火</a></td>
<td valign="top" width="200">KA</td>
<td valign="top" width="200">hi</td>
<td valign="top" width="200">fire</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">82B1</td>
<td style="text-align:center;" valign="top" width="30"><a title="花" href="https://nihongoichiban.com/2011/04/09/%e8%8a%b1/" target="_blank">花</a></td>
<td valign="top" width="200">KA</td>
<td valign="top" width="200">hana</td>
<td valign="top" width="200">flower, blossom</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E0B</td>
<td style="text-align:center;" valign="top" width="30"><a title="下" href="https://nihongoichiban.com/2011/03/26/%e4%b8%8b/" target="_blank">下</a></td>
<td valign="top" width="200">KA, GE</td>
<td valign="top" width="200">shimo, sa(geru), o(rosu), ku(daru)</td>
<td valign="top" width="200">below, down</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4F55</td>
<td style="text-align:center;" valign="top" width="30"><a title="何" href="https://nihongoichiban.com/2011/04/09/%e4%bd%95/" target="_blank">何</a></td>
<td valign="top" width="200">KA</td>
<td valign="top" width="200">nani</td>
<td valign="top" width="200">what, how many, which</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4FLA</td>
<td style="text-align:center;" valign="top" width="30"><a title="会" href="https://nihongoichiban.com/2011/04/09/%e4%bc%9a/" target="_blank">会</a></td>
<td valign="top" width="200">KAI, E</td>
<td valign="top" width="200">a(u)</td>
<td valign="top" width="200">to meet, to come together, society</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5916</td>
<td style="text-align:center;" valign="top" width="30"><a title="外" href="https://nihongoichiban.com/2011/04/09/%e5%a4%96/" target="_blank">外</a></td>
<td valign="top" width="200">GAI, GE</td>
<td valign="top" width="200">soto, hoka, hazu(reru), hazu(su)</td>
<td valign="top" width="200">outside, other, disconnect</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5B66</td>
<td style="text-align:center;" valign="top" width="30"><a title="学" href="https://nihongoichiban.com/2011/04/09/%e5%ad%a6/" target="_blank">学</a></td>
<td valign="top" width="200">GAKU</td>
<td valign="top" width="200">mana(bu)</td>
<td valign="top" width="200">school, science, learning</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">9593</td>
<td style="text-align:center;" valign="top" width="30"><a title="間" href="https://nihongoichiban.com/2011/03/29/%e9%96%93/" target="_blank">間</a></td>
<td valign="top" width="200">KAN, KEN</td>
<td valign="top" width="200">aida</td>
<td valign="top" width="200">time, time span</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6C17</td>
<td style="text-align:center;" valign="top" width="30"><a title="気" href="https://nihongoichiban.com/2011/04/09/%e6%b0%97/" target="_blank">気</a></td>
<td valign="top" width="200">KI, KE</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">soul, spirit</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E5D</td>
<td style="text-align:center;" valign="top" width="30"><a title="九" href="https://nihongoichiban.com/2011/03/21/%e4%b9%9d/" target="_blank">九</a></td>
<td valign="top" width="200">KYUU, KU</td>
<td valign="top" width="200">kokono(tsu), kokono-</td>
<td valign="top" width="200">nine</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4F11</td>
<td style="text-align:center;" valign="top" width="30"><a title="休" href="https://nihongoichiban.com/2011/04/03/%e4%bc%91/" target="_blank">休</a></td>
<td valign="top" width="200">KYUU</td>
<td valign="top" width="200">yasu(mu)</td>
<td valign="top" width="200">to rest</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">9B5A</td>
<td style="text-align:center;" valign="top" width="30"><a title="魚" href="https://nihongoichiban.com/2011/04/09/%e9%ad%9a/" target="_blank">魚</a></td>
<td valign="top" width="200">GYO</td>
<td valign="top" width="200">sakana, uo</td>
<td valign="top" width="200">fish</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">91D1</td>
<td style="text-align:center;" valign="top" width="30"><a title="金" href="https://nihongoichiban.com/2011/03/26/%e9%87%91/" target="_blank">金</a></td>
<td valign="top" width="200">KIN, KON</td>
<td valign="top" width="200">kane</td>
<td valign="top" width="200">gold, metal, money</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">7A7A</td>
<td style="text-align:center;" valign="top" width="30"><a title="空" href="https://nihongoichiban.com/2011/04/09/%e7%a9%ba/" target="_blank">空</a></td>
<td valign="top" width="200">KUU</td>
<td valign="top" width="200">sora, a(keru), kara</td>
<td valign="top" width="200">sky, to become free, empty</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6708</td>
<td style="text-align:center;" valign="top" width="30"><a title="月" href="https://nihongoichiban.com/2011/03/24/%e6%9c%88/" target="_blank">月</a></td>
<td valign="top" width="200">GETSU, GATSU</td>
<td valign="top" width="200">tsuki</td>
<td valign="top" width="200">month, moon</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">898B</td>
<td style="text-align:center;" valign="top" width="30"><a title="見" href="https://nihongoichiban.com/2011/04/03/%e8%a6%8b/" target="_blank">見</a></td>
<td valign="top" width="200">KEN</td>
<td valign="top" width="200">mi(ru), mi(eru), mi(seru)</td>
<td valign="top" width="200">to see, to be visible, to show</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8A00</td>
<td style="text-align:center;" valign="top" width="30"><a title="言" href="https://nihongoichiban.com/2011/04/09/%e8%a8%80/" target="_blank">言</a></td>
<td valign="top" width="200">GEN, GON</td>
<td valign="top" width="200">i(u)</td>
<td valign="top" width="200">word, to talk</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">53E4</td>
<td style="text-align:center;" valign="top" width="30"><a title="古" href="https://nihongoichiban.com/2011/04/09/%e5%8f%a4/" target="_blank">古</a></td>
<td valign="top" width="200">KO</td>
<td valign="top" width="200">furu(i)</td>
<td valign="top" width="200">old, used</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E94</td>
<td style="text-align:center;" valign="top" width="30"><a title="五" href="https://nihongoichiban.com/2011/03/21/%e4%ba%94/">五</a></td>
<td valign="top" width="200">GO</td>
<td valign="top" width="200">itsu(tsu), itsu-</td>
<td valign="top" width="200">five</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5F8C</td>
<td style="text-align:center;" valign="top" width="30"><a title="後" href="https://nihongoichiban.com/2011/04/02/%e5%be%8c/" target="_blank">後</a></td>
<td valign="top" width="200">GO, KOU</td>
<td valign="top" width="200">ato, oku(reru), nochi</td>
<td valign="top" width="200">after, later, back, to stay behind</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5348</td>
<td style="text-align:center;" valign="top" width="30"><a title="午" href="https://nihongoichiban.com/2011/04/02/%e5%8d%88/" target="_blank">午</a></td>
<td valign="top" width="200">GO</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">noon</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8A9E</td>
<td style="text-align:center;" valign="top" width="30"><a title="語" href="https://nihongoichiban.com/2011/04/05/%e8%aa%9e/" target="_blank">語</a></td>
<td valign="top" width="200">GO</td>
<td valign="top" width="200">kata(ru), kata(rau)</td>
<td valign="top" width="200">word, to talk</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6821</td>
<td style="text-align:center;" valign="top" width="30"><a title="校" href="https://nihongoichiban.com/2011/04/09/%e6%a0%a1/" target="_blank">校</a></td>
<td valign="top" width="200">KOU</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">school</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">53E3</td>
<td style="text-align:center;" valign="top" width="30"><a title="口" href="https://nihongoichiban.com/2011/04/09/%e5%8f%a3/" target="_blank">口</a></td>
<td valign="top" width="200">KOU, KU</td>
<td valign="top" width="200">kuchi</td>
<td valign="top" width="200">mouth</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">884C</td>
<td style="text-align:center;" valign="top" width="30"><a title="行" href="https://nihongoichiban.com/2011/04/05/jlpt-kanji-行/" target="_blank">行</a></td>
<td valign="top" width="200">KOU</td>
<td valign="top" width="200">i(ku), yu(ku), okona(u)</td>
<td valign="top" width="200">to walk. to go, to do, to carry out</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">9AD8</td>
<td style="text-align:center;" valign="top" width="30"><a title="高" href="https://nihongoichiban.com/2011/04/09/%e9%ab%98/" target="_blank">高</a></td>
<td valign="top" width="200">KOU</td>
<td valign="top" width="200">taka(i), taka(maru), taka(meru)</td>
<td valign="top" width="200">high, expensive, increase, quantity</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">56FD</td>
<td style="text-align:center;" valign="top" width="30"><a title="国" href="https://nihongoichiban.com/2011/03/27/%e5%9b%bd/">国</a></td>
<td valign="top" width="200">KOKU</td>
<td valign="top" width="200">kuni</td>
<td valign="top" width="200">country</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4ECA</td>
<td style="text-align:center;" valign="top" width="30"><a title="今" href="https://nihongoichiban.com/2011/04/02/%e4%bb%8a/" target="_blank">今</a></td>
<td valign="top" width="200">KON, KIN</td>
<td valign="top" width="200">ima</td>
<td valign="top" width="200">now</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5DE6</td>
<td style="text-align:center;" valign="top" width="30"><a title="左" href="https://nihongoichiban.com/2011/04/09/%e5%b7%a6/" target="_blank">左</a></td>
<td valign="top" width="200">SA</td>
<td valign="top" width="200">hidari</td>
<td valign="top" width="200">left</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E09</td>
<td style="text-align:center;" valign="top" width="30"><a title="三" href="https://nihongoichiban.com/2011/03/21/%e4%b8%89/" target="_blank">三</a></td>
<td valign="top" width="200">SAN</td>
<td valign="top" width="200">mit(tsu), mi-</td>
<td valign="top" width="200">three</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5C71</td>
<td style="text-align:center;" valign="top" width="30"><a title="山" href="https://nihongoichiban.com/2011/03/27/%e5%b1%b1/">山</a></td>
<td valign="top" width="200">SAN</td>
<td valign="top" width="200">yama</td>
<td valign="top" width="200">mountain</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">56DB</td>
<td style="text-align:center;" valign="top" width="30"><a title="四" href="https://nihongoichiban.com/2011/03/21/%e5%9b%9b/">四</a></td>
<td valign="top" width="200">SHI</td>
<td valign="top" width="200">yo(ttsu), yu(tsu), yo-, yon-</td>
<td valign="top" width="200">four</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5B50</td>
<td style="text-align:center;" valign="top" width="30"><a title="子" href="https://nihongoichiban.com/2011/04/09/%e5%ad%90/" target="_blank">子</a></td>
<td valign="top" width="200">SHI, SU</td>
<td valign="top" width="200">ko</td>
<td valign="top" width="200">child</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8033</td>
<td style="text-align:center;" valign="top" width="30"><a title="耳" href="https://nihongoichiban.com/2011/04/03/%e8%80%b3/" target="_blank">耳</a></td>
<td valign="top" width="200">JI</td>
<td valign="top" width="200">mimi</td>
<td valign="top" width="200">ear</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6642</td>
<td style="text-align:center;" valign="top" width="30"><a title="時" href="https://nihongoichiban.com/2011/03/27/%e6%99%82/">時</a></td>
<td valign="top" width="200">JI</td>
<td valign="top" width="200">toki</td>
<td valign="top" width="200">time, hour</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E03</td>
<td style="text-align:center;" valign="top" width="30"><a title="七" href="https://nihongoichiban.com/2011/03/21/%e4%b8%83/" target="_blank">七</a></td>
<td valign="top" width="200">SHICHI</td>
<td valign="top" width="200">nana(tsu), nana-, nano-</td>
<td valign="top" width="200">seven</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8ECA</td>
<td style="text-align:center;" valign="top" width="30"><a title="車" href="https://nihongoichiban.com/2011/04/09/%e8%bb%8a/" target="_blank">車</a></td>
<td valign="top" width="200">SHA</td>
<td valign="top" width="200">kuruma</td>
<td valign="top" width="200">car, wheel</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">793E</td>
<td style="text-align:center;" valign="top" width="30"><a title="社" href="https://nihongoichiban.com/2011/04/09/%e7%a4%be/" target="_blank">社</a></td>
<td valign="top" width="200">SHA</td>
<td valign="top" width="200">yashiro</td>
<td valign="top" width="200">shinto shrine, society</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">624B</td>
<td style="text-align:center;" valign="top" width="30"><a title="手" href="https://nihongoichiban.com/2011/04/09/%e6%89%8b/" target="_blank">手</a></td>
<td valign="top" width="200">SHU</td>
<td valign="top" width="200">te</td>
<td valign="top" width="200">hand</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">9031</td>
<td style="text-align:center;" valign="top" width="30"><a title="週" href="https://nihongoichiban.com/2011/04/09/%e9%80%b1/" target="_blank">週</a></td>
<td valign="top" width="200">SHUU</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">week</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5341</td>
<td style="text-align:center;" valign="top" width="30"><a title="十" href="https://nihongoichiban.com/2011/03/21/%e5%8d%81/" target="_blank">十</a></td>
<td valign="top" width="200">JUU, JI</td>
<td valign="top" width="200">too, to-</td>
<td valign="top" width="200">ten, cross</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">51FA</td>
<td style="text-align:center;" valign="top" width="30"><a title="出" href="https://nihongoichiban.com/2011/04/03/%e5%87%ba/" target="_blank">出</a></td>
<td valign="top" width="200">SHUTSU</td>
<td valign="top" width="200">da(su), de(ru)</td>
<td valign="top" width="200">to leave, to get out. to take out</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">66F8</td>
<td style="text-align:center;" valign="top" width="30"><a title="書" href="https://nihongoichiban.com/2011/04/09/%e6%9b%b8/" target="_blank">書</a></td>
<td valign="top" width="200">SHO</td>
<td valign="top" width="200">ka(ku)</td>
<td valign="top" width="200">to write</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5073</td>
<td style="text-align:center;" valign="top" width="30"><a title="女" href="https://nihongoichiban.com/2011/04/09/%e5%a5%b3/" target="_blank">女</a></td>
<td valign="top" width="200">JO, NYO</td>
<td valign="top" width="200">onna, me</td>
<td valign="top" width="200">woman, female</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5C0F</td>
<td style="text-align:center;" valign="top" width="30"><a title="小" href="https://nihongoichiban.com/2011/04/09/%e5%b0%8f-2/" target="_blank">小</a></td>
<td valign="top" width="200">SHOU</td>
<td valign="top" width="200">chii(sai), ko-, o-</td>
<td valign="top" width="200">small</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5C11</td>
<td style="text-align:center;" valign="top" width="30"><a title="少" href="https://nihongoichiban.com/2011/04/09/%e5%b0%91/" target="_blank">少</a></td>
<td valign="top" width="200">SHOU</td>
<td valign="top" width="200">suko(shi), suku(nai)</td>
<td valign="top" width="200">a little</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E0A</td>
<td style="text-align:center;" valign="top" width="30"><a title="上" href="https://nihongoichiban.com/2011/03/27/%e4%b8%8a/" target="_blank">上</a></td>
<td valign="top" width="200">SHOU, JOU</td>
<td valign="top" width="200">ue, kami, a(geru), a(garu)</td>
<td valign="top" width="200">above, upper</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">98DF</td>
<td style="text-align:center;" valign="top" width="30"><a title="食" href="https://nihongoichiban.com/2011/04/10/%e9%a3%9f/" target="_blank">食</a></td>
<td valign="top" width="200">SHOKU</td>
<td valign="top" width="200">ta(beru), ku(ru), ku(rau)</td>
<td valign="top" width="200">to eat</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">65B0</td>
<td style="text-align:center;" valign="top" width="30"><a title="新" href="https://nihongoichiban.com/2011/04/10/%e6%96%b0/" target="_blank">新</a></td>
<td valign="top" width="200">SHIN</td>
<td valign="top" width="200">atara(shii), ara(ta), nii-</td>
<td valign="top" width="200">new</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4EBA</td>
<td style="text-align:center;" valign="top" width="30"><a title="人" href="https://nihongoichiban.com/2011/03/24/%e4%ba%ba/" target="_blank">人</a></td>
<td valign="top" width="200">JIN, NIN</td>
<td valign="top" width="200">hito</td>
<td valign="top" width="200">person</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6C34</td>
<td style="text-align:center;" valign="top" width="30"><a title="水" href="https://nihongoichiban.com/2011/03/24/%e6%b0%b4/" target="_blank">水</a></td>
<td valign="top" width="200">SUI</td>
<td valign="top" width="200">mizu</td>
<td valign="top" width="200">water</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">751F</td>
<td style="text-align:center;" valign="top" width="30"><a title="生" href="https://nihongoichiban.com/2011/03/30/%e7%94%9f/" target="_blank">生</a></td>
<td valign="top" width="200">SEI, SHOU</td>
<td valign="top" width="200">i(kiru), u(mu), ha(yasu), nama, ki</td>
<td valign="top" width="200">to live, to grow, to be born, raw</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">897F</td>
<td style="text-align:center;" valign="top" width="30"><a title="西" href="https://nihongoichiban.com/2011/04/06/%e8%a5%bf/" target="_blank">西</a></td>
<td valign="top" width="200">SEI, SAI</td>
<td valign="top" width="200">nishi</td>
<td valign="top" width="200">west</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5DDD</td>
<td style="text-align:center;" valign="top" width="30"><a title="川" href="https://nihongoichiban.com/2011/03/27/%e5%b7%9d/">川</a></td>
<td valign="top" width="200">SEN</td>
<td valign="top" width="200">kawa</td>
<td valign="top" width="200">river</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5343</td>
<td style="text-align:center;" valign="top" width="30"><a title="千" href="https://nihongoichiban.com/2011/03/21/%e5%8d%83/" target="_blank">千</a></td>
<td valign="top" width="200">SEN</td>
<td valign="top" width="200">chi</td>
<td valign="top" width="200">thousand</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5148</td>
<td style="text-align:center;" valign="top" width="30"><a title="先" href="https://nihongoichiban.com/2011/04/02/%e5%85%88/" target="_blank">先</a></td>
<td valign="top" width="200">SEN</td>
<td valign="top" width="200">saki</td>
<td valign="top" width="200">before, in future</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">524D</td>
<td style="text-align:center;" valign="top" width="30"><a title="前" href="https://nihongoichiban.com/2011/04/01/%e5%89%8d/" target="_blank">前</a></td>
<td valign="top" width="200">ZEN</td>
<td valign="top" width="200">mae</td>
<td valign="top" width="200">before</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8DB3</td>
<td style="text-align:center;" valign="top" width="30"><a title="足" href="https://nihongoichiban.com/2011/04/10/%e8%b6%b3/" target="_blank">足</a></td>
<td valign="top" width="200">SOKU</td>
<td valign="top" width="200">ashi, ta(riru), ta(su)</td>
<td valign="top" width="200">foot, to be sufficient, to add</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">491A</td>
<td style="text-align:center;" valign="top" width="30"><a title="多" href="https://nihongoichiban.com/2011/04/10/%e5%a4%9a/" target="_blank">多</a></td>
<td valign="top" width="200">TA</td>
<td valign="top" width="200">oo(i)</td>
<td valign="top" width="200">many</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5927</td>
<td style="text-align:center;" valign="top" width="30"><a title="大" href="https://nihongoichiban.com/2011/03/26/%e5%a4%a7/" target="_blank">大</a></td>
<td valign="top" width="200">DAI, TAI</td>
<td valign="top" width="200">ou(kii), oo(i)</td>
<td valign="top" width="200">big, a lot</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">7537</td>
<td style="text-align:center;" valign="top" width="30"><a title="男" href="https://nihongoichiban.com/2011/04/09/%e7%94%b7/" target="_blank">男</a></td>
<td valign="top" width="200">DAN, NAN</td>
<td valign="top" width="200">otoko</td>
<td valign="top" width="200">man, male</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E2D</td>
<td style="text-align:center;" valign="top" width="30"><a title="中" href="https://nihongoichiban.com/2011/03/26/%e4%b8%ad/" target="_blank">中</a></td>
<td valign="top" width="200">CHUU</td>
<td valign="top" width="200">naka</td>
<td valign="top" width="200">inner, center, between</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">9577</td>
<td style="text-align:center;" valign="top" width="30"><a title="長" href="https://nihongoichiban.com/2011/04/09/%e9%95%b7/" target="_blank">長</a></td>
<td valign="top" width="200">CHOU</td>
<td valign="top" width="200">naga(i)</td>
<td valign="top" width="200">long, leader</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5929</td>
<td style="text-align:center;" valign="top" width="30"><a title="天" href="https://nihongoichiban.com/2011/04/10/%e5%a4%a9/" target="_blank">天</a></td>
<td valign="top" width="200">TEN</td>
<td valign="top" width="200">ame, ama</td>
<td valign="top" width="200">sky</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5E97</td>
<td style="text-align:center;" valign="top" width="30"><a title="店" href="https://nihongoichiban.com/2011/04/10/%e5%ba%97/" target="_blank">店</a></td>
<td valign="top" width="200">TEN</td>
<td valign="top" width="200">mise</td>
<td valign="top" width="200">shop</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">96FB</td>
<td style="text-align:center;" valign="top" width="30"><a title="電" href="https://nihongoichiban.com/2011/04/10/%e9%9b%bb/" target="_blank">電</a></td>
<td valign="top" width="200">DEN</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">electricity</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">571F</td>
<td style="text-align:center;" valign="top" width="30"><a title="土" href="https://nihongoichiban.com/2011/03/26/%e5%9c%9f/" target="_blank">土</a></td>
<td valign="top" width="200">DO, TO</td>
<td valign="top" width="200">tsuchi</td>
<td valign="top" width="200">earth, ground</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6771</td>
<td style="text-align:center;" valign="top" width="30"><a title="東" href="https://nihongoichiban.com/2011/04/06/jlpt-kanji-東/" target="_blank">東</a></td>
<td valign="top" width="200">TOU</td>
<td valign="top" width="200">higashi</td>
<td valign="top" width="200">east</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">9053</td>
<td style="text-align:center;" valign="top" width="30"><a title="道" href="https://nihongoichiban.com/2011/04/10/%e9%81%93/" target="_blank">道</a></td>
<td valign="top" width="200">DOU</td>
<td valign="top" width="200">michi</td>
<td valign="top" width="200">street, path</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8AAD</td>
<td style="text-align:center;" valign="top" width="30"><a title="読" href="https://nihongoichiban.com/2011/04/10/%e8%aa%ad/" target="_blank">読</a></td>
<td valign="top" width="200">DOKU</td>
<td valign="top" width="200">yo(mu)</td>
<td valign="top" width="200">to read</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5357</td>
<td style="text-align:center;" valign="top" width="30"><a title="南" href="https://nihongoichiban.com/2011/04/07/%e5%8d%97/" target="_blank">南</a></td>
<td valign="top" width="200">NAN</td>
<td valign="top" width="200">minami</td>
<td valign="top" width="200">south</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E8C</td>
<td style="text-align:center;" valign="top" width="30"><a title="二" href="https://nihongoichiban.com/2011/03/21/%e4%ba%8c/" target="_blank">ニ</a></td>
<td valign="top" width="200">NI</td>
<td valign="top" width="200">futa(tsu), futa-</td>
<td valign="top" width="200">two</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">65E5</td>
<td style="text-align:center;" valign="top" width="30"><a title="日" href="https://nihongoichiban.com/2011/03/21/%e6%97%a5/">日</a></td>
<td valign="top" width="200">NICHI, JITSU</td>
<td valign="top" width="200">hi, -ka</td>
<td valign="top" width="200">day, sun</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5165</td>
<td style="text-align:center;" valign="top" width="30"><a title="入" href="https://nihongoichiban.com/2011/04/02/%e5%85%a5/" target="_blank">入</a></td>
<td valign="top" width="200">NYUU</td>
<td valign="top" width="200">hai(ru), i(ru), i(reru)</td>
<td valign="top" width="200">to enter, to insert</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5E74</td>
<td style="text-align:center;" valign="top" width="30"><a title="年" href="https://nihongoichiban.com/2011/04/01/%e5%b9%b4/" target="_blank">年</a></td>
<td valign="top" width="200">NEN</td>
<td valign="top" width="200">toshi</td>
<td valign="top" width="200">year</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8CB7</td>
<td style="text-align:center;" valign="top" width="30"><a title="買" href="https://nihongoichiban.com/2011/04/10/%e8%b2%b7/" target="_blank">買</a></td>
<td valign="top" width="200">BAI</td>
<td valign="top" width="200">ka(u)</td>
<td valign="top" width="200">to buy</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">767D</td>
<td style="text-align:center;" valign="top" width="30"><a title="白" href="https://nihongoichiban.com/2011/04/10/%e7%99%bd/" target="_blank">白</a></td>
<td valign="top" width="200">HAKU, BYAKU</td>
<td valign="top" width="200">shiro(i), shiro</td>
<td valign="top" width="200">white</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">516B</td>
<td style="text-align:center;" valign="top" width="30"><a title="八" href="https://nihongoichiban.com/2011/03/21/%e5%85%ab/">八</a></td>
<td valign="top" width="200">HACHI</td>
<td valign="top" width="200">yat(tsu), ya(tsu), ya-, you-</td>
<td valign="top" width="200">eight</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">534A</td>
<td style="text-align:center;" valign="top" width="30"><a title="半" href="https://nihongoichiban.com/2011/04/10/%e5%8d%8a/" target="_blank">半</a></td>
<td valign="top" width="200">HAN</td>
<td valign="top" width="200">naka(ba)</td>
<td valign="top" width="200">half, middle, semi-</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">767E</td>
<td style="text-align:center;" valign="top" width="30"><a title="百" href="https://nihongoichiban.com/2011/03/21/%e7%99%be/">百</a></td>
<td valign="top" width="200">HYAKU</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">hundred</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">7236</td>
<td style="text-align:center;" valign="top" width="30"><a title="父" href="https://nihongoichiban.com/2011/04/10/%e7%88%b6/" target="_blank">父</a></td>
<td valign="top" width="200">FU</td>
<td valign="top" width="200">chichi</td>
<td valign="top" width="200">father</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5206</td>
<td style="text-align:center;" valign="top" width="30"><a title="分" href="https://nihongoichiban.com/2011/03/27/%e5%88%86/">分</a></td>
<td valign="top" width="200">BUN, BU, FUN</td>
<td valign="top" width="200">wa(keru), wa(kareru), wa(karu)</td>
<td valign="top" width="200">part, minute, to divide, to understand</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">805E</td>
<td style="text-align:center;" valign="top" width="30"><a title="聞" href="https://nihongoichiban.com/2011/04/03/%e8%81%9e/" target="_blank">聞</a></td>
<td valign="top" width="200">BUN, MON</td>
<td valign="top" width="200">ki(ku), ki(koeru)</td>
<td valign="top" width="200">to hear, to listen, to ask</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6BCD</td>
<td style="text-align:center;" valign="top" width="30"><a title="母" href="https://nihongoichiban.com/2011/04/10/%e6%af%8d/" target="_blank">母</a></td>
<td valign="top" width="200">BO</td>
<td valign="top" width="200">haha</td>
<td valign="top" width="200">mother</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">5317</td>
<td style="text-align:center;" valign="top" width="30"><a title="北" href="https://nihongoichiban.com/2011/04/07/%e5%8c%97/" target="_blank">北</a></td>
<td valign="top" width="200">HOKU</td>
<td valign="top" width="200">kita</td>
<td valign="top" width="200">north</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6728</td>
<td style="text-align:center;" valign="top" width="30"><a title="木" href="https://nihongoichiban.com/2011/03/25/%e6%9c%a8/" target="_blank">木</a></td>
<td valign="top" width="200">BOKU, MOKU</td>
<td valign="top" width="200">ki, ko</td>
<td valign="top" width="200">tree, wood</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">672C</td>
<td style="text-align:center;" valign="top" width="30"><a title="本" href="https://nihongoichiban.com/2011/03/26/%e6%9c%ac/" target="_blank">本</a></td>
<td valign="top" width="200">HON</td>
<td valign="top" width="200">moto</td>
<td valign="top" width="200">book, source, main-</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6BCE</td>
<td style="text-align:center;" valign="top" width="30"><a title="毎" href="https://nihongoichiban.com/2011/04/10/%e6%af%8e/" target="_blank">毎</a></td>
<td valign="top" width="200">MAI</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">each, every</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">4E07</td>
<td style="text-align:center;" valign="top" width="30"><a title="万" href="https://nihongoichiban.com/2011/03/21/%e4%b8%87/" target="_blank">万</a></td>
<td valign="top" width="200">MAN, BAN</td>
<td valign="top" width="200">&#8211;</td>
<td valign="top" width="200">ten thousand, all, many</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">540D</td>
<td style="text-align:center;" valign="top" width="30"><a title="名" href="https://nihongoichiban.com/2011/04/09/%e5%90%8d/" target="_blank">名</a></td>
<td valign="top" width="200">MEI, MYOU</td>
<td valign="top" width="200">na</td>
<td valign="top" width="200">name, reputation</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">76EE</td>
<td style="text-align:center;" valign="top" width="30"><a title="目" href="https://nihongoichiban.com/2011/04/09/%e7%9b%ae/" target="_blank">目</a></td>
<td valign="top" width="200">MOKU</td>
<td valign="top" width="200">me</td>
<td valign="top" width="200">eye</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">53CB</td>
<td style="text-align:center;" valign="top" width="30"><a title="友" href="https://nihongoichiban.com/2011/04/09/%e5%8f%8b/" target="_blank">友</a></td>
<td valign="top" width="200">YUU</td>
<td valign="top" width="200">tomo</td>
<td valign="top" width="200">friend</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">6765</td>
<td style="text-align:center;" valign="top" width="30"><a title="来" href="https://nihongoichiban.com/2011/04/06/%e6%9d%a5/" target="_blank">来</a></td>
<td valign="top" width="200">RAI</td>
<td valign="top" width="200">ku(ru), kita(ru), kita(su)</td>
<td valign="top" width="200">to come</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">7ABC</td>
<td style="text-align:center;" valign="top" width="30"><a title="立" href="https://nihongoichiban.com/2011/04/09/%e7%ab%8b/" target="_blank">立</a></td>
<td valign="top" width="200">RITSU</td>
<td valign="top" width="200">ta(tsu), ta(teru)</td>
<td valign="top" width="200">to stand, to establish</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">516D</td>
<td style="text-align:center;" valign="top" width="30"><a title="六" href="https://nihongoichiban.com/2011/03/21/%e5%85%ad/">六</a></td>
<td valign="top" width="200">ROKU</td>
<td valign="top" width="200">mutt(su), mu(tsu), mu, mui</td>
<td valign="top" width="200">six</td>
</tr>
<tr>
<td style="text-align:center;" valign="top" width="20">8A71</td>
<td style="text-align:center;" valign="top" width="30"><a title="話" href="https://nihongoichiban.com/2011/04/09/%e8%a9%b1/" target="_blank">話</a></td>
<td valign="top" width="200">WA</td>
<td valign="top" width="200">hanashi, hana(su)</td>
<td valign="top" width="200">speech, to talk, story, conversation</td>
</tr>
"""

# Парсим HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Ищем все строки таблицы
rows = soup.find_all('tr')

# Извлечение кандзи и каны
words = []
for row in rows:
    columns = row.find_all('td')  # Находим все ячейки в строке
    if len(columns) >= 2:  # Проверяем, что ячеек достаточно
        kanji = columns[1].get_text(strip=True)
        onyomi = columns[2].get_text(strip=True)
        kunyomi = columns[3].get_text(strip=True)
        meaning_en = columns[4].get_text(strip=True)
        words.append((kanji, onyomi, kunyomi, meaning_en))

# Сохранение в файл
with open('kanji_n5.txt', 'w', encoding='utf-8') as file:
    for kanji, onyomi, kunyomi, meaning_en in words:
        file.write(f"{kanji}\t{onyomi}\t{kunyomi}\t{meaning_en}\n")

print("Данные сохранены в файл kanji_n5.txt")
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import csv

html = """
<tr valign="top">
<td align="middle" bgcolor="#ffffff"> 60AA</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="悪" href="https://nihongoichiban.com/2011/04/11/%e6%82%aa/" target="_blank">悪</a></td>
<td align="left" bgcolor="#ffffff">AKU, O</td>
<td align="left" bgcolor="#ffffff">waru(i)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">bad, mean</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff"> 6697</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="暗" href="https://nihongoichiban.com/2011/04/12/%e6%9a%97/" target="_blank">暗</a></td>
<td align="left" bgcolor="#ffffff">AN</td>
<td align="left" bgcolor="#ffffff">kura(i)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">dark</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">533B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="医" href="https://nihongoichiban.com/2011/04/12/%e5%8c%bb/" target="_blank">医</a></td>
<td align="left" bgcolor="#ffffff">I</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">medicine</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">610F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="意" href="https://nihongoichiban.com/2011/04/13/%e6%84%8f/" target="_blank">意</a></td>
<td align="left" bgcolor="#ffffff">I</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">will, heart, meaning</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4EE5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="以" href="https://nihongoichiban.com/2011/04/14/%e4%bb%a5/" target="_blank">以</a></td>
<td align="left" bgcolor="#ffffff">I</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">prefix</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5F15</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="引" href="https://nihongoichiban.com/2011/04/14/%e5%bc%95/" target="_blank">引</a></td>
<td align="left" bgcolor="#ffffff">IN</td>
<td align="left" bgcolor="#ffffff">hi(ku), hi(keru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to pull, make cheaper</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9662</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="院" href="https://nihongoichiban.com/2011/04/14/%e9%99%a2/" target="_blank">院</a></td>
<td align="left" bgcolor="#ffffff">IN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">institute, establishment</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">54E1</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="員" href="https://nihongoichiban.com/2011/04/15/%e5%93%a1/" target="_blank">員</a></td>
<td align="left" bgcolor="#ffffff">IN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">member</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">904B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="運" href="https://nihongoichiban.com/2011/04/15/%e9%81%8b/" target="_blank">運</a></td>
<td align="left" bgcolor="#ffffff">UN</td>
<td align="left" bgcolor="#ffffff">hako(bu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">destiny, transport, carry</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">82F1</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="英" href="https://nihongoichiban.com/2011/04/16/%e8%8b%b1/" target="_blank">英</a></td>
<td align="left" bgcolor="#ffffff">EI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">brilliant, talented</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6620</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="映" href="https://nihongoichiban.com/2011/04/16/%e6%98%a0/" target="_blank">映</a></td>
<td align="left" bgcolor="#ffffff">EI</td>
<td align="left" bgcolor="#ffffff">utsu(su), he(eru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to project, to glint</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9060</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="遠" href="https://nihongoichiban.com/2011/04/16/%e9%81%a0/" target="_blank">遠</a></td>
<td align="left" bgcolor="#ffffff">EN</td>
<td align="left" bgcolor="#ffffff">too(i)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">far away</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff"> 5C4B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="屋" href="https://nihongoichiban.com/2011/04/17/%e5%b1%8b/" target="_blank">屋</a></td>
<td align="left" bgcolor="#ffffff">OKU</td>
<td align="left" bgcolor="#ffffff">ya</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">room, house</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">97F3</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="音" href="https://nihongoichiban.com/2011/04/17/%e9%9f%b3/" target="_blank">音</a></td>
<td align="left" bgcolor="#ffffff">ON, IN</td>
<td align="left" bgcolor="#ffffff">oto, ne</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">sound</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6B4C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="歌" href="https://nihongoichiban.com/2011/04/17/%e6%ad%8c/" target="_blank">歌</a></td>
<td align="left" bgcolor="#ffffff">KA</td>
<td align="left" bgcolor="#ffffff">uta, uta(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">song, poem, to sing</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">590F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="夏" href="https://nihongoichiban.com/2011/04/18/%e5%a4%8f/" target="_blank">夏</a></td>
<td align="left" bgcolor="#ffffff">KA</td>
<td align="left" bgcolor="#ffffff">natsu</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">summer</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5BB6</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="家" href="https://nihongoichiban.com/2011/04/18/%e5%ae%b6/" target="_blank">家</a></td>
<td align="left" bgcolor="#ffffff">KA, KE</td>
<td align="left" bgcolor="#ffffff">ie, ya</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">house, home</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">753B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="画" href="https://nihongoichiban.com/2011/04/19/%e7%94%bb/" target="_blank">画</a></td>
<td align="left" bgcolor="#ffffff">GA, KAKU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">picture, line of a character</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6D77</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="海" href="https://nihongoichiban.com/2011/04/19/%e6%b5%b7/" target="_blank">海</a></td>
<td align="left" bgcolor="#ffffff">KAI</td>
<td align="left" bgcolor="#ffffff">umi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">sea, ocean</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">56DE</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="回" href="https://nihongoichiban.com/2011/04/20/%e5%9b%9e/" target="_blank">回</a></td>
<td align="left" bgcolor="#ffffff">KAI</td>
<td align="left" bgcolor="#ffffff">mawa(su)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">times, occurrences</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">958B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="開" href="https://nihongoichiban.com/2011/04/20/%e9%96%8b/" target="_blank">開</a></td>
<td align="left" bgcolor="#ffffff">KAI</td>
<td align="left" bgcolor="#ffffff">a(keru), Hira(ku)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to open, vent, develop</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">754C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="界" href="https://nihongoichiban.com/2011/04/21/%e7%95%8c/" target="_blank">界</a></td>
<td align="left" bgcolor="#ffffff">KAI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">world</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">697D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="楽" href="https://nihongoichiban.com/2011/04/21/%e6%a5%bd/" target="_blank">楽</a></td>
<td align="left" bgcolor="#ffffff">GAKU, RAKU</td>
<td align="left" bgcolor="#ffffff">tano(shii), tano(shimu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">music, comfort, ease, joyful</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff"> 9928</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="館" href="https://nihongoichiban.com/2011/04/22/%e9%a4%a8/" target="_blank">館</a></td>
<td align="left" bgcolor="#ffffff">KAN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">big hall, building</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6F22</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="漢" href="https://nihongoichiban.com/2011/04/22/%e6%bc%a2/" target="_blank">漢</a></td>
<td align="left" bgcolor="#ffffff">KAN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">China, man</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5BD2</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="寒" href="https://nihongoichiban.com/2011/04/23/%e5%af%92/" target="_blank">寒</a></td>
<td align="left" bgcolor="#ffffff">KAN</td>
<td align="left" bgcolor="#ffffff">samu(i)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">cold temperature</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9854</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="顔" href="https://nihongoichiban.com/2011/04/23/%e9%a1%94/" target="_blank">顔</a></td>
<td align="left" bgcolor="#ffffff">GAN</td>
<td align="left" bgcolor="#ffffff">kao</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">face</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5E30</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="帰" href="https://nihongoichiban.com/2011/04/23/%e5%b8%b0/" target="_blank">帰</a></td>
<td align="left" bgcolor="#ffffff">KI</td>
<td align="left" bgcolor="#ffffff">kae(ru), kae(su)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">return home, return</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8D77</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="起" href="https://nihongoichiban.com/2011/04/23/%e8%b5%b7/" target="_blank">起</a></td>
<td align="left" bgcolor="#ffffff">KI</td>
<td align="left" bgcolor="#ffffff">o(kiru), o(kuro)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">stand up, start, cause</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7A76</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="究" href="https://nihongoichiban.com/2011/04/24/%e7%a9%b6/" target="_blank">究</a></td>
<td align="left" bgcolor="#ffffff">KYUU</td>
<td align="left" bgcolor="#ffffff">kiwa(meru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to explore, investigate</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6025</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="急" href="https://nihongoichiban.com/2011/04/24/%e6%80%a5/" target="_blank">急</a></td>
<td align="left" bgcolor="#ffffff">KYUU</td>
<td align="left" bgcolor="#ffffff">iso(gu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">urgent, quick, sudden, to hurry</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">725B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="牛" href="https://nihongoichiban.com/2011/04/24/%e7%89%9b/" target="_blank">牛</a></td>
<td align="left" bgcolor="#ffffff">GYUU</td>
<td align="left" bgcolor="#ffffff">ushi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">cow</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">53BB</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="去" href="https://nihongoichiban.com/2011/04/25/%e5%8e%bb/" target="_blank">去</a></td>
<td align="left" bgcolor="#ffffff">KYO, KO</td>
<td align="left" bgcolor="#ffffff">sa(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to pass by</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5F37</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="強" href="https://nihongoichiban.com/2011/04/25/%e5%bc%b7/" target="_blank">強</a></td>
<td align="left" bgcolor="#ffffff">KYOU, GOU</td>
<td align="left" bgcolor="#ffffff">tsuyo(i), tsuyo(maru), shi(iru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">strong, make stronger, to force</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6559</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="教" href="https://nihongoichiban.com/2011/04/25/%e6%95%99/" target="_blank">教</a></td>
<td align="left" bgcolor="#ffffff">KYOU</td>
<td align="left" bgcolor="#ffffff">oshi(eru), oso(waru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to teach, to learn</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4EAC</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="京" href="https://nihongoichiban.com/2011/04/26/%e4%ba%ac/" target="_blank">京</a></td>
<td align="left" bgcolor="#ffffff">KYOU, KEI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">capital</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">696D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="業" href="https://nihongoichiban.com/2011/04/26/%e6%a5%ad/" target="_blank">業</a></td>
<td align="left" bgcolor="#ffffff">GYOU, GOU</td>
<td align="left" bgcolor="#ffffff">waza</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">company, business, profession, art</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8FD1</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="近" href="https://nihongoichiban.com/2011/04/27/%e8%bf%91/" target="_blank">近</a></td>
<td align="left" bgcolor="#ffffff">KIN</td>
<td align="left" bgcolor="#ffffff">chika(i)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">near</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9280</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="銀" href="https://nihongoichiban.com/2011/04/27/%e9%8a%80/" target="_blank">銀</a></td>
<td align="left" bgcolor="#ffffff">GIN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">silver</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">533A</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="区" href="https://nihongoichiban.com/2011/04/27/%e5%8c%ba/" target="_blank">区</a></td>
<td align="left" bgcolor="#ffffff">KU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">city district</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8A08</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="計" href="https://nihongoichiban.com/2011/04/29/%e8%a8%88/" target="_blank">計</a></td>
<td align="left" bgcolor="#ffffff">KEI</td>
<td align="left" bgcolor="#ffffff">haka(ru), haka(rau)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to measure, to proceed</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5144</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="兄" href="https://nihongoichiban.com/2011/04/29/%e5%85%84/" target="_blank">兄</a></td>
<td align="left" bgcolor="#ffffff">KEI, KYOU</td>
<td align="left" bgcolor="#ffffff">ani</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">older brother</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8EFD</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="軽" href="https://nihongoichiban.com/2011/04/29/%e8%bb%bd/" target="_blank">軽</a></td>
<td align="left" bgcolor="#ffffff">KEI</td>
<td align="left" bgcolor="#ffffff">karu(i), karo(yaka)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">light (weight)</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">75AC</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="犬" href="https://nihongoichiban.com/2011/04/29/%e7%8a%ac/" target="_blank">犬</a></td>
<td align="left" bgcolor="#ffffff">KEN</td>
<td align="left" bgcolor="#ffffff">inu</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">dog</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7814</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="研" href="https://nihongoichiban.com/2011/04/30/%e7%a0%94/" target="_blank">研</a></td>
<td align="left" bgcolor="#ffffff">KEN</td>
<td align="left" bgcolor="#ffffff">to(gu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to polish, sharpen, wash rice</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">770C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="県" href="https://nihongoichiban.com/2011/04/30/%e7%9c%8c/" target="_blank">県</a></td>
<td align="left" bgcolor="#ffffff">KEN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">prefecture</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5EFA</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="建" href="https://nihongoichiban.com/2011/05/01/%e5%bb%ba/" target="_blank">建</a></td>
<td align="left" bgcolor="#ffffff">KEN</td>
<td align="left" bgcolor="#ffffff">ta(teru), ta(su)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to construct, build</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9A13</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="験" href="https://nihongoichiban.com/2011/05/01/%e9%a8%93/" target="_blank">験</a></td>
<td align="left" bgcolor="#ffffff">KEN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">test, effect</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5143</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="元" href="https://nihongoichiban.com/2011/05/01/%e5%85%83/" target="_blank">元</a></td>
<td align="left" bgcolor="#ffffff">GEN, GAN</td>
<td align="left" bgcolor="#ffffff">moto</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">reason, original</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5DE5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="工" href="https://nihongoichiban.com/2011/05/01/%e5%b7%a5/" target="_blank">工</a></td>
<td align="left" bgcolor="#ffffff">KOU, KU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to construct</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5A83</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="広" href="https://nihongoichiban.com/2011/05/01/%e5%ba%83/" target="_blank">広</a></td>
<td align="left" bgcolor="#ffffff">KOU</td>
<td align="left" bgcolor="#ffffff">hiro(i), hiro(geru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">broad, wide, to widen, to expand</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8003</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="考" href="https://nihongoichiban.com/2011/05/01/%e8%80%83/" target="_blank">考</a></td>
<td align="left" bgcolor="#ffffff">KOU</td>
<td align="left" bgcolor="#ffffff">kanga(eru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to think, thought</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5149</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="光" href="https://nihongoichiban.com/2011/05/01/%e5%85%89/" target="_blank">光</a></td>
<td align="left" bgcolor="#ffffff">KOU</td>
<td align="left" bgcolor="#ffffff">hikari, hika(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">light, to shine</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">597D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="好" href="https://nihongoichiban.com/2011/05/01/%e5%a5%bd/" target="_blank">好</a></td>
<td align="left" bgcolor="#ffffff">KOU</td>
<td align="left" bgcolor="#ffffff">kono(mu), su(ku)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to like</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5408</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="合" href="https://nihongoichiban.com/2011/05/01/%e5%90%88/" target="_blank">合</a></td>
<td align="left" bgcolor="#ffffff">GOU, GA</td>
<td align="left" bgcolor="#ffffff">a(waseru), a(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to fit, to connect</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9ED2</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="黒" href="https://nihongoichiban.com/2011/05/01/%e9%bb%92/" target="_blank">黒</a></td>
<td align="left" bgcolor="#ffffff">KOKU</td>
<td align="left" bgcolor="#ffffff">kuro(i), kuro</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">black</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">83DC</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="菜" href="https://nihongoichiban.com/2011/05/02/%e8%8f%9c/" target="_blank">菜</a></td>
<td align="left" bgcolor="#ffffff">SAI</td>
<td align="left" bgcolor="#ffffff">na</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">vegetable, rape</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4F5C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="作" href="https://nihongoichiban.com/2011/05/02/%e4%bd%9c/" target="_blank">作</a></td>
<td align="left" bgcolor="#ffffff">SAKU, SA</td>
<td align="left" bgcolor="#ffffff">tsuku(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to make, to build</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7523</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="産" href="https://nihongoichiban.com/2011/05/02/%e7%94%a3/" target="_blank">産</a></td>
<td align="left" bgcolor="#ffffff">SAN</td>
<td align="left" bgcolor="#ffffff">u(mu), u(mareru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">birth, production</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7D19</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="紙" href="https://nihongoichiban.com/2011/05/02/%e7%b4%99/" target="_blank">紙</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">kami</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">paper</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">601D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="思" href="https://nihongoichiban.com/2011/05/02/%e6%80%9d/" target="_blank">思</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">omo(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to think, to believe</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">59C9</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="姉" href="https://nihongoichiban.com/2011/05/02/%e5%a7%89/" target="_blank">姉</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">ane</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">older sister</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6B62</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="止" href="https://nihongoichiban.com/2011/05/02/%e6%ad%a2/" target="_blank">止</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">to(maru), to(meru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to stop</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5E02</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="市" href="https://nihongoichiban.com/2011/05/03/%e5%b8%82/" target="_blank">市</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">ichi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">city, market</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4ED5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="仕" href="https://nihongoichiban.com/2011/05/03/%e4%bb%95/" target="_blank">仕</a></td>
<td align="left" bgcolor="#ffffff">SHI, JI</td>
<td align="left" bgcolor="#ffffff">tsuka(eru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to serve</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6B7B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="死" href="https://nihongoichiban.com/2011/05/03/%e6%ad%bb/" target="_blank">死</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">shi(nu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">death, to die</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4F7F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="使" href="https://nihongoichiban.com/2011/05/03/%e4%bd%bf/" target="_blank">使</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">tsuka(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">use, messenger</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">59CB</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="始" href="https://nihongoichiban.com/2011/05/03/%e5%a7%8b/" target="_blank">始</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">haji(meru/maru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">start, to begin</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8A66</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="試" href="https://nihongoichiban.com/2011/05/03/%e8%a9%a6/" target="_blank">試</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">kokoro(miru), tame(su)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to try</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">79C1</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="私" href="https://nihongoichiban.com/2011/05/04/%e7%a7%81/" target="_blank">私</a></td>
<td align="left" bgcolor="#ffffff">SHI</td>
<td align="left" bgcolor="#ffffff">watashi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">I, me, private</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5B57</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="字" href="https://nihongoichiban.com/2011/05/04/%e5%ad%97/" target="_blank">字</a></td>
<td align="left" bgcolor="#ffffff">JI</td>
<td align="left" bgcolor="#ffffff">aza</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">character, sector of a village</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">81EA</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="自" href="https://nihongoichiban.com/2011/05/04/%e8%87%aa/" target="_blank">自</a></td>
<td align="left" bgcolor="#ffffff">JI, SHI</td>
<td align="left" bgcolor="#ffffff">mizuka(ra)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">self</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4E8B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="事" href="https://nihongoichiban.com/2011/05/04/%e4%ba%8b/" target="_blank">事</a></td>
<td align="left" bgcolor="#ffffff">JI</td>
<td align="left" bgcolor="#ffffff">koto</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">thing, matter</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6301</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="持" href="https://nihongoichiban.com/2011/05/04/%e6%8c%81/" target="_blank">持</a></td>
<td align="left" bgcolor="#ffffff">JI</td>
<td align="left" bgcolor="#ffffff">mo(tsu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to own, to carry</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5BA4</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="室" href="https://nihongoichiban.com/2011/05/04/%e5%ae%a4/" target="_blank">室</a></td>
<td align="left" bgcolor="#ffffff">SHITSU</td>
<td align="left" bgcolor="#ffffff">muro</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">room, cellar</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8CEA</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="質" href="https://nihongoichiban.com/2011/05/04/%e8%b3%aa/" target="_blank">質</a></td>
<td align="left" bgcolor="#ffffff">SHITSU, SHICHI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">quality, nature</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5199</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="写" href="https://nihongoichiban.com/2011/05/04/%e5%86%99/" target="_blank">写</a></td>
<td align="left" bgcolor="#ffffff">SHA</td>
<td align="left" bgcolor="#ffffff">utsu(su), utsu(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">copy, photograph</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8005</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="者" href="https://nihongoichiban.com/2011/05/05/%e8%80%85/" target="_blank">者</a></td>
<td align="left" bgcolor="#ffffff">SHA</td>
<td align="left" bgcolor="#ffffff">mono</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">person</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">501F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="借" href="https://nihongoichiban.com/2011/05/05/%e5%80%9f/" target="_blank">借</a></td>
<td align="left" bgcolor="#ffffff">SHAKU</td>
<td align="left" bgcolor="#ffffff">ka(riru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to rent, to borrow</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5F31</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="弱" href="https://nihongoichiban.com/2011/05/05/%e5%bc%b1/" target="_blank">弱</a></td>
<td align="left" bgcolor="#ffffff">JAKU</td>
<td align="left" bgcolor="#ffffff">yowa(i), yowa(ru), yowa(meru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">weak, to weaken</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9996</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="首" href="https://nihongoichiban.com/2011/05/05/%e9%a6%96/" target="_blank">首</a></td>
<td align="left" bgcolor="#ffffff">SHU</td>
<td align="left" bgcolor="#ffffff">kubi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">neck, head</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4E3B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="主" href="https://nihongoichiban.com/2011/05/05/%e4%b8%bb/" target="_blank">主</a></td>
<td align="left" bgcolor="#ffffff">SHU</td>
<td align="left" bgcolor="#ffffff">nushi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">owner, main-</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">79CB</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="秋" href="https://nihongoichiban.com/2011/05/05/%e7%a7%8b/" target="_blank">秋</a></td>
<td align="left" bgcolor="#ffffff">SHUU</td>
<td align="left" bgcolor="#ffffff">aki</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">autumn, fall</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">96C6</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="集" href="https://nihongoichiban.com/2011/05/05/%e9%9b%86/" target="_blank">集</a></td>
<td align="left" bgcolor="#ffffff">SHUU</td>
<td align="left" bgcolor="#ffffff">atsu(maru/meru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to meet, to gather</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7FD2</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="習" href="https://nihongoichiban.com/2011/05/06/%e7%bf%92/" target="_blank">習</a></td>
<td align="left" bgcolor="#ffffff">SHUU</td>
<td align="left" bgcolor="#ffffff">nara(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to learn</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7D42</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="終" href="https://nihongoichiban.com/2011/05/06/%e7%b5%82/" target="_blank">終</a></td>
<td align="left" bgcolor="#ffffff">SHUU</td>
<td align="left" bgcolor="#ffffff">o(waru), o(eru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">end</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4F4F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="住" href="https://nihongoichiban.com/2011/05/06/%e4%bd%8f/" target="_blank">住</a></td>
<td align="left" bgcolor="#ffffff">JUU</td>
<td align="left" bgcolor="#ffffff">su(mu), su(mau)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to live in, to reside</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">91CD</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="重" href="https://nihongoichiban.com/2011/05/07/%e9%87%8d/" target="_blank">重</a></td>
<td align="left" bgcolor="#ffffff">JUU, CHOU</td>
<td align="left" bgcolor="#ffffff">omo(i), kasa(naru), -e</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">heavy, serious, -fold</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6625</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="春" href="https://nihongoichiban.com/2011/05/07/%e6%98%a5/" target="_blank">春</a></td>
<td align="left" bgcolor="#ffffff">SHUN</td>
<td align="left" bgcolor="#ffffff">haru</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">spring</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6240</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="所" href="https://nihongoichiban.com/2011/05/07/%e6%89%80/" target="_blank">所</a></td>
<td align="left" bgcolor="#ffffff">SHO</td>
<td align="left" bgcolor="#ffffff">tokoro</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">a place</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6691</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="暑" href="https://nihongoichiban.com/2011/05/08/%e6%9a%91/" target="_blank">暑</a></td>
<td align="left" bgcolor="#ffffff">SHO</td>
<td align="left" bgcolor="#ffffff">atsu(i)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">hot (temperature)</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5834</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="場" href="https://nihongoichiban.com/2011/05/08/%e5%a0%b4/" target="_blank">場</a></td>
<td align="left" bgcolor="#ffffff">JOU</td>
<td align="left" bgcolor="#ffffff">ba</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">a place</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4E57</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="乗" href="https://nihongoichiban.com/2011/05/08/%e4%b9%97/" target="_blank">乗</a></td>
<td align="left" bgcolor="#ffffff">JOU</td>
<td align="left" bgcolor="#ffffff">no(ru), no(seru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to drive, to ride, to fool</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8272</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="色" href="https://nihongoichiban.com/2011/05/08/%e8%89%b2/" target="_blank">色</a></td>
<td align="left" bgcolor="#ffffff">SHOKU</td>
<td align="left" bgcolor="#ffffff">iro</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">color, sensuality</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">68EE</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="森" href="https://nihongoichiban.com/2011/05/08/%e6%a3%ae/" target="_blank">森</a></td>
<td align="left" bgcolor="#ffffff">SHIN</td>
<td align="left" bgcolor="#ffffff">mori</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">forest</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5FC3</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="心" href="https://nihongoichiban.com/2011/05/09/%e5%bf%83/" target="_blank">心</a></td>
<td align="left" bgcolor="#ffffff">SHIN</td>
<td align="left" bgcolor="#ffffff">kokoro</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">heart, mind</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">89AA</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="親" href="https://nihongoichiban.com/2011/05/09/%e8%a6%aa/" target="_blank">親</a></td>
<td align="left" bgcolor="#ffffff">SHIN</td>
<td align="left" bgcolor="#ffffff">oya, shita(shii), shita(shimu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">parents, to be close, to be friends</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">771F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="真" href="https://nihongoichiban.com/2011/05/10/%e7%9c%9f/" target="_blank">真</a></td>
<td align="left" bgcolor="#ffffff">SHIN</td>
<td align="left" bgcolor="#ffffff">ma-</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">truth, reality, purity</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9032</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="進" href="https://nihongoichiban.com/2011/05/10/%e9%80%b2/" target="_blank">進</a></td>
<td align="left" bgcolor="#ffffff">SHIN</td>
<td align="left" bgcolor="#ffffff">susu(mu), susu(meru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">continue, proceed, promote</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">56F3</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="図" href="https://nihongoichiban.com/2011/05/10/%e5%9b%b3/" target="_blank">図</a></td>
<td align="left" bgcolor="#ffffff">ZU, TO</td>
<td align="left" bgcolor="#ffffff">haka(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">drawing, plan</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9752</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="青" href="https://nihongoichiban.com/2011/05/11/%e9%9d%92/" target="_blank">青</a></td>
<td align="left" bgcolor="#ffffff">SEI</td>
<td align="left" bgcolor="#ffffff">ao(i), ao</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">blue, green, unripe</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6B63</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="正" href="https://nihongoichiban.com/2011/05/11/%e6%ad%a3/" target="_blank">正</a></td>
<td align="left" bgcolor="#ffffff">SEI, SHOU</td>
<td align="left" bgcolor="#ffffff">tada(shii), tada(su), masa</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">correct, right</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">58F0</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="声" href="https://nihongoichiban.com/2011/05/12/%e5%a3%b0/" target="_blank">声</a></td>
<td align="left" bgcolor="#ffffff">SEI</td>
<td align="left" bgcolor="#ffffff">koe</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">voice</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4E16</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="世" href="https://nihongoichiban.com/2011/05/12/%e4%b8%96/" target="_blank">世</a></td>
<td align="left" bgcolor="#ffffff">SEI, SE</td>
<td align="left" bgcolor="#ffffff">yo</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">world, age</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8D64</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="赤" href="https://nihongoichiban.com/2011/05/12/%e8%b5%a4/" target="_blank">赤</a></td>
<td align="left" bgcolor="#ffffff">SEKI, SHAKU</td>
<td align="left" bgcolor="#ffffff">aka(i), aka(maru), aka(rameru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">red, to flush</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5915</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="夕" href="https://nihongoichiban.com/2011/05/12/%e5%a4%95/" target="_blank">夕</a></td>
<td align="left" bgcolor="#ffffff">SEKI</td>
<td align="left" bgcolor="#ffffff">yuu</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">evening</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5207</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="切" href="https://nihongoichiban.com/2011/05/12/%e5%88%87/" target="_blank">切</a></td>
<td align="left" bgcolor="#ffffff">SETSU, SAI</td>
<td align="left" bgcolor="#ffffff">ki(ru), ki(reru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to cut, come to an end</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8AAC</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="説" href="https://nihongoichiban.com/2011/05/13/%e8%aa%ac/" target="_blank">説</a></td>
<td align="left" bgcolor="#ffffff">SETSU</td>
<td align="left" bgcolor="#ffffff">to(ku)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">opinion, theory, explain</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6D17</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="洗" href="https://nihongoichiban.com/2011/05/14/%e6%b4%97/" target="_blank">洗</a></td>
<td align="left" bgcolor="#ffffff">SEN</td>
<td align="left" bgcolor="#ffffff">ara(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to wash</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">65E9</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="早" href="https://nihongoichiban.com/2011/05/14/%e6%97%a9/" target="_blank">早</a></td>
<td align="left" bgcolor="#ffffff">SOU, SA</td>
<td align="left" bgcolor="#ffffff">haya(i), haya(meru/maru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">fast, early, to speed up</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8D70</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="走" href="https://nihongoichiban.com/2011/05/14/%e8%b5%b0/" target="_blank">走</a></td>
<td align="left" bgcolor="#ffffff">SOU</td>
<td align="left" bgcolor="#ffffff">hashi(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to run</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9001</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="送" href="https://nihongoichiban.com/2011/05/14/%e9%80%81/" target="_blank">送</a></td>
<td align="left" bgcolor="#ffffff">SOU</td>
<td align="left" bgcolor="#ffffff">oku(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to send</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">65CF</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="族" href="https://nihongoichiban.com/2011/05/14/%e6%97%8f/" target="_blank">族</a></td>
<td align="left" bgcolor="#ffffff">ZOKU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">family, tribe</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6751</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="村" href="https://nihongoichiban.com/2011/05/14/%e6%9d%91/" target="_blank">村</a></td>
<td align="left" bgcolor="#ffffff">SON</td>
<td align="left" bgcolor="#ffffff">mura</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">village</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4F53</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="体" href="https://nihongoichiban.com/2011/05/14/%e4%bd%93/" target="_blank">体</a></td>
<td align="left" bgcolor="#ffffff">TAI, TEI</td>
<td align="left" bgcolor="#ffffff">karada</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">body</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">592A</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="太" href="https://nihongoichiban.com/2011/05/14/%e5%a4%aa/" target="_blank">太</a></td>
<td align="left" bgcolor="#ffffff">TAI, TA</td>
<td align="left" bgcolor="#ffffff">futo(i), futo(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">bold, thick</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5F85</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="待" href="https://nihongoichiban.com/2011/05/15/%e5%be%85/" target="_blank">待</a></td>
<td align="left" bgcolor="#ffffff">TAI</td>
<td align="left" bgcolor="#ffffff">ma(tsu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to wait</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8CB8</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="貸" href="https://nihongoichiban.com/2011/05/15/%e8%b2%b8/" target="_blank">貸</a></td>
<td align="left" bgcolor="#ffffff">TAI</td>
<td align="left" bgcolor="#ffffff">ka(su)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to lend</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">53F0</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="台" href="https://nihongoichiban.com/2011/05/15/%e5%8f%b0/" target="_blank">台</a></td>
<td align="left" bgcolor="#ffffff">DAI, TAI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">frame, basis, pedestal</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4EE3</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="代" href="https://nihongoichiban.com/2011/05/15/%e4%bb%a3/" target="_blank">代</a></td>
<td align="left" bgcolor="#ffffff">DAI, TAI</td>
<td align="left" bgcolor="#ffffff">ka(waru), ka(eru), yo, shiro</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">generation, age, replace</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">984C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="題" href="https://nihongoichiban.com/2011/05/15/%e9%a1%8c/" target="_blank">題</a></td>
<td align="left" bgcolor="#ffffff">DAI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">title, theme, subject</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">77ED</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="短" href="https://nihongoichiban.com/2011/05/15/%e7%9f%ad/" target="_blank">短</a></td>
<td align="left" bgcolor="#ffffff">TAN</td>
<td align="left" bgcolor="#ffffff">mijika(i)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">short</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">77E5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="知" href="https://nihongoichiban.com/2011/05/15/%e7%9f%a5/" target="_blank">知</a></td>
<td align="left" bgcolor="#ffffff">CHI</td>
<td align="left" bgcolor="#ffffff">shi(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to know</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5730</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="地" href="https://nihongoichiban.com/2011/05/15/%e5%9c%b0/" target="_blank">地</a></td>
<td align="left" bgcolor="#ffffff">CHI, JI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">earth, land</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6C60</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="池" href="https://nihongoichiban.com/2011/05/15/%e6%b1%a0/" target="_blank">池</a></td>
<td align="left" bgcolor="#ffffff">CHI</td>
<td align="left" bgcolor="#ffffff">ike</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">pond</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8336</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="茶" href="https://nihongoichiban.com/2011/05/16/%e8%8c%b6/" target="_blank">茶</a></td>
<td align="left" bgcolor="#ffffff">CHA, SA</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">tea</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7740</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="着" href="https://nihongoichiban.com/2011/05/16/%e7%9d%80/" target="_blank">着</a></td>
<td align="left" bgcolor="#ffffff">CHAKU</td>
<td align="left" bgcolor="#ffffff">ki(ru), tsu(keru), ki(seru), tsu(ku)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">arrival, clothes</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">663C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="昼" href="https://nihongoichiban.com/2011/05/16/%e6%98%bc/" target="_blank">昼</a></td>
<td align="left" bgcolor="#ffffff">CHUU</td>
<td align="left" bgcolor="#ffffff">hiru</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">noon</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6CE8</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="注" href="https://nihongoichiban.com/2011/05/17/%e6%b3%a8/" target="_blank">注</a></td>
<td align="left" bgcolor="#ffffff">CHUU</td>
<td align="left" bgcolor="#ffffff">soso(gu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">notice, attention, flow</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">753A</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="町" href="https://nihongoichiban.com/2011/05/17/%e7%94%ba/" target="_blank">町</a></td>
<td align="left" bgcolor="#ffffff">CHOU</td>
<td align="left" bgcolor="#ffffff">machi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">city, quarter, district</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9CE5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="鳥" href="https://nihongoichiban.com/2011/05/17/%e9%b3%a5/" target="_blank">鳥</a></td>
<td align="left" bgcolor="#ffffff">CHOU</td>
<td align="left" bgcolor="#ffffff">tori</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">bird</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">671D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="朝" href="https://nihongoichiban.com/2011/05/17/%e6%9c%9d/" target="_blank">朝</a></td>
<td align="left" bgcolor="#ffffff">CHOU</td>
<td align="left" bgcolor="#ffffff">asa</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">morning</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">901A</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="通" href="https://nihongoichiban.com/2011/05/18/%e9%80%9a/" target="_blank">通</a></td>
<td align="left" bgcolor="#ffffff">TSUU</td>
<td align="left" bgcolor="#ffffff">tou(ru), tou(su), kayo(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to pass</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5F1F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="弟" href="https://nihongoichiban.com/2011/05/18/%e5%bc%9f/" target="_blank">弟</a></td>
<td align="left" bgcolor="#ffffff">TEI</td>
<td align="left" bgcolor="#ffffff">otouto</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">younger brother</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4F4E</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="低" href="https://nihongoichiban.com/2011/05/18/%e4%bd%8e/" target="_blank">低</a></td>
<td align="left" bgcolor="#ffffff">TEI</td>
<td align="left" bgcolor="#ffffff">hiku(i), hiku(meru/maru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">low, to lower</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8EE2</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="転" href="https://nihongoichiban.com/2011/05/18/%e8%bb%a2/" target="_blank">転</a></td>
<td align="left" bgcolor="#ffffff">TEN</td>
<td align="left" bgcolor="#ffffff">koro(bu), koro(garu/geru), koro(gasu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to roll, to turn</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7530</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="田" href="https://nihongoichiban.com/2011/05/19/%e7%94%b0/" target="_blank">田</a></td>
<td align="left" bgcolor="#ffffff">DEN</td>
<td align="left" bgcolor="#ffffff">ta</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">rice field</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">90FD</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="都" href="https://nihongoichiban.com/2011/05/19/%e9%83%bd/" target="_blank">都</a></td>
<td align="left" bgcolor="#ffffff">TO, TSU</td>
<td align="left" bgcolor="#ffffff">miyako</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">capital</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5EA8</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="度" href="https://nihongoichiban.com/2011/05/20/%e5%ba%a6/" target="_blank">度</a></td>
<td align="left" bgcolor="#ffffff">DO</td>
<td align="left" bgcolor="#ffffff">tabi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">measure, degree</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7B54</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="答" href="https://nihongoichiban.com/2011/05/21/%e7%ad%94/" target="_blank">答</a></td>
<td align="left" bgcolor="#ffffff">TOU</td>
<td align="left" bgcolor="#ffffff">kota(e), kota(eru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">answer</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">51AC</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="冬" href="https://nihongoichiban.com/2011/05/21/%e5%86%ac/" target="_blank">冬</a></td>
<td align="left" bgcolor="#ffffff">TOU</td>
<td align="left" bgcolor="#ffffff">fuyu</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">winter</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">982D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="頭" href="https://nihongoichiban.com/2011/05/21/%e9%a0%ad/" target="_blank">頭</a></td>
<td align="left" bgcolor="#ffffff">TOU, ZU</td>
<td align="left" bgcolor="#ffffff">atama, kashira</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">head, master540C</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">540C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="同" href="https://nihongoichiban.com/2011/05/21/%e5%90%8c/" target="_blank">同</a></td>
<td align="left" bgcolor="#ffffff">DOU</td>
<td align="left" bgcolor="#ffffff">ona(ji)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">same</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">52D5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="動" href="https://nihongoichiban.com/2011/05/21/%e5%8b%95/" target="_blank">動</a></td>
<td align="left" bgcolor="#ffffff">DOU</td>
<td align="left" bgcolor="#ffffff">ugo(ku), ugo(kasu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to move</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5802</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="堂" href="https://nihongoichiban.com/2011/05/22/%e5%a0%82/" target="_blank">堂</a></td>
<td align="left" bgcolor="#ffffff">DOU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">room, hall, temple</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">50CD</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="働" href="https://nihongoichiban.com/2011/05/22/%e5%83%8d/" target="_blank">働</a></td>
<td align="left" bgcolor="#ffffff">DOU</td>
<td align="left" bgcolor="#ffffff">hatara(ku)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to work</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7279</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="特" href="https://nihongoichiban.com/2011/05/22/%e7%89%b9/" target="_blank">特</a></td>
<td align="left" bgcolor="#ffffff">TOKU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">special</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">8089</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="肉" href="https://nihongoichiban.com/2011/05/22/%e8%82%89/" target="_blank">肉</a></td>
<td align="left" bgcolor="#ffffff">NIKU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">meat</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">58F2</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="売" href="https://nihongoichiban.com/2011/05/22/%e5%a3%b2/" target="_blank">売</a></td>
<td align="left" bgcolor="#ffffff">BAI</td>
<td align="left" bgcolor="#ffffff">u(ru), u(reru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to sell</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">767A</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="発" href="https://nihongoichiban.com/2011/05/22/%e7%99%ba/" target="_blank">発</a></td>
<td align="left" bgcolor="#ffffff">HATSU, HOTSU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">start, to leave, issue</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">98EF</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="飯" href="https://nihongoichiban.com/2011/05/22/%e9%a3%af/" target="_blank">飯</a></td>
<td align="left" bgcolor="#ffffff">HAN</td>
<td align="left" bgcolor="#ffffff">meshi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">meal, cooked rice</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">75C5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="病" href="https://nihongoichiban.com/2011/05/23/%e7%97%85/" target="_blank">病</a></td>
<td align="left" bgcolor="#ffffff">BYOU</td>
<td align="left" bgcolor="#ffffff">ya(mu), yamai</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff"> sickness, illness</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">54C1</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="品" href="https://nihongoichiban.com/2011/05/23/%e5%93%81/" target="_blank">品</a></td>
<td align="left" bgcolor="#ffffff">HIN</td>
<td align="left" bgcolor="#ffffff">shina</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">product, quality</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4E0D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="不" href="https://nihongoichiban.com/2011/05/24/%e4%b8%8d/" target="_blank">不</a></td>
<td align="left" bgcolor="#ffffff">FU, BU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">not</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">98A8</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="風" href="https://nihongoichiban.com/2011/05/25/%e9%a2%a8/" target="_blank">風</a></td>
<td align="left" bgcolor="#ffffff">FUU</td>
<td align="left" bgcolor="#ffffff">kaze</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">wind, style</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">670D</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="服" href="https://nihongoichiban.com/2011/05/25/%e6%9c%8d/" target="_blank">服</a></td>
<td align="left" bgcolor="#ffffff">FUKU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">clothing</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7269</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="物" href="https://nihongoichiban.com/2011/05/25/%e7%89%a9/" target="_blank">物</a></td>
<td align="left" bgcolor="#ffffff">BUTSU, MOTSU</td>
<td align="left" bgcolor="#ffffff">mono</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">thing</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6587</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="文" href="https://nihongoichiban.com/2011/05/26/%e6%96%87/" target="_blank">文</a></td>
<td align="left" bgcolor="#ffffff">BUN, MON</td>
<td align="left" bgcolor="#ffffff">fumi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">literature, sentence, letter</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5225</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="別" href="https://nihongoichiban.com/2011/05/26/%e5%88%a5/" target="_blank">別</a></td>
<td align="left" bgcolor="#ffffff">BETSU</td>
<td align="left" bgcolor="#ffffff">waka(reru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">difference, to part</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">52C9</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="勉" href="https://nihongoichiban.com/2011/05/27/%e5%8b%89/" target="_blank">勉</a></td>
<td align="left" bgcolor="#ffffff">BEN</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">hard work, effort</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">4FBF</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="便" href="https://nihongoichiban.com/2011/05/28/%e4%be%bf/" target="_blank">便</a></td>
<td align="left" bgcolor="#ffffff">BEN, BIN</td>
<td align="left" bgcolor="#ffffff">tayo(ri)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">comfort, excrement, message</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6B69</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="歩" href="https://nihongoichiban.com/2011/05/28/%e6%ad%a9/" target="_blank">歩</a></td>
<td align="left" bgcolor="#ffffff">HO, BU</td>
<td align="left" bgcolor="#ffffff">aru(ku), ayu(mu)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to walk</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">65B9</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="方" href="https://nihongoichiban.com/2011/05/28/%e6%96%b9/" target="_blank">方</a></td>
<td align="left" bgcolor="#ffffff">HOU</td>
<td align="left" bgcolor="#ffffff">kata</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">direction, person</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">59B9</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="妹" href="https://nihongoichiban.com/2011/05/28/%e5%a6%b9/" target="_blank">妹</a></td>
<td align="left" bgcolor="#ffffff">MAI</td>
<td align="left" bgcolor="#ffffff">imouto</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">younger sister</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">5473</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="味" href="https://nihongoichiban.com/2011/05/28/%e5%91%b3/" target="_blank">味</a></td>
<td align="left" bgcolor="#ffffff">MI</td>
<td align="left" bgcolor="#ffffff">aji, aji(waru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">taste, to savor, to enjoy</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6C11</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="民" href="https://nihongoichiban.com/2011/05/28/%e6%b0%91/" target="_blank">民</a></td>
<td align="left" bgcolor="#ffffff">MIN</td>
<td align="left" bgcolor="#ffffff">tami</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">nation, people</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">660E</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="明" href="https://nihongoichiban.com/2011/05/28/%e6%98%8e/" target="_blank">明</a></td>
<td align="left" bgcolor="#ffffff">MEI</td>
<td align="left" bgcolor="#ffffff">a(kari), aka(rui)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">light, brightness, to be open</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">9580</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="門" href="https://nihongoichiban.com/2011/05/28/%e9%96%80/" target="_blank">門</a></td>
<td align="left" bgcolor="#ffffff">MON</td>
<td align="left" bgcolor="#ffffff">kado</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">gate</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">554F</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="問" href="https://nihongoichiban.com/2011/05/28/%e5%95%8f/" target="_blank">問</a></td>
<td align="left" bgcolor="#ffffff">MON</td>
<td align="left" bgcolor="#ffffff">to(i), to(u)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">question, take care of</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">591C</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="夜" href="https://nihongoichiban.com/2011/05/28/%e5%a4%9c/" target="_blank">夜</a></td>
<td align="left" bgcolor="#ffffff">YA</td>
<td align="left" bgcolor="#ffffff">yoro, yo~</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">night</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">91CE</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="野" href="https://nihongoichiban.com/2011/05/30/%e9%87%8e/" target="_blank">野</a></td>
<td align="left" bgcolor="#ffffff">YA</td>
<td align="left" bgcolor="#ffffff">no</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">field</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">85AC</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="薬" href="https://nihongoichiban.com/2011/05/29/%e8%96%ac/" target="_blank">薬</a></td>
<td align="left" bgcolor="#ffffff">YAKU</td>
<td align="left" bgcolor="#ffffff">kusuri</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">drug, medicine, chemical</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6709</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="有" href="https://nihongoichiban.com/2011/05/29/%e6%9c%89/" target="_blank">有</a></td>
<td align="left" bgcolor="#ffffff">YUU, U</td>
<td align="left" bgcolor="#ffffff">a(ru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">to exist, to be, to have</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">66DC</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="曜" href="https://nihongoichiban.com/2011/05/29/%e6%9b%9c/" target="_blank">曜</a></td>
<td align="left" bgcolor="#ffffff">YOU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">weekday</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7528</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="用" href="https://nihongoichiban.com/2011/05/29/%e7%94%a8/" target="_blank">用</a></td>
<td align="left" bgcolor="#ffffff">YOU</td>
<td align="left" bgcolor="#ffffff">mochi(iru)</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">issue, to use</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6D0B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="洋" href="https://nihongoichiban.com/2011/05/29/%e6%b4%8b/" target="_blank">洋</a></td>
<td align="left" bgcolor="#ffffff">YOU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">ocean, western, foreign</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">7406</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="理" href="https://nihongoichiban.com/2011/05/29/%e7%90%86/" target="_blank">理</a></td>
<td align="left" bgcolor="#ffffff">RI</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">reason, principle</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">65C5</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="旅" href="https://nihongoichiban.com/2011/05/30/%e6%97%85/" target="_blank">旅</a></td>
<td align="left" bgcolor="#ffffff">RYO</td>
<td align="left" bgcolor="#ffffff">tabi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">trip, travel</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6599</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="料" href="https://nihongoichiban.com/2011/05/30/%e6%96%99/" target="_blank">料</a></td>
<td align="left" bgcolor="#ffffff">RYOU</td>
<td align="left" bgcolor="#ffffff">&#8211;</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">material, charge</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">529B</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="力" href="https://nihongoichiban.com/2011/05/30/%e5%8a%9b/" target="_blank">力</a></td>
<td align="left" bgcolor="#ffffff">RYOKU, RIKI</td>
<td align="left" bgcolor="#ffffff">chikara</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">power, force</td>
</tr>
<tr valign="top">
<td align="middle" bgcolor="#ffffff">6797</td>
<td style="text-align:center;" align="left" bgcolor="#ffffff"><a title="林" href="https://nihongoichiban.com/2011/05/30/%e6%9e%97/" target="_blank">林</a></td>
<td align="left" bgcolor="#ffffff">RIN</td>
<td align="left" bgcolor="#ffffff">hayashi</td>
<td style="text-align:left;" align="middle" bgcolor="#ffffff">woods</td>
</tr>"""
# Парсинг HTML
soup = BeautifulSoup(html, 'html.parser')

# Создание CSV
with open('kanji_n4_ENG.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['kanji', 'meaning'])

    for row in soup.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) >= 5:
            kanji = cells[1].text.strip()
            meaning = cells[4].text.strip()
            writer.writerow([kanji, meaning])

print("Файл 'kanji_n4_ENG.csv' успешно создан.")
from bs4 import BeautifulSoup

# Пример HTML-кода (замените на свой)
html_content = """
<tr class="row0" id="0">
        <td class="pos">
          0
        </td>
        <td class="kanji">
          あ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          int
        </td>
        <td class="eng">
          Ah
        </td>
      </tr>
      <tr class="row1" id="1">
        <td class="pos">
          1
        </td>
        <td class="kanji">
          ああ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          int
        </td>
        <td class="eng">
          like that, that way
        </td>
      </tr>
      <tr class="row0" id="2">
        <td class="pos">
          2
        </td>
        <td class="kanji">
          あいさつ・する
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          greeting
        </td>
      </tr>
      <tr class="row1" id="3">
        <td class="pos">
          3
        </td>
        <td class="kanji">
          あいだ
        </td>
        <td class="kanji">
          間
        </td>
        <td>
          n
        </td>
        <td class="eng">
          space, interval
        </td>
      </tr>
      <tr class="row0" id="4">
        <td class="pos">
          4
        </td>
        <td class="kanji">
          あう
        </td>
        <td class="kanji">
          合う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to fit, to match
        </td>
      </tr>
      <tr class="row1" id="5">
        <td class="pos">
          5
        </td>
        <td class="kanji">
          あかちゃん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          baby, infant
        </td>
      </tr>
      <tr class="row0" id="6">
        <td class="pos">
          6
        </td>
        <td class="kanji">
          あがる
        </td>
        <td class="kanji">
          上がる
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to rise, to go up
        </td>
      </tr>
      <tr class="row1" id="7">
        <td class="pos">
          7
        </td>
        <td class="kanji">
          あかんぼう
        </td>
        <td class="kanji">
          赤ん坊
        </td>
        <td>
          n
        </td>
        <td class="eng">
          baby
        </td>
      </tr>
      <tr class="row0" id="8">
        <td class="pos">
          8
        </td>
        <td class="kanji">
          あく
        </td>
        <td class="kanji">
          空く
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to open, to become empty
        </td>
      </tr>
      <tr class="row1" id="9">
        <td class="pos">
          9
        </td>
        <td class="kanji">
          アクセサリー
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          accessory
        </td>
      </tr>
      <tr class="row0" id="10">
        <td class="pos">
          10
        </td>
        <td class="kanji">
          あげる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to give
        </td>
      </tr>
      <tr class="row1" id="11">
        <td class="pos">
          11
        </td>
        <td class="kanji">
          あさい
        </td>
        <td class="kanji">
          浅い
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          shallow, superficial
        </td>
      </tr>
      <tr class="row0" id="12">
        <td class="pos">
          12
        </td>
        <td class="kanji">
          あじ
        </td>
        <td class="kanji">
          味
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          flavor, taste
        </td>
      </tr>
      <tr class="row1" id="13">
        <td class="pos">
          13
        </td>
        <td class="kanji">
          アジア
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          Asia
        </td>
      </tr>
      <tr class="row0" id="14">
        <td class="pos">
          14
        </td>
        <td class="kanji">
          あす
        </td>
        <td class="kanji">
          明日
        </td>
        <td>
          n-t
        </td>
        <td class="eng">
          tomorrow
        </td>
      </tr>
      <tr class="row1" id="15">
        <td class="pos">
          15
        </td>
        <td class="kanji">
          あそび
        </td>
        <td class="kanji">
          遊び
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          play
        </td>
      </tr>
      <tr class="row0" id="16">
        <td class="pos">
          16
        </td>
        <td class="kanji">
          あつまる
        </td>
        <td class="kanji">
          集る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to gather, to collect
        </td>
      </tr>
      <tr class="row1" id="17">
        <td class="pos">
          17
        </td>
        <td class="kanji">
          あつめる
        </td>
        <td class="kanji">
          集める
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to collect, to assemble
        </td>
      </tr>
      <tr class="row0" id="18">
        <td class="pos">
          18
        </td>
        <td class="kanji">
          アナウンサー
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          announcer
        </td>
      </tr>
      <tr class="row1" id="19">
        <td class="pos">
          19
        </td>
        <td class="kanji">
          アフリカ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          Africa
        </td>
      </tr>
      <tr class="row0" id="20">
        <td class="pos">
          20
        </td>
        <td class="kanji">
          アメリカ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          America
        </td>
      </tr>
      <tr class="row1" id="21">
        <td class="pos">
          21
        </td>
        <td class="kanji">
          あやまる
        </td>
        <td class="kanji">
          謝る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to apologize
        </td>
      </tr>
      <tr class="row0" id="22">
        <td class="pos">
          22
        </td>
        <td class="kanji">
          アルコール
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          alcohol
        </td>
      </tr>
      <tr class="row1" id="23">
        <td class="pos">
          23
        </td>
        <td class="kanji">
          アルバイト
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          part-time job
        </td>
      </tr>
      <tr class="row0" id="24">
        <td class="pos">
          24
        </td>
        <td class="kanji">
          あんしん
        </td>
        <td class="kanji">
          安心
        </td>
        <td>
          adj-na,n, vs
        </td>
        <td class="eng">
          peace of mind, relief
        </td>
      </tr>
      <tr class="row1" id="25">
        <td class="pos">
          25
        </td>
        <td class="kanji">
          あんぜん
        </td>
        <td class="kanji">
          安全
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          safety, security
        </td>
      </tr>
      <tr class="row0" id="26">
        <td class="pos">
          26
        </td>
        <td class="kanji">
          あんな
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,adj-pn
        </td>
        <td class="eng">
          such, like that
        </td>
      </tr>
      <tr class="row1" id="27">
        <td class="pos">
          27
        </td>
        <td class="kanji">
          あんない・する
        </td>
        <td class="kanji">
          案内
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          information, guidance
        </td>
      </tr>
      <tr class="row0" id="28">
        <td class="pos">
          28
        </td>
        <td class="kanji">
          いか
        </td>
        <td class="kanji">
          以下
        </td>
        <td>
          n
        </td>
        <td class="eng">
          less than, below
        </td>
      </tr>
      <tr class="row1" id="29">
        <td class="pos">
          29
        </td>
        <td class="kanji">
          いがい
        </td>
        <td class="kanji">
          以外
        </td>
        <td>
          n
        </td>
        <td class="eng">
          with the exception of, excepting
        </td>
      </tr>
      <tr class="row0" id="30">
        <td class="pos">
          30
        </td>
        <td class="kanji">
          いがく
        </td>
        <td class="kanji">
          医学
        </td>
        <td>
          n
        </td>
        <td class="eng">
          medical science
        </td>
      </tr>
      <tr class="row1" id="31">
        <td class="pos">
          31
        </td>
        <td class="kanji">
          いきる
        </td>
        <td class="kanji">
          生きる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to live, to exist
        </td>
      </tr>
      <tr class="row0" id="32">
        <td class="pos">
          32
        </td>
        <td class="kanji">
          いくら～ても
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          however much one may ～
        </td>
      </tr>
      <tr class="row1" id="33">
        <td class="pos">
          33
        </td>
        <td class="kanji">
          いけん
        </td>
        <td class="kanji">
          意見
        </td>
        <td>
          n
        </td>
        <td class="eng">
          opinion, view
        </td>
      </tr>
      <tr class="row0" id="34">
        <td class="pos">
          34
        </td>
        <td class="kanji">
          いし
        </td>
        <td class="kanji">
          石
        </td>
        <td>
          n
        </td>
        <td class="eng">
          stone
        </td>
      </tr>
      <tr class="row1" id="35">
        <td class="pos">
          35
        </td>
        <td class="kanji">
          いじめる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to tease, to torment
        </td>
      </tr>
      <tr class="row0" id="36">
        <td class="pos">
          36
        </td>
        <td class="kanji">
          いじょう
        </td>
        <td class="kanji">
          以上
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          more than, this is all
        </td>
      </tr>
      <tr class="row1" id="37">
        <td class="pos">
          37
        </td>
        <td class="kanji">
          いそぐ
        </td>
        <td class="kanji">
          急ぐ
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to hurry, to rush
        </td>
      </tr>
      <tr class="row0" id="38">
        <td class="pos">
          38
        </td>
        <td class="kanji">
          いたす
        </td>
        <td class="kanji">
          致す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (hum) to do
        </td>
      </tr>
      <tr class="row0" id="38">
        <td class="pos">
          38
        </td>
        <td class="kanji">
          いたす
        </td>
        <td class="kanji">
          致す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (hum) to do
        </td>
      </tr><tr class="row1" id="39">
        <td class="pos">
          39
        </td>
        <td class="kanji">
          いただく
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to receive, to take food or drink (hum)
        </td>
      </tr>
      <tr class="row0" id="40">
        <td class="pos">
          40
        </td>
        <td class="kanji">
          いちど
        </td>
        <td class="kanji">
          一度
        </td>
        <td>
          n-adv
        </td>
        <td class="eng">
          once, one time
        </td>
      </tr>
      <tr class="row1" id="41">
        <td class="pos">
          41
        </td>
        <td class="kanji">
          いっしょうけんめい
        </td>
        <td class="kanji">
          一生懸命
        </td>
        <td>
          adj-na,n-adv,n
        </td>
        <td class="eng">
          as well as one can, with utmost effort
        </td>
      </tr>
      <tr class="row0" id="42">
        <td class="pos">
          42
        </td>
        <td class="kanji">
          いっぱい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          full, to the utmost
        </td>
      </tr>
      <tr class="row1" id="43">
        <td class="pos">
          43
        </td>
        <td class="kanji">
          いと
        </td>
        <td class="kanji">
          糸
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          thread
        </td>
      </tr>
      <tr class="row0" id="44">
        <td class="pos">
          44
        </td>
        <td class="kanji">
          いない
        </td>
        <td class="kanji">
          以内
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          within, inside of
        </td>
      </tr>
      <tr class="row1" id="45">
        <td class="pos">
          45
        </td>
        <td class="kanji">
          いなか
        </td>
        <td class="kanji">
          田舎
        </td>
        <td>
          giku n
        </td>
        <td class="eng">
          rural, countryside
        </td>
      </tr>
      <tr class="row0" id="46">
        <td class="pos">
          46
        </td>
        <td class="kanji">
          いのる
        </td>
        <td class="kanji">
          祈る
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to pray, to wish
        </td>
      </tr>
      <tr class="row1" id="47">
        <td class="pos">
          47
        </td>
        <td class="kanji">
          いらっしゃる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          aru-v
        </td>
        <td class="eng">
          (hon) to be, to come, to go
        </td>
      </tr>
      <tr class="row0" id="48">
        <td class="pos">
          48
        </td>
        <td class="kanji">
          ～いん
        </td>
        <td class="kanji">
          ～員
        </td>
        <td>
          n-suf
        </td>
        <td class="eng">
          member of ～
        </td>
      </tr>
      <tr class="row1" id="49">
        <td class="pos">
          49
        </td>
        <td class="kanji">
          うえる
        </td>
        <td class="kanji">
          植える
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to plant, to grow
        </td>
      </tr>
      <tr class="row0" id="50">
        <td class="pos">
          50
        </td>
        <td class="kanji">
          うかがう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v,vi,vt
        </td>
        <td class="eng">
          to visit
        </td>
      </tr>
      <tr class="row1" id="51">
        <td class="pos">
          51
        </td>
        <td class="kanji">
          うかがう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v,vi,vt
        </td>
        <td class="eng">
          to ask
        </td>
      </tr>
      <tr class="row0" id="52">
        <td class="pos">
          52
        </td>
        <td class="kanji">
          うけつけ
        </td>
        <td class="kanji">
          受付
        </td>
        <td>
          n
        </td>
        <td class="eng">
          reception (desk), information ガス
        </td>
      </tr>
      <tr class="row1" id="53">
        <td class="pos">
          53
        </td>
        <td class="kanji">
          うける
        </td>
        <td class="kanji">
          受ける
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to take (lesson, test), to undergo
        </td>
      </tr>
      <tr class="row0" id="54">
        <td class="pos">
          54
        </td>
        <td class="kanji">
          うごく
        </td>
        <td class="kanji">
          動く
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to move
        </td>
      </tr>
      <tr class="row1" id="55">
        <td class="pos">
          55
        </td>
        <td class="kanji">
          うそ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          lie
        </td>
      </tr>
      <tr class="row0" id="56">
        <td class="pos">
          56
        </td>
        <td class="kanji">
          うち
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          within
        </td>
      </tr>
      <tr class="row1" id="57">
        <td class="pos">
          57
        </td>
        <td class="kanji">
          うつ
        </td>
        <td class="kanji">
          打つ
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to hit, to strike
        </td>
      </tr>
      <tr class="row0" id="58">
        <td class="pos">
          58
        </td>
        <td class="kanji">
          うつくしい
        </td>
        <td class="kanji">
          美しい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          beautiful, lovely
        </td>
      </tr>
      <tr class="row1" id="59">
        <td class="pos">
          59
        </td>
        <td class="kanji">
          うつす
        </td>
        <td class="kanji">
          写す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          copy, to photograph, to film
        </td>
      </tr>
      <tr class="row0" id="60">
        <td class="pos">
          60
        </td>
        <td class="kanji">
          うつる
        </td>
        <td class="kanji">
          移る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to move (house), to transfer (department)
        </td>
      </tr>
      <tr class="row1" id="61">
        <td class="pos">
          61
        </td>
        <td class="kanji">
          うで
        </td>
        <td class="kanji">
          腕
        </td>
        <td>
          n
        </td>
        <td class="eng">
          arm
        </td>
      </tr>
      <tr class="row0" id="62">
        <td class="pos">
          62
        </td>
        <td class="kanji">
          うまい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          delicious
        </td>
      </tr>
      <tr class="row1" id="63">
        <td class="pos">
          63
        </td>
        <td class="kanji">
          うら
        </td>
        <td class="kanji">
          裏
        </td>
        <td>
          n
        </td>
        <td class="eng">
          reverse side, wrong side, back
        </td>
      </tr>
      <tr class="row0" id="64">
        <td class="pos">
          64
        </td>
        <td class="kanji">
          うりば
        </td>
        <td class="kanji">
          売り場
        </td>
        <td>
          adj-no,n
        </td>
        <td class="eng">
          place where things are sold
        </td>
      </tr>
      <tr class="row1" id="65">
        <td class="pos">
          65
        </td>
        <td class="kanji">
          うれしい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          happy, glad
        </td>
      </tr>
      <tr class="row0" id="66">
        <td class="pos">
          66
        </td>
        <td class="kanji">
          うん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          yes (informal), alright
        </td>
      </tr>
      <tr class="row1" id="67">
        <td class="pos">
          67
        </td>
        <td class="kanji">
          うんてんしゅ
        </td>
        <td class="kanji">
          運転手
        </td>
        <td>
          n
        </td>
        <td class="eng">
          driver, chauffeur
        </td>
      </tr>
      <tr class="row0" id="68">
        <td class="pos">
          68
        </td>
        <td class="kanji">
          うんてん・する
        </td>
        <td class="kanji">
          運転
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          driving
        </td>
      </tr>
      <tr class="row1" id="69">
        <td class="pos">
          69
        </td>
        <td class="kanji">
          うんどう・する
        </td>
        <td class="kanji">
          運動
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          exercise
        </td>
      </tr>
      <tr class="row0" id="70">
        <td class="pos">
          70
        </td>
        <td class="kanji">
          エスカレーター
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          escalator
        </td>
      </tr>
      <tr class="row1" id="71">
        <td class="pos">
          71
        </td>
        <td class="kanji">
          えだ
        </td>
        <td class="kanji">
          枝
        </td>
        <td>
          n
        </td>
        <td class="eng">
          branch, twig
        </td>
      </tr>
      <tr class="row0" id="72">
        <td class="pos">
          72
        </td>
        <td class="kanji">
          えらぶ
        </td>
        <td class="kanji">
          選ぶ
        </td>
        <td>
          v5b
        </td>
        <td class="eng">
          to choose, to select
        </td>
      </tr>
      <tr class="row1" id="73">
        <td class="pos">
          73
        </td>
        <td class="kanji">
          えんりょ・する
        </td>
        <td class="kanji">
          遠慮
        </td>
        <td>
          adj-na,n,vs
        </td>
        <td class="eng">
          restraint, reserve
        </td>
      </tr>
      <tr class="row0" id="74">
        <td class="pos">
          74
        </td>
        <td class="kanji">
          おいでになる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (hon)to be
        </td>
      </tr>
      <tr class="row1" id="75">
        <td class="pos">
          75
        </td>
        <td class="kanji">
          おいわい
        </td>
        <td class="kanji">
          お祝い
        </td>
        <td>
          n
        </td>
        <td class="eng">
          congratulation, celebration
        </td>
      </tr>
      <tr class="row0" id="76">
        <td class="pos">
          76
        </td>
        <td class="kanji">
          オートバイ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          motorcycle (lit: auto-bi(ke))
        </td>
      </tr>
      <tr class="row1" id="77">
        <td class="pos">
          77
        </td>
        <td class="kanji">
          オーバー
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,n,vs
        </td>
        <td class="eng">
          overcoat
        </td>
      </tr>
      <tr class="row0" id="78">
        <td class="pos">
          78
        </td>
        <td class="kanji">
          おかげ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          thanks or owing to
        </td>
      </tr>
      <tr class="row1" id="79">
        <td class="pos">
          79
        </td>
        <td class="kanji">
          おかしい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          strange, funny
        </td>
      </tr>
      <tr class="row0" id="80">
        <td class="pos">
          80
        </td>
        <td class="kanji">
          ～おき
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          after every ～
        </td>
      </tr>
      <tr class="row1" id="81">
        <td class="pos">
          81
        </td>
        <td class="kanji">
          おく
        </td>
        <td class="kanji">
          億
        </td>
        <td>
          num
        </td>
        <td class="eng">
          100,000,000, hundred million
        </td>
      </tr>
      <tr class="row0" id="82">
        <td class="pos">
          82
        </td>
        <td class="kanji">
          おくじょう
        </td>
        <td class="kanji">
          屋上
        </td>
        <td>
          n
        </td>
        <td class="eng">
          rooftop
        </td>
      </tr>
      <tr class="row1" id="83">
        <td class="pos">
          83
        </td>
        <td class="kanji">
          おくりもの
        </td>
        <td class="kanji">
          贈り物
        </td>
        <td>
          n
        </td>
        <td class="eng">
          present, gift
        </td>
      </tr>
      <tr class="row0" id="84">
        <td class="pos">
          84
        </td>
        <td class="kanji">
          おくる
        </td>
        <td class="kanji">
          送る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to send (a thing), to dispatch
        </td>
      </tr>
      <tr class="row1" id="85">
        <td class="pos">
          85
        </td>
        <td class="kanji">
          おくれる
        </td>
        <td class="kanji">
          遅れる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to be late, to be delayed
        </td>
      </tr>
      <tr class="row0" id="86">
        <td class="pos">
          86
        </td>
        <td class="kanji">
          おこさん
        </td>
        <td class="kanji">
          お子さん
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (someone else's) child
        </td>
      </tr>
      <tr class="row1" id="87">
        <td class="pos">
          87
        </td>
        <td class="kanji">
          おこす
        </td>
        <td class="kanji">
          起こす
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to wake someone
        </td>
      </tr>
      <tr class="row0" id="88">
        <td class="pos">
          88
        </td>
        <td class="kanji">
          おこなう
        </td>
        <td class="kanji">
          行う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to perform, to do, to carry out
        </td>
      </tr>
      <tr class="row1" id="89">
        <td class="pos">
          89
        </td>
        <td class="kanji">
          おこる
        </td>
        <td class="kanji">
          怒る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to get angry, to be angry
        </td>
      </tr>
      <tr class="row0" id="90">
        <td class="pos">
          90
        </td>
        <td class="kanji">
          おしいれ
        </td>
        <td class="kanji">
          押し入れ
        </td>
        <td>
          n
        </td>
        <td class="eng">
          closet
        </td>
      </tr>
      <tr class="row1" id="91">
        <td class="pos">
          91
        </td>
        <td class="kanji">
          おじょうさん
        </td>
        <td class="kanji">
          お嬢さん
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (1) (hon) daughter, (2) young lady
        </td>
      </tr>
      <tr class="row0" id="92">
        <td class="pos">
          92
        </td>
        <td class="kanji">
          おたく
        </td>
        <td class="kanji">
          お宅
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (pol) your house, your home
        </td>
      </tr>
      <tr class="row1" id="93">
        <td class="pos">
          93
        </td>
        <td class="kanji">
          おちる
        </td>
        <td class="kanji">
          落ちる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to fall, to drop
        </td>
      </tr>
      <tr class="row0" id="94">
        <td class="pos">
          94
        </td>
        <td class="kanji">
          おっしゃる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          aru-v
        </td>
        <td class="eng">
          (hon) to say, to speak
        </td>
      </tr>
      <tr class="row1" id="95">
        <td class="pos">
          95
        </td>
        <td class="kanji">
          おっと
        </td>
        <td class="kanji">
          夫
        </td>
        <td>
          n
        </td>
        <td class="eng">
          husband
        </td>
      </tr>
      <tr class="row0" id="96">
        <td class="pos">
          96
        </td>
        <td class="kanji">
          おつり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          change (money), balance
        </td>
      </tr>
      <tr class="row1" id="97">
        <td class="pos">
          97
        </td>
        <td class="kanji">
          おと
        </td>
        <td class="kanji">
          音
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          sound, note
        </td>
      </tr>
      <tr class="row0" id="98">
        <td class="pos">
          98
        </td>
        <td class="kanji">
          おとす
        </td>
        <td class="kanji">
          落す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to drop, to lose
        </td>
      </tr>
      <tr class="row1" id="99">
        <td class="pos">
          99
        </td>
        <td class="kanji">
          おどり
        </td>
        <td class="kanji">
          踊り
        </td>
        <td>
          n
        </td>
        <td class="eng">
          dance
        </td>
      </tr>
      <tr class="row0" id="100">
        <td class="pos">
          100
        </td>
        <td class="kanji">
          おどる
        </td>
        <td class="kanji">
          踊る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to dance
        </td>
      </tr>
      <tr class="row1" id="101">
        <td class="pos">
          101
        </td>
        <td class="kanji">
          おどろく
        </td>
        <td class="kanji">
          驚く
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to be surprised, to be astonished
        </td>
      </tr>
      <tr class="row0" id="102">
        <td class="pos">
          102
        </td>
        <td class="kanji">
          おまつり
        </td>
        <td class="kanji">
          お祭り
        </td>
        <td>
          
        </td>
        <td class="eng">
          festival
        </td>
      </tr>
      <tr class="row1" id="103">
        <td class="pos">
          103
        </td>
        <td class="kanji">
          おみまい
        </td>
        <td class="kanji">
          お見舞い
        </td>
        <td>
          n
        </td>
        <td class="eng">
          calling on someone who is ill, enquiry
        </td>
      </tr>
      <tr class="row0" id="104">
        <td class="pos">
          104
        </td>
        <td class="kanji">
          おみやげ
        </td>
        <td class="kanji">
          お土産
        </td>
        <td>
          n
        </td>
        <td class="eng">
          souvenir
        </td>
      </tr>
      <tr class="row1" id="105">
        <td class="pos">
          105
        </td>
        <td class="kanji">
          おもいだす
        </td>
        <td class="kanji">
          思い出す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to recall, to remember
        </td>
      </tr>
      <tr class="row0" id="106">
        <td class="pos">
          106
        </td>
        <td class="kanji">
          おもう
        </td>
        <td class="kanji">
          思う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to think, to feel
        </td>
      </tr>
      <tr class="row1" id="107">
        <td class="pos">
          107
        </td>
        <td class="kanji">
          おもちゃ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          toy
        </td>
      </tr>
      <tr class="row0" id="108">
        <td class="pos">
          108
        </td>
        <td class="kanji">
          おもて
        </td>
        <td class="kanji">
          表
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          the front, surface, exterior
        </td>
      </tr>
      <tr class="row1" id="109">
        <td class="pos">
          109
        </td>
        <td class="kanji">
          おや
        </td>
        <td class="kanji">
          親
        </td>
        <td>
          n
        </td>
        <td class="eng">
          parents
        </td>
      </tr>
      <tr class="row0" id="110">
        <td class="pos">
          110
        </td>
        <td class="kanji">
          おりる
        </td>
        <td class="kanji">
          下りる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to descend a mountain, to (descend) go down stairs
        </td>
      </tr>
      <tr class="row1" id="111">
        <td class="pos">
          111
        </td>
        <td class="kanji">
          おる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to be (polite version of いる)
        </td>
      </tr>
      <tr class="row0" id="112">
        <td class="pos">
          112
        </td>
        <td class="kanji">
          おる
        </td>
        <td class="kanji">
          折る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to break, to fold, to pick a flower
        </td>
      </tr>
      <tr class="row1" id="113">
        <td class="pos">
          113
        </td>
        <td class="kanji">
          おれい
        </td>
        <td class="kanji">
          お礼
        </td>
        <td>
          n
        </td>
        <td class="eng">
          thanking, expression of gratitude
        </td>
      </tr>
      <tr class="row0" id="114">
        <td class="pos">
          114
        </td>
        <td class="kanji">
          おれる
        </td>
        <td class="kanji">
          折れる
        </td>
        <td>
          ru-v,vi,vt
        </td>
        <td class="eng">
          to break, to be folded, to give in, to turn (a corner)
        </td>
      </tr>
      <tr class="row1" id="115">
        <td class="pos">
          115
        </td>
        <td class="kanji">
          おわり
        </td>
        <td class="kanji">
          終わり
        </td>
        <td>
          n
        </td>
        <td class="eng">
          the end
        </td>
      </tr>
      <tr class="row0" id="116">
        <td class="pos">
          116
        </td>
        <td class="kanji">
          ～おわる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          suf
        </td>
        <td class="eng">
          end of ～
        </td>
      </tr>
      <tr class="row1" id="117">
        <td class="pos">
          117
        </td>
        <td class="kanji">
          ～か
        </td>
        <td class="kanji">
          ～家
        </td>
        <td>
          
        </td>
        <td class="eng">
          professional ～
        </td>
      </tr>
      <tr class="row0" id="118">
        <td class="pos">
          118
        </td>
        <td class="kanji">
          カーテン
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          curtain
        </td>
      </tr>
      <tr class="row1" id="119">
        <td class="pos">
          119
        </td>
        <td class="kanji">
          ～かい
        </td>
        <td class="kanji">
          ～会
        </td>
        <td>
          
        </td>
        <td class="eng">
          ～ meeting
        </td>
      </tr>
      <tr class="row0" id="120">
        <td class="pos">
          120
        </td>
        <td class="kanji">
          かいがん
        </td>
        <td class="kanji">
          海岸
        </td>
        <td>
          n
        </td>
        <td class="eng">
          coast, beach
        </td>
      </tr>
      <tr class="row1" id="121">
        <td class="pos">
          121
        </td>
        <td class="kanji">
          かいぎ
        </td>
        <td class="kanji">
          会議
        </td>
        <td>
          n
        </td>
        <td class="eng">
          meeting, conference
        </td>
      </tr>
      <tr class="row0" id="122">
        <td class="pos">
          122
        </td>
        <td class="kanji">
          かいぎしつ
        </td>
        <td class="kanji">
          会議室
        </td>
        <td>
          n
        </td>
        <td class="eng">
          conference room
        </td>
      </tr>
      <tr class="row1" id="123">
        <td class="pos">
          123
        </td>
        <td class="kanji">
          かいじょう
        </td>
        <td class="kanji">
          会場
        </td>
        <td>
          n
        </td>
        <td class="eng">
          assembly hall, meeting place, the grounds
        </td>
      </tr>
      <tr class="row0" id="124">
        <td class="pos">
          124
        </td>
        <td class="kanji">
          かいわ
        </td>
        <td class="kanji">
          会話
        </td>
        <td>
          n
        </td>
        <td class="eng">
          conversation
        </td>
      </tr>
      <tr class="row1" id="125">
        <td class="pos">
          125
        </td>
        <td class="kanji">
          かえり
        </td>
        <td class="kanji">
          帰り
        </td>
        <td>
          n
        </td>
        <td class="eng">
          return, coming back
        </td>
      </tr>
      <tr class="row0" id="126">
        <td class="pos">
          126
        </td>
        <td class="kanji">
          かえる
        </td>
        <td class="kanji">
          変える
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to change, to alter, to vary
        </td>
      </tr>
      <tr class="row1" id="127">
        <td class="pos">
          127
        </td>
        <td class="kanji">
          かがく
        </td>
        <td class="kanji">
          科学
        </td>
        <td>
          n
        </td>
        <td class="eng">
          science
        </td>
      </tr>
      <tr class="row0" id="128">
        <td class="pos">
          128
        </td>
        <td class="kanji">
          かがみ
        </td>
        <td class="kanji">
          鏡
        </td>
        <td>
          n
        </td>
        <td class="eng">
          mirror
        </td>
      </tr>
      <tr class="row1" id="129">
        <td class="pos">
          129
        </td>
        <td class="kanji">
          ～がくぶ
        </td>
        <td class="kanji">
          ～学部
        </td>
        <td>
          
        </td>
        <td class="eng">
          department of a university
        </td>
      </tr>
      <tr class="row0" id="130">
        <td class="pos">
          130
        </td>
        <td class="kanji">
          かける
        </td>
        <td class="kanji">
          掛ける
        </td>
        <td>
          
        </td>
        <td class="eng">
          to hang, to put on (eg wall)
        </td>
      </tr>
      <tr class="row1" id="131">
        <td class="pos">
          131
        </td>
        <td class="kanji">
          かける
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          to sit down
        </td>
      </tr>
      <tr class="row0" id="132">
        <td class="pos">
          132
        </td>
        <td class="kanji">
          かける
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          to begin to
        </td>
      </tr>
      <tr class="row1" id="133">
        <td class="pos">
          133
        </td>
        <td class="kanji">
          かざる
        </td>
        <td class="kanji">
          飾る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to decorate, to ornament, to adorn
        </td>
      </tr>
      <tr class="row0" id="134">
        <td class="pos">
          134
        </td>
        <td class="kanji">
          かじ
        </td>
        <td class="kanji">
          火事
        </td>
        <td>
          n
        </td>
        <td class="eng">
          fire
        </td>
      </tr>
      <tr class="row1" id="135">
        <td class="pos">
          135
        </td>
        <td class="kanji">
          ガス
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          gas
        </td>
      </tr>
      <tr class="row0" id="136">
        <td class="pos">
          136
        </td>
        <td class="kanji">
          ガソリン
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          gasoline, petrol
        </td>
      </tr>
      <tr class="row1" id="137">
        <td class="pos">
          137
        </td>
        <td class="kanji">
          ガソリンスタンド
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          gasoline stand, gas station, petrol station
        </td>
      </tr>
      <tr class="row0" id="138">
        <td class="pos">
          138
        </td>
        <td class="kanji">
          かた
        </td>
        <td class="kanji">
          方
        </td>
        <td>
          n-suf
        </td>
        <td class="eng">
          way of doing
        </td>
      </tr>
      <tr class="row1" id="139">
        <td class="pos">
          139
        </td>
        <td class="kanji">
          かたい
        </td>
        <td class="kanji">
          堅/硬/固い
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          solid, hard, firm
        </td>
      </tr>
      <tr class="row0" id="140">
        <td class="pos">
          140
        </td>
        <td class="kanji">
          かたち
        </td>
        <td class="kanji">
          形
        </td>
        <td>
          n
        </td>
        <td class="eng">
          shape
        </td>
      </tr>
      <tr class="row1" id="141">
        <td class="pos">
          141
        </td>
        <td class="kanji">
          かたづける
        </td>
        <td class="kanji">
          片付ける
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to tidy up, to put in order, to put away
        </td>
      </tr>
      <tr class="row0" id="142">
        <td class="pos">
          142
        </td>
        <td class="kanji">
          かちょう
        </td>
        <td class="kanji">
          課長
        </td>
        <td>
          n
        </td>
        <td class="eng">
          section manager
        </td>
      </tr>
      <tr class="row1" id="143">
        <td class="pos">
          143
        </td>
        <td class="kanji">
          かつ
        </td>
        <td class="kanji">
          勝つ
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to win, to gain victory
        </td>
      </tr>
      <tr class="row0" id="144">
        <td class="pos">
          144
        </td>
        <td class="kanji">
          かっこう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          no--adj, na-adj
        </td>
        <td class="eng">
          appearance, manner
        </td>
      </tr>
      <tr class="row1" id="145">
        <td class="pos">
          145
        </td>
        <td class="kanji">
          かない
        </td>
        <td class="kanji">
          家内
        </td>
        <td>
          n
        </td>
        <td class="eng">
          housewife
        </td>
      </tr>
      <tr class="row0" id="146">
        <td class="pos">
          146
        </td>
        <td class="kanji">
          かなしい
        </td>
        <td class="kanji">
          悲しい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          sad, sorrowful
        </td>
      </tr>
      <tr class="row1" id="147">
        <td class="pos">
          147
        </td>
        <td class="kanji">
          かならず
        </td>
        <td class="kanji">
          必ず
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          certainly, necessarily, invariably
        </td>
      </tr>
      <tr class="row0" id="148">
        <td class="pos">
          148
        </td>
        <td class="kanji">
          かねもち/おかねもち
        </td>
        <td class="kanji">
          お・金持ち
        </td>
        <td>
          n
        </td>
        <td class="eng">
          rich man
        </td>
      </tr>
      <tr class="row1" id="149">
        <td class="pos">
          149
        </td>
        <td class="kanji">
          かのじょ
        </td>
        <td class="kanji">
          彼女
        </td>
        <td>
          n
        </td>
        <td class="eng">
          she, girl-friend
        </td>
      </tr>
      <tr class="row0" id="150">
        <td class="pos">
          150
        </td>
        <td class="kanji">
          かべ
        </td>
        <td class="kanji">
          壁
        </td>
        <td>
          n
        </td>
        <td class="eng">
          wall
        </td>
      </tr>
      <tr class="row1" id="151">
        <td class="pos">
          151
        </td>
        <td class="kanji">
          かまう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to mind, to care about
        </td>
      </tr>
      <tr class="row0" id="152">
        <td class="pos">
          152
        </td>
        <td class="kanji">
          かみ
        </td>
        <td class="kanji">
          髪
        </td>
        <td>
          n
        </td>
        <td class="eng">
          hair
        </td>
      </tr>
      <tr class="row1" id="153">
        <td class="pos">
          153
        </td>
        <td class="kanji">
          かむ
        </td>
        <td class="kanji">
          噛む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to bite, to chew
        </td>
      </tr>
      <tr class="row0" id="154">
        <td class="pos">
          154
        </td>
        <td class="kanji">
          かよう
        </td>
        <td class="kanji">
          通う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (1) to go back and forth, (2) to commute
        </td>
      </tr>
      <tr class="row1" id="155">
        <td class="pos">
          155
        </td>
        <td class="kanji">
          ガラス
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          glass, pane
        </td>
      </tr>
      <tr class="row0" id="156">
        <td class="pos">
          156
        </td>
        <td class="kanji">
          かれ
        </td>
        <td class="kanji">
          彼
        </td>
        <td>
          n
        </td>
        <td class="eng">
          he, boyfriend
        </td>
      </tr>
      <tr class="row1" id="157">
        <td class="pos">
          157
        </td>
        <td class="kanji">
          かれら
        </td>
        <td class="kanji">
          彼ら
        </td>
        <td>
          n
        </td>
        <td class="eng">
          they (usually male)
        </td>
      </tr>
      <tr class="row0" id="158">
        <td class="pos">
          158
        </td>
        <td class="kanji">
          かわく
        </td>
        <td class="kanji">
          乾く
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to get dry
        </td>
      </tr>
      <tr class="row1" id="159">
        <td class="pos">
          159
        </td>
        <td class="kanji">
          かわり
        </td>
        <td class="kanji">
          代わり
        </td>
        <td>
          n
        </td>
        <td class="eng">
          substitute, alternate
        </td>
      </tr>
      <tr class="row0" id="160">
        <td class="pos">
          160
        </td>
        <td class="kanji">
          かわる
        </td>
        <td class="kanji">
          変わる
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to change, to be transformed, to vary
        </td>
      </tr>
      <tr class="row1" id="161">
        <td class="pos">
          161
        </td>
        <td class="kanji">
          かんがえる
        </td>
        <td class="kanji">
          考える
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to consider
        </td>
      </tr>
      <tr class="row0" id="162">
        <td class="pos">
          162
        </td>
        <td class="kanji">
          かんけい
        </td>
        <td class="kanji">
          関係
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          relation, connection
        </td>
      </tr>
      <tr class="row1" id="163">
        <td class="pos">
          163
        </td>
        <td class="kanji">
          かんごふ
        </td>
        <td class="kanji">
          看護婦
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (female) nurse
        </td>
      </tr>
      <tr class="row0" id="164">
        <td class="pos">
          164
        </td>
        <td class="kanji">
          かんたん
        </td>
        <td class="kanji">
          簡単
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          simple
        </td>
      </tr>
      <tr class="row1" id="165">
        <td class="pos">
          165
        </td>
        <td class="kanji">
          がんばる
        </td>
        <td class="kanji">
          頑張る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to try one's best, to persist
        </td>
      </tr>
      <tr class="row0" id="166">
        <td class="pos">
          166
        </td>
        <td class="kanji">
          き
        </td>
        <td class="kanji">
          気
        </td>
        <td>
          n
        </td>
        <td class="eng">
          spirit, mood
        </td>
      </tr>
      <tr class="row1" id="167">
        <td class="pos">
          167
        </td>
        <td class="kanji">
          きかい
        </td>
        <td class="kanji">
          機会
        </td>
        <td>
          n
        </td>
        <td class="eng">
          chance, opportunity
        </td>
      </tr>
      <tr class="row0" id="168">
        <td class="pos">
          168
        </td>
        <td class="kanji">
          きけん
        </td>
        <td class="kanji">
          危険
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          danger, peril, hazard
        </td>
      </tr>
      <tr class="row1" id="169">
        <td class="pos">
          169
        </td>
        <td class="kanji">
          きこえる
        </td>
        <td class="kanji">
          聞こえる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to be heard, to be audible
        </td>
      </tr>
      <tr class="row0" id="170">
        <td class="pos">
          170
        </td>
        <td class="kanji">
          きしゃ
        </td>
        <td class="kanji">
          汽車
        </td>
        <td>
          n
        </td>
        <td class="eng">
          train (steam)
        </td>
      </tr>
      <tr class="row1" id="171">
        <td class="pos">
          171
        </td>
        <td class="kanji">
          ぎじゅつ
        </td>
        <td class="kanji">
          技術
        </td>
        <td>
          n
        </td>
        <td class="eng">
          art, technique, technology, skill
        </td>
      </tr>
      <tr class="row0" id="172">
        <td class="pos">
          172
        </td>
        <td class="kanji">
          きせつ
        </td>
        <td class="kanji">
          季節
        </td>
        <td>
          n
        </td>
        <td class="eng">
          season
        </td>
      </tr>
      <tr class="row1" id="173">
        <td class="pos">
          173
        </td>
        <td class="kanji">
          きそく
        </td>
        <td class="kanji">
          規則
        </td>
        <td>
          n
        </td>
        <td class="eng">
          rule, regulations
        </td>
      </tr>
      <tr class="row0" id="174">
        <td class="pos">
          174
        </td>
        <td class="kanji">
          きっと
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,n
        </td>
        <td class="eng">
          surely, definitely
        </td>
      </tr>
      <tr class="row1" id="175">
        <td class="pos">
          175
        </td>
        <td class="kanji">
          きぬ
        </td>
        <td class="kanji">
          絹
        </td>
        <td>
          n
        </td>
        <td class="eng">
          silk
        </td>
      </tr>
      <tr class="row0" id="176">
        <td class="pos">
          176
        </td>
        <td class="kanji">
          きびしい
        </td>
        <td class="kanji">
          厳しい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          strict
        </td>
      </tr>
      <tr class="row1" id="177">
        <td class="pos">
          177
        </td>
        <td class="kanji">
          きぶん
        </td>
        <td class="kanji">
          気分
        </td>
        <td>
          n
        </td>
        <td class="eng">
          feeling, mood
        </td>
      </tr>
      <tr class="row0" id="178">
        <td class="pos">
          178
        </td>
        <td class="kanji">
          きまる
        </td>
        <td class="kanji">
          決る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to be decided, to be settled
        </td>
      </tr>
      <tr class="row1" id="179">
        <td class="pos">
          179
        </td>
        <td class="kanji">
          きみ
        </td>
        <td class="kanji">
          君
        </td>
        <td>
          n,suf
        </td>
        <td class="eng">
          You (masculine term for female)
        </td>
      </tr>
      <tr class="row0" id="180">
        <td class="pos">
          180
        </td>
        <td class="kanji">
          きめる
        </td>
        <td class="kanji">
          決める
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to decide
        </td>
      </tr>
      <tr class="row1" id="181">
        <td class="pos">
          181
        </td>
        <td class="kanji">
          きもち
        </td>
        <td class="kanji">
          気持ち
        </td>
        <td>
          n
        </td>
        <td class="eng">
          feeling, sensation, mood
        </td>
      </tr>
      <tr class="row0" id="182">
        <td class="pos">
          182
        </td>
        <td class="kanji">
          きもの
        </td>
        <td class="kanji">
          着物
        </td>
        <td>
          n
        </td>
        <td class="eng">
          kimono
        </td>
      </tr>
      <tr class="row1" id="183">
        <td class="pos">
          183
        </td>
        <td class="kanji">
          きゃく
        </td>
        <td class="kanji">
          客
        </td>
        <td>
          n
        </td>
        <td class="eng">
          guest, customer
        </td>
      </tr>
      <tr class="row0" id="184">
        <td class="pos">
          184
        </td>
        <td class="kanji">
          きゅう
        </td>
        <td class="kanji">
          急
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          (1) urgent, sudden, (2) steep
        </td>
      </tr>
      <tr class="row1" id="185">
        <td class="pos">
          185
        </td>
        <td class="kanji">
          きゅうこう
        </td>
        <td class="kanji">
          急行
        </td>
        <td>
          n
        </td>
        <td class="eng">
          express (eg train that bypasses stations)
        </td>
      </tr>
      <tr class="row0" id="186">
        <td class="pos">
          186
        </td>
        <td class="kanji">
          きょういく
        </td>
        <td class="kanji">
          教育
        </td>
        <td>
          adj-no,n,vs
        </td>
        <td class="eng">
          training, education
        </td>
      </tr>
      <tr class="row1" id="187">
        <td class="pos">
          187
        </td>
        <td class="kanji">
          きょうかい
        </td>
        <td class="kanji">
          教会
        </td>
        <td>
          n
        </td>
        <td class="eng">
          church
        </td>
      </tr>
      <tr class="row0" id="188">
        <td class="pos">
          188
        </td>
        <td class="kanji">
          きょうそう
        </td>
        <td class="kanji">
          競争
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          competition, contest
        </td>
      </tr>
      <tr class="row1" id="189">
        <td class="pos">
          189
        </td>
        <td class="kanji">
          きょうみ
        </td>
        <td class="kanji">
          興味
        </td>
        <td>
          n
        </td>
        <td class="eng">
          interest (in something)
        </td>
      </tr>
      <tr class="row0" id="190">
        <td class="pos">
          190
        </td>
        <td class="kanji">
          きんじょ
        </td>
        <td class="kanji">
          近所
        </td>
        <td>
          n
        </td>
        <td class="eng">
          neighbourhood
        </td>
      </tr>
      <tr class="row1" id="191">
        <td class="pos">
          191
        </td>
        <td class="kanji">
          ～く
        </td>
        <td class="kanji">
          ～区
        </td>
        <td>
          n
        </td>
        <td class="eng">
          district ～
        </td>
      </tr>
      <tr class="row0" id="192">
        <td class="pos">
          192
        </td>
        <td class="kanji">
          ぐあい
        </td>
        <td class="kanji">
          具合
        </td>
        <td>
          n
        </td>
        <td class="eng">
          condition, state, health
        </td>
      </tr>
      <tr class="row1" id="193">
        <td class="pos">
          193
        </td>
        <td class="kanji">
          くうき
        </td>
        <td class="kanji">
          空気
        </td>
        <td>
          n
        </td>
        <td class="eng">
          air, atmosphere
        </td>
      </tr>
      <tr class="row0" id="194">
        <td class="pos">
          194
        </td>
        <td class="kanji">
          くうこう
        </td>
        <td class="kanji">
          空港
        </td>
        <td>
          n
        </td>
        <td class="eng">
          airport
        </td>
      </tr>
      <tr class="row1" id="195">
        <td class="pos">
          195
        </td>
        <td class="kanji">
          くさ
        </td>
        <td class="kanji">
          草
        </td>
        <td>
          n
        </td>
        <td class="eng">
          grass
        </td>
      </tr>
      <tr class="row0" id="196">
        <td class="pos">
          196
        </td>
        <td class="kanji">
          くださる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          aru-v
        </td>
        <td class="eng">
          (hon) to give, to confer
        </td>
      </tr>
      <tr class="row1" id="197">
        <td class="pos">
          197
        </td>
        <td class="kanji">
          くび
        </td>
        <td class="kanji">
          首
        </td>
        <td>
          n
        </td>
        <td class="eng">
          neck
        </td>
      </tr>
      <tr class="row0" id="198">
        <td class="pos">
          198
        </td>
        <td class="kanji">
          くも
        </td>
        <td class="kanji">
          雲
        </td>
        <td>
          n
        </td>
        <td class="eng">
          cloud
        </td>
      </tr>
      <tr class="row1" id="199">
        <td class="pos">
          199
        </td>
        <td class="kanji">
          くらべる
        </td>
        <td class="kanji">
          比べる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to compare
        </td>
      </tr>
      <tr class="row0" id="200">
        <td class="pos">
          200
        </td>
        <td class="kanji">
          くれる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to give, to do for
        </td>
      </tr>
      <tr class="row1" id="201">
        <td class="pos">
          201
        </td>
        <td class="kanji">
          くれる
        </td>
        <td class="kanji">
          暮れる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to get dark, to come to an end
        </td>
      </tr>
      <tr class="row0" id="202">
        <td class="pos">
          202
        </td>
        <td class="kanji">
          ～くん
        </td>
        <td class="kanji">
          ～君
        </td>
        <td>
          n-suf
        </td>
        <td class="eng">
          Mr (junior) ～, master ～
        </td>
      </tr>
      <tr class="row1" id="203">
        <td class="pos">
          203
        </td>
        <td class="kanji">
          け
        </td>
        <td class="kanji">
          毛
        </td>
        <td>
          n
        </td>
        <td class="eng">
          hair
        </td>
      </tr>
      <tr class="row0" id="204">
        <td class="pos">
          204
        </td>
        <td class="kanji">
          け
        </td>
        <td class="kanji">
          毛
        </td>
        <td>
          n
        </td>
        <td class="eng">
          fur
        </td>
      </tr>
      <tr class="row1" id="205">
        <td class="pos">
          205
        </td>
        <td class="kanji">
          けいかく・する
        </td>
        <td class="kanji">
          計画
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          plan, project, schedule
        </td>
      </tr>
      <tr class="row0" id="206">
        <td class="pos">
          206
        </td>
        <td class="kanji">
          けいけん・する
        </td>
        <td class="kanji">
          経験
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          experience
        </td>
      </tr>
      <tr class="row1" id="207">
        <td class="pos">
          207
        </td>
        <td class="kanji">
          けいざい
        </td>
        <td class="kanji">
          経済
        </td>
        <td>
          n
        </td>
        <td class="eng">
          economics, finance, economy
        </td>
      </tr>
      <tr class="row0" id="208">
        <td class="pos">
          208
        </td>
        <td class="kanji">
          けいさつ
        </td>
        <td class="kanji">
          警察
        </td>
        <td>
          n
        </td>
        <td class="eng">
          police
        </td>
      </tr>
      <tr class="row1" id="209">
        <td class="pos">
          209
        </td>
        <td class="kanji">
          けが・する
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          injury (to animate object), hurt
        </td>
      </tr>
      <tr class="row0" id="210">
        <td class="pos">
          210
        </td>
        <td class="kanji">
          ケーキ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          cake
        </td>
      </tr>
      <tr class="row1" id="211">
        <td class="pos">
          211
        </td>
        <td class="kanji">
          けしき
        </td>
        <td class="kanji">
          景色
        </td>
        <td>
          n
        </td>
        <td class="eng">
          scenery, scene, landscape
        </td>
      </tr>
      <tr class="row0" id="212">
        <td class="pos">
          212
        </td>
        <td class="kanji">
          けしゴム
        </td>
        <td class="kanji">
          消しゴム
        </td>
        <td>
          n
        </td>
        <td class="eng">
          eraser
        </td>
      </tr>
      <tr class="row1" id="213">
        <td class="pos">
          213
        </td>
        <td class="kanji">
          げしゅく
        </td>
        <td class="kanji">
          下宿
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          boarding, lodging, boarding house
        </td>
      </tr>
      <tr class="row0" id="214">
        <td class="pos">
          214
        </td>
        <td class="kanji">
          けっして
        </td>
        <td class="kanji">
          決して
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          never
        </td>
      </tr>
      <tr class="row1" id="215">
        <td class="pos">
          215
        </td>
        <td class="kanji">
          けれど/けれども
        </td>
        <td class="kanji">
          
        </td>
        <td>
          conj
        </td>
        <td class="eng">
          but, however
        </td>
      </tr>
      <tr class="row0" id="216">
        <td class="pos">
          216
        </td>
        <td class="kanji">
          ～けん
        </td>
        <td class="kanji">
          ～軒
        </td>
        <td>
          
        </td>
        <td class="eng">
          counter for houses
        </td>
      </tr>
      <tr class="row1" id="217">
        <td class="pos">
          217
        </td>
        <td class="kanji">
          げんいん
        </td>
        <td class="kanji">
          原因
        </td>
        <td>
          n
        </td>
        <td class="eng">
          cause, origin, source
        </td>
      </tr>
      <tr class="row0" id="218">
        <td class="pos">
          218
        </td>
        <td class="kanji">
          けんか・する
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          quarrel
        </td>
      </tr>
      <tr class="row1" id="219">
        <td class="pos">
          219
        </td>
        <td class="kanji">
          げんかん
        </td>
        <td class="kanji">
          玄関
        </td>
        <td>
          n
        </td>
        <td class="eng">
          entrance way (in Japanese house)
        </td>
      </tr>
      <tr class="row0" id="220">
        <td class="pos">
          220
        </td>
        <td class="kanji">
          けんきゅう
        </td>
        <td class="kanji">
          研究
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          study, research, investigation
        </td>
      </tr>
      <tr class="row1" id="221">
        <td class="pos">
          221
        </td>
        <td class="kanji">
          けんきゅうしつ
        </td>
        <td class="kanji">
          研究室
        </td>
        <td>
          n
        </td>
        <td class="eng">
          study room, laboratory
        </td>
      </tr>
      <tr class="row0" id="222">
        <td class="pos">
          222
        </td>
        <td class="kanji">
          けんぶつ
        </td>
        <td class="kanji">
          見物
        </td>
        <td>
          n
        </td>
        <td class="eng">
          a sight, an attraction
        </td>
      </tr>
      <tr class="row1" id="223">
        <td class="pos">
          223
        </td>
        <td class="kanji">
          こ
        </td>
        <td class="kanji">
          子
        </td>
        <td>
          n
        </td>
        <td class="eng">
          child
        </td>
      </tr>
      <tr class="row0" id="224">
        <td class="pos">
          224
        </td>
        <td class="kanji">
          ご～
        </td>
        <td class="kanji">
          御～
        </td>
        <td>
          prefix
        </td>
        <td class="eng">
          honourable ～
        </td>
      </tr>
      <tr class="row1" id="225">
        <td class="pos">
          225
        </td>
        <td class="kanji">
          こう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,int-n
        </td>
        <td class="eng">
          like this, this way
        </td>
      </tr>
      <tr class="row0" id="226">
        <td class="pos">
          226
        </td>
        <td class="kanji">
          こうがい
        </td>
        <td class="kanji">
          郊外
        </td>
        <td>
          n
        </td>
        <td class="eng">
          suburb, outskirts
        </td>
      </tr>
      <tr class="row1" id="227">
        <td class="pos">
          227
        </td>
        <td class="kanji">
          こうぎ
        </td>
        <td class="kanji">
          講義
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          lecture
        </td>
      </tr>
      <tr class="row0" id="228">
        <td class="pos">
          228
        </td>
        <td class="kanji">
          こうぎょう
        </td>
        <td class="kanji">
          工業
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (manufacturing) industry
        </td>
      </tr>
      <tr class="row1" id="229">
        <td class="pos">
          229
        </td>
        <td class="kanji">
          こうこう/こうとうがっこう
        </td>
        <td class="kanji">
          高校/高等学校
        </td>
        <td>
          n
        </td>
        <td class="eng">
          high school/senior high school
        </td>
      </tr>
      <tr class="row0" id="230">
        <td class="pos">
          230
        </td>
        <td class="kanji">
          こうこうせい
        </td>
        <td class="kanji">
          高校生
        </td>
        <td>
          n
        </td>
        <td class="eng">
          high school student
        </td>
      </tr>
      <tr class="row1" id="231">
        <td class="pos">
          231
        </td>
        <td class="kanji">
          こうじょう
        </td>
        <td class="kanji">
          工場
        </td>
        <td>
          n
        </td>
        <td class="eng">
          factory
        </td>
      </tr>
      <tr class="row0" id="232">
        <td class="pos">
          232
        </td>
        <td class="kanji">
          こうちょう
        </td>
        <td class="kanji">
          校長
        </td>
        <td>
          n
        </td>
        <td class="eng">
          principal, headmaster
        </td>
      </tr>
      <tr class="row1" id="233">
        <td class="pos">
          233
        </td>
        <td class="kanji">
          こうつう
        </td>
        <td class="kanji">
          交通
        </td>
        <td>
          n
        </td>
        <td class="eng">
          traffic, transportation
        </td>
      </tr>
      <tr class="row0" id="234">
        <td class="pos">
          234
        </td>
        <td class="kanji">
          こうどう
        </td>
        <td class="kanji">
          講堂
        </td>
        <td>
          n
        </td>
        <td class="eng">
          auditorium
        </td>
      </tr>
      <tr class="row1" id="235">
        <td class="pos">
          235
        </td>
        <td class="kanji">
          こうむいん
        </td>
        <td class="kanji">
          公務員
        </td>
        <td>
          n
        </td>
        <td class="eng">
          government worker, public servant
        </td>
      </tr>
      <tr class="row0" id="236">
        <td class="pos">
          236
        </td>
        <td class="kanji">
          こくさい
        </td>
        <td class="kanji">
          国際
        </td>
        <td>
          n
        </td>
        <td class="eng">
          international
        </td>
      </tr>
      <tr class="row1" id="237">
        <td class="pos">
          237
        </td>
        <td class="kanji">
          こころ
        </td>
        <td class="kanji">
          心
        </td>
        <td>
          n
        </td>
        <td class="eng">
          core, heart
        </td>
      </tr>
      <tr class="row0" id="238">
        <td class="pos">
          238
        </td>
        <td class="kanji">
          ～ございます
        </td>
        <td class="kanji">
          
        </td>
        <td>
          expr
        </td>
        <td class="eng">
          to be (polite), to exist
        </td>
      </tr>
      <tr class="row1" id="239">
        <td class="pos">
          239
        </td>
        <td class="kanji">
          ごしゅじん
        </td>
        <td class="kanji">
          ご主人
        </td>
        <td>
          n
        </td>
        <td class="eng">
          your husband, her husband
        </td>
      </tr>
      <tr class="row0" id="240">
        <td class="pos">
          240
        </td>
        <td class="kanji">
          こしょう・する
        </td>
        <td class="kanji">
          故障
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          break-down
        </td>
      </tr>
      <tr class="row1" id="241">
        <td class="pos">
          241
        </td>
        <td class="kanji">
          ごぞんじ
        </td>
        <td class="kanji">
          ご存じ
        </td>
        <td>
          n
        </td>
        <td class="eng">
          knowing, acquaintance
        </td>
      </tr>
      <tr class="row0" id="242">
        <td class="pos">
          242
        </td>
        <td class="kanji">
          こたえ
        </td>
        <td class="kanji">
          答
        </td>
        <td>
          n
        </td>
        <td class="eng">
          answer, response
        </td>
      </tr>
      <tr class="row1" id="243">
        <td class="pos">
          243
        </td>
        <td class="kanji">
          ごちそう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          feast, treating (someone)
        </td>
      </tr>
      <tr class="row0" id="244">
        <td class="pos">
          244
        </td>
        <td class="kanji">
          こっち
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (1) this person, (2) this direction, (3) this side, (4) thereafter
        </td>
      </tr>
      <tr class="row1" id="245">
        <td class="pos">
          245
        </td>
        <td class="kanji">
          こと
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          thing, matter, fact
        </td>
      </tr>
      <tr class="row0" id="246">
        <td class="pos">
          246
        </td>
        <td class="kanji">
          ことり
        </td>
        <td class="kanji">
          小鳥
        </td>
        <td>
          n
        </td>
        <td class="eng">
          small bird
        </td>
      </tr>
      <tr class="row1" id="247">
        <td class="pos">
          247
        </td>
        <td class="kanji">
          このあいだ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n-adv
        </td>
        <td class="eng">
          the other day, recently
        </td>
      </tr>
      <tr class="row0" id="248">
        <td class="pos">
          248
        </td>
        <td class="kanji">
          このごろ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          these days, nowadays
        </td>
      </tr>
      <tr class="row1" id="249">
        <td class="pos">
          249
        </td>
        <td class="kanji">
          こまかい
        </td>
        <td class="kanji">
          細かい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          (1) small, (2) fine, minute
        </td>
      </tr>
      <tr class="row0" id="250">
        <td class="pos">
          250
        </td>
        <td class="kanji">
          ごみ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          rubbish, trash, garbage
        </td>
      </tr>
      <tr class="row1" id="251">
        <td class="pos">
          251
        </td>
        <td class="kanji">
          こむ
        </td>
        <td class="kanji">
          込む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to be crowded
        </td>
      </tr>
      <tr class="row0" id="252">
        <td class="pos">
          252
        </td>
        <td class="kanji">
          こめ
        </td>
        <td class="kanji">
          米
        </td>
        <td>
          n
        </td>
        <td class="eng">
          uncooked rice
        </td>
      </tr>
      <tr class="row1" id="253">
        <td class="pos">
          253
        </td>
        <td class="kanji">
          ごらんになる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          (hon) to see
        </td>
      </tr>
      <tr class="row0" id="254">
        <td class="pos">
          254
        </td>
        <td class="kanji">
          これから
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n-t
        </td>
        <td class="eng">
          after this
        </td>
      </tr>
      <tr class="row1" id="255">
        <td class="pos">
          255
        </td>
        <td class="kanji">
          こわい
        </td>
        <td class="kanji">
          怖い
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          scary, frightening
        </td>
      </tr>
      <tr class="row0" id="256">
        <td class="pos">
          256
        </td>
        <td class="kanji">
          こわす
        </td>
        <td class="kanji">
          壊す
        </td>
        <td>
          u-v,vt
        </td>
        <td class="eng">
          to break, to break down
        </td>
      </tr>
      <tr class="row1" id="257">
        <td class="pos">
          257
        </td>
        <td class="kanji">
          こわれる
        </td>
        <td class="kanji">
          壊れる
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to be broken, to break
        </td>
      </tr>
      <tr class="row0" id="258">
        <td class="pos">
          258
        </td>
        <td class="kanji">
          コンサート
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          concert
        </td>
      </tr>
      <tr class="row1" id="259">
        <td class="pos">
          259
        </td>
        <td class="kanji">
          こんど
        </td>
        <td class="kanji">
          今度
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          now, next time
        </td>
      </tr>
      <tr class="row0" id="260">
        <td class="pos">
          260
        </td>
        <td class="kanji">
          コンピュータ/コンピューター
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          computer
        </td>
      </tr>
      <tr class="row1" id="261">
        <td class="pos">
          261
        </td>
        <td class="kanji">
          こんや
        </td>
        <td class="kanji">
          今夜
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          this evening, tonight
        </td>
      </tr>
      <tr class="row0" id="262">
        <td class="pos">
          262
        </td>
        <td class="kanji">
          さいきん
        </td>
        <td class="kanji">
          最近
        </td>
        <td>
          adj-no,n-adv,n-t
        </td>
        <td class="eng">
          latest, most recent, nowadays
        </td>
      </tr>
      <tr class="row1" id="263">
        <td class="pos">
          263
        </td>
        <td class="kanji">
          さいご
        </td>
        <td class="kanji">
          最後
        </td>
        <td>
          n
        </td>
        <td class="eng">
          last, end, conclusion
        </td>
      </tr>
      <tr class="row0" id="264">
        <td class="pos">
          264
        </td>
        <td class="kanji">
          さいしょ
        </td>
        <td class="kanji">
          最初
        </td>
        <td>
          adj-no,n-adv,n-t
        </td>
        <td class="eng">
          beginning, first
        </td>
      </tr>
      <tr class="row1" id="265">
        <td class="pos">
          265
        </td>
        <td class="kanji">
          さか
        </td>
        <td class="kanji">
          坂
        </td>
        <td>
          n
        </td>
        <td class="eng">
          slope, hill
        </td>
      </tr>
      <tr class="row0" id="266">
        <td class="pos">
          266
        </td>
        <td class="kanji">
          さがす
        </td>
        <td class="kanji">
          探す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to search, to seek, to look for
        </td>
      </tr>
      <tr class="row1" id="267">
        <td class="pos">
          267
        </td>
        <td class="kanji">
          さがる
        </td>
        <td class="kanji">
          下る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to get down, to descend
        </td>
      </tr>
      <tr class="row0" id="268">
        <td class="pos">
          268
        </td>
        <td class="kanji">
          さかん
        </td>
        <td class="kanji">
          盛ん
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          popularity, prosperous
        </td>
      </tr>
      <tr class="row1" id="269">
        <td class="pos">
          269
        </td>
        <td class="kanji">
          さげる
        </td>
        <td class="kanji">
          下げる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to hang, to lower, to move back
        </td>
      </tr>
      <tr class="row0" id="270">
        <td class="pos">
          270
        </td>
        <td class="kanji">
          さしあげる
        </td>
        <td class="kanji">
          差し上げる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          (polite) to give, to offer
        </td>
      </tr>
      <tr class="row1" id="271">
        <td class="pos">
          271
        </td>
        <td class="kanji">
          さっき
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          some time ago
        </td>
      </tr>
      <tr class="row0" id="272">
        <td class="pos">
          272
        </td>
        <td class="kanji">
          さびしい
        </td>
        <td class="kanji">
          寂しい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          lonely, lonesome
        </td>
      </tr>
      <tr class="row1" id="273">
        <td class="pos">
          273
        </td>
        <td class="kanji">
          ～さま
        </td>
        <td class="kanji">
          ～様
        </td>
        <td>
          n-suf
        </td>
        <td class="eng">
          Mr or Mrs ～
        </td>
      </tr>
      <tr class="row0" id="274">
        <td class="pos">
          274
        </td>
        <td class="kanji">
          さらいげつ
        </td>
        <td class="kanji">
          さ来月
        </td>
        <td>
          
        </td>
        <td class="eng">
          the month after next
        </td>
      </tr>
      <tr class="row1" id="275">
        <td class="pos">
          275
        </td>
        <td class="kanji">
          さらいしゅう
        </td>
        <td class="kanji">
          さ来週
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          the week after next
        </td>
      </tr>
      <tr class="row0" id="276">
        <td class="pos">
          276
        </td>
        <td class="kanji">
          サラダ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          salad
        </td>
      </tr>
      <tr class="row1" id="277">
        <td class="pos">
          277
        </td>
        <td class="kanji">
          さわぐ
        </td>
        <td class="kanji">
          騒ぐ
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to make noise, to clamor, to be excited
        </td>
      </tr>
      <tr class="row0" id="278">
        <td class="pos">
          278
        </td>
        <td class="kanji">
          さわる
        </td>
        <td class="kanji">
          触る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to touch, to feel
        </td>
      </tr>
      <tr class="row1" id="279">
        <td class="pos">
          279
        </td>
        <td class="kanji">
          さんぎょう
        </td>
        <td class="kanji">
          産業
        </td>
        <td>
          n
        </td>
        <td class="eng">
          industry
        </td>
      </tr>
      <tr class="row0" id="280">
        <td class="pos">
          280
        </td>
        <td class="kanji">
          サンダル
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          sandal
        </td>
      </tr>
      <tr class="row1" id="281">
        <td class="pos">
          281
        </td>
        <td class="kanji">
          サンドイッチ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          sandwich
        </td>
      </tr>
      <tr class="row0" id="282">
        <td class="pos">
          282
        </td>
        <td class="kanji">
          ざんねん
        </td>
        <td class="kanji">
          残念
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          bad luck, disappointment
        </td>
      </tr>
      <tr class="row1" id="283">
        <td class="pos">
          283
        </td>
        <td class="kanji">
          し
        </td>
        <td class="kanji">
          市
        </td>
        <td>
          n
        </td>
        <td class="eng">
          city
        </td>
      </tr>
      <tr class="row0" id="284">
        <td class="pos">
          284
        </td>
        <td class="kanji">
          じ
        </td>
        <td class="kanji">
          字
        </td>
        <td>
          n
        </td>
        <td class="eng">
          character, hand-writing
        </td>
      </tr>
      <tr class="row1" id="285">
        <td class="pos">
          285
        </td>
        <td class="kanji">
          しあい
        </td>
        <td class="kanji">
          試合
        </td>
        <td>
          n
        </td>
        <td class="eng">
          match, game, contest
        </td>
      </tr>
      <tr class="row0" id="286">
        <td class="pos">
          286
        </td>
        <td class="kanji">
          しかた
        </td>
        <td class="kanji">
          仕方
        </td>
        <td>
          n
        </td>
        <td class="eng">
          way, method
        </td>
      </tr>
      <tr class="row1" id="287">
        <td class="pos">
          287
        </td>
        <td class="kanji">
          しかる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to scold
        </td>
      </tr>
      <tr class="row0" id="288">
        <td class="pos">
          288
        </td>
        <td class="kanji">
          ～しき
        </td>
        <td class="kanji">
          ～式
        </td>
        <td>
          
        </td>
        <td class="eng">
          ceremony
        </td>
      </tr>
      <tr class="row1" id="289">
        <td class="pos">
          289
        </td>
        <td class="kanji">
          しけん
        </td>
        <td class="kanji">
          試験
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          examination, test, study
        </td>
      </tr>
      <tr class="row0" id="290">
        <td class="pos">
          290
        </td>
        <td class="kanji">
          じこ
        </td>
        <td class="kanji">
          事故
        </td>
        <td>
          n
        </td>
        <td class="eng">
          accident
        </td>
      </tr>
      <tr class="row1" id="291">
        <td class="pos">
          291
        </td>
        <td class="kanji">
          じしん
        </td>
        <td class="kanji">
          地震
        </td>
        <td>
          n
        </td>
        <td class="eng">
          earthquake
        </td>
      </tr>
      <tr class="row0" id="292">
        <td class="pos">
          292
        </td>
        <td class="kanji">
          じだい
        </td>
        <td class="kanji">
          時代
        </td>
        <td>
          n-t
        </td>
        <td class="eng">
          period, epoch, era
        </td>
      </tr>
      <tr class="row1" id="293">
        <td class="pos">
          293
        </td>
        <td class="kanji">
          したぎ
        </td>
        <td class="kanji">
          下着
        </td>
        <td>
          n
        </td>
        <td class="eng">
          underwear
        </td>
      </tr>
      <tr class="row0" id="294">
        <td class="pos">
          294
        </td>
        <td class="kanji">
          したく・する
        </td>
        <td class="kanji">
          支度
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          preparation
        </td>
      </tr>
      <tr class="row1" id="295">
        <td class="pos">
          295
        </td>
        <td class="kanji">
          しっかり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,adv,n
        </td>
        <td class="eng">
          firmly, tightly, steady
        </td>
      </tr>
      <tr class="row0" id="296">
        <td class="pos">
          296
        </td>
        <td class="kanji">
          しっぱい
        </td>
        <td class="kanji">
          失敗
        </td>
        <td>
          adj-no,n,vs
        </td>
        <td class="eng">
          failure, mistake, blunder
        </td>
      </tr>
      <tr class="row1" id="297">
        <td class="pos">
          297
        </td>
        <td class="kanji">
          しつれい
        </td>
        <td class="kanji">
          失礼
        </td>
        <td>
          adj-na,int,n,vs,exp
        </td>
        <td class="eng">
          (1) discourtesy, impoliteness, (2) Excuse me, Goodbye
        </td>
      </tr>
      <tr class="row0" id="298">
        <td class="pos">
          298
        </td>
        <td class="kanji">
          じてん
        </td>
        <td class="kanji">
          辞典
        </td>
        <td>
          n
        </td>
        <td class="eng">
          dictionary
        </td>
      </tr>
      <tr class="row1" id="299">
        <td class="pos">
          299
        </td>
        <td class="kanji">
          しなもの
        </td>
        <td class="kanji">
          品物
        </td>
        <td>
          n
        </td>
        <td class="eng">
          goods
        </td>
      </tr>
      <tr class="row0" id="300">
        <td class="pos">
          300
        </td>
        <td class="kanji">
          しばらく
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,int
        </td>
        <td class="eng">
          little while
        </td>
      </tr>
      <tr class="row1" id="301">
        <td class="pos">
          301
        </td>
        <td class="kanji">
          しま
        </td>
        <td class="kanji">
          島
        </td>
        <td>
          n
        </td>
        <td class="eng">
          island
        </td>
      </tr>
      <tr class="row0" id="302">
        <td class="pos">
          302
        </td>
        <td class="kanji">
          （～て）しまう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to end up ～
        </td>
      </tr>
      <tr class="row1" id="303">
        <td class="pos">
          303
        </td>
        <td class="kanji">
          しみん
        </td>
        <td class="kanji">
          市民
        </td>
        <td>
          n
        </td>
        <td class="eng">
          citizen
        </td>
      </tr>
      <tr class="row0" id="304">
        <td class="pos">
          304
        </td>
        <td class="kanji">
          じむしょ
        </td>
        <td class="kanji">
          事務所
        </td>
        <td>
          n
        </td>
        <td class="eng">
          office
        </td>
      </tr>
      <tr class="row1" id="305">
        <td class="pos">
          305
        </td>
        <td class="kanji">
          しゃかい
        </td>
        <td class="kanji">
          社会
        </td>
        <td>
          n
        </td>
        <td class="eng">
          society, public
        </td>
      </tr>
      <tr class="row0" id="306">
        <td class="pos">
          306
        </td>
        <td class="kanji">
          しゃちょう
        </td>
        <td class="kanji">
          社長
        </td>
        <td>
          n
        </td>
        <td class="eng">
          company president, manager, director
        </td>
      </tr>
      <tr class="row1" id="307">
        <td class="pos">
          307
        </td>
        <td class="kanji">
          じゃま
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,n,vs
        </td>
        <td class="eng">
          hindrance, intrusion
        </td>
      </tr>
      <tr class="row0" id="308">
        <td class="pos">
          308
        </td>
        <td class="kanji">
          ジャム
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          jam
        </td>
      </tr>
      <tr class="row1" id="309">
        <td class="pos">
          309
        </td>
        <td class="kanji">
          じゆう
        </td>
        <td class="kanji">
          自由
        </td>
        <td>
          adj-na,exp,n
        </td>
        <td class="eng">
          freedom
        </td>
      </tr>
      <tr class="row0" id="310">
        <td class="pos">
          310
        </td>
        <td class="kanji">
          しゅうかん
        </td>
        <td class="kanji">
          習慣
        </td>
        <td>
          n
        </td>
        <td class="eng">
          custom, habit, manners
        </td>
      </tr>
      <tr class="row1" id="311">
        <td class="pos">
          311
        </td>
        <td class="kanji">
          じゅうしょ
        </td>
        <td class="kanji">
          住所
        </td>
        <td>
          n
        </td>
        <td class="eng">
          address (eg of house), residence, domicile
        </td>
      </tr>
      <tr class="row0" id="312">
        <td class="pos">
          312
        </td>
        <td class="kanji">
          じゅうどう
        </td>
        <td class="kanji">
          柔道
        </td>
        <td>
          n
        </td>
        <td class="eng">
          judo
        </td>
      </tr>
      <tr class="row1" id="313">
        <td class="pos">
          313
        </td>
        <td class="kanji">
          じゅうぶん
        </td>
        <td class="kanji">
          十分
        </td>
        <td>
          
        </td>
        <td class="eng">
          enough , sufficient
        </td>
      </tr>
      <tr class="row0" id="314">
        <td class="pos">
          314
        </td>
        <td class="kanji">
          しゅっせき・する
        </td>
        <td class="kanji">
          出席
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          attendance, presence
        </td>
      </tr>
      <tr class="row1" id="315">
        <td class="pos">
          315
        </td>
        <td class="kanji">
          しゅっぱつ・する
        </td>
        <td class="kanji">
          出発
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          departure
        </td>
      </tr>
      <tr class="row0" id="316">
        <td class="pos">
          316
        </td>
        <td class="kanji">
          しゅみ
        </td>
        <td class="kanji">
          趣味
        </td>
        <td>
          n
        </td>
        <td class="eng">
          hobby
        </td>
      </tr>
      <tr class="row1" id="317">
        <td class="pos">
          317
        </td>
        <td class="kanji">
          じゅんび・する
        </td>
        <td class="kanji">
          準備
        </td>
        <td>
          n
        </td>
        <td class="eng">
          prepare
        </td>
      </tr>
      <tr class="row0" id="318">
        <td class="pos">
          318
        </td>
        <td class="kanji">
          しょうかい
        </td>
        <td class="kanji">
          紹介
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          introduction
        </td>
      </tr>
      <tr class="row1" id="319">
        <td class="pos">
          319
        </td>
        <td class="kanji">
          しょうがつ
        </td>
        <td class="kanji">
          正月
        </td>
        <td>
          n
        </td>
        <td class="eng">
          New Year, New Year's Day
        </td>
      </tr>
      <tr class="row0" id="320">
        <td class="pos">
          320
        </td>
        <td class="kanji">
          しょうがっこう
        </td>
        <td class="kanji">
          小学校
        </td>
        <td>
          n
        </td>
        <td class="eng">
          primary school, elementary school
        </td>
      </tr>
      <tr class="row1" id="321">
        <td class="pos">
          321
        </td>
        <td class="kanji">
          しょうせつ
        </td>
        <td class="kanji">
          小説
        </td>
        <td>
          n
        </td>
        <td class="eng">
          novel, story
        </td>
      </tr>
      <tr class="row0" id="322">
        <td class="pos">
          322
        </td>
        <td class="kanji">
          しょうたい・する
        </td>
        <td class="kanji">
          招待
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          invitation
        </td>
      </tr>
      <tr class="row1" id="323">
        <td class="pos">
          323
        </td>
        <td class="kanji">
          しょうち・する
        </td>
        <td class="kanji">
          承知
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          consent, acceptance
        </td>
      </tr>
      <tr class="row0" id="324">
        <td class="pos">
          324
        </td>
        <td class="kanji">
          しょうらい
        </td>
        <td class="kanji">
          将来
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          future, prospects
        </td>
      </tr>
      <tr class="row1" id="325">
        <td class="pos">
          325
        </td>
        <td class="kanji">
          しょくじ・する
        </td>
        <td class="kanji">
          食事
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          meal
        </td>
      </tr>
      <tr class="row0" id="326">
        <td class="pos">
          326
        </td>
        <td class="kanji">
          しょくりょうひん
        </td>
        <td class="kanji">
          食料品
        </td>
        <td>
          n
        </td>
        <td class="eng">
          foodstuff, groceries
        </td>
      </tr>
      <tr class="row1" id="327">
        <td class="pos">
          327
        </td>
        <td class="kanji">
          じょせい
        </td>
        <td class="kanji">
          女性
        </td>
        <td>
          n
        </td>
        <td class="eng">
          woman
        </td>
      </tr>
      <tr class="row0" id="328">
        <td class="pos">
          328
        </td>
        <td class="kanji">
          しらせる
        </td>
        <td class="kanji">
          知らせる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to notify, to advise
        </td>
      </tr>
      <tr class="row1" id="329">
        <td class="pos">
          329
        </td>
        <td class="kanji">
          しらべる
        </td>
        <td class="kanji">
          調べる
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to investigate, to check up
        </td>
      </tr>
      <tr class="row0" id="330">
        <td class="pos">
          330
        </td>
        <td class="kanji">
          じんこう
        </td>
        <td class="kanji">
          人口
        </td>
        <td>
          n
        </td>
        <td class="eng">
          population
        </td>
      </tr>
      <tr class="row1" id="331">
        <td class="pos">
          331
        </td>
        <td class="kanji">
          じんじゃ
        </td>
        <td class="kanji">
          神社
        </td>
        <td>
          n
        </td>
        <td class="eng">
          Shinto shrine
        </td>
      </tr>
      <tr class="row0" id="332">
        <td class="pos">
          332
        </td>
        <td class="kanji">
          しんせつ
        </td>
        <td class="kanji">
          親切
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          kindness, gentleness
        </td>
      </tr>
      <tr class="row1" id="333">
        <td class="pos">
          333
        </td>
        <td class="kanji">
          しんぱい・する
        </td>
        <td class="kanji">
          心配
        </td>
        <td>
          adj-na,n,vs
        </td>
        <td class="eng">
          worry, concern
        </td>
      </tr>
      <tr class="row0" id="334">
        <td class="pos">
          334
        </td>
        <td class="kanji">
          しんぶんしゃ
        </td>
        <td class="kanji">
          新聞社
        </td>
        <td>
          n
        </td>
        <td class="eng">
          newspaper company
        </td>
      </tr>
      <tr class="row1" id="335">
        <td class="pos">
          335
        </td>
        <td class="kanji">
          すいえい
        </td>
        <td class="kanji">
          水泳
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          swimming
        </td>
      </tr>
      <tr class="row0" id="336">
        <td class="pos">
          336
        </td>
        <td class="kanji">
          すいどう
        </td>
        <td class="kanji">
          水道
        </td>
        <td>
          n
        </td>
        <td class="eng">
          water service, water supply
        </td>
      </tr>
      <tr class="row1" id="337">
        <td class="pos">
          337
        </td>
        <td class="kanji">
          ずいぶん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,n-adv
        </td>
        <td class="eng">
          extremely
        </td>
      </tr>
      <tr class="row0" id="338">
        <td class="pos">
          338
        </td>
        <td class="kanji">
          すうがく
        </td>
        <td class="kanji">
          数学
        </td>
        <td>
          n
        </td>
        <td class="eng">
          mathematics, arithmetic
        </td>
      </tr>
      <tr class="row1" id="339">
        <td class="pos">
          339
        </td>
        <td class="kanji">
          スーツ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          suit
        </td>
      </tr>
      <tr class="row0" id="340">
        <td class="pos">
          340
        </td>
        <td class="kanji">
          スーツケース
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          suitcase
        </td>
      </tr>
      <tr class="row1" id="341">
        <td class="pos">
          341
        </td>
        <td class="kanji">
          スーパー（マーケット）
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          super (market)
        </td>
      </tr>
      <tr class="row0" id="342">
        <td class="pos">
          342
        </td>
        <td class="kanji">
          すぎる
        </td>
        <td class="kanji">
          過ぎる
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to exceed, to go beyond
        </td>
      </tr>
      <tr class="row1" id="343">
        <td class="pos">
          343
        </td>
        <td class="kanji">
          すく
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to become empty
        </td>
      </tr>
      <tr class="row0" id="344">
        <td class="pos">
          344
        </td>
        <td class="kanji">
          すく
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to be less crowded
        </td>
      </tr>
      <tr class="row1" id="345">
        <td class="pos">
          345
        </td>
        <td class="kanji">
          スクリーン
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          screen
        </td>
      </tr>
      <tr class="row0" id="346">
        <td class="pos">
          346
        </td>
        <td class="kanji">
          すごい
        </td>
        <td class="kanji">
          凄い
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          terrific, amazing, to a great extent
        </td>
      </tr>
      <tr class="row1" id="347">
        <td class="pos">
          347
        </td>
        <td class="kanji">
          すすむ
        </td>
        <td class="kanji">
          進む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to make progress, to advance, to proceed
        </td>
      </tr>
      <tr class="row0" id="348">
        <td class="pos">
          348
        </td>
        <td class="kanji">
          すっかり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          all, completely, thoroughly
        </td>
      </tr>
      <tr class="row1" id="349">
        <td class="pos">
          349
        </td>
        <td class="kanji">
          ずっと
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,n
        </td>
        <td class="eng">
          straight, quickly, all of a sudden
        </td>
      </tr>
      <tr class="row0" id="350">
        <td class="pos">
          350
        </td>
        <td class="kanji">
          ステーキ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          steak
        </td>
      </tr>
      <tr class="row1" id="351">
        <td class="pos">
          351
        </td>
        <td class="kanji">
          ステレオ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          stereo
        </td>
      </tr>
      <tr class="row0" id="352">
        <td class="pos">
          352
        </td>
        <td class="kanji">
          すてる
        </td>
        <td class="kanji">
          捨てる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to throw away
        </td>
      </tr>
      <tr class="row1" id="353">
        <td class="pos">
          353
        </td>
        <td class="kanji">
          すな
        </td>
        <td class="kanji">
          砂
        </td>
        <td>
          n
        </td>
        <td class="eng">
          sand
        </td>
      </tr>
      <tr class="row0" id="354">
        <td class="pos">
          354
        </td>
        <td class="kanji">
          すばらしい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          wonderful, splendid
        </td>
      </tr>
      <tr class="row1" id="355">
        <td class="pos">
          355
        </td>
        <td class="kanji">
          すべる
        </td>
        <td class="kanji">
          滑る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to slide, to slip
        </td>
      </tr>
      <tr class="row0" id="356">
        <td class="pos">
          356
        </td>
        <td class="kanji">
          すみ
        </td>
        <td class="kanji">
          隅
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          corner, nook
        </td>
      </tr>
      <tr class="row1" id="357">
        <td class="pos">
          357
        </td>
        <td class="kanji">
          すむ
        </td>
        <td class="kanji">
          済む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to finish, to end
        </td>
      </tr>
      <tr class="row0" id="358">
        <td class="pos">
          358
        </td>
        <td class="kanji">
          すり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          pickpocket
        </td>
      </tr>
      <tr class="row1" id="359">
        <td class="pos">
          359
        </td>
        <td class="kanji">
          すると
        </td>
        <td class="kanji">
          
        </td>
        <td>
          conj
        </td>
        <td class="eng">
          and, then
        </td>
      </tr>
      <tr class="row0" id="360">
        <td class="pos">
          360
        </td>
        <td class="kanji">
          ～せい
        </td>
        <td class="kanji">
          ～製
        </td>
        <td>
          
        </td>
        <td class="eng">
          made in　～
        </td>
      </tr>
      <tr class="row1" id="361">
        <td class="pos">
          361
        </td>
        <td class="kanji">
          せいかつ・する
        </td>
        <td class="kanji">
          生活
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          living, life (one's daily existence), livelihood
        </td>
      </tr>
      <tr class="row0" id="362">
        <td class="pos">
          362
        </td>
        <td class="kanji">
          せいさん・する
        </td>
        <td class="kanji">
          生産
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          production, manufacture
        </td>
      </tr>
      <tr class="row1" id="363">
        <td class="pos">
          363
        </td>
        <td class="kanji">
          せいじ
        </td>
        <td class="kanji">
          政治
        </td>
        <td>
          n
        </td>
        <td class="eng">
          politics, government
        </td>
      </tr>
      <tr class="row0" id="364">
        <td class="pos">
          364
        </td>
        <td class="kanji">
          せいよう
        </td>
        <td class="kanji">
          西洋
        </td>
        <td>
          n
        </td>
        <td class="eng">
          the west, Western countries
        </td>
      </tr>
      <tr class="row1" id="365">
        <td class="pos">
          365
        </td>
        <td class="kanji">
          せかい
        </td>
        <td class="kanji">
          世界
        </td>
        <td>
          n
        </td>
        <td class="eng">
          the world
        </td>
      </tr>
      <tr class="row0" id="366">
        <td class="pos">
          366
        </td>
        <td class="kanji">
          せき
        </td>
        <td class="kanji">
          席
        </td>
        <td>
          n
        </td>
        <td class="eng">
          seat
        </td>
      </tr>
      <tr class="row1" id="367">
        <td class="pos">
          367
        </td>
        <td class="kanji">
          せつめい
        </td>
        <td class="kanji">
          説明
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          explanation
        </td>
      </tr>
      <tr class="row0" id="368">
        <td class="pos">
          368
        </td>
        <td class="kanji">
          せなか
        </td>
        <td class="kanji">
          背中
        </td>
        <td>
          n
        </td>
        <td class="eng">
          back (of body)
        </td>
      </tr>
      <tr class="row1" id="369">
        <td class="pos">
          369
        </td>
        <td class="kanji">
          ぜひ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,n
        </td>
        <td class="eng">
          certainly, without fail
        </td>
      </tr>
      <tr class="row0" id="370">
        <td class="pos">
          370
        </td>
        <td class="kanji">
          せわ・する
        </td>
        <td class="kanji">
          世話
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          looking after, help
        </td>
      </tr>
      <tr class="row1" id="371">
        <td class="pos">
          371
        </td>
        <td class="kanji">
          せん
        </td>
        <td class="kanji">
          線
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          line, wire
        </td>
      </tr>
      <tr class="row0" id="372">
        <td class="pos">
          372
        </td>
        <td class="kanji">
          ぜんぜん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          wholly, entirely
        </td>
      </tr>
      <tr class="row1" id="373">
        <td class="pos">
          373
        </td>
        <td class="kanji">
          せんそう
        </td>
        <td class="kanji">
          戦争
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          war
        </td>
      </tr>
      <tr class="row0" id="374">
        <td class="pos">
          374
        </td>
        <td class="kanji">
          せんぱい
        </td>
        <td class="kanji">
          先輩
        </td>
        <td>
          n
        </td>
        <td class="eng">
          senior, superior, elder
        </td>
      </tr>
      <tr class="row1" id="375">
        <td class="pos">
          375
        </td>
        <td class="kanji">
          せんもん
        </td>
        <td class="kanji">
          専門
        </td>
        <td>
          n
        </td>
        <td class="eng">
          speciality, study major
        </td>
      </tr>
      <tr class="row0" id="376">
        <td class="pos">
          376
        </td>
        <td class="kanji">
          そう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          really
        </td>
      </tr>
      <tr class="row1" id="377">
        <td class="pos">
          377
        </td>
        <td class="kanji">
          そうだん・する
        </td>
        <td class="kanji">
          相談
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          consultation, discussion
        </td>
      </tr>
      <tr class="row0" id="378">
        <td class="pos">
          378
        </td>
        <td class="kanji">
          そだてる
        </td>
        <td class="kanji">
          育てる
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to raise, to rear, to bring up
        </td>
      </tr>
      <tr class="row1" id="379">
        <td class="pos">
          379
        </td>
        <td class="kanji">
          そつぎょう
        </td>
        <td class="kanji">
          卒業
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          graduation
        </td>
      </tr>
      <tr class="row0" id="380">
        <td class="pos">
          380
        </td>
        <td class="kanji">
          そふ
        </td>
        <td class="kanji">
          祖父
        </td>
        <td>
          n
        </td>
        <td class="eng">
          grandfather
        </td>
      </tr>
      <tr class="row1" id="381">
        <td class="pos">
          381
        </td>
        <td class="kanji">
          ソフト
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          soft
        </td>
      </tr>
      <tr class="row0" id="382">
        <td class="pos">
          382
        </td>
        <td class="kanji">
          そぼ
        </td>
        <td class="kanji">
          祖母
        </td>
        <td>
          n
        </td>
        <td class="eng">
          grandmother
        </td>
      </tr>
      <tr class="row1" id="383">
        <td class="pos">
          383
        </td>
        <td class="kanji">
          それで
        </td>
        <td class="kanji">
          
        </td>
        <td>
          conj
        </td>
        <td class="eng">
          and, thereupon, because of that
        </td>
      </tr>
      <tr class="row0" id="384">
        <td class="pos">
          384
        </td>
        <td class="kanji">
          それに
        </td>
        <td class="kanji">
          
        </td>
        <td>
          conj
        </td>
        <td class="eng">
          besides, moreover
        </td>
      </tr>
      <tr class="row1" id="385">
        <td class="pos">
          385
        </td>
        <td class="kanji">
          それほど
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          to that degree, extent
        </td>
      </tr>
      <tr class="row0" id="386">
        <td class="pos">
          386
        </td>
        <td class="kanji">
          そろそろ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          gradually, steadily, soon
        </td>
      </tr>
      <tr class="row1" id="387">
        <td class="pos">
          387
        </td>
        <td class="kanji">
          そんな
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,adj-pn,adv,n
        </td>
        <td class="eng">
          such, like that, that sort of
        </td>
      </tr>
      <tr class="row0" id="388">
        <td class="pos">
          388
        </td>
        <td class="kanji">
          そんなに
        </td>
        <td class="kanji">
          
        </td>
        <td>
          uk
        </td>
        <td class="eng">
          so much, like that
        </td>
      </tr>
      <tr class="row1" id="389">
        <td class="pos">
          389
        </td>
        <td class="kanji">
          ～だい
        </td>
        <td class="kanji">
          ～代
        </td>
        <td>
          
        </td>
        <td class="eng">
          ～ age/period
        </td>
      </tr>
      <tr class="row0" id="390">
        <td class="pos">
          390
        </td>
        <td class="kanji">
          たいいん・する
        </td>
        <td class="kanji">
          退院
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          leaving hospital
        </td>
      </tr>
      <tr class="row1" id="391">
        <td class="pos">
          391
        </td>
        <td class="kanji">
          だいがくせい
        </td>
        <td class="kanji">
          大学生
        </td>
        <td>
          n
        </td>
        <td class="eng">
          college student, university student
        </td>
      </tr>
      <tr class="row0" id="392">
        <td class="pos">
          392
        </td>
        <td class="kanji">
          だいじ
        </td>
        <td class="kanji">
          大事
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          important, valuable, serious matter
        </td>
      </tr>
      <tr class="row1" id="393">
        <td class="pos">
          393
        </td>
        <td class="kanji">
          だいたい
        </td>
        <td class="kanji">
          大体
        </td>
        <td>
          n
        </td>
        <td class="eng">
          generally, substantially
        </td>
      </tr>
      <tr class="row0" id="394">
        <td class="pos">
          394
        </td>
        <td class="kanji">
          たいてい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,adv,n
        </td>
        <td class="eng">
          generally, usually
        </td>
      </tr>
      <tr class="row1" id="395">
        <td class="pos">
          395
        </td>
        <td class="kanji">
          タイプ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          type, style
        </td>
      </tr>
      <tr class="row0" id="396">
        <td class="pos">
          396
        </td>
        <td class="kanji">
          だいぶ
        </td>
        <td class="kanji">
          大分
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          considerably, greatly, a lot
        </td>
      </tr>
      <tr class="row1" id="397">
        <td class="pos">
          397
        </td>
        <td class="kanji">
          たいふう
        </td>
        <td class="kanji">
          台風
        </td>
        <td>
          n
        </td>
        <td class="eng">
          typhoon
        </td>
      </tr>
      <tr class="row0" id="398">
        <td class="pos">
          398
        </td>
        <td class="kanji">
          たおれる
        </td>
        <td class="kanji">
          倒れる
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to collapse, to break down
        </td>
      </tr>
      <tr class="row1" id="399">
        <td class="pos">
          399
        </td>
        <td class="kanji">
          だから
        </td>
        <td class="kanji">
          
        </td>
        <td>
          conj,n
        </td>
        <td class="eng">
          so, therefore
        </td>
      </tr>
      <tr class="row0" id="400">
        <td class="pos">
          400
        </td>
        <td class="kanji">
          たしか
        </td>
        <td class="kanji">
          確か
        </td>
        <td>
          adj-na,adv,exp,n
        </td>
        <td class="eng">
          certain, sure, definite
        </td>
      </tr>
      <tr class="row1" id="401">
        <td class="pos">
          401
        </td>
        <td class="kanji">
          たす
        </td>
        <td class="kanji">
          足す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to add (numbers), to do (eg. one's business)
        </td>
      </tr>
      <tr class="row0" id="402">
        <td class="pos">
          402
        </td>
        <td class="kanji">
          ～だす
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          start to ～
        </td>
      </tr>
      <tr class="row1" id="403">
        <td class="pos">
          403
        </td>
        <td class="kanji">
          たずねる
        </td>
        <td class="kanji">
          訪ねる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to visit
        </td>
      </tr>
      <tr class="row0" id="404">
        <td class="pos">
          404
        </td>
        <td class="kanji">
          たずねる
        </td>
        <td class="kanji">
          尋ねる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to ask
        </td>
      </tr>
      <tr class="row1" id="405">
        <td class="pos">
          405
        </td>
        <td class="kanji">
          ただしい
        </td>
        <td class="kanji">
          正しい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          right, just, correct
        </td>
      </tr>
      <tr class="row0" id="406">
        <td class="pos">
          406
        </td>
        <td class="kanji">
          たたみ
        </td>
        <td class="kanji">
          畳
        </td>
        <td>
          n
        </td>
        <td class="eng">
          tatami mat (Japanese straw mat)
        </td>
      </tr>
      <tr class="row1" id="407">
        <td class="pos">
          407
        </td>
        <td class="kanji">
          ～だて
        </td>
        <td class="kanji">
          建て
        </td>
        <td>
          n
        </td>
        <td class="eng">
          two storied, separate housing
        </td>
      </tr>
      <tr class="row0" id="408">
        <td class="pos">
          408
        </td>
        <td class="kanji">
          たてる
        </td>
        <td class="kanji">
          立てる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to stand (something) up, to erect (something)
        </td>
      </tr>
      <tr class="row1" id="409">
        <td class="pos">
          409
        </td>
        <td class="kanji">
          たてる
        </td>
        <td class="kanji">
          建てる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to build, to construct
        </td>
      </tr>
      <tr class="row0" id="410">
        <td class="pos">
          410
        </td>
        <td class="kanji">
          たとえば
        </td>
        <td class="kanji">
          例えば
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          for example, eg.
        </td>
      </tr>
      <tr class="row1" id="411">
        <td class="pos">
          411
        </td>
        <td class="kanji">
          たな
        </td>
        <td class="kanji">
          棚
        </td>
        <td>
          n
        </td>
        <td class="eng">
          shelves, rack
        </td>
      </tr>
      <tr class="row0" id="412">
        <td class="pos">
          412
        </td>
        <td class="kanji">
          たのしむ
        </td>
        <td class="kanji">
          楽む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to enjoy oneself
        </td>
      </tr>
      <tr class="row1" id="413">
        <td class="pos">
          413
        </td>
        <td class="kanji">
          たのしみ
        </td>
        <td class="kanji">
          楽しみ
        </td>
        <td>
          n
        </td>
        <td class="eng">
          pleasure, joy
        </td>
      </tr>
      <tr class="row0" id="414">
        <td class="pos">
          414
        </td>
        <td class="kanji">
          たまに
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,suf
        </td>
        <td class="eng">
          occasionally, once in a while
        </td>
      </tr>
      <tr class="row1" id="415">
        <td class="pos">
          415
        </td>
        <td class="kanji">
          ため
        </td>
        <td class="kanji">
          為
        </td>
        <td>
          n
        </td>
        <td class="eng">
          good, advantage, in order to
        </td>
      </tr>
      <tr class="row0" id="416">
        <td class="pos">
          416
        </td>
        <td class="kanji">
          だめ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          useless, no good, hopeless
        </td>
      </tr>
      <tr class="row1" id="417">
        <td class="pos">
          417
        </td>
        <td class="kanji">
          たりる
        </td>
        <td class="kanji">
          足りる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to be sufficient, to be enough
        </td>
      </tr>
      <tr class="row0" id="418">
        <td class="pos">
          418
        </td>
        <td class="kanji">
          だんせい
        </td>
        <td class="kanji">
          男性
        </td>
        <td>
          n
        </td>
        <td class="eng">
          male, man
        </td>
      </tr>
      <tr class="row1" id="419">
        <td class="pos">
          419
        </td>
        <td class="kanji">
          だんぼう
        </td>
        <td class="kanji">
          暖房
        </td>
        <td>
          n
        </td>
        <td class="eng">
          heating
        </td>
      </tr>
      <tr class="row0" id="420">
        <td class="pos">
          420
        </td>
        <td class="kanji">
          ち
        </td>
        <td class="kanji">
          血
        </td>
        <td>
          n
        </td>
        <td class="eng">
          blood
        </td>
      </tr>
      <tr class="row1" id="421">
        <td class="pos">
          421
        </td>
        <td class="kanji">
          チェック・する
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          check
        </td>
      </tr>
      <tr class="row0" id="422">
        <td class="pos">
          422
        </td>
        <td class="kanji">
          ちから
        </td>
        <td class="kanji">
          力
        </td>
        <td>
          n-suf
        </td>
        <td class="eng">
          strength, power
        </td>
      </tr>
      <tr class="row1" id="423">
        <td class="pos">
          423
        </td>
        <td class="kanji">
          ちっとも
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          not at all (neg. verb)
        </td>
      </tr>
      <tr class="row0" id="424">
        <td class="pos">
          424
        </td>
        <td class="kanji">
          ～ちゃん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          suffix for familiar (female) person
        </td>
      </tr>
      <tr class="row1" id="425">
        <td class="pos">
          425
        </td>
        <td class="kanji">
          ちゅうい
        </td>
        <td class="kanji">
          注意
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          caution, being careful, attention (heed)
        </td>
      </tr>
      <tr class="row0" id="426">
        <td class="pos">
          426
        </td>
        <td class="kanji">
          ちゅうがっこう
        </td>
        <td class="kanji">
          中学校
        </td>
        <td>
          n
        </td>
        <td class="eng">
          junior high school, middle school pupil
        </td>
      </tr>
      <tr class="row1" id="427">
        <td class="pos">
          427
        </td>
        <td class="kanji">
          ちゅうしゃ
        </td>
        <td class="kanji">
          注射
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          injection
        </td>
      </tr>
      <tr class="row0" id="428">
        <td class="pos">
          428
        </td>
        <td class="kanji">
          ちゅうしゃじょう
        </td>
        <td class="kanji">
          駐車場
        </td>
        <td>
          n
        </td>
        <td class="eng">
          parking lot, parking place
        </td>
      </tr>
      <tr class="row1" id="429">
        <td class="pos">
          429
        </td>
        <td class="kanji">
          ～ちょう
        </td>
        <td class="kanji">
          ～町
        </td>
        <td>
          n
        </td>
        <td class="eng">
          ～ of the town
        </td>
      </tr>
      <tr class="row0" id="430">
        <td class="pos">
          430
        </td>
        <td class="kanji">
          ちり
        </td>
        <td class="kanji">
          地理
        </td>
        <td>
          n
        </td>
        <td class="eng">
          geography
        </td>
      </tr>
      <tr class="row1" id="431">
        <td class="pos">
          431
        </td>
        <td class="kanji">
          ～（に）ついて
        </td>
        <td class="kanji">
          
        </td>
        <td>
          expr
        </td>
        <td class="eng">
          about, concerning, regarding
        </td>
      </tr>
      <tr class="row0" id="432">
        <td class="pos">
          432
        </td>
        <td class="kanji">
          つかまえる
        </td>
        <td class="kanji">
          捕まえる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to catch, to arrest, to seize
        </td>
      </tr>
      <tr class="row1" id="433">
        <td class="pos">
          433
        </td>
        <td class="kanji">
          つき
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n-suf
        </td>
        <td class="eng">
          moon
        </td>
      </tr>
      <tr class="row0" id="434">
        <td class="pos">
          434
        </td>
        <td class="kanji">
          ～つき
        </td>
        <td class="kanji">
          ～月
        </td>
        <td>
          n-temp
        </td>
        <td class="eng">
          month
        </td>
      </tr>
      <tr class="row1" id="435">
        <td class="pos">
          435
        </td>
        <td class="kanji">
          つく
        </td>
        <td class="kanji">
          点く
        </td>
        <td>
          u-v, intrans-verb
        </td>
        <td class="eng">
          to be started, to be switched on
        </td>
      </tr>
      <tr class="row0" id="436">
        <td class="pos">
          436
        </td>
        <td class="kanji">
          つける
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to take
        </td>
      </tr>
      <tr class="row1" id="437">
        <td class="pos">
          437
        </td>
        <td class="kanji">
          つける
        </td>
        <td class="kanji">
          漬ける
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to soak, to moisten, to pickle
        </td>
      </tr>
      <tr class="row0" id="438">
        <td class="pos">
          438
        </td>
        <td class="kanji">
          つごう
        </td>
        <td class="kanji">
          都合
        </td>
        <td>
          adv,n
        </td>
        <td class="eng">
          circumstances, condition, convenience
        </td>
      </tr>
      <tr class="row1" id="439">
        <td class="pos">
          439
        </td>
        <td class="kanji">
          つたえる
        </td>
        <td class="kanji">
          伝える
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to tell, to report
        </td>
      </tr>
      <tr class="row0" id="440">
        <td class="pos">
          440
        </td>
        <td class="kanji">
          つづく
        </td>
        <td class="kanji">
          続く
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to be continued
        </td>
      </tr>
      <tr class="row1" id="441">
        <td class="pos">
          441
        </td>
        <td class="kanji">
          ～つづける
        </td>
        <td class="kanji">
          ～続ける
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to continue doing ～
        </td>
      </tr>
      <tr class="row0" id="442">
        <td class="pos">
          442
        </td>
        <td class="kanji">
          つづける
        </td>
        <td class="kanji">
          続ける
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to continue, to keep up, to keep on
        </td>
      </tr>
      <tr class="row1" id="443">
        <td class="pos">
          443
        </td>
        <td class="kanji">
          つつむ
        </td>
        <td class="kanji">
          包む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          wrap, pack
        </td>
      </tr>
      <tr class="row0" id="444">
        <td class="pos">
          444
        </td>
        <td class="kanji">
          つま
        </td>
        <td class="kanji">
          妻
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (hum) wife
        </td>
      </tr>
      <tr class="row1" id="445">
        <td class="pos">
          445
        </td>
        <td class="kanji">
          つもり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          intention, plan
        </td>
      </tr>
      <tr class="row0" id="446">
        <td class="pos">
          446
        </td>
        <td class="kanji">
          つる
        </td>
        <td class="kanji">
          釣る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to fish
        </td>
      </tr>
      <tr class="row1" id="447">
        <td class="pos">
          447
        </td>
        <td class="kanji">
          つれる
        </td>
        <td class="kanji">
          連れる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to lead, to take (a person)
        </td>
      </tr>
      <tr class="row0" id="448">
        <td class="pos">
          448
        </td>
        <td class="kanji">
          ていねい
        </td>
        <td class="kanji">
          丁寧
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          polite, courteous
        </td>
      </tr>
      <tr class="row1" id="449">
        <td class="pos">
          449
        </td>
        <td class="kanji">
          テキスト
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (1)text, (2)text book
        </td>
      </tr>
      <tr class="row0" id="450">
        <td class="pos">
          450
        </td>
        <td class="kanji">
          てきとう
        </td>
        <td class="kanji">
          適当
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          fitness, suitability
        </td>
      </tr>
      <tr class="row1" id="451">
        <td class="pos">
          451
        </td>
        <td class="kanji">
          できる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to be able to do
        </td>
      </tr>
      <tr class="row0" id="452">
        <td class="pos">
          452
        </td>
        <td class="kanji">
          できるだけ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          if at all possible, as much as possible
        </td>
      </tr>
      <tr class="row1" id="453">
        <td class="pos">
          453
        </td>
        <td class="kanji">
          てつだう
        </td>
        <td class="kanji">
          手伝う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to help, to assist, to take part in
        </td>
      </tr>
      <tr class="row0" id="454">
        <td class="pos">
          454
        </td>
        <td class="kanji">
          テニス
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          tennis
        </td>
      </tr>
      <tr class="row1" id="455">
        <td class="pos">
          455
        </td>
        <td class="kanji">
          てぶくろ
        </td>
        <td class="kanji">
          手袋
        </td>
        <td>
          n
        </td>
        <td class="eng">
          glove
        </td>
      </tr>
      <tr class="row0" id="456">
        <td class="pos">
          456
        </td>
        <td class="kanji">
          てら
        </td>
        <td class="kanji">
          寺
        </td>
        <td>
          n
        </td>
        <td class="eng">
          temple
        </td>
      </tr>
      <tr class="row1" id="457">
        <td class="pos">
          457
        </td>
        <td class="kanji">
          てん
        </td>
        <td class="kanji">
          点
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          spot, mark, point, dot
        </td>
      </tr>
      <tr class="row0" id="458">
        <td class="pos">
          458
        </td>
        <td class="kanji">
          てんいん
        </td>
        <td class="kanji">
          店員
        </td>
        <td>
          n
        </td>
        <td class="eng">
          shop assistant, employee, clerk, salesperson
        </td>
      </tr>
      <tr class="row1" id="459">
        <td class="pos">
          459
        </td>
        <td class="kanji">
          てんきよほう
        </td>
        <td class="kanji">
          天気予報
        </td>
        <td>
          
        </td>
        <td class="eng">
          weather forecast, weather report
        </td>
      </tr>
      <tr class="row0" id="460">
        <td class="pos">
          460
        </td>
        <td class="kanji">
          でんとう
        </td>
        <td class="kanji">
          電灯
        </td>
        <td>
          n
        </td>
        <td class="eng">
          electric light
        </td>
      </tr>
      <tr class="row1" id="461">
        <td class="pos">
          461
        </td>
        <td class="kanji">
          でんぽう
        </td>
        <td class="kanji">
          電報
        </td>
        <td>
          n
        </td>
        <td class="eng">
          telegram
        </td>
      </tr>
      <tr class="row0" id="462">
        <td class="pos">
          462
        </td>
        <td class="kanji">
          てんらんかい
        </td>
        <td class="kanji">
          展覧会
        </td>
        <td>
          n
        </td>
        <td class="eng">
          exhibition
        </td>
      </tr>
      <tr class="row1" id="463">
        <td class="pos">
          463
        </td>
        <td class="kanji">
          と
        </td>
        <td class="kanji">
          都
        </td>
        <td>
          n
        </td>
        <td class="eng">
          metroplitan, municipal
        </td>
      </tr>
      <tr class="row0" id="464">
        <td class="pos">
          464
        </td>
        <td class="kanji">
          どうぐ
        </td>
        <td class="kanji">
          道具
        </td>
        <td>
          n
        </td>
        <td class="eng">
          tool, means
        </td>
      </tr>
      <tr class="row1" id="465">
        <td class="pos">
          465
        </td>
        <td class="kanji">
          とうとう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          finally, at last
        </td>
      </tr>
      <tr class="row0" id="466">
        <td class="pos">
          466
        </td>
        <td class="kanji">
          どうぶつえん
        </td>
        <td class="kanji">
          動物園
        </td>
        <td>
          n
        </td>
        <td class="eng">
          zoo
        </td>
      </tr>
      <tr class="row1" id="467">
        <td class="pos">
          467
        </td>
        <td class="kanji">
          とおく
        </td>
        <td class="kanji">
          遠く
        </td>
        <td>
          adj-no,n-adv,n
        </td>
        <td class="eng">
          far away, distant
        </td>
      </tr>
      <tr class="row0" id="468">
        <td class="pos">
          468
        </td>
        <td class="kanji">
          とおり
        </td>
        <td class="kanji">
          通り
        </td>
        <td>
          n-suf
        </td>
        <td class="eng">
          ～ Street, ～ Avenue
        </td>
      </tr>
      <tr class="row1" id="469">
        <td class="pos">
          469
        </td>
        <td class="kanji">
          とおる
        </td>
        <td class="kanji">
          通る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to pass (by), to go through
        </td>
      </tr>
      <tr class="row0" id="470">
        <td class="pos">
          470
        </td>
        <td class="kanji">
          とくに
        </td>
        <td class="kanji">
          特に
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          particularly, especially
        </td>
      </tr>
      <tr class="row1" id="471">
        <td class="pos">
          471
        </td>
        <td class="kanji">
          とくべつ
        </td>
        <td class="kanji">
          特別
        </td>
        <td>
          adj-na,adv,n
        </td>
        <td class="eng">
          special
        </td>
      </tr>
      <tr class="row0" id="472">
        <td class="pos">
          472
        </td>
        <td class="kanji">
          とこや
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          barber
        </td>
      </tr>
      <tr class="row1" id="473">
        <td class="pos">
          473
        </td>
        <td class="kanji">
          とちゅう
        </td>
        <td class="kanji">
          途中
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          on the way, en route, midway
        </td>
      </tr>
      <tr class="row0" id="474">
        <td class="pos">
          474
        </td>
        <td class="kanji">
          とっきゅう
        </td>
        <td class="kanji">
          特急
        </td>
        <td>
          n
        </td>
        <td class="eng">
          limited express (train, faster than an express)
        </td>
      </tr>
      <tr class="row1" id="475">
        <td class="pos">
          475
        </td>
        <td class="kanji">
          とどける
        </td>
        <td class="kanji">
          届ける
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to reach
        </td>
      </tr>
      <tr class="row0" id="476">
        <td class="pos">
          476
        </td>
        <td class="kanji">
          とまる
        </td>
        <td class="kanji">
          泊まる
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to stay at (eg. hotel)
        </td>
      </tr>
      <tr class="row1" id="477">
        <td class="pos">
          477
        </td>
        <td class="kanji">
          とめる
        </td>
        <td class="kanji">
          止める
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to stop (something)
        </td>
      </tr>
      <tr class="row0" id="478">
        <td class="pos">
          478
        </td>
        <td class="kanji">
          とりかえる
        </td>
        <td class="kanji">
          取り替える
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to exchange, to replace
        </td>
      </tr>
      <tr class="row1" id="479">
        <td class="pos">
          479
        </td>
        <td class="kanji">
          どろぼう
        </td>
        <td class="kanji">
          泥棒
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          thief, burglar, robber
        </td>
      </tr>
      <tr class="row0" id="480">
        <td class="pos">
          480
        </td>
        <td class="kanji">
          どんどん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          steadily, little by little
        </td>
      </tr>
      <tr class="row1" id="481">
        <td class="pos">
          481
        </td>
        <td class="kanji">
          なおす
        </td>
        <td class="kanji">
          直す
        </td>
        <td>
          u-v,vt
        </td>
        <td class="eng">
          to fix, to repair
        </td>
      </tr>
      <tr class="row0" id="482">
        <td class="pos">
          482
        </td>
        <td class="kanji">
          なおる
        </td>
        <td class="kanji">
          直る
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to be fixed, to be repaired
        </td>
      </tr>
      <tr class="row1" id="483">
        <td class="pos">
          483
        </td>
        <td class="kanji">
          なおる
        </td>
        <td class="kanji">
          治る
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to be cured, to heal
        </td>
      </tr>
      <tr class="row0" id="484">
        <td class="pos">
          484
        </td>
        <td class="kanji">
          なかなか
        </td>
        <td class="kanji">
          中々
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          very, considerably, quite
        </td>
      </tr>
      <tr class="row1" id="485">
        <td class="pos">
          485
        </td>
        <td class="kanji">
          なく
        </td>
        <td class="kanji">
          泣く
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to cry, to weep
        </td>
      </tr>
      <tr class="row0" id="486">
        <td class="pos">
          486
        </td>
        <td class="kanji">
          なくなる
        </td>
        <td class="kanji">
          無くなる
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to disappear, to get lost
        </td>
      </tr>
      <tr class="row1" id="487">
        <td class="pos">
          487
        </td>
        <td class="kanji">
          なくなる
        </td>
        <td class="kanji">
          亡くなる
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to die
        </td>
      </tr>
      <tr class="row0" id="488">
        <td class="pos">
          488
        </td>
        <td class="kanji">
          なげる
        </td>
        <td class="kanji">
          投げる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to throw, to cast away
        </td>
      </tr>
      <tr class="row1" id="489">
        <td class="pos">
          489
        </td>
        <td class="kanji">
          なさる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          aru-v
        </td>
        <td class="eng">
          (hon) to do
        </td>
      </tr>
      <tr class="row0" id="490">
        <td class="pos">
          490
        </td>
        <td class="kanji">
          なる
        </td>
        <td class="kanji">
          鳴る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to sound, to ring, to resound
        </td>
      </tr>
      <tr class="row1" id="491">
        <td class="pos">
          491
        </td>
        <td class="kanji">
          なるべく
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          as much as possible
        </td>
      </tr>
      <tr class="row0" id="492">
        <td class="pos">
          492
        </td>
        <td class="kanji">
          なるほど
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,exp
        </td>
        <td class="eng">
          I see, now I understand
        </td>
      </tr>
      <tr class="row1" id="493">
        <td class="pos">
          493
        </td>
        <td class="kanji">
          なれる
        </td>
        <td class="kanji">
          慣れる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to grow accustomed to
        </td>
      </tr>
      <tr class="row0" id="494">
        <td class="pos">
          494
        </td>
        <td class="kanji">
          におい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          odour, scent, smell
        </td>
      </tr>
      <tr class="row1" id="495">
        <td class="pos">
          495
        </td>
        <td class="kanji">
          にがい
        </td>
        <td class="kanji">
          苦い
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          bitter
        </td>
      </tr>
      <tr class="row0" id="496">
        <td class="pos">
          496
        </td>
        <td class="kanji">
          ～にくい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          suf
        </td>
        <td class="eng">
          difficult to do ～
        </td>
      </tr>
      <tr class="row1" id="497">
        <td class="pos">
          497
        </td>
        <td class="kanji">
          にげる
        </td>
        <td class="kanji">
          逃げる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to escape, to run away
        </td>
      </tr>
      <tr class="row0" id="498">
        <td class="pos">
          498
        </td>
        <td class="kanji">
          にっき
        </td>
        <td class="kanji">
          日記
        </td>
        <td>
          n
        </td>
        <td class="eng">
          diary, journal
        </td>
      </tr>
      <tr class="row1" id="499">
        <td class="pos">
          499
        </td>
        <td class="kanji">
          にゅういん・する
        </td>
        <td class="kanji">
          入院
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          hospitalization
        </td>
      </tr>
      <tr class="row0" id="500">
        <td class="pos">
          500
        </td>
        <td class="kanji">
          にゅうがく・する
        </td>
        <td class="kanji">
          入学
        </td>
        <td>
          n
        </td>
        <td class="eng">
          entry to school or university, matriculation
        </td>
      </tr>
      <tr class="row1" id="501">
        <td class="pos">
          501
        </td>
        <td class="kanji">
          にる
        </td>
        <td class="kanji">
          似る
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to resemble, to be similar
        </td>
      </tr>
      <tr class="row0" id="502">
        <td class="pos">
          502
        </td>
        <td class="kanji">
          にんぎょう
        </td>
        <td class="kanji">
          人形
        </td>
        <td>
          n
        </td>
        <td class="eng">
          doll, puppet, figure
        </td>
      </tr>
      <tr class="row1" id="503">
        <td class="pos">
          503
        </td>
        <td class="kanji">
          ぬすむ
        </td>
        <td class="kanji">
          盗む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to steal
        </td>
      </tr>
      <tr class="row0" id="504">
        <td class="pos">
          504
        </td>
        <td class="kanji">
          ぬる
        </td>
        <td class="kanji">
          塗る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to paint, to plaster
        </td>
      </tr>
      <tr class="row1" id="505">
        <td class="pos">
          505
        </td>
        <td class="kanji">
          ぬれる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to get wet
        </td>
      </tr>
      <tr class="row0" id="506">
        <td class="pos">
          506
        </td>
        <td class="kanji">
          ねだん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          price, cost
        </td>
      </tr>
      <tr class="row1" id="507">
        <td class="pos">
          507
        </td>
        <td class="kanji">
          ねつ
        </td>
        <td class="kanji">
          熱
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          fever, temperature
        </td>
      </tr>
      <tr class="row0" id="508">
        <td class="pos">
          508
        </td>
        <td class="kanji">
          ねっしん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          zeal, enthusiasm
        </td>
      </tr>
      <tr class="row1" id="509">
        <td class="pos">
          509
        </td>
        <td class="kanji">
          ねぼう
        </td>
        <td class="kanji">
          寝坊
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          sleeping in late
        </td>
      </tr>
      <tr class="row0" id="510">
        <td class="pos">
          510
        </td>
        <td class="kanji">
          ねむい
        </td>
        <td class="kanji">
          眠い
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          sleepy, drowsy
        </td>
      </tr>
      <tr class="row1" id="511">
        <td class="pos">
          511
        </td>
        <td class="kanji">
          ねむる
        </td>
        <td class="kanji">
          眠る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to sleep
        </td>
      </tr>
      <tr class="row0" id="512">
        <td class="pos">
          512
        </td>
        <td class="kanji">
          のこる
        </td>
        <td class="kanji">
          残る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to remain, to be left
        </td>
      </tr>
      <tr class="row1" id="513">
        <td class="pos">
          513
        </td>
        <td class="kanji">
          のど
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          throat
        </td>
      </tr>
      <tr class="row0" id="514">
        <td class="pos">
          514
        </td>
        <td class="kanji">
          のりかえる
        </td>
        <td class="kanji">
          乗り換える
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to transfer (trains), to change (bus, train)
        </td>
      </tr>
      <tr class="row1" id="515">
        <td class="pos">
          515
        </td>
        <td class="kanji">
          のりもの
        </td>
        <td class="kanji">
          乗り物
        </td>
        <td>
          n
        </td>
        <td class="eng">
          vehicle
        </td>
      </tr>
      <tr class="row0" id="516">
        <td class="pos">
          516
        </td>
        <td class="kanji">
          は
        </td>
        <td class="kanji">
          葉
        </td>
        <td>
          n
        </td>
        <td class="eng">
          leaf
        </td>
      </tr>
      <tr class="row1" id="517">
        <td class="pos">
          517
        </td>
        <td class="kanji">
          ばあい
        </td>
        <td class="kanji">
          場合
        </td>
        <td>
          n-adv,n
        </td>
        <td class="eng">
          case, situation
        </td>
      </tr>
      <tr class="row0" id="518">
        <td class="pos">
          518
        </td>
        <td class="kanji">
          パート（タイム）
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n-adv,n
        </td>
        <td class="eng">
          part time (esp female part time employees)
        </td>
      </tr>
      <tr class="row1" id="519">
        <td class="pos">
          519
        </td>
        <td class="kanji">
          ばい
        </td>
        <td class="kanji">
          倍
        </td>
        <td>
          n,vi,vs,vt
        </td>
        <td class="eng">
          twice, double
        </td>
      </tr>
      <tr class="row0" id="520">
        <td class="pos">
          520
        </td>
        <td class="kanji">
          はいけん・する
        </td>
        <td class="kanji">
          拝見
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          (hum) (pol) seeing, look at
        </td>
      </tr>
      <tr class="row1" id="521">
        <td class="pos">
          521
        </td>
        <td class="kanji">
          はいしゃ
        </td>
        <td class="kanji">
          歯医者
        </td>
        <td>
          n
        </td>
        <td class="eng">
          dentist
        </td>
      </tr>
      <tr class="row0" id="522">
        <td class="pos">
          522
        </td>
        <td class="kanji">
          ～ばかり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          suf
        </td>
        <td class="eng">
          just did ～, only
        </td>
      </tr>
      <tr class="row1" id="523">
        <td class="pos">
          523
        </td>
        <td class="kanji">
          はこぶ
        </td>
        <td class="kanji">
          運ぶ
        </td>
        <td>
          v5b
        </td>
        <td class="eng">
          to transport, to carry
        </td>
      </tr>
      <tr class="row0" id="524">
        <td class="pos">
          524
        </td>
        <td class="kanji">
          ～はじめる
        </td>
        <td class="kanji">
          ～始める
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to start doing　～, the beginning of ～
        </td>
      </tr>
      <tr class="row1" id="525">
        <td class="pos">
          525
        </td>
        <td class="kanji">
          はじめる
        </td>
        <td class="kanji">
          始める
        </td>
        <td>
          ru-v,vt
        </td>
        <td class="eng">
          to start, to begin
        </td>
      </tr>
      <tr class="row0" id="526">
        <td class="pos">
          526
        </td>
        <td class="kanji">
          ばしょ
        </td>
        <td class="kanji">
          場所
        </td>
        <td>
          n
        </td>
        <td class="eng">
          place, location
        </td>
      </tr>
      <tr class="row1" id="527">
        <td class="pos">
          527
        </td>
        <td class="kanji">
          はず
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          it should be so
        </td>
      </tr>
      <tr class="row0" id="528">
        <td class="pos">
          528
        </td>
        <td class="kanji">
          はずかしい
        </td>
        <td class="kanji">
          恥ずかしい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          shy, ashamed, embarrassed
        </td>
      </tr>
      <tr class="row1" id="529">
        <td class="pos">
          529
        </td>
        <td class="kanji">
          パソコン
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (personal) computer
        </td>
      </tr>
      <tr class="row0" id="530">
        <td class="pos">
          530
        </td>
        <td class="kanji">
          はつおん
        </td>
        <td class="kanji">
          発音
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          pronunciation
        </td>
      </tr>
      <tr class="row1" id="531">
        <td class="pos">
          531
        </td>
        <td class="kanji">
          はっきり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,n
        </td>
        <td class="eng">
          clearly, plainly, distinctly
        </td>
      </tr>
      <tr class="row0" id="532">
        <td class="pos">
          532
        </td>
        <td class="kanji">
          はなみ
        </td>
        <td class="kanji">
          花見
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          cherry-blossom viewing, flower viewing
        </td>
      </tr>
      <tr class="row1" id="533">
        <td class="pos">
          533
        </td>
        <td class="kanji">
          パパ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          papa, father
        </td>
      </tr>
      <tr class="row0" id="534">
        <td class="pos">
          534
        </td>
        <td class="kanji">
          はやし
        </td>
        <td class="kanji">
          林
        </td>
        <td>
          n
        </td>
        <td class="eng">
          woods, forester
        </td>
      </tr>
      <tr class="row1" id="535">
        <td class="pos">
          535
        </td>
        <td class="kanji">
          はらう
        </td>
        <td class="kanji">
          払う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to pay
        </td>
      </tr>
      <tr class="row0" id="536">
        <td class="pos">
          536
        </td>
        <td class="kanji">
          ばんぐみ
        </td>
        <td class="kanji">
          番組
        </td>
        <td>
          n
        </td>
        <td class="eng">
          program (eg. TV)
        </td>
      </tr>
      <tr class="row1" id="537">
        <td class="pos">
          537
        </td>
        <td class="kanji">
          はんたい
        </td>
        <td class="kanji">
          反対
        </td>
        <td>
          adj-na,n,vs
        </td>
        <td class="eng">
          oppose, opposition, resistance
        </td>
      </tr>
      <tr class="row0" id="538">
        <td class="pos">
          538
        </td>
        <td class="kanji">
          ハンバーグ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          hamburger (meat, no bun)
        </td>
      </tr>
      <tr class="row1" id="539">
        <td class="pos">
          539
        </td>
        <td class="kanji">
          ひ
        </td>
        <td class="kanji">
          日
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          sun, sunshine, day
        </td>
      </tr>
      <tr class="row0" id="540">
        <td class="pos">
          540
        </td>
        <td class="kanji">
          ひ
        </td>
        <td class="kanji">
          火
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          fire, flame, blaze
        </td>
      </tr>
      <tr class="row1" id="541">
        <td class="pos">
          541
        </td>
        <td class="kanji">
          ピアノ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          piano
        </td>
      </tr>
      <tr class="row0" id="542">
        <td class="pos">
          542
        </td>
        <td class="kanji">
          ひえる
        </td>
        <td class="kanji">
          冷える
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to grow cold, to get chilly, to cool down
        </td>
      </tr>
      <tr class="row1" id="543">
        <td class="pos">
          543
        </td>
        <td class="kanji">
          ひかる
        </td>
        <td class="kanji">
          光る
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to shine, to glitter
        </td>
      </tr>
      <tr class="row0" id="544">
        <td class="pos">
          544
        </td>
        <td class="kanji">
          ひかり
        </td>
        <td class="kanji">
          光
        </td>
        <td>
          n
        </td>
        <td class="eng">
          light
        </td>
      </tr>
      <tr class="row1" id="545">
        <td class="pos">
          545
        </td>
        <td class="kanji">
          ひきだし
        </td>
        <td class="kanji">
          引き出し
        </td>
        <td>
          n
        </td>
        <td class="eng">
          drawer, drawing out
        </td>
      </tr>
      <tr class="row0" id="546">
        <td class="pos">
          546
        </td>
        <td class="kanji">
          ひげ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          beard
        </td>
      </tr>
      <tr class="row1" id="547">
        <td class="pos">
          547
        </td>
        <td class="kanji">
          ひこうじょう
        </td>
        <td class="kanji">
          飛行場
        </td>
        <td>
          n
        </td>
        <td class="eng">
          airport
        </td>
      </tr>
      <tr class="row0" id="548">
        <td class="pos">
          548
        </td>
        <td class="kanji">
          ひさしぶり
        </td>
        <td class="kanji">
          久しぶり
        </td>
        <td>
          exp
        </td>
        <td class="eng">
          after a long time
        </td>
      </tr>
      <tr class="row1" id="549">
        <td class="pos">
          549
        </td>
        <td class="kanji">
          びじゅつかん
        </td>
        <td class="kanji">
          美術館
        </td>
        <td>
          n
        </td>
        <td class="eng">
          art gallery, art museum
        </td>
      </tr>
      <tr class="row0" id="550">
        <td class="pos">
          550
        </td>
        <td class="kanji">
          ひじょうに
        </td>
        <td class="kanji">
          非常に
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          very, extremely, exceedingly
        </td>
      </tr>
      <tr class="row1" id="551">
        <td class="pos">
          551
        </td>
        <td class="kanji">
          びっくりする
        </td>
        <td class="kanji">
          
        </td>
        <td>
          vs
        </td>
        <td class="eng">
          to be surprised
        </td>
      </tr>
      <tr class="row0" id="552">
        <td class="pos">
          552
        </td>
        <td class="kanji">
          ひっこす
        </td>
        <td class="kanji">
          引っ越す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to move, to change residence
        </td>
      </tr>
      <tr class="row1" id="553">
        <td class="pos">
          553
        </td>
        <td class="kanji">
          ひつよう
        </td>
        <td class="kanji">
          必要
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          necessary, essential
        </td>
      </tr>
      <tr class="row0" id="554">
        <td class="pos">
          554
        </td>
        <td class="kanji">
          ひどい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          cruel, awful
        </td>
      </tr>
      <tr class="row1" id="555">
        <td class="pos">
          555
        </td>
        <td class="kanji">
          ひらく
        </td>
        <td class="kanji">
          開く
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to open (eg. a festival)
        </td>
      </tr>
      <tr class="row0" id="556">
        <td class="pos">
          556
        </td>
        <td class="kanji">
          ビル
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (abbr) building, bill
        </td>
      </tr>
      <tr class="row1" id="557">
        <td class="pos">
          557
        </td>
        <td class="kanji">
          ひるま
        </td>
        <td class="kanji">
          昼間
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          daytime, during the day
        </td>
      </tr>
      <tr class="row0" id="558">
        <td class="pos">
          558
        </td>
        <td class="kanji">
          ひるやすみ
        </td>
        <td class="kanji">
          昼休み
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          lunch break, noon recess, noon rest period
        </td>
      </tr>
      <tr class="row1" id="559">
        <td class="pos">
          559
        </td>
        <td class="kanji">
          ひろう
        </td>
        <td class="kanji">
          拾う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to pick up, to find, to gather
        </td>
      </tr>
      <tr class="row0" id="560">
        <td class="pos">
          560
        </td>
        <td class="kanji">
          ファックス
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          fax
        </td>
      </tr>
      <tr class="row1" id="561">
        <td class="pos">
          561
        </td>
        <td class="kanji">
          ふえる
        </td>
        <td class="kanji">
          増える
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to increase, to multiply
        </td>
      </tr>
      <tr class="row0" id="562">
        <td class="pos">
          562
        </td>
        <td class="kanji">
          ふかい
        </td>
        <td class="kanji">
          深い
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          deep, profound, thick
        </td>
      </tr>
      <tr class="row1" id="563">
        <td class="pos">
          563
        </td>
        <td class="kanji">
          ふくざつ
        </td>
        <td class="kanji">
          複雑
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          complexity, complication
        </td>
      </tr>
      <tr class="row0" id="564">
        <td class="pos">
          564
        </td>
        <td class="kanji">
          ふくしゅう
        </td>
        <td class="kanji">
          復習
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          review, revision
        </td>
      </tr>
      <tr class="row1" id="565">
        <td class="pos">
          565
        </td>
        <td class="kanji">
          ぶちょう
        </td>
        <td class="kanji">
          部長
        </td>
        <td>
          adjn
        </td>
        <td class="eng">
          head of a section
        </td>
      </tr>
      <tr class="row0" id="566">
        <td class="pos">
          566
        </td>
        <td class="kanji">
          ふつう
        </td>
        <td class="kanji">
          普通
        </td>
        <td>
          adj-na,adj-no,adv,n
        </td>
        <td class="eng">
          (1) generally, ordinarily, usually, (2) train that stops at every station
        </td>
      </tr>
      <tr class="row1" id="567">
        <td class="pos">
          567
        </td>
        <td class="kanji">
          ぶどう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          grapes
        </td>
      </tr>
      <tr class="row0" id="568">
        <td class="pos">
          568
        </td>
        <td class="kanji">
          ふとる
        </td>
        <td class="kanji">
          太る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to grow fat (stout, plump), to become fat
        </td>
      </tr>
      <tr class="row1" id="569">
        <td class="pos">
          569
        </td>
        <td class="kanji">
          ふとん
        </td>
        <td class="kanji">
          布団
        </td>
        <td>
          n
        </td>
        <td class="eng">
          bedding (Japanese style), futon
        </td>
      </tr>
      <tr class="row0" id="570">
        <td class="pos">
          570
        </td>
        <td class="kanji">
          ふね
        </td>
        <td class="kanji">
          舟
        </td>
        <td>
          n
        </td>
        <td class="eng">
          ship, boat
        </td>
      </tr>
      <tr class="row1" id="571">
        <td class="pos">
          571
        </td>
        <td class="kanji">
          ふべん
        </td>
        <td class="kanji">
          不便
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          inconvenience
        </td>
      </tr>
      <tr class="row0" id="572">
        <td class="pos">
          572
        </td>
        <td class="kanji">
          ふむ
        </td>
        <td class="kanji">
          踏む
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to step on, to tread on
        </td>
      </tr>
      <tr class="row1" id="573">
        <td class="pos">
          573
        </td>
        <td class="kanji">
          プレゼント
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          present, gift
        </td>
      </tr>
      <tr class="row0" id="574">
        <td class="pos">
          574
        </td>
        <td class="kanji">
          ぶんか
        </td>
        <td class="kanji">
          文化
        </td>
        <td>
          n
        </td>
        <td class="eng">
          culture, civilization
        </td>
      </tr>
      <tr class="row1" id="575">
        <td class="pos">
          575
        </td>
        <td class="kanji">
          ぶんがく
        </td>
        <td class="kanji">
          文学
        </td>
        <td>
          n
        </td>
        <td class="eng">
          literature
        </td>
      </tr>
      <tr class="row0" id="576">
        <td class="pos">
          576
        </td>
        <td class="kanji">
          ぶんぽう
        </td>
        <td class="kanji">
          文法
        </td>
        <td>
          n
        </td>
        <td class="eng">
          grammar
        </td>
      </tr>
      <tr class="row1" id="577">
        <td class="pos">
          577
        </td>
        <td class="kanji">
          べつ
        </td>
        <td class="kanji">
          別
        </td>
        <td>
          adj-na,n,n-suf
        </td>
        <td class="eng">
          distinction, different
        </td>
      </tr>
      <tr class="row0" id="578">
        <td class="pos">
          578
        </td>
        <td class="kanji">
          ベル
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          bell
        </td>
      </tr>
      <tr class="row1" id="579">
        <td class="pos">
          579
        </td>
        <td class="kanji">
          へん
        </td>
        <td class="kanji">
          変
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          strange, odd, peculiar
        </td>
      </tr>
      <tr class="row0" id="580">
        <td class="pos">
          580
        </td>
        <td class="kanji">
          へんじ
        </td>
        <td class="kanji">
          返事
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          reply, answer
        </td>
      </tr>
      <tr class="row1" id="581">
        <td class="pos">
          581
        </td>
        <td class="kanji">
          ぼうえき
        </td>
        <td class="kanji">
          貿易
        </td>
        <td>
          n
        </td>
        <td class="eng">
          trade (foreign)
        </td>
      </tr>
      <tr class="row0" id="582">
        <td class="pos">
          582
        </td>
        <td class="kanji">
          ほうそう・する
        </td>
        <td class="kanji">
          放送
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          broadcast, broadcasting
        </td>
      </tr>
      <tr class="row1" id="583">
        <td class="pos">
          583
        </td>
        <td class="kanji">
          ほうりつ
        </td>
        <td class="kanji">
          法律
        </td>
        <td>
          n
        </td>
        <td class="eng">
          law
        </td>
      </tr>
      <tr class="row0" id="584">
        <td class="pos">
          584
        </td>
        <td class="kanji">
          ぼく
        </td>
        <td class="kanji">
          僕
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (male) I, manservant
        </td>
      </tr>
      <tr class="row1" id="585">
        <td class="pos">
          585
        </td>
        <td class="kanji">
          ほし
        </td>
        <td class="kanji">
          星
        </td>
        <td>
          n
        </td>
        <td class="eng">
          star
        </td>
      </tr>
      <tr class="row0" id="586">
        <td class="pos">
          586
        </td>
        <td class="kanji">
          ほど
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          degree, extent
        </td>
      </tr>
      <tr class="row1" id="587">
        <td class="pos">
          587
        </td>
        <td class="kanji">
          ほとんど
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n-adv,n-t
        </td>
        <td class="eng">
          mostly, almost
        </td>
      </tr>
      <tr class="row0" id="588">
        <td class="pos">
          588
        </td>
        <td class="kanji">
          ほめる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to praise
        </td>
      </tr>
      <tr class="row1" id="589">
        <td class="pos">
          589
        </td>
        <td class="kanji">
          ほんやく
        </td>
        <td class="kanji">
          翻訳
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          translation (written)
        </td>
      </tr>
      <tr class="row0" id="590">
        <td class="pos">
          590
        </td>
        <td class="kanji">
          まいる
        </td>
        <td class="kanji">
          参る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (1) (hum) to go, to come
        </td>
      </tr>
      <tr class="row1" id="591">
        <td class="pos">
          591
        </td>
        <td class="kanji">
          まける
        </td>
        <td class="kanji">
          負ける
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to lose, to be defeated
        </td>
      </tr>
      <tr class="row0" id="592">
        <td class="pos">
          592
        </td>
        <td class="kanji">
          まじめ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj-na,n
        </td>
        <td class="eng">
          diligent, serious
        </td>
      </tr>
      <tr class="row1" id="593">
        <td class="pos">
          593
        </td>
        <td class="kanji">
          まず
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          first (of all), to start with
        </td>
      </tr>
      <tr class="row0" id="594">
        <td class="pos">
          594
        </td>
        <td class="kanji">
          または
        </td>
        <td class="kanji">
          
        </td>
        <td>
          conj,exp
        </td>
        <td class="eng">
          or, otherwise
        </td>
      </tr>
      <tr class="row1" id="595">
        <td class="pos">
          595
        </td>
        <td class="kanji">
          まちがえる
        </td>
        <td class="kanji">
          間違える
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to err, to make a mistake
        </td>
      </tr>
      <tr class="row0" id="596">
        <td class="pos">
          596
        </td>
        <td class="kanji">
          まにあう
        </td>
        <td class="kanji">
          間に合う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (1) to be in time for
        </td>
      </tr>
      <tr class="row1" id="597">
        <td class="pos">
          597
        </td>
        <td class="kanji">
          ～まま
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          as it is
        </td>
      </tr>
      <tr class="row0" id="598">
        <td class="pos">
          598
        </td>
        <td class="kanji">
          まわり
        </td>
        <td class="kanji">
          周り
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          surroundings, circulation
        </td>
      </tr>
      <tr class="row1" id="599">
        <td class="pos">
          599
        </td>
        <td class="kanji">
          まわる
        </td>
        <td class="kanji">
          回る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to go around, to revolve
        </td>
      </tr>
      <tr class="row0" id="600">
        <td class="pos">
          600
        </td>
        <td class="kanji">
          まんが
        </td>
        <td class="kanji">
          漫画
        </td>
        <td>
          n
        </td>
        <td class="eng">
          comic, cartoon
        </td>
      </tr>
      <tr class="row1" id="601">
        <td class="pos">
          601
        </td>
        <td class="kanji">
          まんなか
        </td>
        <td class="kanji">
          真中
        </td>
        <td>
          n
        </td>
        <td class="eng">
          middle, centre
        </td>
      </tr>
      <tr class="row0" id="602">
        <td class="pos">
          602
        </td>
        <td class="kanji">
          みえる
        </td>
        <td class="kanji">
          見える
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to be seen, to be in sight
        </td>
      </tr>
      <tr class="row1" id="603">
        <td class="pos">
          603
        </td>
        <td class="kanji">
          みずうみ
        </td>
        <td class="kanji">
          湖
        </td>
        <td>
          n
        </td>
        <td class="eng">
          lake
        </td>
      </tr>
      <tr class="row0" id="604">
        <td class="pos">
          604
        </td>
        <td class="kanji">
          みそ
        </td>
        <td class="kanji">
          味噌
        </td>
        <td>
          n
        </td>
        <td class="eng">
          miso, bean paste
        </td>
      </tr>
      <tr class="row1" id="605">
        <td class="pos">
          605
        </td>
        <td class="kanji">
          みつかる
        </td>
        <td class="kanji">
          見つかる
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (uk) to be found, to be discovered
        </td>
      </tr>
      <tr class="row0" id="606">
        <td class="pos">
          606
        </td>
        <td class="kanji">
          みつける
        </td>
        <td class="kanji">
          見つける
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to discover, to find
        </td>
      </tr>
      <tr class="row1" id="607">
        <td class="pos">
          607
        </td>
        <td class="kanji">
          みな
        </td>
        <td class="kanji">
          皆
        </td>
        <td>
          adv,n
        </td>
        <td class="eng">
          everyone, everybody
        </td>
      </tr>
      <tr class="row0" id="608">
        <td class="pos">
          608
        </td>
        <td class="kanji">
          みなと
        </td>
        <td class="kanji">
          港
        </td>
        <td>
          n
        </td>
        <td class="eng">
          harbour, port
        </td>
      </tr>
      <tr class="row1" id="609">
        <td class="pos">
          609
        </td>
        <td class="kanji">
          むかえる
        </td>
        <td class="kanji">
          迎える
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to go out to meet
        </td>
      </tr>
      <tr class="row0" id="610">
        <td class="pos">
          610
        </td>
        <td class="kanji">
          むかう
        </td>
        <td class="kanji">
          向かう
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to face, to go towards
        </td>
      </tr>
      <tr class="row1" id="611">
        <td class="pos">
          611
        </td>
        <td class="kanji">
          むかし
        </td>
        <td class="kanji">
          昔
        </td>
        <td>
          adj-no,n-adv,n-t
        </td>
        <td class="eng">
          olden days, former
        </td>
      </tr>
      <tr class="row0" id="612">
        <td class="pos">
          612
        </td>
        <td class="kanji">
          むし
        </td>
        <td class="kanji">
          虫
        </td>
        <td>
          n
        </td>
        <td class="eng">
          insect
        </td>
      </tr>
      <tr class="row1" id="613">
        <td class="pos">
          613
        </td>
        <td class="kanji">
          むすこ
        </td>
        <td class="kanji">
          息子
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (hum) son
        </td>
      </tr>
      <tr class="row0" id="614">
        <td class="pos">
          614
        </td>
        <td class="kanji">
          むすめ
        </td>
        <td class="kanji">
          娘
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (hum) daughter
        </td>
      </tr>
      <tr class="row1" id="615">
        <td class="pos">
          615
        </td>
        <td class="kanji">
          むり
        </td>
        <td class="kanji">
          無理
        </td>
        <td>
          adj-na,n,vs
        </td>
        <td class="eng">
          unreasonable, impossible
        </td>
      </tr>
      <tr class="row0" id="616">
        <td class="pos">
          616
        </td>
        <td class="kanji">
          ～め
        </td>
        <td class="kanji">
          ～目
        </td>
        <td>
          suf
        </td>
        <td class="eng">
          number ～ sequence, ～nd/th
        </td>
      </tr>
      <tr class="row1" id="617">
        <td class="pos">
          617
        </td>
        <td class="kanji">
          めしあがる
        </td>
        <td class="kanji">
          召し上がる
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (pol) to eat
        </td>
      </tr>
      <tr class="row0" id="618">
        <td class="pos">
          618
        </td>
        <td class="kanji">
          めずらしい
        </td>
        <td class="kanji">
          珍しい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          unusual, rare
        </td>
      </tr>
      <tr class="row1" id="619">
        <td class="pos">
          619
        </td>
        <td class="kanji">
          もうしあげる
        </td>
        <td class="kanji">
          申し上げる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to say, to tell
        </td>
      </tr>
      <tr class="row0" id="620">
        <td class="pos">
          620
        </td>
        <td class="kanji">
          もうす
        </td>
        <td class="kanji">
          申す
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (hum) to be called, to say
        </td>
      </tr>
      <tr class="row1" id="621">
        <td class="pos">
          621
        </td>
        <td class="kanji">
          もうすぐ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          expr
        </td>
        <td class="eng">
          soon, very soon
        </td>
      </tr>
      <tr class="row0" id="622">
        <td class="pos">
          622
        </td>
        <td class="kanji">
          もし
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          if
        </td>
      </tr>
      <tr class="row1" id="623">
        <td class="pos">
          623
        </td>
        <td class="kanji">
          もちろん
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          certainly, of course
        </td>
      </tr>
      <tr class="row0" id="624">
        <td class="pos">
          624
        </td>
        <td class="kanji">
          もっとも
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          most, extremely
        </td>
      </tr>
      <tr class="row1" id="625">
        <td class="pos">
          625
        </td>
        <td class="kanji">
          もどる
        </td>
        <td class="kanji">
          戻る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to turn back, to return
        </td>
      </tr>
      <tr class="row0" id="626">
        <td class="pos">
          626
        </td>
        <td class="kanji">
          もめん
        </td>
        <td class="kanji">
          木綿
        </td>
        <td>
          n
        </td>
        <td class="eng">
          cotton
        </td>
      </tr>
      <tr class="row1" id="627">
        <td class="pos">
          627
        </td>
        <td class="kanji">
          もらう
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to receive
        </td>
      </tr>
      <tr class="row0" id="628">
        <td class="pos">
          628
        </td>
        <td class="kanji">
          もり
        </td>
        <td class="kanji">
          森
        </td>
        <td>
          n
        </td>
        <td class="eng">
          forest
        </td>
      </tr>
      <tr class="row1" id="629">
        <td class="pos">
          629
        </td>
        <td class="kanji">
          やく
        </td>
        <td class="kanji">
          焼く
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to bake, to grill
        </td>
      </tr>
      <tr class="row0" id="630">
        <td class="pos">
          630
        </td>
        <td class="kanji">
          やくにたつ
        </td>
        <td class="kanji">
          役に立つ
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to be helpful, to be useful
        </td>
      </tr>
      <tr class="row1" id="631">
        <td class="pos">
          631
        </td>
        <td class="kanji">
          やくそく
        </td>
        <td class="kanji">
          約束
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          arrangement, promise
        </td>
      </tr>
      <tr class="row0" id="632">
        <td class="pos">
          632
        </td>
        <td class="kanji">
          やける
        </td>
        <td class="kanji">
          焼ける
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to burn, to be roasted, to be sunburnt
        </td>
      </tr>
      <tr class="row1" id="633">
        <td class="pos">
          633
        </td>
        <td class="kanji">
          やさしい
        </td>
        <td class="kanji">
          優しい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          kind, gentle
        </td>
      </tr>
      <tr class="row0" id="634">
        <td class="pos">
          634
        </td>
        <td class="kanji">
          ～やすい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          easy to do ～
        </td>
      </tr>
      <tr class="row1" id="635">
        <td class="pos">
          635
        </td>
        <td class="kanji">
          やせる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to become thin, to lose weight
        </td>
      </tr>
      <tr class="row0" id="636">
        <td class="pos">
          636
        </td>
        <td class="kanji">
          やっと
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv
        </td>
        <td class="eng">
          at last, at length
        </td>
      </tr>
      <tr class="row1" id="637">
        <td class="pos">
          637
        </td>
        <td class="kanji">
          やはり/やっぱり
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adv,exp
        </td>
        <td class="eng">
          as I thought, absolutely
        </td>
      </tr>
      <tr class="row0" id="638">
        <td class="pos">
          638
        </td>
        <td class="kanji">
          やむ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v,vi
        </td>
        <td class="eng">
          to cease, to stop
        </td>
      </tr>
      <tr class="row1" id="639">
        <td class="pos">
          639
        </td>
        <td class="kanji">
          やめる
        </td>
        <td class="kanji">
          止める
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to end, to stop, to resign
        </td>
      </tr>
      <tr class="row0" id="640">
        <td class="pos">
          640
        </td>
        <td class="kanji">
          やる
        </td>
        <td class="kanji">
          
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          (col)to do
        </td>
      </tr>
      <tr class="row1" id="641">
        <td class="pos">
          641
        </td>
        <td class="kanji">
          やわらかい
        </td>
        <td class="kanji">
          柔らかい
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          soft, tender
        </td>
      </tr>
      <tr class="row0" id="642">
        <td class="pos">
          642
        </td>
        <td class="kanji">
          ゆ
        </td>
        <td class="kanji">
          湯
        </td>
        <td>
          n
        </td>
        <td class="eng">
          hot water
        </td>
      </tr>
      <tr class="row1" id="643">
        <td class="pos">
          643
        </td>
        <td class="kanji">
          ゆうはん
        </td>
        <td class="kanji">
          夕飯
        </td>
        <td>
          n
        </td>
        <td class="eng">
          evening meal
        </td>
      </tr>
      <tr class="row0" id="644">
        <td class="pos">
          644
        </td>
        <td class="kanji">
          ゆしゅつ・する
        </td>
        <td class="kanji">
          輸出
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          export
        </td>
      </tr>
      <tr class="row1" id="645">
        <td class="pos">
          645
        </td>
        <td class="kanji">
          ゆにゅう・する
        </td>
        <td class="kanji">
          輸入
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          import
        </td>
      </tr>
      <tr class="row0" id="646">
        <td class="pos">
          646
        </td>
        <td class="kanji">
          ゆび
        </td>
        <td class="kanji">
          指
        </td>
        <td>
          n
        </td>
        <td class="eng">
          finger
        </td>
      </tr>
      <tr class="row1" id="647">
        <td class="pos">
          647
        </td>
        <td class="kanji">
          ゆびわ
        </td>
        <td class="kanji">
          指輪
        </td>
        <td>
          n
        </td>
        <td class="eng">
          (finger) ring
        </td>
      </tr>
      <tr class="row0" id="648">
        <td class="pos">
          648
        </td>
        <td class="kanji">
          ゆめ
        </td>
        <td class="kanji">
          夢
        </td>
        <td>
          n
        </td>
        <td class="eng">
          dream
        </td>
      </tr>
      <tr class="row1" id="649">
        <td class="pos">
          649
        </td>
        <td class="kanji">
          ゆれる
        </td>
        <td class="kanji">
          揺れる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to shake, to sway
        </td>
      </tr>
      <tr class="row0" id="650">
        <td class="pos">
          650
        </td>
        <td class="kanji">
          よう
        </td>
        <td class="kanji">
          様
        </td>
        <td>
          adj-na
        </td>
        <td class="eng">
          way, manner, kind
        </td>
      </tr>
      <tr class="row1" id="651">
        <td class="pos">
          651
        </td>
        <td class="kanji">
          よう
        </td>
        <td class="kanji">
          用
        </td>
        <td>
          n,n-suf
        </td>
        <td class="eng">
          task, business, use
        </td>
      </tr>
      <tr class="row0" id="652">
        <td class="pos">
          652
        </td>
        <td class="kanji">
          ようい
        </td>
        <td class="kanji">
          用意
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          preparation
        </td>
      </tr>
      <tr class="row1" id="653">
        <td class="pos">
          653
        </td>
        <td class="kanji">
          ようじ
        </td>
        <td class="kanji">
          用事
        </td>
        <td>
          n
        </td>
        <td class="eng">
          tasks, chores
        </td>
      </tr>
      <tr class="row0" id="654">
        <td class="pos">
          654
        </td>
        <td class="kanji">
          よごれる
        </td>
        <td class="kanji">
          汚れる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to get dirty, to become dirty
        </td>
      </tr>
      <tr class="row1" id="655">
        <td class="pos">
          655
        </td>
        <td class="kanji">
          よしゅう
        </td>
        <td class="kanji">
          予習
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          preparation for a lesson
        </td>
      </tr>
      <tr class="row0" id="656">
        <td class="pos">
          656
        </td>
        <td class="kanji">
          よてい
        </td>
        <td class="kanji">
          予定
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          plans, arrangement, schedule
        </td>
      </tr>
      <tr class="row1" id="657">
        <td class="pos">
          657
        </td>
        <td class="kanji">
          よやく
        </td>
        <td class="kanji">
          予約
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          reservation, booking
        </td>
      </tr>
      <tr class="row0" id="658">
        <td class="pos">
          658
        </td>
        <td class="kanji">
          よる
        </td>
        <td class="kanji">
          寄る
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to visit, to drop in
        </td>
      </tr>
      <tr class="row1" id="659">
        <td class="pos">
          659
        </td>
        <td class="kanji">
          （～に）よると
        </td>
        <td class="kanji">
          
        </td>
        <td>
          
        </td>
        <td class="eng">
          according to ～
        </td>
      </tr>
      <tr class="row0" id="660">
        <td class="pos">
          660
        </td>
        <td class="kanji">
          よろこぶ
        </td>
        <td class="kanji">
          喜ぶ
        </td>
        <td>
          v5b
        </td>
        <td class="eng">
          to be delighted, to be glad
        </td>
      </tr>
      <tr class="row1" id="661">
        <td class="pos">
          661
        </td>
        <td class="kanji">
          よろしい
        </td>
        <td class="kanji">
          
        </td>
        <td>
          adj
        </td>
        <td class="eng">
          (hon) good, OK, all right
        </td>
      </tr>
      <tr class="row0" id="662">
        <td class="pos">
          662
        </td>
        <td class="kanji">
          りゆう
        </td>
        <td class="kanji">
          理由
        </td>
        <td>
          n
        </td>
        <td class="eng">
          reason, pretext, motive
        </td>
      </tr>
      <tr class="row1" id="663">
        <td class="pos">
          663
        </td>
        <td class="kanji">
          りよう
        </td>
        <td class="kanji">
          利用
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          use, utilization
        </td>
      </tr>
      <tr class="row0" id="664">
        <td class="pos">
          664
        </td>
        <td class="kanji">
          りょうほう
        </td>
        <td class="kanji">
          両方
        </td>
        <td>
          n
        </td>
        <td class="eng">
          both sides, both parties
        </td>
      </tr>
      <tr class="row1" id="665">
        <td class="pos">
          665
        </td>
        <td class="kanji">
          りょかん
        </td>
        <td class="kanji">
          旅館
        </td>
        <td>
          n
        </td>
        <td class="eng">
          Japanese hotel, inn
        </td>
      </tr>
      <tr class="row0" id="666">
        <td class="pos">
          666
        </td>
        <td class="kanji">
          るす
        </td>
        <td class="kanji">
          留守
        </td>
        <td>
          n
        </td>
        <td class="eng">
          absence, being away from home
        </td>
      </tr>
      <tr class="row1" id="667">
        <td class="pos">
          667
        </td>
        <td class="kanji">
          れいぼう
        </td>
        <td class="kanji">
          冷房
        </td>
        <td>
          n
        </td>
        <td class="eng">
          cooling, air conditioning
        </td>
      </tr>
      <tr class="row0" id="668">
        <td class="pos">
          668
        </td>
        <td class="kanji">
          れきし
        </td>
        <td class="kanji">
          歴史
        </td>
        <td>
          n
        </td>
        <td class="eng">
          history
        </td>
      </tr>
      <tr class="row1" id="669">
        <td class="pos">
          669
        </td>
        <td class="kanji">
          レジ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          register
        </td>
      </tr>
      <tr class="row0" id="670">
        <td class="pos">
          670
        </td>
        <td class="kanji">
          レポート/リポート
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          report, essay, assignment (aus)
        </td>
      </tr>
      <tr class="row1" id="671">
        <td class="pos">
          671
        </td>
        <td class="kanji">
          れんらく
        </td>
        <td class="kanji">
          連絡
        </td>
        <td>
          n,vs
        </td>
        <td class="eng">
          communication, contact, connection
        </td>
      </tr>
      <tr class="row0" id="672">
        <td class="pos">
          672
        </td>
        <td class="kanji">
          ワープロ
        </td>
        <td class="kanji">
          
        </td>
        <td>
          n
        </td>
        <td class="eng">
          word processor
        </td>
      </tr>
      <tr class="row1" id="673">
        <td class="pos">
          673
        </td>
        <td class="kanji">
          わかす
        </td>
        <td class="kanji">
          沸かす
        </td>
        <td>
          u-v,vt
        </td>
        <td class="eng">
          to boil, to heat
        </td>
      </tr>
      <tr class="row0" id="674">
        <td class="pos">
          674
        </td>
        <td class="kanji">
          わかれる
        </td>
        <td class="kanji">
          別れる
        </td>
        <td>
          ru-v
        </td>
        <td class="eng">
          to be divided, to part from, to separate
        </td>
      </tr>
      <tr class="row1" id="675">
        <td class="pos">
          675
        </td>
        <td class="kanji">
          わく
        </td>
        <td class="kanji">
          沸く
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to boil, to grow hot, to get excited
        </td>
      </tr>
      <tr class="row0" id="676">
        <td class="pos">
          676
        </td>
        <td class="kanji">
          わけ
        </td>
        <td class="kanji">
          訳
        </td>
        <td>
          n
        </td>
        <td class="eng">
          meaning, reason
        </td>
      </tr>
      <tr class="row1" id="677">
        <td class="pos">
          677
        </td>
        <td class="kanji">
          わすれもの
        </td>
        <td class="kanji">
          忘れ物
        </td>
        <td>
          n
        </td>
        <td class="eng">
          lost article, something forgotten
        </td>
      </tr>
      <tr class="row0" id="678">
        <td class="pos">
          678
        </td>
        <td class="kanji">
          わらう
        </td>
        <td class="kanji">
          笑う
        </td>
        <td>
          u-v
        </td>
        <td class="eng">
          to laugh, to smile
        </td>
      </tr>
      <tr class="row1" id="679">
        <td class="pos">
          679
        </td>
        <td class="kanji">
          わりあい
        </td>
        <td class="kanji">
          割合
        </td>
        <td>
          adv,n
        </td>
        <td class="eng">
          rate, ratio, percentage
        </td>
      </tr>
      <tr class="row0" id="680">
        <td class="pos">
          680
        </td>
        <td class="kanji">
          われる
        </td>
        <td class="kanji">
          割れる
        </td>
        <td>
          ru-v,vi
        </td>
        <td class="eng">
          to break
        </td>
      </tr>"""

# Парсим HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Ищем все строки таблицы
rows = soup.find_all('tr')

# Извлечение кандзи и каны
words = []
def detect_part_of_speech(line):
    stripped = line.strip().lower()
    tokens = [word.strip() for word in stripped.split(',') if word.strip()]

    if 'u-v' in tokens or 'ru-v' in tokens:
        return 'verb'
    elif len(tokens) == 1 and tokens[0] == 'n':
        return 'noun'
    elif 'adj' in tokens:
        return 'i-adjective'
    elif 'adj-na' in tokens:
        return 'na-adjective'
    elif 'adv' in tokens:
        return 'adverb'
    elif 'suf' in tokens:
        return 'suffix'
    elif 'num' in tokens:
        return 'counter'
    elif 'conj' in tokens:
        return 'conjunction'
    elif 'int' in tokens:
        return 'interjection'
    else:
        return None

for row in rows:
    columns = row.find_all('td')
    if len(columns) >= 5:
        kana = columns[1].get_text(strip=True)
        kanji = columns[2].get_text(strip=True)
        pos_raw = columns[3].get_text(strip=True)
        meaning_en = columns[4].get_text(strip=True)

        part_of_speech = detect_part_of_speech(pos_raw)
        words.append((kanji, kana, meaning_en, part_of_speech))

with open('kana_words_n4.txt', 'w', encoding='utf-8') as file:
    for kana in words:
        file.write(f"{kanji}\t{kana}\t{meaning_en}\t{part_of_speech}\n")

print("Данные сохранены в файл words_n4.txt")
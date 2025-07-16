import streamlit as st
import pandas as pd
import plotly.express as px

# エンコーディングを指定してCSVを読み込む
df = pd.read_csv('sanrio_2.csv', encoding='shift_jis')

st.title("サンリオキャラクター大賞")
st.subheader("これまでとこれから")
st.caption("サンリオキャラクター大賞のこれまでを知り、あなただけの推しを見つけましょう！")

st.markdown("---")
st.subheader("過去５年のサンリオキャラクター大賞の結果")
st.write("過去5年の1〜10位の推移を見てみましょう!")

if 'Year' in df.columns and 'Rank' in df.columns and 'Character' in df.columns:
    # 過去5年間の10位までのデータをフィルタリング
    top_10_df = df[df['Rank'] <= 10]
    
    # 年度ごとに表を分けて表示
    st.write("**年度ごとの順位表**")
    for year in sorted(top_10_df['Year'].unique()):
        year_df = top_10_df[top_10_df['Year'] == year]
        pivot_table = year_df.pivot(index='Year', columns='Rank', values='Character')
        st.write(f"{year}年の順位表:")
        st.dataframe(pivot_table)
    
    # 折れ線グラフを作成
    fig_line = px.line(
        top_10_df,
        x='Year',
        y='Rank',
        color='Character',
        title="過去5年間の10位までのキャラクターの順位推移（折れ線グラフ）",
        labels={'Year': '年', 'Rank': '順位', 'Character': 'キャラクター'}
    )
    fig_line.update_yaxes(autorange="reversed")  # Y軸を反転して順位が低いほど上に表示
    st.plotly_chart(fig_line)

    # キャラクター名の一覧を表示
    st.markdown("---")
    st.subheader("登場したキャラクターたち")
    characters = top_10_df['Character'].unique()
    selected_character = st.selectbox("気になったキャラクターを選択してください!", characters)

    # キャラクター画像とプロフィールデータを辞書で定義
    character_info = {
        "ポムポムプリン": {
            "image": "chara/pom.PNG",
            "introduction": """こげ茶色のベレー帽がトレードマークの、ゴールデンレトリバーの男のコ。
- のんびり屋で、好きな言葉は「おでかけ」、嫌いな言葉は「おるすばん」。
- くつ集めが趣味。飼い主のお父さんの革ぐつ、お母さんのサンダルなど、片っぽずつ、こっそり隠している。
- ミルクと、ふにゃふにゃしたものと、ママが作ったプリンが好き。
- 特技は、お昼寝とプリン体操、誰とでもなかよくなれちゃうこと。
- 将来の夢は、もっともっとおっきくなること。
- 飼い主のお姉さんの家の玄関にあるプリン用バスケットがお家。""",
            "quote": "「プリンが大好き！一緒に食べようね！」"
        },
        "シナモロール": {
            "image": "chara/sina.PNG",
            "introduction": """遠いお空の雲の上で生まれた、白いこいぬの男のコ。
- 「カフェ・シナモン」のお姉さんに見つけられ、そのままいっしょに住むことに。
- シッポがまるでシナモンロールのようにくるくる巻いているので、「シナモン」という名前をつけてもらう。
- 特技は、大きな耳をパタパタさせて、空を飛ぶこと。
- おとなしいけれど、とても人なつっこくて、お客さんのひざの上で寝ちゃうこともある。""",
            "quote": "「ふわふわの雲の上で一緒に遊ぼう！」"
        },
        "ポチャッコ": {
            "image": "chara/pocha.PNG",
            "introduction": """名前の由来は、ぽちゃぽちゃしているからポチャッコ。
- 好奇心旺盛でおっちょこちょいで、ちょっぴりおせっかい。
- より道お散歩が大好きなイヌの男のコ。
- 身長は、大好きなバナナアイスのラージサイズのカップ4個分。
- 体重は、ふわふわタウンのにんじん畑でたま〜にとれる、おばけニンジン3本分。
- 好きなお花は、れんげ草。友だちもい〜っぱい。""",
            "quote": "「一緒に散歩しよう！」"
        },
        "クロミ": {
            "image": "chara/kuro.PNG",
            "introduction": """クロミのプロフィール情報。
- 詳細は後日更新予定。""",
            "quote": "「いたずらしちゃうぞ！」"
        },
        "ハローキティ": {
            "image": "chara/hello.PNG",
            "introduction": """本名はキティ・ホワイト。生まれた場所はイギリス ロンドンの郊外。
- 身長はりんご５個分。体重はりんご３個分。
- 明るくてやさしい女のコ。クッキーを作ったりピアノを弾くのが大好き。
- 夢はピアニストか詩人になること。音楽と英語が得意。
- 好きな食べ物は、ママが作ったアップルパイ。
- 双子の妹、ミミィとは大のなかよし。""",
            "quote": "「アップルパイを一緒に食べましょう！」"
        },
        "マイメロディ": {
            "image": "chara/my.PNG",
            "introduction": """すなおで明るい、弟思いの女のコ。
- 宝物は、おばあちゃんが作ってくれた、かわいいずきん。
- お母さんといっしょにクッキーを焼くのが好き。
- 好きな食べ物は、アーモンドパウンドケーキ。""",
            "quote": "「一緒にクッキーを焼こう！」"
        },
        "リトルツインスターズ": {
            "image": "chara/little.PNG",
            "introduction": """ゆめ星雲の思いやり星でうまれたふたごのきょうだい星。
- お姉さんのララは、こわがりでちょっぴり泣き虫。絵や詩をかくのが大好きで特技はお料理。
- 弟のキキは好奇心旺盛。ちょっぴりあわてんぼうでいたずら好き。
- 星釣りと物を作ること（発明）が大好き。特技は背中の星で空を飛ぶこと。""",
            "quote": "「星空の冒険に出かけよう！」"
        },
        "ハンギョドン": {
            "image": "chara/hangyo.PNG",
            "introduction": """中国生まれの半魚人。
- 人を笑わせることが得意。でも実は、さびしがり屋のロマンチスト。
- いつもヒーローになりたがっているけど、なぜかうまくいかない。
- 好きなものは、冷やし中華、エビセン、鍋物、温泉。
- タコのさゆりちゃんとは、大のなかよし。""",
            "quote": "「笑顔が一番だよ！」"
        },
        "タキシードサム": {
            "image": "chara/taxi.PNG",
            "introduction": """南極のタキシードアイランドからやってきた、おしゃれなペンギンの男のコ。
- 食いしん坊で、ちょっぴりドジくん。
- 蝶ネクタイを365本も持ってる。
- 由緒ある家柄で、イギリス留学もしたことがある。英語もペラペラ。
- サムとそっくりな2人の弟、しっかりものの『パム』と甘えん坊の『タム』がいる。
- サムの大親友は、明るいアザラシの男のコ、『チップ』。""",
            "quote": "「おしゃれな蝶ネクタイを見てね！」"
        },
        "あひるのペックル": {
            "image": "chara/ahiru.PNG",
            "introduction": """おひとよしで、ココロのやさしい男のコ。
- 泳ぎが苦手で、歌とダンスが大好き。
- ピッチが手拍子をすると、つい踊ってしまう。ただ今、タップダンスのレッスン中！
- 宝物は、よく持ち歩いているバケツ。青、赤、グレーなど、いろいろな色がある。
- ピッチのプールにもなっちゃう。
- 夢は空を飛ぶこと。""",
            "quote": "「一緒にダンスしよう！」"
        },
        "けろけろけろっぴ": {
            "image": "chara/kero.PNG",
            "introduction": """冒険好きで、元気いっぱい！ドーナツ池の人気者。
- ころっぴ、ぴっきと、三つ子のきょうだい。
- カエル泳ぎは苦手で、クロールが得意。
- 歌が上手なカエルの男のコ。
- 家族は、「はすの上医院」のお医者さんのお父さん。
- レストランを開いている、料理が得意なお母さん。
- 美人で木登りと料理が好きな、お姉さんのぴっき。
- 努力家で機械いじりが趣味の、けろっぴそっくり、弟のころっぴ。
- ドーナツ池の島にある「けろけろハウス」に住んでいる。""",
            "quote": "「冒険に出かけよう！」"
        },
        "バッドばつ丸": {
            "image": "chara/bad.PNG",
            "introduction": """いたずら好きで、あまのじゃくなペンギンの男のコ。
- 好きな食べ物は、銀座の高級お寿司とポリパリラーメン。
- パパはコワモテだけど超楽天家、ママは超教育ママ。
- 悪役スターのブロマイドを集めている。
- 将来の夢は、社長になること。
- ひねくれ者に見えるけど本当はイイヤツ？""",
            "quote": "「悪役スターも悪くないよね！」"
        },
        "こぎみゅん": {
            "image": "chara/kogi.PNG",
            "introduction": """コギムーナ（小麦粉の精）のおんなのこ。
- 本当はおにぎりになりたいと思っているけれど、おにぎりがどんなものかは分かっていない。
- ちょっとしたことで散ってしまう、とてもとても儚い性格。
- おじいちゃんはコギムコーポの管理人で、今は旅をしているのでこぎみゅんが管理人代行中。""",
            "quote": "「儚いけど頑張るよ！」"
        },
        "SHOW BY ROCK!!": {
            "image": "chara/show.PNG",
            "introduction": """音楽を制する者が王として君臨する都市MIDICITY。
- この物語は、トップスターを夢見る少年少女達の音楽伝説である。
- 全宇宙のロッカーさん達の応援のおかげで2022年に10周年を迎えた。
- ありがとにゃん!!""",
            "quote": "「音楽で世界を変えよう！」"
        }
    }

    # キャラクターごとに色を定義
    character_colors = {
        "ポムポムプリン": "#FFD700",  # ゴールド
        "シナモロール": "#87CEEB",  # スカイブルー
        "ポチャッコ": "#FFB6C1",  # ライトピンク
        "クロミ": "#8A2BE2",  # パープル
        "ハローキティ": "#FF69B4",  # ホットピンク
        "マイメロディ": "#FFC0CB",  # ピンク
        "リトルツインスターズ": "#ADD8E6",  # ライトブルー
        "ハンギョドン": "#00CED1",  # ダークターコイズ
        "タキシードサム": "#4682B4",  # スチールブルー
        "あひるのペックル": "#FFFFE0",  # ライトイエロー
        "けろけろけろっぴ": "#98FB98",  # ペールグリーン
        "バッドばつ丸": "#696969",  # ブラック
        "こぎみゅん": "#F5DEB3",  # ウィート
        "SHOW BY ROCK!!": "#FF4500",  # オレンジレッド
    }

    # サイドバーに選択されたキャラクターの詳細を表示
    st.sidebar.title("キャラクターの詳細")

    if selected_character:
        # サイドバーの背景色を変更するCSSを適用
        sidebar_color = character_colors.get(selected_character, "#FFFFFF")  # デフォルトは白
        st.sidebar.markdown(
            f"""
            <style>
            [data-testid="stSidebar"] {{
                background-color: {sidebar_color};
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        character_details = top_10_df[top_10_df['Character'] == selected_character]
        st.sidebar.write(f"**選択されたキャラクター:** {selected_character}")
        st.sidebar.write("**これまでの順位**")
        st.sidebar.dataframe(character_details)
        
        # 画像とプロフィールを表示
        if selected_character in character_info:
            st.sidebar.image(character_info[selected_character]["image"], use_container_width=True)
            st.sidebar.write(f"**紹介:** {character_info[selected_character]['introduction']}")
            
            # キャラクターからの一言を表示（枠で囲む）
            st.markdown(
        f"""
        <div style="border: 2px solid {sidebar_color}; padding: 10px; border-radius: 10px; margin-top: 20px;">
            <h4 style="text-align: center; color: {sidebar_color};">{selected_character}からの一言:</h4>
            <p style="text-align: center;">{character_info[selected_character]['quote']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
            
            # 参照元をグレーの文字で表示
            st.sidebar.markdown(
                """
                <p style="color:gray; font-size:12px; text-align:center;">
                画像参照元: <a href="https://www.sanrio.co.jp/characters/" target="_blank" style="color:gray;">Sanrio公式サイト</a>
                </p>
                """,
                unsafe_allow_html=True
            )
        else:
            st.sidebar.write("画像や紹介情報が見つかりません。")
else:
    st.error("データに必要な列が含まれていません。'Year', 'Rank', 'Character'列を確認してください。")


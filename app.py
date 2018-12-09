from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
"""
やりたいこと
    キーワードプランナーAPIを呼び出す
    フォームに入力したキーワード、ボリュームから条件に合致する関連キーワードを取得
    関連キーワードの出力
    スプレッドシートに自動保存
"""


# @ デコレート
@app.route("/")
def search_volume():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def search_keywords():
    """
    入力されたキーワードを検索する関数
    """
    # フォームに入力されたデータを取得する
    keywords = request.form["keywords"]
    min_volume = request.form["min_volume"]
    max_volume = request.form["max_volume"]
    max_hit = request.form["max_hit"]

    # キーワードプランナーに情報を送信
    # 結果を取得

    # index()にリダイレクトする
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

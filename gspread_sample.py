import gspread

# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials


# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
def spread(datas):
    """スプレッドシートにデータを記述する関数"""
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # 認証情報設定
    # ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
    credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project keywords-168900eb1c81.json', scope)

    # OAuth2の資格情報を使用してGoogle APIにログインします。
    gc = gspread.authorize(credentials)

    # 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
    SPREADSHEET_KEY = '1rT8qZxf_ikcV_BpVrNaLeGs8eCUB22p3XZEYZ9n4WD4'

    # 共有設定したスプレッドシートのシート1を開く
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    line_numbers = list(range(2, 2 + len(datas)))

    for idx, num in enumerate(line_numbers):
        worksheet.update_cell(num, 2, datas[idx][0])
        worksheet.update_cell(num, 3, datas[idx][1])


if __name__ == "__main__":
    datas = [
        ["ブログ", "10000"],
        ["ゲーム", "23945"],
        ["記事", "333333"],
    ]

    spread(datas)

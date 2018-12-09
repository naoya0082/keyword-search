import gspread

# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
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

# A1セルの値を受け取る
# import_value = int(worksheet.acell('A1').value)

# A1セルの値に100加算した値をB1セルに表示させる
# export_value = import_value + 10000
# worksheet.update_cell(1, 2, export_value)

data = [
    ["ブログ", "10000"],
    ["ゲーム", "23945"],
    ["記事", "333333"],
]

# line = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# column = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]
# X = [0, 0, 1, 1, 2, 2]
# Y = [0, 1, 0, 1, 0, 1]
#
# print(line)
# print(column)
# print(data)
#
#
#
# for i in data:
#     pass
# for l in line:
#     pass
# for c in column:
#     pass
# for x in X:
#     pass
# for y in Y:
#     pass

# worksheet.update_cell(l, c, data[x][y])
worksheet.update_cell(2, 2, data[0][0])
worksheet.update_cell(2, 3, data[0][1])
worksheet.update_cell(3, 2, data[1][0])
worksheet.update_cell(3, 3, data[1][1])
worksheet.update_cell(4, 2, data[2][0])
worksheet.update_cell(4, 3, data[2][1])

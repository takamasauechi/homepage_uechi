import requests

# アプリのIDとシークレット
app_id = '1313426459625470'
app_secret = '5db836f788ca377ff18f294fbb472b15'

# アクセストークン取得用のURL
url = f'https://graph.facebook.com/oauth/access_token?client_id={app_id}&client_secret={app_secret}&grant_type=client_credentials'

# リクエストを送信してアクセストークンを取得
response = requests.get(url)
data = response.json()

# アクセストークンを出力
print("アクセストークン:", data['access_token'])
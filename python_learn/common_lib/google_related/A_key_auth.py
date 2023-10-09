# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client
from oauth2client.service_account import ServiceAccountCredentials

SCOPES_readonly = ['https://www.googleapis.com/auth/drive.metadata.readonly']
    # 下載需要用到 SCOPES_all
SCOPES_all = ['https://www.googleapis.com/auth/drive']
# SCOPES 可以在這裡查看 : https://developers.google.com/drive/api/guides/api-specific-auth?hl=zh-tw

# 取得金鑰(.json檔),有需要以後再做筆記

#這是憑證認證的標準作業
def get_authorize() :
    scope = SCOPES_all
    credentials = ServiceAccountCredentials.from_json_keyfile_name('stock-key.json', scope)
    return credentials


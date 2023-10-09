from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from A_key_auth import get_authorize

# download
import io
from googleapiclient.http import MediaIoBaseDownload

# upload
from googleapiclient.http import MediaFileUpload

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = get_authorize()

    try:
        DRIVE = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        page_token = None
        results = DRIVE.files().list(
            q = "mimeType='image/jpeg'",    # 搜尋條件
            # q = "parents='DIR-ID'",       # 只列出某個資料夾底下的檔案
            # spaces='domain',              # 搜尋範圍 尚未研究?? 有看 https://developers.google.com/drive/api/guides/about-files?hl=zh-tw#org 但是會跳錯
            pageSize=10,                    # 限制數量
            pageToken=page_token,           # 從第幾筆資料繼續搜尋
            fields="nextPageToken, files(id, name, mimeType, parents)" #限制回傳的欄位
        ).execute()

        # fields
            # permissions
            # nextPageToken
            # maxResults 
            
            # files
                # id : 每個檔案獨一無二
                # name : 檔案名稱
                # mimeType : 檔案種類 (folder, jpeg, spreadsheet)
                # parents : 上層資料夾
                # https://developers.google.com/drive/api/reference/rest/v3/files?hl=zh-tw#File

        # 資料有沒有取完 (可以透過更改 pageSize 測試)
            # 要注意因為連資料夾都會算個數，所以檔案數量蠻多的
            # 可以透過設定 q = 來減少檔案數量
        # 所以可以用 while True 迴圈取出全部資料
        page_token = results.get('nextPageToken', None)
        if page_token == None:
            print("資料已取完")
        else :
            print("資料尚未取完")
        
        download_id = ""
        # 印出全部檔案(資料夾自己會算一個)
        items = results.get('files', [])
        print('list just files')
        for item in items:
            print(f'{item["name"]}, id : {item["id"]}, {item["mimeType"]}, {item["parents"]}')
            if "jpeg" in item["mimeType"]:
                download_id = item["id"]
        print("-------------------------------------")

        # 下載檔案
        request = DRIVE.files().get_media(fileId=download_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')
        download_byte = file.getvalue()
        
        with open("./down.jpeg", "wb") as fw : 
            fw.write(download_byte)
            
        # # 上傳檔案 (會存到獲取 auth 的 email 的 drive 裡面)
        # file_metadata = {'name': 'upload.jpeg'}
        # # 把剛剛下載的檔案讀取進來上傳
        # media = MediaFileUpload('down.jpeg',
        #                         mimetype='image/jpeg')
        # file = DRIVE.files().create(body=file_metadata, media_body=media,
        #                               fields='id').execute()
        # print(F'File ID: {file.get("id")}')
        # print(dir(file))

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
if __name__ == '__main__':
    main()
    print("main execute finish")
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from A_key_auth import get_authorize

gauth = GoogleAuth()
gauth.credentials = get_authorize()
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    print(f'title: {file1["title"]}, id: {file1["id"]}')
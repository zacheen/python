from A_key_auth import get_authorize

def get_gspread_authorize():
    import gspread
    gc = gspread.authorize(get_authorize())
    return gc
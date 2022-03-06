
def judge_win(client_init, client_end, server_win):
    if client_init-client_end == server_win:
        return True
    elif client_init*10-client_end == server_win:
        return True
    elif client_init*100-client_end == server_win:
        return True
    elif client_init-client_end*10 == server_win:
        return True
    elif client_init-client_end*100 == server_win:
        return True
    elif client_init-client_end == server_win*10:
        return True
    elif client_init*10-client_end == server_win*10:
        return True
    elif client_init*100-client_end == server_win*10:
        return True
    elif client_init-client_end*10 == server_win*10:
        return True
    elif client_init-client_end*100 == server_win*10:
        return True
    elif client_init-client_end == server_win*100:
        return True
    elif client_init*10-client_end == server_win*100:
        return True
    elif client_init*100-client_end == server_win*100:
        return True
    elif client_init-client_end*10 == server_win*100:
        return True
    elif client_init-client_end*100 == server_win*100:
        return True
    else :  
        return False

if __name__ == '__main__' :
    print(judge_win(1000, 99, 1))
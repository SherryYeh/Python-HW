import signal
def exit(signal, frame):
    return
def main():
    signal.signal(signal.SIGINT,exit)
    try:
        account=input()
        secret=input()
        if(account=='test' and secret=='12345678'):
	        print("正確") 
        elif(account=='test' and secret!='12345678'):
            print("8碼以上")
    except:
        print("錯誤")	    
    print("保管密碼")
main()
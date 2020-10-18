#Мандатное управление доступом
login=None
pasw=None
users_login=["root","admin","user","guest","leo","new_user","Boris"]
users_pasw=["toor","123","1234","12345"]
users_mark=[0,1,2,5,3,4,5]
files=["Object 1","Object 2","Object 3","Object 4","Object 5","Object 6"]
files_mark=[0,5,4,3,5,1,2,2,0,3]
mark=["SU","OV","SS","S","DSP","NS"]
def Log_in():
    login=input("Enter your Login : \n")
    pasw=input("Enter your Password : \n")
    if Auth(login,pasw):
        Welcome(login)
        return login,pasw
    return None,None
def Auth(login,pasw):
    if (login in users_login):
        if (users_pasw[users_login.index(login)]==pasw):
            return True
    else:
        print("Invalid Login or Password\n")
        return False
def Welcome(login):
    print("\n")
    print("Identification was successful, welcome to the system!")
    PrintAccessFiles(login)
    print("\n")
def PrintAccessFiles(login):
    user_mark=users_mark[users_login.index(login)];
    print("You have access to files : \n")
    for mark_num in range(len(files_mark)):
        if user_mark<=files_mark[mark_num]:
            print(files[mark_num])
def CheckAccess(login,file_num):
    user_mark=users_mark[users_login.index(login)];
    file_mark=files_mark[file_num-1];
    if user_mark<=file_mark:
        return True
    else:
        return False
def Request(login):
    file_num=int(input("Enter the number of the file you want to access : \n"))
    if CheckAccess(login,file_num):
        print("Operation was successfully completed")
    else:
        print("Access denied. Not enough rights.")
def ChangeMarkUser(login):
    if users_mark[users_login.index(login)]==0 :
        login_change=input("Input user login : \n")
        new_mark=int(input("Input new mark : \n"))
        users_mark[users_login.index(login_change)]=new_mark
    else:
        print("Access denied. Not enough rights.")
def ChangeMarkFile(login):
    if users_mark[users_login.index(login)]==0 :
        file_change=int(input("Input file nimber : \n"))
        new_mark=int(input("Input new mark : \n"))
        files_mark[file_change-1]=new_mark
    else:
        print("Access denied. Not enough rights.")
def PrintRights(login):
    if users_mark[users_login.index(login)]==0 :
        print("\n")
        for user_id in range(len(users_login)):
            print(users_login[user_id]," - ",mark[users_mark[user_id]])
        print("\n")
        for file_id in range(len(files)):
            print(files[file_id]," - ",mark[files_mark[file_id]])
        print("\n")
    else:
        print("Access denied. Not enough rights.")
def Quit(login):
    print("\n")
    print(login," complete work. GoodBye!");
    print("\n")
    return None,None
command=""
while(command!="close"):
    if login==None:
        login,pasw=Log_in()
    command=input("Enter command : \n")
    if command=="quit":
        login,pasw=Quit(login);
    if command=="request":
        Request(login)
    if command=="chngmau":
        ChangeMarkUser(login)
    if command=="chngmf":
        ChangeMarkFile(login)
    if command=="right":
        PrintRights(login)

class User: 
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

def home(user):
    a = input("1.Register\n2.Login\n ")
    if(a == "1" or a == "Register"):
        register()
    elif(a == "2" or a == "login"):
        login(user)
    else:
        print("Choose a valid option")
        home('')

def register():
    n = input("Name: ")
    u = input("Username: ")
    p = input("Password: ")
    u = User(n, u, p)
    print("Welcome, " + u.name)
    home(u)

def login(user):
    l = input("Username: ")
    l2 = input("Password")
    if(l2 == user.password):
        print("Welcome, " + user.name)
        cinema() 
    else:
        print("Incorrect username or password")
        login(user)

def cinema():
    print("**********welcome to movie ticket booking:********** ")
    print("where you want to watch movie?:\n1.inox\n2.pvr\n3.santhi")
    th = int(input("choose your option: "))
    if th == 1:
     center()
    elif th == 2:
      center()
    elif th == 3:
      center()
    else:
     print("wrong choice")

def t_movie():
    global booktik
    booktik = 0
    booktik = booktik+1
    print("which movie do you want to watch?\n1.BEAST\n2.RRR\n3.VIKRAM\n4.back")
    movie = int(input("choose your movie: "))
    if movie == 4:
     center()
     theater()
     return 0
    if booktik == 1:
      theater()

def theater():
    print("which Screen do you want to watch movie:\n1.Screen 1\n2.Screen 2\n3.Screen 3 ")
    a = int(input("choose your Screen: "))
    ticket = int(input("number of ticket do you want?: "))
    print(str(ticket)+"  ticket booked successfully")
   

def center():
    print("Select seat Sliver-Gold-Platinam \n1.Sliver\n2.Gold\n3.platinum")
    print("4.back")
    a = int(input("choose your option: "))
    movie(a)
    return 0

def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        cinema()
    else:
        print("wrong choice")

home('')


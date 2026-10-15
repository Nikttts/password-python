def checklogin(username, password):
    if username == "me" and password == "me123":
        print("Welcome")
        return True     
    else:
        print("invalid password or username")
        return False  

while True:
    username = input("enter your username : ")
    password = input("enter your password : ")
    
    if checklogin(username, password):
        break
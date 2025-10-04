username = "admin"
password = 1234
count = 0
while count < 3 :
    user = input("enter your username " )
    passw = input("enter your password " )
    if(user == username and passw == str(password)):
        print(" login successfull")
        break
else :
    print ("wrong username or password")
    count += 1
    if count == 3 :
        print (" account locked ")
        exit()
        n = int(input("enter a number n"))
        for num in range (2,n+1):
            for i in range (2 , num):
                if num % i == 0:
                    break
            else:
                print (num)
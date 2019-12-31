# health management system
# 3 client saurabh,suraj,harshul
# take input as an in lock and retireve

print("Welcome!! This is Health Mangement system")
print("1-Suraj\n 2-Sauarbh\n,3-Harshul\n")
client_input=input("choose the client")
client_action=int(input("enter 1 for lock and enter 2 for retreving the data"))
client_request=input("for the food or the excercise\n tip-you can write f for the food and ex for the excercise")
def gettime():
    import datetime
    date=datetime.datetime.now()
    return date
def food():
    data = input("enter the food")
    return data
def excercise():
    data=input("enter the excercise")
    return data
def data_lock(filename):
    print("you choose tht option lock")
    with open(filename,"a+") as f:
        content=f.write(str([str(gettime())])+" "+food())
        return content

def data_lock1(filename):
    print("you choose tht option lock")
    with open(filename,"a+") as f:
        content=f.write(str([str(gettime())])+" "+excercise())
        return content

def data_retrive(filename):
    print("you choose the option data retrieve")
    with open(filename) as f:
        data=print(f.read())
        return data
if client_input=="Suraj" or "suraj":
    if client_request=="f":
        while(1):
            y=""
            n=""
            if client_action==1:
                lock=data_lock("suraj"+".txt")
                print("data updated successfully!!")
            elif client_action==2:
                retrive=data_retrive("suraj"+".txt")
                print(retrive)
            still_continue=input("you want to see it again?")
            if still_continue=="y":
                client_action = int(input("enter 1 for lock and enter 2 for retreving the data"))
                continue
            elif still_continue=="n":
                break
    if client_request=="ex":
        while(1):
            y = ""
            n = ""
            if client_action == 1:
                lock = data_lock1("surajex" + ".txt")
                print("data updated successfully!!")
            elif client_action == 2:
                retrive = data_retrive("surajex" + ".txt")
                print(retrive)
            still_continue = input("you want to see it again?")
            if still_continue == "y":
                client_action = int(input("enter 1 for lock and enter 2 for retreving the data"))
                continue
            elif still_continue == "n":
                break
if client_input=="Saurabh" or "saurabh":
    if client_request=="f":
        while(1):
            y=""
            n=""
            if client_action==1:
                lock=data_lock("saurabh"+".txt")
                print("data updated successfully!!")
            elif client_action==2:
                retrive=data_retrive("saurabh"+".txt")
                print(retrive)
            still_continue=input("you want to see it again?")
            if still_continue=="y":
                client_action = int(input("enter 1 for lock and enter 2 for retreving the data"))
                continue
            elif still_continue=="n":
                break

    if client_request == "ex":
        while (1):
            y = ""
            n = ""
            if client_action == 1:
                lock = data_lock1("saurabhex" + ".txt")
                print("data updated successfully!!")
            elif client_action == 2:
                retrive = data_retrive("saurabhex" + ".txt")
                print(retrive)
            still_continue = input("you want to see it again?")
            if still_continue == "y":
                client_action = int(input("enter 1 for lock and enter 2 for retreving the data"))
                continue
            elif still_continue == "n":
                break
if client_input=="Harshul" or "harshul":
    if client_request=="f":
        while(1):
            y=""
            n=""
            if client_action==1:
                lock=data_lock("harshul"+".txt")
                print("data updated successfully!!")
            elif client_action==2:
                retrive=data_retrive("harshul"+".txt")
                print(retrive)
            still_continue=input("you want to see it again?")
            if still_continue=="y":
                client_action = int(input("enter 1 for lock and enter 2 for retreving the data"))
                continue
            elif still_continue=="n":
                break
    if client_request == "ex":
        while (1):
            y = ""
            n = ""
            if client_action == 1:
                lock = data_lock1("harshulex" + ".txt")
                print("data updated successfully!!")
            elif client_action == 2:
                retrive = data_retrive("harshulex" + ".txt")
                print(retrive)
            still_continue = input("you want to see it again?")
            if still_continue == "y":
                client_action = int(input("enter 1 for lock and enter 2 for retreving the data"))
                continue
            elif still_continue == "n":
                break







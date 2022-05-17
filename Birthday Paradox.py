import random

T = 100000 #simulation times

print ("How many birthdays shall I generate? (Max 100)")
No = input ()

while not No.isdecimal() or int(No) > 100 or int(No) < 0:
    print ("The birthdays should be integer and between 0 to 100")
    No = input ()

def main():
    Days = int(No)
    Birthday = []

    # random select Birthday
    for i in range (Days):
        Month = ["Jan ","Feb ","Mar ","April ",
                "May ","June ","July ","Aug ",
                "Sep ","Oct ","Nov ","Dec "]

        Month = Month [random.randint (0,11)]

        if Month == "Jan " or "Mar " or "May " or "July " or "Aug " or "Oct " or "Dec ":
            Day = random.randint (1,31)
        elif Month == "April " or "June " or "Sep " or "Nov ":
            Day = random.randint (1,30)
        elif Month == "Feb ":
            Day = random.randint (1,28)

        Birthday.append("{}".format(Month) + "{}".format(Day)) #save birthday in list

    # if there are same birthday, it would return 1 otherwise 0
    count = 0
    for j in range(len(Birthday)):
        for k in range(j + 1, len(Birthday)):
            if Birthday[j] == Birthday[k]:
                count = count + 1
            else :

                count = count + 0
    if count > 0 :
        count = 1
    elif count == 0 :
        count = 0
    return count

Days = int(No)
Birthday = []
for i in range (Days):
    Month = ["Jan ","Feb ","Mar ","April ",
            "May ","June ","July ","Aug ",
            "Sep ","Oct ","Nov ","Dec "]

    Month = Month [random.randint (0,11)]

    if Month == "Jan " or "Mar " or "May " or "July " or "Aug " or "Oct " or "Dec ":
        Day = random.randint (1,31)
    elif Month == "April " or "June " or "Sep " or "Nov ":
        Day = random.randint (1,30)
    elif Month == "Feb ":
        Day = random.randint (1,28)

    print ("{}".format(Month) + "{}".format(Day))

    Birthday.append("{}".format(Month) + "{}".format(Day))
print (Birthday)

for j in range(len(Birthday)):
    for k in range(j + 1, len(Birthday)):
        if Birthday[j] == Birthday[k]:
            print ("In this simulation, multiple people have a birthday on " + Birthday[j])
        else:
            print ("In this simulation, no people have same birthday")

NoOfSame = 0 #No of same birthday in the simulation
print ("Generating {}".format(No) + "random birthdays {} ".format(T) + "times..." + \
        "Press Enter to begin...")
Enter = input()
if Enter == "":
    print ("Let's run another {} ".format(T) + "simulations.")
    for L in range (T):
        NoOfSame = NoOfSame + main()
        if L == 0:
            print ("0 simulations run...")
        elif L == 10000:
            print ("10000 simulations run...")
        elif L == T:
            print ("{} simulations run.".format(T))

precent = (NoOfSame*100)/T
print ("Out of {} ".format(T) + "simulations of {} people, there was a ".format(No) + \
        "matching birthday in that group {} times. This means ".format(NoOfSame) + \
        "that {} people have a ".format(No) + "{} % chance of".format(precent) + \
        "having a matching birthday in their group." + \
        "That's probably more than you would think!")

years = int(input("How many years would you like to have? "))

spendingmoneylist = []
spentmoneylist = []

for i in range(1, years+1):
    spendingmoney = float(input("How much money is allowed to be spent in year " + str(i) + "?  "))
    spentmoney = float(input("How much money was spent in year " + str(i) + "?  "))
    spendingmoneylist.append(spendingmoney)
    spentmoneylist.append(spentmoney)

spendindex = 0
spentindex = 0

for i in range (len(spentmoneylist)):
    print('\n')
    if spentmoneylist[spentindex] > spendingmoneylist[spendindex]:
        print("In year ", spendindex+1, ", there was a deficit of ", spentmoneylist[spentindex]-spendingmoneylist[spendindex], ". ")
    if spentmoneylist[spentindex] < spendingmoneylist[spendindex]:
        print("In year ", spendindex + 1, ", there was a surplus of ", spendingmoneylist[spendindex]-spentmoneylist[spentindex], ". ")
    if spentmoneylist[spentindex] == spendingmoneylist[spendindex]:
        print("In year ", spendindex + 1, ", there was no surplus or deficit.")
    spendindex = spendindex + 1
    spentindex = spentindex + 1


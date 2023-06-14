x=input("How many items would you like to add to your list (positive integer)")
fruitlist = []
bag = 0
for i in range (1,int(x)+1):
    y=input("input item " + str(i) + "  ")
    fruitlist.append(y)
print(fruitlist)
w=input("What would you like to search for in the list?")
if w in fruitlist:
    print("Your item is in the list. This is the position in the list that your item is in. (starts at 0)")
    for j in range (0, int(x)):
        if w in fruitlist[j]:
            print(w, "is in the list at", j, "position")
else:
    print(w, "is not in the  list")
    e=input("Would you like to add your item to the list? (type '1' for yes, '2' for no)")
    if int(e)==1:
        fruitlist.append(w)
        print("This is your new list:")
        print(fruitlist)
    else:
        print("The End")
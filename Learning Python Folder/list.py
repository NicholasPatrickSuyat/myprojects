mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

#If index is too large for example [4] it will show an error because there are no 4th option on the list
item =  mylist[0]
print(item)

#if the "" is in the list it will automatically print yes otherwise, it will print no
if "banana" in mylist:
    print("yes")
else:
    print("no")

#if you put len infront of the list, it will show you how many list you have
print(len(mylist))

#if you want to add something in the list put .append on the input's name 
mylist.append("lemon")
print(mylist)

#if you want to add something in a specific order add the order number
mylist.insert(1, "blueberry")
print(mylist)

#if you want to remove something in your list .pop or .remove, clear(if remove everything)
item = mylist.pop(0)
print(item)
print(mylist)

#if you want to sort a number
mylist3 = [3, 6, -2, 0, 5]
mylist3.sort()
print(mylist3)
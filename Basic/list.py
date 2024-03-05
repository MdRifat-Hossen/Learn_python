# mylist=["apple","Rifat","Habib"]
# print(mylist)
# print(len(mylist))
# lis1=["1","2","3",'4']
# list2=[True,False,True]
# print(lis1)
# print(list2)
# #print(lis1)
# print(type(list2))

#------------------#
#Accesses of list item
list1=["1",'2','3','5']
print(list1[-1])
#list rang of the index
print(list1[0:3])
#list of spcific
print(list1[:3])

#cheack item is exits
#ckange the list item
list1[2]="8"
print(list1)
#chang range of the item value
list1[0:3]=["Rifat","habib","mijan"]
print(list1)

#insert a item any position
list1.insert(2,"Shamim")
print(list1)

#insert at end using append( function)
list1.append("Noma")
print(list1)
list1.insert(0,"Md")
print(list1)

#one list to other list transfer usingg extend(function)
lis2=["1","2","3"]
lis2.extend(list1)
print(lis2)
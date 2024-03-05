# age=int(input("Enther a integer number :"))
# if age<=18:
#     print("He is adoult")
# elif age==18:
#     print("pure age")
# elif ((age>18) or (age<19)):
#     grade=age-5
#     print("got {} grade".format(grade))
# else:
#     print("goto colloge")

# import random as r
# rand_num=r.randrange(1,20)
# print("Number is guess : ",rand_num)
# i=1
# while True:
#     print("Guess number: ",i)
#     if i==rand_num:
#         print("rand number hasbeen sunccefuly")
#         break
#     i+=1

for i in range(1,23):
    if i%2==0:
        continue
    print(i)
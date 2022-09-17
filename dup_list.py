#remove duplicate from a list

list1 = [1,1,2,2,3,4,'a','b','a','b']
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
               
print(list1)
print(list2)


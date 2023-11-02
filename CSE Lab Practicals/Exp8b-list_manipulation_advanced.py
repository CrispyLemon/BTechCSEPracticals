
u = lambda x: x+1
list1 = [1,2,3,4]
print(list1)
list2 = list(map(u, list1))
print(list2)
def lester(x):
    if x<18:
        return False
    else:
        return True
    
list3 = [17,23,54,20,1,32,4,7,9,22]
list4 = list(filter(lester, list3))
print(list3)
print(list4)

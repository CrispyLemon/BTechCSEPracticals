#perform various operations on lists (eg. slicing, sorting, pop, reverse, etc.)

#list of numbers
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

#slicing
print(list1[2:5])

#sorting
#defining sort functions
def sort(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if(list1[i]>list1[j]):
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    return list1

#calling sort function
list1 = sort(list1)
print(list1)

#pop
list1.pop()

#reverse
list1.reverse()

#displaying list
print(list1)

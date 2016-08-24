#define function to sort the list, pass in one parameter (the list to be sorted)
def sortFunc (aList):
#iterate through the list using range() to get the length of the list minus one (which will be the item we are sorting currently). Minus the list length by 1 on each iteration so we are comparing only the numbers which have not been sorted already.
    for p in range(len(aList)-1,0,-1):
#nested for loop to take the list item output in the outer loop and check if the item is greater than the item just after it
        for i in range(p):
            if myList[i]>aList[i+1]:
#if the item is greate than the one just after it, switch the two items
                aList[i], aList[i+1] = aList[i+1], aList[i]

#make a list to be sorted               
myList = [89, 23, 33, 45, 10, 12, 45, 45, 45]

#call the sort function and pass the list as a parameter
sortFunc(myList)

#print out the newly sorted list
print(myList)

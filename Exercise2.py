#alist is the list of numbers being added to the function called afunction

alist = [-8,-5,-3,-1,0,3,6,8,12]
def afunction(alist):

#If function made to check to see if list is actually a list, and return an TypeError
#if the if function detected something other than a list.

    if  type(alist) != list:
        raise TypeError

    print "Here are the numbers in the list"

#Prints out what numbers were found in the function: list

    for x in alist:
        print (x)

    #Prints out the total amount of values inside of alist

    print ("There are " + str(len(alist)) + " numbers in this list")

    #variable made to hold the amount of numbers greater than -1
    count = 0

    #For loop created to detect the value held in list, and if greater than -1
    #add +1 to the variable count. At the end, count holds the amount of numbers
    #detected greater than -1

    for x in alist:
        if x > -1:
            count += 1
    print "There are " + str(count) +  " positive numbers in this list"


#End of function

afunction(alist)

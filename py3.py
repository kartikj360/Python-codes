# DONE BY 3932 KARTIK JOSHI
# QUESTION NO.2

# FUNCTION TO CALCULATE THE LIST OF MULTIPLE
def mtpl():  # FUNCTION DEFINATION

    list1 = []  # FIRST LIST
    # INPUT===============================================================

    # TAKING THE NUMBER OF ELEMENTS FROM THE USER
    num = int(input("Enter the number of elements: "))

    # INPUT END==========================================================

    # PROCESSING=========================================================

    for i in range(1, num+1):
        list2 = []  # USING SECOND LIST TO STORE
        for j in range(1, 6):
            list2.append(j*i)  # MULTIPLYING AND APPENDING TO THE LIST
        list1.append(list2)  # APPENDING THE 2ND LIST TO THE 1ST ONE
    return list1  # RETURNING THE THE 1ST LIST TO THE MAIN

    # PROCESSING END======================================================

# OUTPIT==================================================================

LIST3=mtpl()  #CALLING THE FUCTION AND STORING THE VALUE INTO THE LIST
print(*LIST3) #PRINTING THE LIST AND DEREFRENCING IT SO THAT EXTRA PAIR OF BRACKET DON'T SHOW 

# OUTPUT END==============================================================

# DONE BY 3932 KARTIK JOSHI
# QUESTION NO.1

# PROCESSING=================================================================================================
# TO CALCULATE THE REMARK AND COMMISION OF EACH SALESMEN
def check_com(sale, num):
    # LIST TO RETURN THE VALUE OF REMARK AND COMMISION
    mark, com, sales = [], [], []
    for i in sale:
        tot_sal = 0
        for j in i:
            tot_sal += j

        sales.append(tot_sal)

        # MONTH IS COUNTED AS 28 DAY IN
        if(tot_sal >= 50000):
            # CALUCULATION THE COMMISION IF THE SALES ARE GREATER THEN 50000,BY RESULTING THE PRODUCT OF SALES INTO 0.05
            com.append(0.05 * tot_sal)
        else:
            com.append(0)

        # CALCULATION OF THE REMARK OF EACH SALESMEN
        if(tot_sal >= 80000):
            mark.append("EXECELENT ;)")
        elif(tot_sal >= 60000):
            mark.append("GOOD  :)")
        elif(tot_sal >= 60000):
            mark.append("AVERAGE...")
        else:
            mark.append("WORK HARD..!!")

    return mark, com, sales

# PROCESSING END=============================================================================================


# INPUT======================================================================================================

# NUMBER OF SALESMEN
num = int(input("ENTER NUMBER OF SALESMEN  :  "))

# TAKING THE DATA OF EVERY WEEK FOR PER SALESMEN
sale = []

for i in range(1, num+1):
    i1 = []
    for j in range(1, 5):
        j1 = int(input("NUMBER OF SALESMEN:  " + (str)
                 (i) + " OF " + " WEEK NUMBER " + (str)(j) + " :  "))
        i1.append(j1)
    sale.append(i1)
    print("\n")

# CALLING FUNCTION TO GET THE REMARK AND COMMISION OF EVERY SALES MAN
mark, com, sales = check_com(sale, num)
# INPUT END===================================================================================================

# OUTPUT =====================================================================================================

print("\n\n" + " HERE IS YOUR REQUIRED DATA \n")


for i in range(0, len(mark)):

    print("TOTAL SALES BY THE SALESMEN IS ", i+1, " IS:  ", sales[i])
    print("COMMSION OF SALESMEN  ", i+1, " IS :  ", com[i])
    print("REMARK OF SALESMEN ", i+1, " IS:  ", mark[i])

    print("\n")
# OUTPUT=======================================================================================================

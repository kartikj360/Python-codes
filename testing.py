# # 
# # 

# # zoo_animals=['kartik','harshit','1','#',' ','   ','hrishab','naman']
# # print(len(zoo_animals[1]))

# # for i in zoo_animals:
# #     print(i*len(zoo_animals[1]))
    
# # zoo_animals.sort()
# # print(zoo_animals)     
# # animals=[]    
# # print("kartik"*2) 

# # for j in zoo_animals:
# #     animals.append(j*2)  
# #     animals.append(' ')  
    
# #     animals.sort()
# # print(animals)     

# zo_no={345:100,45:200,65:300}

# for x in zo_no:
#     print(zo_no[x])
# # zo_no.sort()
# print(zo_no)
# del zo_no[345]
# print(zo_no)
# multio={1:1,2:2,3:3,4:4}
# for y and i in zo_no:
#       print(zo_no[y]*multio[i])

# list1=[1,23,34,55]
# # list2=str()
# print(''.join(list1))
from random import randint
randrow=0
randcol=0
board=[]
for i in range(5):
    board.append(['O']*5)
    
def printbd(board):
    for i in board:
        print("-".join(i))    
print board,


printbd(board)    
randrow=randint(0,4)
randcol=randint(0,4)
print("\n\n")
# print(printbd(randset(board)))'
guess=4;result=0
while guess>0 and result==0:
    b=int(input("Enter the row to be guess(between 0 to 4) "))
    a=int(input("Enter the column to be guess(between 0 to 4) "))

    if  board[a][b]=='X':
             print("You have already striked over that location!!")
             guess-=1
    elif a==randcol and b==randrow  :
                print("You sank my ship..YAY!!")
                board[randrow][randcol]='hidden'
                print(printbd(board))
                break
    elif a not in range(5) and b not in range(5):
        print("You have entered out of battle space!!")    
        guess-=1
    
    else:
                print("You made a wrong guess")
                print(randrow)
                print(randcol)
                board[b][a]='X'
                printbd(board)
                print("Give one more try")
                guess-=1
else:
    print("Game over my dear!!")         
         
# c=-1
# while c<0:
#         c=float(c-1123265873847348)
#         print(c)
       
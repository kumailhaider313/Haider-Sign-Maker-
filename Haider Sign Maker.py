print("Hello! Wellcome to Haider Sign Maker. We would be happy to help you.")

#Client information
name = input("Whats your name?\n")
budget = int(input("So," + name +" ! Whats your budget\nRs= "))
size_h = int(input("Please, enter the size of board in feets\nHeigth= "))
size_w = int(input("Weidth= "))
size = size_h*size_w

#Board prefer according to budget
board = ["Flex", 500, "Acrylic", 1000, "Neon sign", 1500, "3D LED", 2000]
if budget>=(size*board[1]):
    print("May I know what type of signboard you need? According to your budget we prefer you:")
    for n in range(0,8,2):
        if budget>=(size * board[(n+1)]):
            print(board[n])
        else:
            break  
else:
    print("Sorry, you have very low budget.")
    exit()

order = input("Please Enter your choice: ")

#flex with light condition
if order == board[0] and budget >= (size * 700):
    flex_choice = input("Great choice! Do you want a flex with light (it will cost Rs:200 more per sq inch)\ny/n\n")
    if flex_choice == "y":
        board[1]=700

price=0
#price calculation
for a in range(0,6,2):
    if order == board[a]:
        price = size * board[(a+1)]
        break

#convertiog flex into flex with light
if board[1] == 700:
    order = "Flex with light"

#summing up the whole deal
print("So, " + name + "! your board size is " + str(size_h) + " X " + str(size_w) + " and you selected " + order + " board.\nThis project will complete in 7 days after the design is approved.\nTotal cost will be Rs: " + str(price))
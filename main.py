from Property import Property
from Player import Player
import time
from random import randint
import os
from MainBoard import Board_main

print("!!!!!!!!!!!!!...Welcome to the Game of Monopoly...!!!!!!!!!!!!!")

playersList = []
players_Count = 2
playersList.append(Player(input("Please enter Player 1 Name : ")))
playersList.append(Player(input("Please enter Player 2 Name : ")))
players_Chance = 0


while (True):
    time.sleep(1)
    player = playersList[players_Chance % 2]
    print(player.playerName + "                                 " + str(player.playerCash))
    if(player.bankrupt==True):
        print("You have no money left. Balance = $" + str(
            player.playerCash))
        
        print("\n1.   If you want to exit the game, Press 1\n")
        print("2.   If you want to sell the property, Press 2\n")
        choice = int(input())
        if choice == 1:
            print("The Winner of The Game is "+ playersList[players_Chance+1]%2)
            break

        elif choice == 2:
            player.stringProperties()
            choice = int(input("Select The Property You want Sell"))
            propertyChoice=player.getProperty(choice)
            print("Starting bid value is $"+ str(propertyChoice.propertyCost*0.7))
            print(playersList[(players_Chance+1)%2].playerName+" Do You wish to bid for the Property.\nEnter Y to place the bid else N to pass the turn")
            sellChoice=input("")
            if sellChoice=='Y':
                bid=int(input("Enter your bid amount"))
                propertyChoice.propertyOwner=(players_Chance+1)%2
                player.playerCash+=bid
                player.collateralsOwned-=propertyChoice.propertyCost
                propertyChoice.propertyOwner=(players_Chance+1)%2
            else:
                player.playerCash += propertyChoice.propertyCost*0.7
                player.collateralsOwned -= propertyChoice.propertyCost
                propertyChoice.propertyOwner = None
                propertyChoice.propertyPurchased = False

        else:
            continue

    if (player.jail):
        print("You have reached JAIL.....You will have to miss the next turn")
        player.jail = False

    print("Now we are rolling the dice")
    die = randint(1, 6)
    time.sleep(1)
    print("Dice Rolled to  " + str(die))
    player.setBoardPositon(die)
    boardState = Board_main.Board[player.boardPosition]
    print(boardState)
    if (boardState == "GO"):
        # A Bonus of 250 Given to Player
        print("You have reached the start point. Please collect your start bonus of $250")
        player.creditMoney(250)

    elif (boardState == "Property"):
        property_Instance = Board_main.Properties[player.boardPosition]
        print("You have reached "+ property_Instance.propertyName)
        if (property_Instance.propertyPurchased):
            if(property_Instance.propertyOwner == players_Chance%2):
                property_Instance.ownerOfProperty(player)
            else:
                print("You Have landed on another player's property. Please pay rent of $"+str(property_Instance.propertyRent))
                player.deductMoney((property_Instance.propertyRent))
                playersList[(players_Chance+1)%2].creditMoney(property_Instance.propertyRent)

        else:
            print("Do you want to buy the property of  $" + str(property_Instance.propertyCost)+"\nEnter Y to buy the property else N to pass the turn")
            bychoice=input()
            if(bychoice=='Y'):
                player.purchaseProperty(property_Instance,players_Chance%2)
            else:
                continue

    elif (boardState == "CommunityChest"):

        ccType = Board_main.CommunityChest[player.boardPosition]
        print("You have Landed on Community Chest")
        time.sleep(1)
        if ccType == "Collect 200":
            print("You have Won $200")
            player.creditMoney(200)
        elif ccType == "FINE 200":
            print("You have been fined 200$")
            player.deductMoney(200)
        elif ccType == "Collect 100":
            print("You have Won $100")
            player.creditMoney(100)
        elif ccType == "FINE 350":
            print("You have been fined 350$")
            player.deductMoney(350)
        else:
            print("You have Won $500")
            player.creditMoney((500))


    elif (boardState == "Jail"):
        player.jail = True
        print("You have landed in Jail and have been fined of $100")
        player.deductMoney(100)


    elif (boardState == "Lounge Area"):
        print("You have Landed on Lounge Area pay a $50 and chill for a while :)")
        player.deductMoney(50)

    elif(boardState == "TAX"):
        typeTax = Board_main.TAX[player.boardPosition]
        if typeTax == "Hotel Tax":
            print("You have to pay HOTEL TAX")
            taxToBePayed = player.hotelsPurchased*25
            print("Amount to be payed is $" + str(taxToBePayed))
            player.deductMoney(taxToBePayed)
            print("$" + str(taxToBePayed) + "  is Deducted ")

        elif typeTax == "Water Tax":
            print("You have to pay WATER TAX")
            taxToBePayed = 25
            print("Amount to be payed is $" + str(taxToBePayed))
            player.deductMoney(taxToBePayed)
            print("$" + str(taxToBePayed) + "  is Deducted ")

        else:
            taxToBePayed = player.incomeTax()
            print("You have to pay INCOME TAX")
            time.sleep(1)
            print("Amount to be payed is $" + str(taxToBePayed))
            player.deductMoney(taxToBePayed)
            print("$" + str(taxToBePayed) + "  is Deducted ")
    players_Chance += 1

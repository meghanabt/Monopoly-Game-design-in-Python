class Property:
    def __init__(self,name,cost,rent):
        self.propertyName = name
        self.propertyCost = cost
        self.propertyRent = rent
        self.propertyOwner = None
        self.hotelExist = False
        self.propertyPurchased = False      

    def ownProperty(self,playerInstance):
        self.playerInstance=playerInstance
        
        print("You own the property so need to pay a service Charge of $" + str(25))
        self.playerInstance.deductMoney(25)
        if (self.hotelExist == False):
            print("Do You wish to Build an Hotel. Enter Y to buy the hotel and N to pass the turn")
            hotelchoice = input()
            if (hotelchoice == 'Y'):
                self.playerInstance.deductMoney(100)
                self.constructHotel()
                self.propertyCost+=100
                self.playerInstance.collateralsOwned += 100
                self.playerInstance.hotelsPurchased += 1
                self.hotelExist=True
    
    def constructHotel(self):
        self.hotelExist=True
        self.propertyRent+=50
        self.propertyCost+=100
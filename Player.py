 from property import Property

class Player:
    def __init__(self,name):
        self.playerName = name
        self.playerCash = 2000
        self.bankrupt = False
        self.boardPosition = 0
        self.hotelsPurchased = 0
        self.collateralsOwned = 0
        self.assetsList = []
        self.playerId = None        
        self.jail = False
       

    def deductMoney(self,amount):
        if(self.playerCash<=100):
            self.statusBankrupcy()
        self.playerCash-=amount
    
    def getProperty(self,choice):
        PropertyInstatnce=self.assetsList.pop(choice)
        return PropertyInstatnce

    def purchaseProperty(self, PropertyObj, playerTurn):
        self.assetsList.append(PropertyObj)
        PropertyObj.owned=True
        PropertyObj.ownedBy = playerTurn
        print("Deducting the property value from balance")
        self.deductMoney(PropertyObj.cost)
        self.collateralsOwned+=PropertyObj.cost
        print("Thankyou for buying the property")

    def creditMoney(self,credit):
        self.playerCash+=credit
    def incomeTax(self):
        return self.collateralsOwned*0.1

    def setBoardPositon(self,pos):
        self.boardPosition+=pos
        if self.boardPosition>15:
            self.boardPosition%=16
    def evaluateMaintanance(self):
        return len(self.assetsList)*25

    def stringProperties(self):
        for i in range(len(self.assetsList)):
            print(i+" "+self.assetsList[i].name)

    def statusBankrupcy(self):
        self.bankrupt = True






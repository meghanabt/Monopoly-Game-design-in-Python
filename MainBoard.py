
from Property import Property

class Board_main:
    
    Board = {0: 'GO', 1: 'Property', 2: 'CommunityChest', 3: 'Property', 4: 'TAX', 5: 'Property',
            6: "Property", 7: 'TAX', 8: 'JAIL', 9: "Property", 11: 'JAIL', 10: "Property",
            12: "Property", 13: 'TAX', 14: "Property", 15: "Property", 16: 'Property', 17: 'Property', 18: 'CommunityChest', 19: 'Property', 20: 'Property',
            21: 'Lounge Area', 22: "Property", 23: 'TAX', 24: 'JAIL', 25: "Property", 26: 'CommunityChest', 27: "Property",
            28: "Property", 29: 'TAX', 30: "JAIL", 31: "Property", 32: 'Property', 33: 'Property', 34: 'Property', 35: 'Property', 36: 'CommunityChest', 
            37: 'Property', 38: "Property", 39: 'TAX', 40: 'JAIL'}

 

    Properties = {1: Property('Atlanta', 400, 150),
                3: Property('New Jersey', 350, 250),
                5: Property('New York', 500, 300),
                6: Property('Colorado', 450, 200),
                9: Property('California', 700, 300),
                10: Property('Florida', 550, 350),
                12: Property('Indianapolis', 950, 550),
                14: Property('Arizona', 800, 450),
                15: Property('Georgia', 650, 250),
                16: Property('Kansas', 450, 200),
                17: Property('Connecticut', 700, 300),
                19: Property('Michigan', 550, 350),
                20: Property('Washington', 950, 550),
                22: Property('Ohio', 800, 450),
                25: Property('Nevada', 650, 250),
                27: Property('Pennsylvania', 700, 300),
                28: Property('Montana', 550, 350),
                31: Property('Oregon', 950, 550),
                32: Property('Texas', 800, 450),
                33: Property('Utah', 650, 250),
                34: Property('Wisconsin', 700, 300),
                35: Property('Oklahoma', 550, 350),
                37: Property('Vermont', 950, 550),
                38: Property('Maryland', 800, 450)
                }

    TAX = {
        4: {'name': "Water Tax"},
        7: {'name': "Hotel Tax"},
        13: {'name': 'Income Tax'},
        23: {'name': 'Income Tax'},
        29: {'name': 'Water Tax'},
        39:{'name': 'Income Tax'}
    }

    CommunityChest = {2: 'Collect 200',
                    11: "FINE 200", 18: "Collect 100", 26: "FINE 350", 36: "Collect 500"}

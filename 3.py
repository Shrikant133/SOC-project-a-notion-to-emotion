import random 


class dice :
    def roll_dice():
        x= random.randint(1,6)
        y= random.randint(1,6)
        
        roll= (x,y)
        return roll

    
num= dice.roll_dice()
print(num)
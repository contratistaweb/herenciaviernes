from classes.People import People

class Client(People):

    def __init__(self):
        self.__balance = None
        
    @property
    def balance(self):
        return self.__balance   

    @balance.setter
    def balance(self, balance):
        self.__balance = balance   
    
    def showBalance(self):
        print(f'{self.__balance}')
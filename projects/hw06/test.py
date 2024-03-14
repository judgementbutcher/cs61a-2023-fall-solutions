
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.funds = 0
        self.num = 0
        

    def vend(self):
        if self.num == 0:
            return 'Nothing left to vend. Please restock.'
        elif self.funds == self.price:
            self.funds = 0
            return "Here is your {}.".format(self.name)
        elif self.funds > self.price:
            self.funds = 0
            return "Here is your {} and ${} change.".format(self.name, self.funds - self.price)
        elif self.funds < self.price:
            return "Please add ${} more funds.".format(self.price - self.funds) 
 
    def restock(self,num):
        self.num += num
        return 'Current {} stock: {}.'.format(self.name,self.num) 
    
    def add_funds(self,funds):
        if self.num == 0:
            return 'Nothing left to vend. Please restock. Here is your ${}.'.format(funds)
        else:
            self.funds += funds
            return 'Current balance: ${}'.format(self.funds)
        
v = VendingMachine('candy',10)
v.vend()
v.add_funds(15)
v.restock(2)
v.vend()

  



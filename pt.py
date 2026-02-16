class Computer:
 def _init_(self):
self. maxprice = 900
 def sell(self):
    print("Selling Price: ()". format(self._maxprice))
 def setMaxPrice(self,price):
    self._maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c. setMaxPrice(1000)
c.sell()
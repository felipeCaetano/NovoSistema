#!/usr/bin/python
#_*_ coding: utf-8 _*_
class Stock(object):

    def __init__(self, stockName):

        # '_' is just a convention and does nothing
        self.__stockName  = stockName   # private now


    @property # when you do Stock.name, it will call this function
    def name(self):
        return self.__stockName

    @name.setter # when you do Stock.name = x, it will call this function
    def name(self, name):
        self.__stockName = name

if __name__ == "__main__":
      myStock = Stock("stock111")
      try:
        myStock.__stockName  # It is private. You can't access it.

      #Now you can myStock.name
      N = float(input("input to your stock: " + str(myStock.name)+" ? "))
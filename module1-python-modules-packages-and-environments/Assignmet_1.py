# import pandas as pd
# df = pd.read_csv('C:\Users\Pedro\Documents\Python\pokemon_data.csv')
# df.head()

class Stats:
    """
    Takes in a list of numbers
    """
    def __init__(self, numbers):
        self.numbers = numbers # Rename the variable
    def sumz(self):
        return(self.numbers)
    def meanz(self):
        return sum(self.numbers)/len(self.numbers)


# nums = [1,2,3,4,5]
# pedro = Stats(nums)
# pedro.numbers
# print(pedro.sumz())
# print(pedro.meanz())

class Leech(Stats):
    pass

rudy = Leech(nums)
rudy.sumz()


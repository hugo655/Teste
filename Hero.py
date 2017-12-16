'''
This is a simple class to train the concepts seen before
'''

class Hero():
    '''
        Simple character prototype that has attributes: name and health
    '''

    __counter = 0 # Helps us keep track of the ammount of heroes out there



    def __init__(self,name):
        self.name = name
        self.health = 100
        Hero.__counter += 1


    def __del__(self):
        type(self).__counter -= 1

    @classmethod
    def getCounter(cls):
        return (cls.__counter)


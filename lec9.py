'''
lecture 9
'''

class car:
    maker = 'Toyota'
    def __init__(self, input_model):
        self.model = input_model
    def report(self):
        return self.maker, self.model
'''      
my_carolla = car('carrola')

my_highlander = car('highlander')

print(my_carolla.report())

my_carolla.maker= 'Ford'

print(my_carolla.maker)
print(my_carolla.report())
'''
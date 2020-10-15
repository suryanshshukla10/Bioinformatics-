class BWT_Alg(object):
"""
This class is used for BWT algorithm
"""

    def __init__(self, DNA_STR):
        self.DNA_STR = DNA_STR

    def convert_to_lst(self):
        a = len(self.DNA_STR) 
        lst = []
        for i in self.DNA_STR:
            lst.append(i)
        return lst

# #rotate the string
    def rotate(list_001):
        
        a = len(list_01)
        b = []
        for j in range(a):
            b.append(list_01[a-j-1])
        return b
    
y = BWT_Alg('abaab$')
y.convert_to_lst()


# class car(object):
#     def __init__(self, model, color, engine):
#         self.model = model
#         self.color = color
#         self.engine = engine
#     def YourCar(self):
#         return self.model

# y = car(1,2,3)
# print(y.YourCar())       
    

  
class BWT_alg(object):
    def __init__(self, dna_str):
        self.dna_str = dna_str
    #this will reverse the string
    def rotate(self):
        a = self.dna_str
        lst = []
        for i in range(len(a)):
            lst.append(a[len(a)- 1- i])
        rev_str = ''.join(lst)
        return rev_str

y = BWT_alg('ncnc')
y.rotate()
class operations:
    def add(self,n1,n2):
        return n1+n2
    def div(self,n1,n2):
        return n1/n2

class MulOperations(operations):
    def mul(self,n1,n2):
        return n1*n2

def main():
    muop=MulOperations()
    print(muop.add(1,3))
    print(muop.mul(1, 3))
    print(muop.div(1, 3))

if __name__ == '__main__':main()

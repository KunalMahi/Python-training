class operations:
    def add(self,n1,n2):
        return n1+n2
    def div(self,n1,n2):
        return n1/n2

class MulOperations(operations):
    def mul(self,n1,n2):
        return n1*n2
    def add(self,n1,n2):
        if (n1+n2)<10:
            return (n1+n2)*2
        else:
            return super().add(n1,n2)


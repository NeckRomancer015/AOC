class Node():
    leftChild=''
    rightChild=''
    def __init__(self, Name):
        self.Name = Name
    
    def __str__(self) -> str:
        ret  = """ {Name} {leftChild} {rightChild}"""
        return ret.format(Name = self.Name, leftChild = self.leftChild, rightChild = self.rightChild)

    def __repr__(self) -> str:
        return self.__str__()


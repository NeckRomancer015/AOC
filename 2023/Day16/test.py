
class Mammal:
    def run(self):
        print("Mammal runs")
    
    def doSomething(self):
        print("Mammal")

class Animal:
    def speak(self):
        print("Animal speaks")
    
    def doSomething(self):
        print("Animal")

class Dog(Animal, Mammal):
    def bark(self):
        print("Dog barks")

# Create an instance of the Dog class
my_dog = Dog()

# Access methods from both base classes
my_dog.speak()  # Output: Animal speaks
my_dog.run()    # Output: Mammal runs
my_dog.bark()   # Output: Dog barks

my_dog.doSomething()

class Stack:
    
    def __init__(self):
        self.__stack = []
        print("Made stack")
    
    def push(self, val):
        self.__stack.append(val)
    
    def pop(self):
        assert len(self.__stack) > 0
        v = self.__stack[-1]
        del self.__stack[-1]
        return v
    
    def len(self):
        return len(self.__stack)

class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0
    
    def push(self,val):
        Stack.push(self,val)
        self.__sum+=val
    
    def pop(self):
        v = Stack.pop(self)
        self.__sum-=v
        return v
    
    def getSum(self):
        return self.__sum

s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)

a  =AddingStack()
a.push(1)
print(a.getSum())

print(s.len())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())


def f(x):
    try:
        x = x / x
    except:
        print("a",end='')
    else:
        print("b",end='')
    finally:
        print("c",end='')


f(1)
f(0)
print()
class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)
        print(len(self.args))

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)
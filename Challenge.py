class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if(self.a>other.a):
         return "obj1 is less than obj2"
        else:
         return "obj2 is less than obj1"
    def __eq__(self, other):
        if(self.a==other.a):
         return "obj1 is equal to obj2"
        else:
         return "not equal"
obj1 = A(2)
obj2 = A(3)
print("passed values:", obj1, obj2)
print(obj1 < obj2)
obj3 = A(4)
obj4 = A(4)
print("passed values:", obj3, obj4)
print(obj3 == obj4)
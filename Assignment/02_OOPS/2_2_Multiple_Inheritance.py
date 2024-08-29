# Base classes
class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

# Derived class
class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")


# Usage
child = Child()

# Inherited from Parent1
child.method1()

# Inherited from Parent2
child.method2()

# Defined in Child
child.method3()
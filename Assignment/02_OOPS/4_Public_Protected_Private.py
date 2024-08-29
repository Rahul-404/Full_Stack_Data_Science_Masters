class Base:
    def __init__(self):
        self.public_attr = "I'm public"
        self._protected_attr = "I'm protected"
        self.__private_attr = "I'm private"

    def public_method(self):
        print("Public method")

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")


class Derived(Base):
    def access_public_attribute(self):
        print(self.public_attr)

    def access_protected_attribute(self):
        print(self._protected_attr)

    def access_private_attribute(self):
        print(self.__private_attr) # it will raise exception

# Usage
obj = Derived()

# accessing variables from parent to child

obj.access_public_attribute() 

obj.access_protected_attribute() 

try:
 obj.access_private_attribute() # this will raise error
except Exception as e:
    print(f"While accessing private variable : {e}")

# accessing methods from parent to child

obj.public_method() 

obj._protected_method() 

try:
 obj.__private_method() # this will raise error
except Exception as e:
    print(f"While accessing private method : {e}")
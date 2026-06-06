class Base:

    def show (self):
        print("Show From Base Class")

#Overide
class Derived(Base):

    def show (self):
        print("Show From Derived Class")

class SubDerived(Derived):

    def show (self):
        print("Show From SunDerived Class")

d1=SubDerived()
d1.show()

print("*"*50)

# Super method.

class Base:

    def show (self):
        print("Show From Base Class")

class Derived(Base):

    def show (self):
        super().show()
        print("Show From Derived Class")

class SubDerived(Derived):

    def show (self):
        super().show()
        print("Show From SunDerived Class")

d1=SubDerived()
d1.show()



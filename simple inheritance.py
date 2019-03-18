class Vehicle():
    def __init__(self,color_arg="blue"):
        self.color =color_arg
        self.__var="pop"

    def get__var(self):
        return self.__var

class Car(Vehicle):
    def __init__(self,brand_name):
        #super(Car,self).__init__("red")
        self.brand_name=brand_name
        self.__var="lol"
        Vehicle.__init__(self)

    def get__var(self):
        return self.__var

def main():
    obj=Car("hydundai")
    print(obj.brand_name)
    print(obj.color)
    print(obj.get__var())

main()
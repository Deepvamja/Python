 #class

class Car:

    #class variable
    total_car = 0 


    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    # class variable
        Car.total_car += 1

# encapsulation
    def get_brand(self):
        return self.brand + '!'
    

#by using ((__)(two underscore) in any variable that variable became private)
     # mean you can access it in class but not in object for ex:
            #def __init__(self,brand,model):
                # self.__brand = brand
                # self.__model = model

# here my_tesla cannot access __brand and it will generate error 
# print(my_tesla.__brand)




#class method
    def full_name(self):
        return f"{self.brand} {self.model}"
    
# polymorphism
    def fuel_type(self):
         return "petrol or diesel"
         
    
#inheritance 
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
            super().__init__(brand,model)
            self.battery_size = battery_size

# polymorphism

    def fuel_type(self):
         return "eletric charge"

my_tesla = ElectricCar('Tesla','model Y','95kwh')
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.get_brand())
print(my_tesla.full_name())


#polymorphism
print(my_tesla.fuel_type())
safari = Car("tata","safari")

print(safari.fuel_type())

# class variable (count total no of car created)
print(Car.total_car)


        
''' (self) is same as (this) in javascript   and other language'''

#object

my_car = Car('bmw','xi 7')
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car('toyato','fortuner')
print(my_new_car.model)
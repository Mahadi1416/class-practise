class Car():

    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.odometer_reading= 0

    def car_massage(self):
        print("Car name " + self.name+".\n" + "Car model "+ self.model+" .\n" + "Car relares year" + str(self.year)+".")
    def orometer(self):
        print("This car orometer reading " + str(self.odometer_reading)+".")

    def updaate_orometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can not roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

My_new_car = Car("Audi","A14",2020)
print(My_new_car.car_massage())
My_new_car.orometer()

###Modifying an Attribute’s Value Directly
My_new_car.odometer_reading=23
My_new_car.orometer()
###Modifying an Attribute’s Value Through a Method
My_new_car.updaate_orometer(27)
My_new_car.orometer()

My_new_car.increment_odometer(100)
My_new_car.orometer()


class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has "+ str(self.battery_size)+" KMW battery ")

my_tesla=Electric_car("Tesla","120",2020)
my_tesla.car_massage()
my_tesla.describe_battery()












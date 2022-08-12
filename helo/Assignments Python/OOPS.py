class Vehicle(object):
     attr = "mammal" #attribute

     def __init__(self,name,plate):
        self.name= name
        self.plate=plate

     def details(self):
        #print('My name is  {}\t'.format(self.name))
        print("and registration num is {}".format(self.plate))

class truck(Vehicle):

    def details(self):
        print("An {} is a large vehicle with reg num {}".format(self.name,self.plate)) #polymorphishm
        

class Driver(Vehicle):  #inheritance
    def __init__(self, name, plate,owner):
        self.owner = owner

        Vehicle.__init__(self,name,plate)

    def identify(self):
        print("{} is the Owner of {}".format(self.name,self.owner))


#obj instant

a=Driver("Joe",1234,"BMW")
a.identify()
a.details()

b=truck("Optimus",1289)
b.details()

class Bulb:
    def __init__(self):
        self.ison=False
    def turnOn(self):
        self.ison=True
    def turnOff(self):
        self.ison=False
    def status(self):
        if self.ison==True:
            print("Bulb Is On")
        else:
            print("Bulb Is Off")

b1=Bulb()
b1.turnOn()
b1.status()
b1.turnOff()
b1.status()
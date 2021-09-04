class vehicles:
    def setv(self,car,bus):
        self.car=car
        self.bus=bus
        print(self.bus,self.car)
class bus(vehicles):
    def setvv(self,tyre,seat):
        self.tyre=tyre
        self.seat=seat
        print(self.tyre,self.seat)
bs=bus()
bs.setv('alto','tata')
bs.setvv(6,43)
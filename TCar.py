from Car import Car

class TCar(Car):
    """A class extends Car"""

    def __init__(self, model, year,power):
        super().__init__(model, year)
        self.power = f"Full Power of {power}"
        print(self.power)


myTCar = TCar("TTCar", 2023, "95%")


"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        if self.cargo + amount <= self.max_cargo:
            self.cargo += amount
        else:
            raise CargoOverload('Cargo overlord')
        
    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
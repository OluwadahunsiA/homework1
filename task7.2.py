from abc import ABC, abstractproperty


class AbstractCloth(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractproperty
    def suit(self):
        pass

    @abstractproperty
    def coat(self):
        pass


class Cloth(AbstractCloth):
    def __init__(self, V, H):
        self.H = H
        self.V = V

    @property
    def suit(self):
        return f'Расход ткани на костюма: {2 * (self.H) + 0.3}'

    @property
    def coat(self, V):
        return f'Расход ткани на пальто: {(self.V/6.5) + 0.5}'


y = Cloth(20, 10)

print(y.suit)

class Stationery:
    def __init__(self, title,):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You are drawing {self.title} with a Pen'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You are drawing {self.title} with a Pencil'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You are drawing {self.title} with a Handle'


stationery = Stationery('Picasso')
print(stationery.draw())

pen = Pen('Cat')
print(pen.draw())

pencil = Pencil('House')
print(pencil.draw())

handle = Handle('Plan')
print(handle.draw())

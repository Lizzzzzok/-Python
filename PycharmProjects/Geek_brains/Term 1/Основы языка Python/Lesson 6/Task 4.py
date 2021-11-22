class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} has started riding.'

    def stop(self):
        return f'{self.name} has stopped.'

    def turn_right(self):
        return f'{self.name} has turned right.'

    def turn_left(self):
        return f'{self.name} has turned left.'

    def show_speed(self):
        return f'Current speed of {self.name} car is {self.speed} km per hour.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of a town car {self.name} is {self.speed} km per hour.')

        if self.speed > 40:
            return f'Speed of the {self.name} car is higher than allowed.'
        else:
            return f'Speed of the {self.name} car is fine.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of the work car {self.name} is {self.speed}km per hour.')

        if self.speed > 60:
            return f'Speed of the {self.name} car is higher than allowed.'
        else:
            return f'Speed of the {self.name} car is fine.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'The {self.name} car police car.'
        else:
            return f'The {self.name} car is not police car.'


Mercedes = SportCar(100, 'Red', 'Mercedes', False)
Suzuki = TownCar(30, 'White', 'Suzuki', False)
Traktor = WorkCar(70, 'Rose', 'Traktor', True)
print(Mercedes.show_speed())
print(Suzuki.show_speed())
print(Traktor.show_speed())

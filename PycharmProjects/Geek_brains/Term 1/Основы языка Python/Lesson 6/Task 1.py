from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    @staticmethod
    def running():
        for i in range(3):
            print(f'Current colour: {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


TrafficLight().running()

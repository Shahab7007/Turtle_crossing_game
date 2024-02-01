from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class car_manager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_gen = random.randint(1,6)
        if random_gen == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(290, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT







class Car:
    def move(self):
        return "🚗 The car is driving on the road."


class Person:
    def move(self):
        return "🚶 The person is walking on the sidewalk."


class Robot:
    def move(self):
        return "🤖 The robot is moving on wheels."


def make_it_move(entity):
    print(entity.move())


# Test duck typing
if __name__ == "__main__":
    objects = [Car(), Person(), Robot()]

    for obj in objects:
        make_it_move(obj)
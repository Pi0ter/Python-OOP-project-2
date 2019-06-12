import numbers

colors = {"white": 'white',
          "black": 'black',
          "red": 'red',
          "green": 'green',
          "blue": 'blue'}


class ColorDesc:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value in colors.keys():
            instance.__dict__[self.storage_name] = colors[value]
        else:
            if value is None or value == "":
                instance.__dict__[self.storage_name] = colors['black']
            else:
                raise ValueError("Color is not one of defined colors")


class LengthDesc:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        value = int(value)
        if value > 0 and isinstance(value, numbers.Real):
            instance.__dict__[self.storage_name] = value  # !
        else:
            raise ValueError("Value is not real and bigger than 0!")


class AngleDesc:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        value = int(value)
        if 0 < value < 360:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("Value of degrees is not between 0 and 360 ")


class SmallAngleDesc:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        value = int(value)
        if 0 < value <= 90:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("Value of "+ self.storage_name +" is not in defined range (0 - 90)")
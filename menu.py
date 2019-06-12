from classes import *


class Menu:
    def __init__(self):
        self.options = {
            "1": self.triangles,
            "2": self.convquads,
            "3": self.regpent,
            "4": self.reghex,
            "5": self.regoct,
            "0": self.quit
        }
        self.menu_triangles = {
            "1": self.triangle,
            "2": self.isctriangle,
            "3": self.equiltriangle
        }
        self.menu_convquads = {
            "1": self.kite,
            "2": self.parrarell,
            "3": self.rhombus,
            "4": self.square
        }

    def triangle(self):
        print("-"*20)
        print("Constructing triangle...    ")
        print()
        print("Pleas input desired lenghts of sides: ")
        a = input("Side A")
        b = input("Side B")
        c = input("Side C")

        temp = [int(a), int(b), int(c)]
        temp = sorted(temp)
        if temp[0] + temp[1] > temp[2]:
            print("Please enter colours of triangle [white, black, red, blue ,green] ")
            fill = input("Colour of the triangle ")
            outline = input("Colour of outline of the triangle ")
            trojkat = Triangle(a, b, c, fill, outline)

            print("Area of triangle: " + str(trojkat.area()))
            print("Perimeter of triangle: " + str(trojkat.perimeter()))
            trojkat.draw()
            input("Press enter to continue")


    def isctriangle(self):
        print("-" * 20)
        print("Constructing triangle...    ")
        print()
        print("Pleas input desired lenghts of sides: ")
        a = input("Side A")
        b = a
        c = input("Side C")
        temp = [int(a), int(b), int(c)]
        temp = sorted(temp)
        if temp[0] + temp[1] > temp[2]:
            print("Please enter colours of triangle [white, black, red, blue ,green] ")
            fill = input("Colour of the triangle ")
            outline = input("Colour of outline of the triangle ")
            trojkatrwn = IsoscelesTriangle(a, c, fill, outline)

            print("Area of triangle: " + str(trojkatrwn.area()))
            print("Perimeter of triangle: " + str(trojkatrwn.perimeter()))
            trojkatrwn.draw()
            input("Press enter to continue")

    def equiltriangle(self):
        print("-" * 20)
        print("Constructing triangle...    ")
        print()
        print("Pleas input desired lenghts of sides: ")
        a = input("Side A")
        b = a
        c = a

        if True:
            print("Please enter colours of triangle [white, black, red, blue ,green] ")
            fill = input("Colour of the triangle ")
            outline = input("Colour of outline of the triangle ")
            trojkatrwnb = IsoscelesTriangle(a, c, fill, outline)

            print("Area of triangle: " + str(trojkatrwnb.area()))
            print("Perimeter of triangle: " + str(trojkatrwnb.perimeter()))
            trojkatrwnb.draw()
            input("Press enter to continue")

    def kite(self):
        print("-" * 20)
        print("Constructing Kite...    ")
        print()
        print("Pleas input desired lenghts of diagonals of kite: ")
        p = input("Diagonal p")
        # b/ = a
        q = input("Diagonal q")
        # d = c
        alpha = input("Angle between two shorter sides of kite in deegrees")

        if True:
            print("Please enter colours of kite [white, black, red, blue ,green] ")
            fill = input("Colour of the kite ")
            outline = input("Colour of outline of the kite ")
            latawiec = Kite(p, q, alpha, fill, outline)

            print("Area of kite: " + str(latawiec.area()))
            print("Perimeter of kite: " + str(latawiec.perimeter()))
            latawiec.draw()
            input("Press enter to continue")

    def parrarell(self):
        print("-" * 20)
        print("Constructing Parralerogram...    ")
        print()
        print("Pleas input desired lenghts of diagonals and sides of Parralerogram: ")
        a = input("Side A")
        b = input("Side B")

        p = input("Diagonal p")

        q = input("Diagonal q")

        if True:
            print("Please enter colours of Parralerogram [white, black, red, blue ,green] ")
            fill = input("Colour of the Parralerogram ")
            outline = input("Colour of outline of the Parralerogram ")
            rownoleglobok = Parallelogram(a, b, p, q, fill, outline)

            print("Area of Parralerogram: " + str(rownoleglobok.area()))
            print("Perimeter of Parralerogram: " + str(rownoleglobok.perimeter()))
            rownoleglobok.draw()
            input("Press enter to continue")

    def rhombus(self):
        print("-" * 20)
        print("Constructing rhombus...    ")
        print()
        print("Pleas input desired lenghts of side  of rhombus and the smaller angle in degrees: ")
        a = input("Side A")
        alpha = input("Smaller angle in deegrees")

        if True:
            print("Please enter colours of rhombus [white, black, red, blue ,green] ")
            fill = input("Colour of the rhombus ")
            outline = input("Colour of outline of the rhombus ")
            romb = Rhombus(a, alpha, fill, outline)

            print("Area of rhombus: " + str(romb.area()))
            print("Perimeter of rhombus: " + str(romb.perimeter()))
            romb.draw()
            input("Press enter to continue")

    def square(self):
        print("-" * 20)
        print("Constructing square...    ")
        print()
        print("Pleas input desired lenghts of side  of square: ")
        a = input("Side A")

        if True:
            print("Please enter colours of square [white, black, red, blue ,green] ")
            fill = input("Colour of the square ")
            outline = input("Colour of outline of the square ")
            kwadrat = Square(a, fill, outline)

            print("Area of square: " + str(kwadrat.area()))
            print("Perimeter of square: " + str(kwadrat.perimeter()))
            kwadrat.draw()
            input("Press enter to continue")

    def convquads(self):
        print("-" * 20)
        print()
        for a, b in self.menu_convquads.items():
            print(f"{a} -- {b.__name__}")
        option_convquads = input("Please select the type of convquads")

        if option_convquads in self.menu_convquads:
            self.menu_convquads[option_convquads]()
        else:
            print("That option does not seem to exist")
            self.convquads()

    def regpent(self):
        print("-" * 20)
        print("Constructing Regular Pentagon...    ")
        print()
        print("Pleas input desired lenghts of sides  of the pentagon: ")
        a = input("Side A")

        if True:
            print("Please enter colours of pentagon [white, black, red, blue ,green] ")
            fill = input("Colour of the pentagon ")
            outline = input("Colour of outline of the pentagon ")
            pent = RegularPentagon(a, fill, outline)

            print("Area of pentagon: " + str(pent.area()))
            print("Perimeter of pentagon: " + str(pent.perimeter()))
            pent.draw()
            input("Press enter to continue")

    def reghex(self):
        print("-" * 20)
        print("Constructing Regular hexagon...    ")
        print()
        print("Pleas input desired lenghts of sides  of the hexagon: ")
        a = input("Side A")

        if True:
            print("Please enter colours of hexagon [white, black, red, blue ,green] ")
            fill = input("Colour of the hexagon ")
            outline = input("Colour of outline of the pentagon ")
            hexa = RegularHexagon(a, fill, outline)

            print("Area of hexagon: " + str(hexa.area()))
            print("Perimeter of hexagon: " + str(hexa.perimeter()))
            hexa.draw()
            input("Press enter to continue")

    def regoct(self):
        print("-" * 20)
        print("Constructing Regular octagon...    ")
        print()
        print("Pleas input desired lenghts of sides  of the octagon: ")
        a = input("Side A")

        if True:
            print("Please enter colours of octagon [white, black, red, blue ,green] ")
            fill = input("Colour of the octagon ")
            outline = input("Colour of outline of the octagon ")
            okta = RegularHexagon(a, fill, outline)

            print("Area of octagon: " + str(okta.area()))
            print("Perimeter of octagon: " + str(okta.perimeter()))
            okta.draw()
            input("Press enter to continue")

    def run(self):
        while True:
            self.show_menu()
            option = input("Please select option")
            if option in self.options:
                self.options[option]()
            else:
                print("That option does not seem to exist")

    def show_menu(self):
        for a, b in self.options.items():
            print(f"{a} -- {b.__name__}")

    def triangles(self):
        print("-"*20)
        print()
        for a, b in self.menu_triangles.items():
            print(f"{a} -- {b.__name__}")
        option_triangles = input("Please select the type of triangle")

        if option_triangles in self.menu_triangles:
            self.menu_triangles[option_triangles]()
        else:
            print("That option does not seem to exist")
            self.triangles()

    def quit(self):
        exit(0)



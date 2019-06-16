from drawing import *
from abc import ABC, abstractmethod
from descriptors import *
import math


class ConvexPolygon(ABC):
    fill_colour = ColorDesc('fill_colour')
    outline_colour = ColorDesc('outline_colour')

    @abstractmethod
    def __init__(self):
        self.fill_colour = None
        self.outline_colour = None

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Triangle(ConvexPolygon):
    length_of_side_a = LengthDesc('length_of_side_a')
    length_of_side_b = LengthDesc('length_of_side_b')
    length_of_side_c = LengthDesc('length_of_side_c')

    def __init__(self, length_of_side_a, length_of_side_b,
                 length_of_side_c, fill=None, outline=None):
        super().__init__()
        self.length_of_side_a = length_of_side_a
        self.length_of_side_b = length_of_side_b
        self.length_of_side_c = length_of_side_c

        self.fill_colour = fill
        self.outline_colour = outline

    def area(self):
        a = self.length_of_side_a
        b = self.length_of_side_b
        c = self.length_of_side_c

        p = (a + b + c)/2
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))

        return area

    def perimeter(self):
        a = self.length_of_side_a
        b = self.length_of_side_b
        c = self.length_of_side_c

        return a + b + c

    def draw(self):

        A = self.length_of_side_a
        B = self.length_of_side_b
        C = self.length_of_side_c

        avg = size_x / max(A, B, C)
        avg = int(avg / 2)
        avg = avg * max(A, B, C)

        By = A - C + B
        By = By /2

        Bx = B**2 - By**2
        Bx = math.sqrt(Bx)

        points = [0 + avg, 0 + avg,
                  Bx + avg, By + avg,
                  0 + avg, A + avg]
        canvas.create_polygon(points, outline=self.outline_colour, fill=self.fill_colour, width=2)

        root.lift()
        canvas.pack()
        root.mainloop()


class ConvexQuadrilateral(ConvexPolygon):
    length_of_side_a = LengthDesc('length_of_side_a')
    length_of_side_b = LengthDesc('length_of_side_b')
    length_of_side_c = LengthDesc('length_of_side_c')
    length_of_side_d = LengthDesc('length_of_side_d')
    length_of_diagonal_p = LengthDesc('length_of_diagonal_p')
    length_of_diagonal_q = LengthDesc('length_of_diagonal_q')

    def __init__(self, length_of_side_a, length_of_side_b, length_of_side_c,
                 length_of_side_d, length_of_diagonal_p, length_of_diagonal_q, fill=None, outline=None,):
        super().__init__()
        self.length_of_side_a = length_of_side_a
        self.length_of_side_b = length_of_side_b
        self.length_of_side_c = length_of_side_c
        self.length_of_side_d = length_of_side_d
        self.length_of_diagonal_p = length_of_diagonal_p
        self.length_of_diagonal_q = length_of_diagonal_q


        # self.alpha = alpha
        # self.beta = beta

        self.fill_colour = fill
        self.outline_colour = outline

    def area(self):
        a = self.length_of_side_a
        b = self.length_of_side_b
        c = self.length_of_side_c
        d = self.length_of_side_d
        p = self.length_of_diagonal_p
        q = self.length_of_diagonal_q


        #  Area formula from z http://www.ambrsoft.com/TrigoCalc/Quadrilateral/Shape1.htm
        area = 4 * p**2 * q**2
        area -= (b**2 + d**2 - a**2 - c**2)**2
        area = math.sqrt(area)
        area = area / 4
        return area

    def perimeter(self):
        a = self.length_of_side_a
        b = self.length_of_side_b
        c = self.length_of_side_c
        d = self.length_of_side_d

        return a + b + c + d

    def draw(self):
        # TODO: Drawing sequence using ...
        pass


class RegularPentagon(ConvexPolygon):
    length_of_side_a = LengthDesc('length_of_side_a')

    def __init__(self, length_of_side_a, fill=None, outline=None):
        super().__init__()
        self.length_of_side_a = length_of_side_a

        self.fill_colour = fill
        self.outline_colour = outline

    def area(self):
        a = self.length_of_side_a
        area = (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * a * a) / 4
        return area

    def perimeter(self):
        return self.length_of_side_a * 5

    def draw(self):
        # TODO: Drawing sequence
        pass


class RegularHexagon(ConvexPolygon):
    length_of_side_a = LengthDesc('length_of_side_a')

    def __init__(self, length_of_side_a, fill=None, outline=None):
        super().__init__()
        self.length_of_side_a = length_of_side_a

        self.fill_colour = fill
        self.outline_colour = outline

    def area(self):
        a = self.length_of_side_a

        area = ((3 * math.sqrt(3) * (a * a)) / 2)

        return area

    def perimeter(self):
        return self.length_of_side_a * 6

    def draw(self):
        pass
        # TODO: drawing sequence


class RegularOctagon(ConvexPolygon):
    length_of_side_a = LengthDesc('length_of_side_a')

    def __init__(self, length_of_side_a, fill=None, outline=None):
        super().__init__()
        self.length_of_side_a = length_of_side_a

        self.fill_colour = fill
        self.outline_colour = outline

    def area(self):
        a = self.length_of_side_a
        area = (2 * (1 + (math.sqrt(2))) * a * a)
        return area

    def perimeter(self):
        return self.length_of_side_a * 8

    def draw(self):
        pass
        # TODO: drawing sequence


class IsoscelesTriangle(Triangle):
    def __init__(self, length_of_side_a, length_of_side_c, fill=None, outline=None):
        super().__init__(length_of_side_a, length_of_side_a, length_of_side_c, fill, outline)


class EquilateralTriangle(Triangle):
    def __init__(self, length_of_side_a, fill=None, outline=None):
        super().__init__(length_of_side_a, length_of_side_a, length_of_side_a, fill, outline)


class Parallelogram(ConvexQuadrilateral):
    alpha = SmallAngleDesc('alpha')

    def __init__(self, length_of_side_a, length_of_side_b, length_of_diagonal_p,
                 length_of_diagonal_q, fill=None, outline=None):
        super().__init__(length_of_side_a, length_of_side_a,
                         length_of_side_b, length_of_side_b, length_of_diagonal_p, length_of_diagonal_q, fill, outline)
        # self.alpha = alpha


class Kite(ConvexPolygon):
    length_of_diagonal_p = LengthDesc('length_of_diagonal_p')
    length_of_diagonal_q = LengthDesc('length_of_diagonal_q')
    alpha = SmallAngleDesc('alpha')

    def __init__(self, length_of_diagonal_p, length_of_diagonal_q, alpha, fill=None, outline=None):
        super().__init__()
        self.length_of_diagonal_p = length_of_diagonal_p
        self.length_of_diagonal_q = length_of_diagonal_q
        self.alpha = alpha

        self.fill_colour = fill
        self.outline_colour = outline

    def area(self):
        return (self.length_of_diagonal_p * self.length_of_diagonal_q)/2

    def perimeter(self):
        p = self.length_of_diagonal_p
        q = self.length_of_diagonal_q

        b = p/2
        c = q/2

        a = math.sqrt(b**2 + c**2)

        return a*4

    def draw(self):
        # TODO: Drawing sequence
        pass


class Rhombus(Parallelogram):
    def __init__(self, length_of_side_a, alpha, fill=None, outline=None):
        super().__init__(length_of_side_a, length_of_side_a, 1, 1, fill, outline)
        self.alpha = alpha

    def area(self):
        a = self.length_of_side_a
        alpha = self.alpha
        return a*2 * math.sin(alpha)

    # def perimeter(self):
    #     return self.length_of_side_a*4
    def draw(self):

        A = self.length_of_side_a
        B = self.length_of_side_a

        alpha = self.alpha *2
        # alpha = 180
        # print("Angle in deg" + str(alpha))
        alpha = math.radians(round(alpha, 4))
        # print("Angle in rad" + str(alpha))

        cosofalpgha = round(math.cos(alpha), 3)
        # print("Cos of alpha =" + str(cosofalpgha))

        C = (A**2 + B**2)
        C = C - (2 * A * B * cosofalpgha)
        C = math.sqrt(C)

        avg = size_x / max(A, B)
        avg = int(avg / 2)
        avg = avg * max(A, B)
        avg = avg / 2

        By = A - C + B
        By = By / 2

        Bx = B ** 2 - By ** 2

        Bx = math.sqrt(Bx)
        print(C)
        print(Bx)

        Cy = A + By
        Cx = Bx

        points = [0 + avg, 0 + avg,
                  Bx + avg, By + avg,
                  Cx + avg, Cy + avg,
                  0 + avg, A + avg,
                  ]
        canvas.create_polygon(points, outline=self.outline_colour, fill=self.fill_colour, width=2)

        root.lift()
        canvas.pack()
        root.mainloop()



class Square(Parallelogram):
    def __init__(self, length_of_side_a, fill=None, outline=None):
        # p = length_of_side_a * math.sqrt(2)
        super().__init__(length_of_side_a, length_of_side_a, 1,
                         1, fill, outline)

    def area(self):
        a = self.length_of_side_a
        return a*a

    def draw(self):
        a = self.length_of_side_a

        avg = size_x - a
        avg = avg / 2
        avg = avg - a / 2
        points = [0 + avg, 0 + avg,
                  100 + avg, 0 + avg,
                  100 + avg, 100 + avg,
                  0 + avg, 100 + avg]
        canvas.create_polygon(points, outline=self.outline_colour,fill=self.fill_colour, width=2)

        root.lift()
        canvas.pack()
        root.mainloop()

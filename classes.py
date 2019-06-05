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
        # TODO: Function doesn't work
        a = self.length_of_side_a
        b = self.length_of_side_b
        c = self.length_of_side_c
        pass


class ConvexQuadrilateral(ConvexPolygon):
    length_of_side_a = LengthDesc('length_of_side_a')
    length_of_side_b = LengthDesc('length_of_side_b')
    length_of_side_c = LengthDesc('length_of_side_c')
    length_of_side_d = LengthDesc('length_of_side_d')
    length_of_diagonal_p = LengthDesc('length_of_diagonal_p')
    length_of_diagonal_q = LengthDesc('length_of_diagonal_q')
    # alpha = AngleDesc('alpha') # alpha to kąt  |DAB|
    # beta = AngleDesc('beta') # beta to kąt |BCD|

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

        # alpha = self.alpha
        # beta = self.beta
        # s = (a + b + c + d)/2
        # area = (s-a)*(s-b)*(s-c)*(s-d)
        # area -= a * b * c * d * (math.cos((alpha+beta)/2))**2
        # area = math.sqrt(area)


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
        # alpha = self.alpha
        # beta = (360 - alpha * 2)/2

        # small triangle
        # b = p/2
        # alp = alpha /2
        # bet = 90 - alp
        #
        # c = b * math.cos(bet)
        # a = c * math.cos(bet)
        #
        # per = c*2
        #
        # d = math.sqrt(b**2 + (q-a)**2)
        # per += d*2
        # return per

        b = p/2
        c = q/2

        a = math.sqrt(b**2 + c**2)

        return a*4

    def draw(self):
        # TODO: Drawing sequence
        pass


class Rhombus(Parallelogram):
    def __init__(self, length_of_side_a, fill=None, outline=None, alpha=50):
        super().__init__(length_of_side_a, length_of_side_a, 1, 1, fill, outline)
        self.alpha = alpha

    def area(self):
        a = self.length_of_side_a
        alpha = self.alpha
        return a*2 * math.sin(alpha)

    # def perimeter(self):
    #     return self.length_of_side_a*4


class Square(Parallelogram):
    def __init__(self, length_of_side_a, fill=None, outline=None):
        # p = length_of_side_a * math.sqrt(2)
        super().__init__(length_of_side_a, length_of_side_a, 1,
                         1, fill, outline)

    def area(self):
        a = self.length_of_side_a
        return a*a

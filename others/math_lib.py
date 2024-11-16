from math import cos, sin, atan2, tau

from utils import sanatizeInputFloat

# Just went full English from this part xD
class Vec2:
    def __init__(self, coord_x: int | float, coord_y: int | float):
        self.x = float(coord_x)
        self.y = float(coord_y)

    def __add__(self, other: "Vec2"):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError

    def __sub__(self, other: "Vec2"):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            raise NotImplementedError

    def __mul__(self, other: "Vec2" | int | float):
        # Dot product
        if isinstance(other, Vec2):
            return (self.x * other.x + self.y * other.y)
        # Product of a 2D vector by a scalar
        elif isinstance(other, (int, float)):
            return Vec2(other * self.x, other * self.y)
        else:
            raise NotImplementedError

    def __truediv__(self, other: int | float):
        if isinstance(other, Vec2):
            raise NotImplementedError("Cannot divide a Vec2 object by another Vec2 object")
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Vec2(self.x / other, self.y / other)
        else:
            return NotImplementedError
    
    def magnitude(self):
        return float((self.x ** 2 + self.y ** 2) ** 0.5)

    def direction(self):
        return atan2(self.y, self.x)
    
    def normalize(self):
        if (self.magnitude() == 0):
            raise NotImplementedError
        return (self / self.magnitude)

    def ToVec3(self, coord_z: int | float = 0):
        return Vec3(self.x, self.y, coord_z)

    def ToComplex(self):
        return Complex(self.x, self.y)
    
    def ToPolar(self):
        return Polar(self.magnitude(), self.direction())

    def __str__(self):
        return f"({self.x}, {self.y})"

class Vec3:
    def __init__(self, coord_x: int | float, coord_y: int | float, coord_z: int | float):
        self.x = float(coord_x)
        self.y = float(coord_y)
        self.z = float(coord_z)

    def __add__(self, other: "Vec3"):
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise NotImplementedError

    def __sub__(self, other: "Vec3"):
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise NotImplementedError

    def __mul__(self, other: "Vec3" | int | float):
        # Dot product
        if isinstance(other, Vec3):
            return (self.x * other.x + self.y * other.y + self.z * other.z)
        # Product of a 2D vector by a scalar
        elif isinstance(other, (int, float)):
            return Vec3(other * self.x, other * self.y, other * self.z)
        else:
            raise NotImplementedError

    def __truediv__(self, other: int | float):
        if isinstance(other, Vec3):
            raise NotImplementedError("Cannot divide a Vec3 object by another Vec3 object")
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Vec3(self.x / other, self.y / other, self.z / other)
        else:
            return NotImplemented
    
    def magnitude(self):
        return float((self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5)
    
    def normalize(self):
        if self.magnitude() == 0:
            raise NotImplementedError
        return (self / self.magnitude())

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def Cross(V1: Vec2 | Vec3, V2: Vec2 | Vec3):
    if isinstance(V1, Vec2):
        if isinstance(V2, Vec2):
            return Vec3(0, 0, ((V1.x * V2.y) - (V1.y * V2. x)))
        elif isinstance(V2, Vec3):
            return Cross(V1. ToVec3(), V2)
        else:
            raise NotImplementedError
    elif isinstance(V1, Vec3):
        if isinstance(V2, Vec2):
            return Cross(V1, V2.ToVec3())
        elif isinstance(V2, Vec3):
            return Vec3(((V1.y * V2.z) - (V1.x * V2.z)), ((V1.z * V2.x) - (V1.x * V2.z)), ((V1.x * V2.y) - (V1.y * V2.x)))
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError

class Imaginary:
    def __init__(self, Value: int | float):
        self.val = float(Value)

    def __add__(self, other: "Imaginary" | int | float):
        if isinstance(other, Imaginary):
            return Imaginary(self.val + other.val)
        elif isinstance(other, (int, float)):
            return Complex(float(other), self.val)
        else:
            raise NotImplementedError

    def __sub__(self, other: "Imaginary" | int | float):
        if isinstance(other, Imaginary):
            return Imaginary(self.val - other.val)
        elif isinstance(other, (int, float)):
            return Complex(float(other), -self.val)
        else:
            raise NotImplementedError

    def __mul__(self, other: "Imaginary" | int | float):
        if isinstance(other, Imaginary):
            return -self.val * other.val
        elif isinstance(other, (int, float)):
            return Imaginary(self.val * float(other))
        else:
            raise NotImplementedError

    def __truediv__(self, other: "Imaginary" | int | float):
        if isinstance(other, Imaginary):
            if other.val == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return float(self.val / other.val)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Imaginary(self.val / float(other))
        else:
            raise NotImplementedError

    def __str__(self):
        return f"{self.val}i"

class Complex:
    def __init__(self, real: int | float, imaginary: int | float):
        self.re = float(real)
        self.im = float(imaginary)
    
    def __add__(self, other: "Complex" | int | float | Imaginary):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        elif isinstance(other, Imaginary):
            return Complex(self.re, self.im + other.val)
        else:
            raise NotImplementedError

    def __sub__(self, other: "Complex" | int | float | Imaginary):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re - float(other), self.im)
        elif isinstance(other, Imaginary):
            return Complex(self.re, self.im - other.val)
        else:
            raise NotImplementedError
    
    def __truediv__(self, other: "Complex" | int | float):
        if isinstance(other, Complex):
            pass
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Complex(self.re / float(other), self.im / float(other))
        else:
            raise NotImplementedError
    
    def conjugate(self):
        return Complex(self.re, -self.im)
    
    def Arg(self):
        return atan2(self.im, self.re)
    
    def arg(self, num: int = 0):
        return (self.Arg() + (int(num) * tau))
    
    def abs(self):
        return float((self.re ** 2 + self.im ** 2) ** 0.5)
    
    def normalize(self):
        if self.abs() == 0:
            raise NotImplementedError
        return (self / self.abs())

    def ToVec2(self):
        return Vec2(self.re, self.im)
    
    def ToPolar(self):
        return Polar(self.magnitude(), self.Arg())

    def ToEulerF(self):
        return EulerF(self.abs(), self.Arg())

    def __str__(self):
        if self.re == 0:
            return f"{self.im}i"
        elif self.im == 0:
            return f"{self.re}"
        elif self.im > 0:
            return f"{self.re} + {self.im}i"
        elif self.im < 0:
            return f"{self.re} - {abs(self.im)}i"

class Polar:
    def __init__(self, radius: int | float, direction: int | float):
        self.r = float(radius)
        self.theta = float(direction)
    
    def __mul__(self, other: int | float):
        if isinstance(other, (int, float)):
            return Polar(self.r * float(other), self.theta)
        else:
            raise NotImplementedError
    
    def ToVec2(self):
        return (self.r * Vec2(cos(self.theta), sin(self.theta)))

    def ToComplex(self):
        return (self.r * Complex(cos(self.theta), sin(self.theta)))
    
    def __str__(self):
        return f"({self.r}, {self.theta})"

class EulerNF:
    def __init__(self, direction: int | float):
        self.theta = float(direction)

    def ToNormalizedVec2(self):
        return Vec2(cos(self.theta), sin(self.theta))

    def ToVec2(self, magnitude: int | float = 1):
        return (float(magnitude) * self.ToNormalizedVec2())

    def ToNormalizedComplex(self):
        return Complex(cos(self.theta), sin(self.theta))
    
    def ToComplex(self, absolute_value: int | float = 1):
        return (abs(float(absolute_value)) * self.ToNormalizedComplex())
    
    def ToPolar(self, radius: int | float = 1):
        return Polar(float(radius), self.theta)

    def ToEulerF(self, Abs: int | float = 1):
        return EulerF(abs(float(Abs)), self.theta)

    def __mul__(self, other: "EulerNF" | int | float):
        if isinstance(other, EulerNF):
            return EulerNF(self.theta + other.theta)
        elif isinstance(other, (int, float)):
            return (float(other) * self.ToNormalizedComplex())
        else:
            raise NotImplementedError

    def __str__(self):
        return f"e^i{self.theta}"

class EulerF:
    def __init__(self, Abs: int | float, theta: int | float):
        self.abs = float(Abs)
        self.theta = float(theta)
    
    def __mul__(self, other: "EulerF" | EulerNF | int | float):
        if isinstance(other, EulerF):
            return EulerF(self.abs * other.abs, self.theta + other.theta)
        elif isinstance(other, EulerNF):
            return EulerF(self.abs, self.theta + other.theta)
        elif isinstance(other, (int, float)):
            return EulerF(self.abs * float(other), self.theta)
        else:
            raise NotImplementedError

    def __truediv__(self, other: "EulerF" | EulerNF | int | float):
        if isinstance(other, EulerF):
            return EulerF(self.abs / other.abs, self.theta - other.theta)
        elif isinstance(other, EulerNF):
            return EulerF(self.abs, self.theta - other.theta)
        elif isinstance(other, (int, float)):
            return EulerF(self.abs / float(other), self.theta)
        else:
            raise NotImplementedError

    def __str__(self):
        if self.abs == 0:
            return f"0"
        elif self.abs == 1:
            return f"e^{self.theta}i"
        else:
            return f"{self.abs}*e^{self.theta}i"

class Point:
    def __init__(self, coord_x: int | float, coord_y: int | float):
        self.x = float(coord_x)
        self.y = float(coord_y)

    def __add__(self, other: "Point"):
        if not isinstance(other, Point):
            raise NotImplementedError
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point"):
        if not isinstance(other, Point):
            raise NotImplementedError
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float):
        if not isinstance(other, (int, float)):
            raise NotImplementedError
        return Point(self.x * float(other), self.y * float(other))

    def __rmul__(self, other: int | float):
        return self * float(other)

    def __truediv__(self, other: int | float):
        if not isinstance(other, (int, float)):
            raise NotImplementedError
        if other == 0:
            raise ZeroDivisionError
        return Point(self.x / float(other), self.y / float(other))

    def distanceToPoint(self, other: "Point"):
        if not isinstance(other, Point):
            raise TypeError
        return float(((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5)

    def toVec2(self):
        return Vec2(self.x, self.y)

    def toComplex(self):
        return Complex(self.x, self.y)

    def toPolar(self):
        return Polar(self.toVec2().magnitude(), self.toVec2().direction())

    def toEulerF(self):
        return EulerF(self.toVec2().magnitude(), self.toVec2().direction())

    def __str__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, Slope: int | float = None, ordinate: int |float = None, A: int | float = None, B: int | float = None, C: int | float = None, pass_point: Point = None):
        if Slope is not None and ordinate is not None:
            self.m = float(Slope)
            self.y_intercept = float(ordinate)
            self.form = "slope-ordinate"
        if A is not None and B is not None and C is not None:
            self.A = float(A)
            self.B = float(B)
            self.C = float(C)
            self.form = "general_eq"
        if Slope is not None and pass_point is not None:
            self.m = float(Slope)
            self.pass_point = pass_point
            self.form = "point-slope"

    def Slope(self):
        if self.form == "slope-ordinate":
            return self.m
        elif self.form == "general_eq":
            if self.B == 0:
                raise ZeroDivisionError
            return -(self.A / self.B)
        elif self.form == "point-slope":
            return self.m

    def Ordinate(self):
        if self.form == "slope-ordinate":
            return self.y_intercept
        elif self.form == "general_eq":
            if self.B == 0:
                raise ZeroDivisionError
            return -(self.C / self.B)
        elif self.form == "point-slope":
            return self.pass_point.y

    def toGeneralEq(self):
        if self.form == "slope-ordinate":
            A = -self.m
            B = 1
            C = -self.y_intercept
            return Line(None, None, A, B, C)
        elif self.form == "general_eq":
            return self
        elif self.form == "point-slope":
            A = -self.m
            B = 1
            C = self.m * self.pass_point.x - self.pass_point.y
            return Line(None, None, A, B, C)

    def distanceToPoint(self, point_1: Point):
        Line_0 = self.toGeneralEq()
        _A = Line_0.A
        _B = Line_0.B
        _C = Line_0.C
        _x0 = point_1.x
        _y0 = point_1.y
        return float(abs(_A * _x0 + _B * _y0 + _C) / ((_A ** 2 + _B ** 2) ** 0.5))

    def __str__(self):
        if self.form == "slope-ordinate":
            return f"y = {self.m}x + {self.y_intercept}"
        elif self.form == "general_eq":
            return f"{self.A}x + {self.B}y + {self.C} = 0"
        elif self.form == "point-slope":
            return f"y - {self.pass_point.y} = {self.m}(x - {self.pass_point.y})"

def readVec2Console(msg: str = "Next you will enter the coordinates of the Vec2", msg_x: str = "Enter the value on the X axis: ", msg_y: str = "Enter the value on the Y axis: "):
    print(msg)
    _x = sanatizeInputFloat(msg_x)
    _y = sanatizeInputFloat(msg_y)
    return Vec2(_x, _y)

def readVec3Console(msg: str = "Next you will enter the coordinates of the Vec3", msg_x: str = "Enter the value on the X axis: ", msg_y: str = "Enter the value on the Y axis: ", msg_z: str = "Enter the value on the Z axis: "):
    print(msg)
    _x = sanatizeInputFloat(msg_x)
    _y = sanatizeInputFloat(msg_y)
    _z = sanatizeInputFloat(msg_z)
    return Vec2(_x, _y, _z)

def readPolarConsole(msg: str = "Next you will enter the coordinates of the Polar", msg_r: str = "Enter the value of the radius: ", msg_theta: str = "Enter the value of the angle: "):
    print(msg)
    _r = sanatizeInputFloat(msg_r)
    _theta = sanatizeInputFloat(msg_theta)
    return Polar(_r, _theta)

class Segment:
    def __init__(self, point0: Point, point1: Point):
        self.p0 = point0
        self.p1 = point1

    def val(self):
        return self.p0.distanceToPoint(self.p1)

    def midPoint(self):
        return Point((self.p0.x + self.p1.x) / 2, (self.p0.y + self.p1.y) / 2)

    def slope(self):
        if self.p1.x == self.p0.x:
            raise ValueError
        return((self.p1.y - self.p0.y) / (self.p1.x - self.p0.x))

    def __str__(self):
        return f"AB = {self.val()}"
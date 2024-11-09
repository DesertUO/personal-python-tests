# "Librería"

from math import cos, sin, atan2, tau

def InputCheckInt(msg, vmin = -9999999999999, vmax = 9999999999999):
    while True:
        try:
            Num = int(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be an integer.")

def InputCheckFloat(msg, vmin = -9999999999999, vmax = 9999999999999):
    while True:
        try:
            Num = float(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be a float.")

# Just went full English from this part xD
class Vec2:
    def __init__(self, coord_x: float, coord_y: float):
        self.x = coord_x
        self.y = coord_y

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            raise NotImplementedError

    def __mul__(self, other):
        # Dot product
        if isinstance(other, Vec2):
            return (self.x * other.x + self.y * other.y)
        # Product of a 2D vector by a scalar
        elif isinstance(other, (int, float)):
            return Vec2(other * self.x, other * self.y)
        else:
            raise NotImplementedError

    def __truediv__(self, other):
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

    def ToVec3(self, coord_z = 0):
        return Vec3(self.x, self.y, coord_z)

    def ToComplex(self):
        return Complex(self.x, self.y)
    
    def ToPolar(self):
        return Polar(self.magnitude(), self.direction())

    def __str__(self):
        return f"({self.x}, {self.y})"

class Vec3:
    def __init__(self, coord_x: float, coord_y: float, coord_z: float):
        self.x = coord_x
        self.y = coord_y
        self.z = coord_z

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise NotImplementedError

    def __mul__(self, other):
        # Dot product
        if isinstance(other, Vec3):
            return (self.x * other.x + self.y * other.y + self.z * other.z)
        # Product of a 2D vector by a scalar
        elif isinstance(other, (int, float)):
            return Vec3(other * self.x, other * self.y, other * self.z)
        else:
            raise NotImplementedError

    def __truediv__(self, other):
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
    def __init__(self, Value: float):
        self.val = Value

    def __add__(self, other):
        if isinstance(other, Imaginary):
            return Imaginary(self.val + other.val)
        elif isinstance(other, (int, float)):
            return Complex(other, self.val)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Imaginary):
            return Imaginary(self.val - other.val)
        elif isinstance(other, (int, float)):
            return Complex(other, -self.val)
        else:
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, Imaginary):
            return -self.val * other.val
        elif isinstance(other, (int, float)):
            return Imaginary(self.val * other)
        else:
            raise NotImplementedError

    def __truediv__(self, other):
        if isinstance(other, Imaginary):
            if other.val == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return float(self.val / other.val)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Imaginary(self.val / other)
        else:
            raise NotImplementedError

    def __str__(self):
        return f"{self.val}i"

class Complex:
    def __init__(self, real: float, imaginary: float):
        self.re = real
        self.im = imaginary
    
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        elif isinstance(other, Imaginary):
            return Complex(self.re, self.im + other.val)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re - other, self.im)
        elif isinstance(other, Imaginary):
            return Complex(self.re, self.im - other.val)
        else:
            raise NotImplementedError
    
    def __truediv__(self, other):
        if isinstance(other, Complex):
            pass
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Complex(self.re / other, self.im / other)
        else:
            raise NotImplementedError
    
    def conjugate(self):
        return Complex(self.re, -self.im)
    
    def Arg(self):
        return atan2(self.im, self.re)
    
    def arg(self, num: int = 0):
        return (self.Arg() + (num * tau))
    
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
    def __init__(self, radius: float, direction):
        self.r = radius
        self.theta = direction
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Polar(self.r * other, self.theta)
        else:
            raise NotImplementedError
    
    def ToVec2(self):
        return (self.r * Vec2(cos(self.theta), sin(self.theta)))

    def ToComplex(self):
        return (self.r * Complex(cos(self.theta), sin(self.theta)))
    
    def __str__(self):
        return f"({self.r}, {self.theta})"

class EulerNF:
    def __init__(self, direction: float):
        self.theta = direction

    def ToNormalizedVec2(self):
        return Vec2(cos(self.theta), sin(self.theta))

    def ToVec2(self, magnitude: float = 1):
        return (magnitude * self.ToNormalizedVec2())

    def ToNormalizedComplex(self):
        return Complex(cos(self.theta), sin(self.theta))
    
    def ToComplex(self, absolute_value: float = 1):
        return (absolute_value * self.ToNormalizedComplex())
    
    def ToPolar(self, radius: float = 1):
        return Polar(radius, self.theta)

    def ToEulerF(self, abs: float = 1):
        return EulerF(abs, self.theta)

    def __mul__(self, other):
        if isinstance(other, EulerNF):
            return EulerNF(self.theta + other.theta)
        elif isinstance(other, (int, float)):
            return (other * self.ToNormalizedComplex())
        else:
            raise NotImplementedError

    def __str__(self):
        return f"e^i{self.theta}"

class EulerF:
    def __init__(self, abs: float, theta: float):
        self.abs = abs
        self.theta = theta
    
    def __mul__(self, other):
        if isinstance(other, EulerF):
            return EulerF(self.abs * other.abs, self.theta + other.theta)
        elif isinstance(other, EulerNF):
            return EulerF(self.abs, self.theta + other.theta)
        elif isinstance(other, (int, float)):
            return EulerF(self.abs * other, self.theta)
        else:
            raise NotImplementedError

    def __truediv__(self, other):
        if isinstance(other, EulerF):
            return EulerF(self.abs / other.abs, self.theta - other.theta)
        elif isinstance(other, EulerNF):
            return EulerF(self.abs, self.theta - other.theta)
        elif isinstance(other, (int, float)):
            return EulerF(self.abs / other, self.theta)
        else:
            raise NotImplementedError

    def __str__(self):
        if self.abs == 0:
            return f"0"
        elif self.abs == 1:
            return f"e^{self.theta}i"
        else:
            return f"{self.abs}*e^{self.theta}i"
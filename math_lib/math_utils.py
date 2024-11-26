from .math_l import *
from utils.utils_l import sanitizeInputFloat

def readVec2Console(msg: str = "Next you will enter the coordinates of the Vec2", msg_x: str = "Enter the value on the X axis: ", msg_y: str = "Enter the value on the Y axis: ") -> Vec2:
    print(msg)
    _x = sanitizeInputFloat(msg_x)
    _y = sanitizeInputFloat(msg_y)
    return Vec2(_x, _y)

def readVec3Console(msg: str = "Next you will enter the coordinates of the Vec3", msg_x: str = "Enter the value on the X axis: ", msg_y: str = "Enter the value on the Y axis: ", msg_z: str = "Enter the value on the Z axis: ") -> Vec3:
    print(msg)
    _x = sanitizeInputFloat(msg_x)
    _y = sanitizeInputFloat(msg_y)
    _z = sanitizeInputFloat(msg_z)
    return Vec3(_x, _y, _z)

def readPolarConsole(msg: str = "Next you will enter the coordinates of the Polar", msg_r: str = "Enter the value of the radius: ", msg_theta: str = "Enter the value of the angle: ") -> Polar:
    print(msg)
    _r = sanitizeInputFloat(msg_r)
    _theta = sanitizeInputFloat(msg_theta)
    return Polar(_r, _theta)

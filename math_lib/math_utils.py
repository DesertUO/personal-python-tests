from .math_l import *
from utils.utils_l import sanatizeInputFloat

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
# WIP
import math_lib as ml
from math_lib.matrices import Matrix
import utils as utils

import time
import os

witdh = 100
height = 10

baseScene = ml.Matrix(height, witdh, "-")


def getPointInScene(scene: Matrix, x: int, y: int) -> str:
    point = scene.get(y, x)
    return point

def getCoordInScene(scene: Matrix, value):
    coords = []
    for y in range(scene.rows):
        for x in range(scene.cols):
            if str(scene.get(y, x)) == str(value):
                coords += [[x, y]]
    return coords

def setPointInScene(scene: Matrix, x: int, y: int, value) -> None:
    scene.set(y, x, str(value))

def drawScene(scene: Matrix, title: str = "Title", printTitle: bool = True):
    if printTitle == True:
        print(title)

    for i in range(scene.rows):
        row = ""
        for j in range(scene.cols):
            element = scene.get(i, j)
            row += str(element)
        print(row)

setPointInScene(baseScene, 1, 1, "A")

def main():
    while True:
        if (getCoordInScene(baseScene, "A")[0][0] > baseScene.cols - 1):
            setPointInScene(baseScene, getCoordInScene(baseScene, "A")[0][0] + 1, getCoordInScene(baseScene, "A")[0][1], "A")
            setPointInScene(baseScene, getCoordInScene(baseScene, "A")[0][0], getCoordInScene(baseScene, "A")[0][1], "-")
        else:
            setPointInScene(baseScene, 0,  getCoordInScene(baseScene, "A")[0][1], "A")
            setPointInScene(baseScene, getCoordInScene(baseScene, "A")[1][0], getCoordInScene(baseScene, "A")[1][1], "-") if len(getCoordInScene(baseScene, "A")) >= 2 else ...
        if (getCoordInScene(baseScene, "A")[0][1] + 1 >= baseScene.rows):
            setPointInScene(baseScene, getCoordInScene(baseScene, "A")[0][0], getCoordInScene(baseScene, "A")[0][1] + 1, "A")
            setPointInScene(baseScene, getCoordInScene(baseScene, "A")[0][0], getCoordInScene(baseScene, "A")[0][1], "-")
        else:
            setPointInScene(baseScene, getCoordInScene(baseScene, "A")[0][1],  0, "A")
            setPointInScene(baseScene, getCoordInScene(baseScene, "A")[1][0], getCoordInScene(baseScene, "A")[1][1], "-") if len(getCoordInScene(baseScene, "A")) >= 2 else ...
        drawScene(baseScene, printTitle=False)
        time.sleep(0.0001)
        os.system("cls||clear")

if __name__ == "__main__":
    main()

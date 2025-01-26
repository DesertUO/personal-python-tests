import sys
import os
import time
import datetime
from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.master.title("Canvas")
        self.pack(fill=BOTH, expand=1)
    
        canvas = Canvas(self)
        canvas.create_rectangle()

class Window:
    def __init__(self , title:str, width:int, height:int, icon_path:str=None):
        self.title = title
        self.width = width
        self.height = height
        self.iconPath = icon_path
        self.window = Tk()

    def setup_window(self):
        self.window.title(self.title)
        self.window.iconbitmap(self.iconPath)
        self.window.geometry(str(self.width) + "x" + str(self.height))

    def sizable(self, is_sizable: bool=True):
        self.window.resizable(is_sizable, is_sizable)
    
    def fixWidth(self, fixed:bool=None):
        self.window.resizable(not(fixed))
    
    def fixHeight(self, fixed:bool=None):
        self.window.resizable(None, not(fixed))

    def show_window(self):
        self.window.mainloop()
    
    def initUi(self):
        self.master.title("Canvas")
    
    def draw_rect(self, x:int, y:int, width:int, height:int, color:str="#000"):
        canvas = Canvas()
        
        canvas.create_rectangle(x, y, width, height, outline=color, fill=color)
        
        canvas.pack(fill=BOTH, expand=1)

# ........

# Game ...

# ........

class Game:
    def __init__(self):
        self.title = "Runbang"
        self.COLS = 120
        self.ROWS = 60
        self.TILE_SCALE = 3
        self.WIDTH = self.COLS * self.TILE_SCALE
        self.HEIGHT = self.ROWS * self.TILE_SCALE
        
        self.FPS = 60
    
    def start(self):
        self.running = True
        
        self.game_loop()
    
    def game_loop(self):
        self.time_per_frame = int(1000000000 / self.FPS)
        self.delta = self.time_per_frame
        self.current_time = datetime.datetime.now()
        self.time_to_next_frame = self.current_time + self.time_per_frame
        while (self.running):
            ...
    
    def update(self):
        ...
    
    def draw_components(self):
        ...

def main():
    ...

if (__name__ == "__main__"):
    main()
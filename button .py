import pygame 
import tools
from typing import Union,List,Tuple

class Button:
    def __init__(self,
                 window,
                 size:Union[list[int],Tuple[int,int,int]],
                 color:Union[str,Tuple[int,int,int]],
                 coordinates:Union[List[int],Tuple[int,int,int]],
                 command:callable = None,
                 background:str = None,
                 tags:str = None):
        self.SIZE_X = size[0]
        self.SIZE_Y = size[1]
        self.CORD_X = coordinates[0]
        self.CORD_Y = coordinates[1]
        self.window = window 
        self.size =(self.SIZE_X,self.SIZE_Y)
        self.color = tools.get_color(color)
        self.coodinates = [self.CORD_X,self.CORD_Y]
        self.command = command
        self.background = background
        self.tags = tags
        
    def pack(self):
        self.rect = tools.draw_rect(window=self.window,
                                    size=self.size,
                                    color=self.color,
                                    coordinates=self.coodinates,
                                    background=self.background,
                                    tags=self.tags)
    def run(self,pos:pygame.mouse):
        self.pos = pos
        self.press = tools.verify_click(self.rect, pos)
        if self.press == True:
            if self.command is not None:
                self.command()
            else:
                pass

def alight_buttons(start_coordinates:list,
                   orientation:str,
                   space:int,
                   buttons:List[Button]):
    start_coordinate = [start_coordinates[0],start_coordinates[1]]
    if orientation == "x":
        for new_but in buttons:
            new_but.coodinates[0] = start_coordinate[0]
            start_coordinate[0] = start_coordinate[0] + space + new_but.SIZE_X
            new_but.coodinates[1] = start_coordinate[1]
    if orientation == "y":
        for new_but in buttons:
            new_but.coodinates[1] = start_coordinate[1]
            start_coordinate[1] = start_coordinate[1] + space + new_but.SIZE_X
            new_but.coodinates[0] = start_coordinate[0]

def get_center_button(size_window:Union[List[int],Tuple[int,int]],
                      button:Button,
                      tags:str = "j"):
    if tags == "x":
        center = (int(size_window[0]/2 - button.SIZE_X/2), button.CORD_Y)
        return center
    if tags == "y":
        center = (button.CORD_X,int(size_window[1]/2 - button.SIZE_Y/2))
        return center
    if tags == "j":
        center = (int(size_window[0]/2 - button.SIZE_X/2),int(size_window[1]/2 - button.SIZE_Y/2))
        return center

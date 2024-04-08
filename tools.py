import pygame
from typing import Union,List,Tuple
from button import Button
@staticmethod
def get_color(name_of_color:Union[str,Tuple[int,int,int]]):
    COLORS = {"red":(255,0,0),
              "green":(0,255,0),
              "blue":(0,0,255),
              "white":(255,255,255),
              "black":(0,0,0)}
    if type(name_of_color) == str:
        name_of_color = name_of_color.lower()
        return COLORS[name_of_color]
    else:
        return name_of_color
@staticmethod
def get_image(path_image:str):
    image = pygame.image.load(path_image)
    return image

@staticmethod
def draw_rect(window,
              size:Union[List[int],Tuple[int,int,int]],
              color:Union[str,List[int],Tuple[int,int,int]],
              coordinates:Union[List[int],Tuple[int,int,int]],
              background:str,
              tags):
    rect = pygame.draw.rect(window,color,(coordinates[0],coordinates[1],size[0],size[1]))
    if background is not None:
        background = get_image(background)
        background = pygame.transform.scale(background,size)
        window.blit(background,coordinates)
    return rect
@staticmethod
def verify_click(rect:pygame.Rect,
                 position:Union[List[int],Tuple[int,int,int]]):
    clicked = rect.collidepoint(position)
    return clicked

def alight_buttons(start_coordinate:list,
                   orientation:str,
                   space:int,
                   buttons:List[Button]):
    if orientation == "x":
        for new_but in buttons:
            new_but.coodinates[0] = start_coordinate[0]
            start_coordinate[0] = start_coordinate[0] + space + new_but.SIZE_X
    if orientation == "y":
        for new_but in buttons:
            new_but.coodinates[1] = start_coordinate[1]
            start_coordinate[1] = start_coordinate[1] + space + new_but.SIZE_X
             

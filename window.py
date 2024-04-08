import pygame
from typing import Union,List,Tuple
import tools

class Window: 
    def __init__(self,
                 size:Union[List[int],Tuple[int,int,int]],
                 color:Union[str,Tuple[int,int,int]],
                 background:str = None):
        self.SIZE_X = size[0]
        self.SIZE_Y = size[1]
        self.size = (self.SIZE_X,self.SIZE_Y)
        self.color = tools.get_color(color)
        self.background = background
        self.START_COORDINATES = (0,0)
    def pack(self):
        self.window = pygame.display.set_mode(size=(self.size))
        self.window.fill(self.color)
        if self.background is not None:
            self.background = tools.get_image(self.background)
            self.background = pygame.transform.scale(self.background,self.size)
            self.window.blit(self.background,self.START_COORDINATES)
        return self.window

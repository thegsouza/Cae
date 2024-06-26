import pygame
import tools
from typing import Union, List, Tuple
pygame.init()

class Input:
    def __init__(self,
                 window,
                 size:Union[List[int],Tuple[int,int,int]],
                 coordinates:Union[List[int],Tuple[int,int,int]],
                 title:str = None,
                 background:str = None,
                 color_title:str = "black",
                 color:str = "white",
                 tags = None):
        self.window = window
        self.size = size
        self.color = tools.get_color(color)
        self.coordinates = coordinates
        self.background = background
        self.text_title = title
        self.size_title = int(20/100*size[0])
        self.color_title = color_title        
        self.tags = tags
        
    def pack(self):
        self.title = tools.insert_text(text=self.text_title,
                                       color=self.color_title,
                                       size=self.size_title,
                                       color2=self.color)
        self.rect = tools.draw_rect(window=self.window,
                                    size=self.size,
                                    color=self.color,
                                    coordinates=self.coordinates,
                                    background=self.background,
                                    tags=self.tags)
        self.grid_text = self.title.get_size()
        self.coordinates_text = [int(self.coordinates[0] + self.size[0]/2 - self.grid_text[0]/2),
                                 int(self.coordinates[1]+ self.size[1]/2 - self.grid_text[1]/2)]
        self.window.blit(self.title,self.coordinates_text)
        self.texts = ""
    def run(self,
            event):
        
        self.press = tools.verify_click(self.rect,event)
        if self.press == True:
            self.window.fill(self.color, self.rect)
            pygame.display.flip()
            self.text_return = self.get_text()
            return self.text_return
        
    def get_text(self):
        self.abnt2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'ã', 'õ', 'â',
    'ê', 'î', 'ô', 'û', 'ç',
    'Á', 'É', 'Í', 'Ó', 'Ú', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Ã', 'Õ', 'Â',
    'Ê', 'Î', 'Ô', 'Û', 'Ç', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        self.loop = True
        while self.loop:
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.breaking = tools.verify_click(self.rect,self.pos)
                    if self.breaking == True:
                        pass
                    else:
                        self.loop = False
                if events.type == pygame.KEYDOWN:
                    self.keys = pygame.key.name(events.key)
                    if self.keys in self.abnt2:
                        self.texts+=self.keys
                        self.text_blit = tools.insert_text(text=self.texts,
                                                           color=self.color_title,
                                                           size=self.size_title,
                                                           color2=self.color)
                        self.size_text_blit = self.text_blit.get_size()
                        if self.size_text_blit[0] >= self.size[0]:
                            if events.key != pygame.K_BACKSPACE or events.key != pygame.K_RETURN:
                                self.k_backspace()
                        self.window.blit(self.text_blit, (self.coordinates[0],self.coordinates_text[1]))
                        pygame.display.flip()
                    if events.key == pygame.K_RETURN:
                        self.clean()
                        return self.texts_off
                    if events.key == pygame.K_BACKSPACE:
                        self.k_backspace()
    def clean(self):
        self.title = tools.insert_text(text=self.text_title,
                                       color=self.color_title,
                                       size=self.size_title,
                                       color2=self.color)
        self.rect = tools.draw_rect(window=self.window,
                                    size=self.size,
                                    color=self.color,
                                    coordinates=self.coordinates,
                                    background=self.background,
                                    tags=self.tags)
        self.grid_text = self.title.get_size()
        self.coordinates_text = [int(self.coordinates[0] + self.size[0]/2 - self.grid_text[0]/2),
                                 int(self.coordinates[1]+ self.size[1]/2 - self.grid_text[1]/2)]
        self.window.blit(self.title,self.coordinates_text)
        self.texts_off = self.texts
        self.texts = ''
        pygame.display.flip()
    def k_backspace(self):
        self.texts = self.texts[:-1]
        self.text_blit = tools.insert_text(text=self.texts,
                                            color=self.color_title,
                                            size=self.size_title,
                                            color2=self.color)
        self.window.fill(self.color, self.rect)
        self.window.blit(self.text_blit, (self.coordinates[0],self.coordinates_text[1]))
        pygame.display.flip()

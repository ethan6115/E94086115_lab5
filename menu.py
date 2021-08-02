import pygame
import os



MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))  #import menu圖片
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))    #import upgrade button圖片
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))          #import sell button圖片

class UpgradeMenu:
    def __init__(self, x, y):
        self.__buttons = [Button(UPGRADE_IMAGE,"upgrade",x-30, y-85),Button(SELL_IMAGE,"sell",x-20, y+55)] #放入兩個bottun 
        self.x=x
        self.y=y
        self.menu_image=pygame.transform.scale(MENU_IMAGE, (200, 200))       
        self.upgrade_image=pygame.transform.scale(UPGRADE_IMAGE, (60, 35))
        self.sell_image=pygame.transform.scale(SELL_IMAGE, (40, 40))
        
        
    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, (self.x-100, self.y-100))   #畫上menu圖片
        # draw button 
        win.blit(self.upgrade_image, (self.x-30, self.y-85))  #畫上upgrade button圖片
        win.blit(self.sell_image, (self.x-20, self.y+55))     #畫上sell button圖片
        


    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons  #return button list


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        
        self.bottun_rect=pygame.Rect(x, y,60, 50)  #創造一個rect，大小約為bottun的大小

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        
        return self.bottun_rect.collidepoint(x, y)  #利用創造的rect來判斷是否有典籍到按鈕

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        
        return self.name   #回傳按鈕的名字
     






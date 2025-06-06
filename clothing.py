import pygame
from image_scaler import scale_image_by_height

class ClothingItem: 
    def __init__(self, name, image_path, wear_pos, icon_height = 150):
        self.name = name
        
        self.image = pygame.image.load(image_path)
        self.image = scale_image_by_height(self.image, 700)
        self.icon = self.load_icon(image_path, icon_height)
        self.icon_rect = None
        self.wear_pos = wear_pos
        self.active = False
    
    def load_icon(self, image_path, icon_height):
        icon_path = image_path[:-4] + "Icon.png"
        try:
            icon_image = pygame.image.load(icon_path)
        except pygame.error as e:
            print(f"Failed to load icon: {icon_path}, Error: {e}")
            raise
        return scale_image_by_height(icon_image, icon_height)

        #next :
        # 1. done button changes game view to final (new file), the selected outfit should be displayed.
        # 2.back button to play screen
        # 3. add attributes to clothes: color and style :) 

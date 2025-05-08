import pygame
import sys 
from clothing import ClothingItem
from image_scaler import scale_image_by_height

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Star up")

character = pygame.image.load("images/ineBase.png")
hair = pygame.image.load("images/ineHair.png")
name = pygame.image.load("images/inerysBtn.png")

character = scale_image_by_height(character, 700)
hair = scale_image_by_height(hair, 700)
name = scale_image_by_height(name, 80)

clothes = [
    ClothingItem("PJ top","images/inePjTop.png", (850, -30)),
    ClothingItem("PJ bottoms", "images/inePjBot.png", (850,-30))
    # more clothes here
]

icon_spacing = 10
icons_per_row = 3
icon_x_start = 50
icon_y_start = 90

icon_x = icon_x_start
icon_y = icon_y_start

for index, item in enumerate(clothes):
    item.icon_rect = item.icon.get_rect(topleft=(icon_x,icon_y))
    icon_x += item.icon_rect.width + icon_spacing

    if(index + 1)% icons_per_row == 0:
        icon_x = icon_x_start
        icon_y += item.icon_rect.height + icon_spacing

font = pygame.font.Font(None,74)

def start_screen():
    screen.fill((255, 182, 193)) #pozadi

    play_button = pygame.image.load("images/playBtn.png")
    play_button = scale_image_by_height(play_button, 400)
    
    play_button_rect = play_button.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(play_button, play_button_rect)
    pygame.display.update()

    return play_button_rect


def game_screen():
    global active_ine_pj_top

    while True:
        screen.fill((255, 182, 193))
        screen.blit(character, (850, -30))
        name_rect = name.get_rect(center=(screen.get_width() // 2, 40))
        screen.blit(name, name_rect)

        for item in clothes:
            if item.active:
                screen.blit(item.image, item.wear_pos)
        
        screen.blit(hair, (850, -30))
        
        for item in clothes:
            pygame.draw.rect(screen, (255, 106, 130), item.icon_rect, border_radius=25)
            screen.blit(item.icon, item.icon_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for item in clothes:
                    if item.icon_rect.collidepoint(event.pos):
                        item.active = not item.active
        pygame.display.update()

def main():
    in_game = False

    while True:
        if not in_game:
            play_button_rect = start_screen() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        in_game = True 
        else:
            game_screen()  


if __name__ == "__main__":
    main()
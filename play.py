import pygame
import sys 
from clothing import ClothingItem
from image_scaler import scale_image_by_height

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Star up")

character = pygame.image.load("images/ineBase.png")
hair = pygame.image.load("images/ineHair.png")

character = scale_image_by_height(character, 700)
hair = scale_image_by_height(hair, 700)

clothes = [
    ClothingItem("PJ top","images/inePjTop.png", (850, -70)),
    ClothingItem("PJ bottoms", "images/inePjBot.png", (850,-70))
    # more clothes here
]

icon_spacing = 10
icon_x = 50
icon_y = 50

for item in clothes:
    item.icon_rect = item.icon.get_rect(topleft=(icon_x, icon_y))
    icon_x += item.icon_rect.width + icon_spacing

font = pygame.font.Font(None,74)

def start_screen():
    screen.fill((255, 182, 193)) #pozadi

    play_button = pygame.Rect(300, 250, 200, 80)
    pygame.draw.rect(screen, (182, 230, 255), play_button)
    text = font.render("Play", True, (255,255,255))
    screen.blit(text,(play_button.x + 60, play_button.y + 20))

    pygame.display.update()

    return play_button

def game_screen():
    global active_ine_pj_top

    while True:
        screen.fill((255, 182, 193))
        screen.blit(character, (850, -70))
        screen.blit(hair, (850, -70))

        for item in clothes:
            if item.active:
                screen.blit(item.image, item.wear_pos)
        
        for item in clothes:
            pygame.draw.rect(screen, (255, 106, 130), item.icon_rect)
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
            play_button = start_screen() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        in_game = True 
        else:
            game_screen()  


if __name__ == "__main__":
    main()
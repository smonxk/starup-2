import pygame

def scale_image_by_height(image, target_height):
    original_width, original_height = image.get_size()
    aspect_ratio = original_width / original_height
    new_width = int(target_height * aspect_ratio)
    return pygame.transform.scale(image, (new_width, target_height))
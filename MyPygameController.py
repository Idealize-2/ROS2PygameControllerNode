# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.joystick.init()
Joy = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(Joy)
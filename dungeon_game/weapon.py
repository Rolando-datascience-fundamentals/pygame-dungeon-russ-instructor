from typing import Optional
import pygame
import math
import constants as cons
from character import Character


class Arrow(pygame.sprite.Sprite):

    def __init__(self, image: pygame.Surface, x: int, y, angle: float):
        pygame.sprite.Sprite.__init__(self)
        self.__original_image = image
        self.__angle = angle
        self.__image = pygame.transform.rotate(self.original_image, self.angle)
        self.__rect = self.image.get_rect()
        self.__rect.center = (x, y)


class Weapon():
    def __init__(self, image: pygame.Surface, arrow_image: pygame.Surface):
        self.__original_image = image
        self.__angle = 0
        self.__image = pygame.transform.rotate(
            self.__original_image, self.__angle)
        self.__arrow_image = arrow_image
        self.__rect = self.__image.get_rect()

    def update(self, player: Character) -> Optional[Arrow]:
        self.__rect.center = player.rect.center
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.__rect.centerx
        # negative because pygame and coordinates increase down the screen
        y_dist = -(pos[1] - self.__rect.centery)
        self.__angle = math.degrees(math.atan2(y_dist, x_dist))

        # get mouseclick
        if pygame.mouse.get_pressed()[0]:
            arrow = Arrow(self.__arrow_image,
                          self.__rect.centerx, self.__rect.centery, self.__angle)
        return arrow

    def draw(self, surface: pygame.Surface):
        self.__image = pygame.transform.rotate(
            self.__original_image, self.__angle)
        coordinates = (self.__rect.centerx - int(self.__image.get_width()/2),
                       self.__rect.centery - int(self.__image.get_height()/2))
        surface.blit(self.__image, coordinates)
        pygame.draw.rect(surface, cons.GREEN, self.__rect, 1)

import os
import pygame
  
BASE_IMG_PATH = 'assets/images/'



def load_image(path,size=None):
    if size:
        img = pygame.transform.scale(pygame.image.load(BASE_IMG_PATH + path).convert_alpha(),size)
    else:
        img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    return img

def load_images(path,size=None):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name,size=size))
    return images

class Bar:
    def __init__(self, pos, size) -> None:
        self.pos = list(pos)
        self.size = list(size)
        
    def draw(self, surface,ratio):
        size = list(self.size)
        size[1] *= ratio
        pygame.draw.rect(surface,(255,255,255),(self.pos[0],self.pos[1]-size[1],*size))
        pygame.draw.rect(surface,(255,255,255),(self.pos[0],self.pos[1]-self.size[1],*self.size),2)


class Bar:
    def __init__(self, pos, size):
        self.pos = list(pos)  # Convert position to a list
        self.size = list(size)  # Convert size to a list

    def draw(self, surface, ratio):
        # Adjust the size of the bar based on the provided ratio
        size = list(self.size)
        size[1] *= ratio

        # Draw the filled rectangle representing the bar
        pygame.draw.rect(surface, (255, 255, 255), (self.pos[0], self.pos[1] - size[1], *size))

        # Draw the outline of the bar
        pygame.draw.rect(surface, (255, 255, 255), (self.pos[0], self.pos[1] - self.size[1], *self.size), 2)

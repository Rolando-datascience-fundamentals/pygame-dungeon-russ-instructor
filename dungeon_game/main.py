import pygame
import constants as cons
from character import Character
from weapon import Weapon

pygame.init()

# setting the screen size
screen = pygame.display.set_mode((cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT))
# changing the game title
pygame.display.set_caption("Dungeon Crawler")

# create clock for maintaining frame rate
clock = pygame.time.Clock()

# define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# helper function to scale image


def scale_img(image: pygame.Surface, scale: float):
    """
    This function generate a image with the scale modifyed
    """
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))


# load weapon images
bow_image = scale_img(pygame.image.load(
    "assets/images/weapons/bow.png").convert_alpha(), cons.WEAPON_SCALE)
arrow_image = scale_img(pygame.image.load(
    "assets/images/weapons/arrow.png").convert_alpha(), cons.WEAPON_SCALE)

# load character images
mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin",
             "muddy", "tiny_zombie", "big_demon"]

animation_types = ["idle", "run"]

for mob in mob_types:
    # load images
    animation_list = []
    for animation in animation_types:
        # reset temporary list of images
        temp_list = []
        for i in range(4):
            # load character image
            image = pygame.image.load(
                f"assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
            # modifying scale image
            image = scale_img(image, cons.SCALE)
            temp_list.append(image)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)

# create player
player = Character(100, 100, mob_animations, 0)

# create player's weapon
bow = Weapon(bow_image, arrow_image)

# main game loop
run = True
while run == True:
    # control frame rate
    clock.tick(cons.FPS)
    screen.fill(cons.BG)

    # calculate player movement
    dx = 0
    dy = 0

    if moving_right == True:
        dx = cons.SPEED
    if moving_left == True:
        dx = -cons.SPEED
    if moving_up == True:
        dy = -cons.SPEED
    if moving_down == True:
        dy = cons.SPEED

    # move player
    player.move(dx, dy)

    # update player frame
    player.update()
    bow.update(player)

    # draw player on screen
    player.draw(screen)
    bow.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
        # keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()

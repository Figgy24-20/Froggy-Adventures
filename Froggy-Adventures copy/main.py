import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Froggy Adventures")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
     
#-----------------------------------------------------loading sprite sheets--------------------------------------------------
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites 
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)

        else:
            all_sprites[image.replace(".png", "")] = sprites 

    return all_sprites

#--------------------------------------------------fetches each block from the terran image----------------------------------------------------
def get_block(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(108, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_sky_block(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(108, 162, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_sky_block_right(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(161, 162, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_sky_block_left(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(53, 162, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_edge_right(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(161, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_edge_left(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(53, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_wall_left(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(53, 54, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_wall_right(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(161, 54, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_inside_corner_left(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(53, 108, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_inside_corner_right(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(161, 108, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_block_corner_right(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(214, 108, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_block_corner_left(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 108, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_block_center(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(108, 54, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_block_top(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(108, 108, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_block_top_left(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 161, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_block_top_right(size):
    path = join("assets", "Terrain", "Terrain5.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(214, 161, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

# ------------------------------------------Player control information-------------------------------------------------------
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0 
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0 
        self.fall_count = 0
        self.jump_count = 0  
        self.hit = False
        self.hit_count = 0

    def jump(self):
        self.y_vel = - self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True
        self.hit_count = 0

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprit_sheet = "idle"
        if self.hit:
            sprit_sheet = "run"
        if self.y_vel < 0:
            if self.jump_count == 1:
                sprit_sheet = "jump"
            elif self.jump_count ==2:
                sprit_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprit_sheet = "fall"
        elif self.x_vel != 0:
            sprit_sheet = "run"

        sprite_sheet_name = sprit_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


#--------------------------------------------------------General object info--------------------------------------------------------
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

#--------------------------------------------------------Importing block images--------------------------------------------------------
class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Sky_Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_sky_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Sky_Block_Right(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_sky_block_right(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Sky_Block_Left(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_sky_block_left(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
class Edge_Right(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_edge_right(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Edge_Left(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_edge_left(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Wall_Right(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_wall_right(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Wall_Left(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_wall_left(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
class Inside_Corner_Right(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_inside_corner_right(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Inside_Corner_Left(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_inside_corner_left(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Corner_Right(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_corner_right(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Corner_Left(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_corner_left(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Center(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_center(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Top(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_top(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Top_Right(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_top_right(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Top_Left(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_top_left(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


#--------------------------------------------------------Importing Trap images--------------------------------------------------------

class Fire(Object):    # fire trap
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def hit(self):
        self.animation_name = "hit"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0 

class Arrow(Object):    # fire trap
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "arrow")
        self.arrow = load_sprite_sheets("Traps", "Arrow", width, height)
        self.image = self.arrow["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def hit(self):
        self.animation_name = "hit"

    def loop(self):
        sprites = self.arrow[self.animation_name]
        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0 

#-----------------------------------------------------------Background image of clouds---------------------------------------------------- -------
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height  = image.get_rect()
    tiles = []

    for i in  range(WIDTH // width +1):
        for j in range(HEIGHT // height +1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, player, objects, offset_x):
    for tile in background:
            window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    pygame.display.update()

#---------------------------------------------------------------------Player movement---------------------------------------–

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
        
            collided_objects.append(obj)

    return collided_objects 

def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = 0
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object

def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    veritical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *veritical_collide]
    for obj in to_check:
        if obj and obj.name == "arrow":
            player.make_hit()


#-----------------------------------------------------------------Main Window---------------------------------------
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Clouds.png")

    block_size = 94

    player = Player(200, HEIGHT - (block_size * 3), 50, 50)
#   player = Player(block_size * 24, HEIGHT - (block_size * 7), 50, 50)
    
    arrow = Arrow(block_size * 23, HEIGHT - (block_size * 6), 18, 18)

    floor = [Block(i * block_size, HEIGHT - block_size, block_size) 
             for i in range((block_size * 28), (block_size * 33))]
    # start_wall = [Wall_Right(i * block_size, WIDTH - block_size, block_size) 
    #         for i in range(0, HEIGHT // block_size)]
    #-----------------------------------------------------------------------------------objects -------------------------------------------
    objects = [
    #   *floor, 
    #   *start_wall, 
    # ----------------------------------------------- Left Wall ---------------------------------------
        Wall_Right(0, HEIGHT - block_size * 2, block_size), 
        Wall_Right(0, HEIGHT - block_size * 3, block_size), 
        Wall_Right(0, HEIGHT - block_size * 4, block_size), 
        Wall_Right(0, HEIGHT - block_size * 5, block_size), 
        Wall_Right(0, HEIGHT - block_size * 6, block_size), 
        Wall_Right(0, HEIGHT - block_size * 7, block_size), 
        Wall_Right(0, HEIGHT - block_size * 8, block_size), 
        Wall_Right(0, HEIGHT - block_size * 9, block_size),  

    # ----------------------------------------------------------------- Floor ----------------------
        Inside_Corner_Right(0, HEIGHT - block_size, block_size),
        Block_Corner_Right(block_size, HEIGHT - block_size, block_size),
        Block(block_size * 2, HEIGHT - block_size, block_size),
        Block(block_size * 3, HEIGHT - block_size, block_size),
        Block_Corner_Left(block_size * 4, HEIGHT - block_size, block_size),
        Inside_Corner_Left(block_size * 5, HEIGHT - block_size, block_size),
        Inside_Corner_Right(block_size * 6, HEIGHT - block_size, block_size),
        Block_Corner_Right(block_size * 7, HEIGHT - block_size, block_size),
        Edge_Right(block_size * 8, HEIGHT - block_size, block_size),

        Edge_Left(block_size * 12, HEIGHT - block_size, block_size),
        Block(block_size * 13, HEIGHT - block_size, block_size),
        Edge_Right(block_size * 14, HEIGHT - block_size, block_size),

        Edge_Left(block_size * 20, HEIGHT - block_size, block_size),
        Block(block_size * 21, HEIGHT - block_size, block_size),
        Block(block_size * 22, HEIGHT - block_size, block_size),
        Block(block_size * 23, HEIGHT - block_size, block_size),
     #   Block(block_size * 24, HEIGHT - block_size, block_size),
        Edge_Right(block_size * 24, HEIGHT - block_size, block_size),

        Edge_Left(block_size * 27, HEIGHT - block_size, block_size),
        Block(block_size * 28, HEIGHT - block_size, block_size),
        Block(block_size * 29, HEIGHT - block_size, block_size),
        Block(block_size * 30, HEIGHT - block_size, block_size),
        Block(block_size * 31, HEIGHT - block_size, block_size),
        Block(block_size * 32, HEIGHT - block_size, block_size),
        Block(block_size * 33, HEIGHT - block_size, block_size),
        
        Block_Corner_Left(block_size * 34, HEIGHT - block_size, block_size),
        Inside_Corner_Left(block_size * 35, HEIGHT - block_size, block_size),
        Block_Center(block_size * 36, HEIGHT - block_size, block_size),
        Block_Center(block_size * 37, HEIGHT - block_size, block_size),
        Block_Center(block_size * 38, HEIGHT - block_size, block_size),
        Block_Center(block_size * 39, HEIGHT - block_size, block_size),
        Block_Center(block_size * 40, HEIGHT - block_size, block_size),

    #-------------------------------------------------------------------------Terrain ----------------------------------------
        Edge_Left(block_size * 5, HEIGHT - block_size * 2, block_size),
        Edge_Right(block_size * 6, HEIGHT - block_size * 2, block_size),

        # ------ Middle Chunk --------

        Edge_Left(block_size * 28, HEIGHT - block_size * 8, block_size),
        Block(block_size * 29, HEIGHT - block_size * 8, block_size),
        Edge_Right(block_size * 30, HEIGHT - block_size * 8, block_size),

#        Wall_Left(block_size * 28, HEIGHT - block_size * 8, block_size),
#        Block_Center(block_size * 29, HEIGHT - block_size * 8, block_size),
#        Wall_Right(block_size * 30, HEIGHT - block_size * 8, block_size),

        Wall_Left(block_size * 28, HEIGHT - block_size * 7, block_size),
        Block_Center(block_size * 29, HEIGHT - block_size * 7, block_size),
        Wall_Right(block_size * 30, HEIGHT - block_size * 7, block_size),

        Wall_Left(block_size * 28, HEIGHT - block_size * 6, block_size),
        Block_Center(block_size * 29, HEIGHT - block_size * 6, block_size),
        Wall_Right(block_size * 30, HEIGHT - block_size * 6, block_size),

        Edge_Left(block_size * 22, HEIGHT - block_size * 5, block_size),
        Block(block_size * 23, HEIGHT - block_size * 5, block_size),
        Block(block_size * 24, HEIGHT - block_size * 5, block_size),
        Block(block_size * 25, HEIGHT - block_size * 5, block_size),
        Block(block_size * 26, HEIGHT - block_size * 5, block_size),
        Block_Corner_Left(block_size * 27, HEIGHT - block_size * 5, block_size),
        Inside_Corner_Left(block_size * 28, HEIGHT - block_size * 5, block_size),
        Block_Center(block_size * 29, HEIGHT - block_size * 5, block_size),
        Wall_Right(block_size * 30, HEIGHT - block_size * 5, block_size),

        Wall_Left(block_size * 22, HEIGHT - block_size * 4, block_size),
        Block_Center(block_size * 23, HEIGHT - block_size * 4, block_size),
        Block_Center(block_size * 24, HEIGHT - block_size * 4, block_size),
        Block_Center(block_size * 25, HEIGHT - block_size * 4, block_size),
        Block_Center(block_size * 26, HEIGHT - block_size * 4, block_size),
        Block_Center(block_size * 27, HEIGHT - block_size * 4, block_size),
        Block_Center(block_size * 28, HEIGHT - block_size * 4, block_size),
        Block_Center(block_size * 29, HEIGHT - block_size * 4, block_size),
        Wall_Right(block_size * 30, HEIGHT - block_size * 4, block_size),

        Block_Top_Left(block_size * 22, HEIGHT - block_size * 3, block_size),
        Block_Top(block_size * 23, HEIGHT - block_size * 3, block_size),
        Block_Top(block_size * 24, HEIGHT - block_size * 3, block_size),
        Block_Top(block_size * 25, HEIGHT - block_size * 3, block_size),
        Block_Top(block_size * 26, HEIGHT - block_size * 3, block_size),
        Block_Top(block_size * 27, HEIGHT - block_size * 3, block_size),
        Block_Top(block_size * 28, HEIGHT - block_size * 3, block_size),
        Block_Top(block_size * 29, HEIGHT - block_size * 3, block_size),
        Block_Top_Right(block_size * 30, HEIGHT - block_size * 3, block_size),

        Wall_Left(block_size * 35, HEIGHT - block_size * 2, block_size),
        Block_Center(block_size * 36, HEIGHT - block_size * 2, block_size),
        Block_Center(block_size * 37, HEIGHT - block_size * 2, block_size),
        Block_Center(block_size * 38, HEIGHT - block_size * 2, block_size),
        Block_Center(block_size * 39, HEIGHT - block_size * 2, block_size),
        Block_Center(block_size * 40, HEIGHT - block_size * 2, block_size),

        Edge_Left(block_size * 35, HEIGHT - block_size * 3, block_size),
        Block(block_size * 36, HEIGHT - block_size * 3, block_size),
        Block(block_size * 37, HEIGHT - block_size * 3, block_size),
        Block(block_size * 38, HEIGHT - block_size * 3, block_size),
        Block_Corner_Left(block_size * 39, HEIGHT - block_size * 3, block_size),
        Inside_Corner_Left(block_size * 40, HEIGHT - block_size * 3, block_size),

    # -------------------------------------------------------------------------- Right Wall ------------------------------
        Wall_Left(block_size * 40, HEIGHT - block_size * 4, block_size),
        Wall_Left(block_size * 40, HEIGHT - block_size * 5, block_size),
        Wall_Left(block_size * 40, HEIGHT - block_size * 6, block_size),
        Wall_Left(block_size * 40, HEIGHT - block_size * 7, block_size),
        Wall_Left(block_size * 40, HEIGHT - block_size * 8, block_size),
        Wall_Left(block_size * 40, HEIGHT - block_size * 9, block_size),
        Wall_Left(block_size * 40, HEIGHT - block_size * 10, block_size),


    #-------------------------------------------------------------------------- Sky Platforms -----------------------------
        Sky_Block_Left(block_size * 8, HEIGHT - block_size * 4, block_size),
        Sky_Block(block_size * 9, HEIGHT - block_size * 4, block_size),
        Sky_Block_Right(block_size * 10, HEIGHT - block_size * 4, block_size),

        Sky_Block_Left(block_size * 12, HEIGHT - block_size * 6, block_size),
        Sky_Block(block_size * 13, HEIGHT - block_size * 6, block_size),
        Sky_Block_Right(block_size * 14, HEIGHT - block_size * 6, block_size),

        Sky_Block_Left(block_size * 16, HEIGHT - block_size * 3, block_size),
        Sky_Block_Right(block_size * 17, HEIGHT - block_size * 3, block_size),

 #       Block_Corner_Right(block_size * 31, HEIGHT - block_size * 5, block_size),
        Sky_Block_Right(block_size * 32, HEIGHT - block_size * 5, block_size),

  #      Sky_Block_Left(block_size * 34, HEIGHT - block_size * 9, block_size),
  #      Sky_Block_Right(block_size * 35, HEIGHT - block_size * 9, block_size),

        Sky_Block_Left(block_size * 35, HEIGHT - block_size * 7, block_size),
        Sky_Block(block_size * 36, HEIGHT - block_size * 7, block_size),
        Sky_Block_Right(block_size * 37, HEIGHT - block_size * 7, block_size),

    #---------------------------------------------------------------- Traps -----------------------------
        arrow
        ]

    offset_x = 0
#    offset_x = block_size * 20
    scroll_area_width = 300

    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        arrow.loop()
        handle_move(player, objects) 
        draw(window, background, bg_image, player, objects, offset_x)

        if offset_x >=0 and (((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0)):
            offset_x += player.x_vel

        if offset_x < 0:
            offset_x = 0 

        if offset_x > (block_size * 30):
            offset_x = (block_size * 30)


        if player.rect.y > HEIGHT:
            player = Player(200, HEIGHT - (block_size * 3), 50, 50)
            while offset_x > 0:
                offset_x = offset_x - 1
    #        player.rect = 80
     #       player.y = 80,  

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)

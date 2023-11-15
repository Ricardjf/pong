# setup
import pygame, sys

# functions

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if (ball.top <= 0) or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if (ball.left <= 0) or (ball.right >= screen_width):
        ball_speed_x *= -1
    if ball.colliderect(player) or ball.colliderect (opponent):
        ball_speed_x *= -1
    
def player_animation():
    player.y += player_speed 
    
    if player.top <= 0: 
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.y += ball.y

    if opponent.bottom > ball.y: 
       opponent.y -= opponent_speed

    if opponent.top <= 0: 
        opponent.top + 0 

    if opponent.bottom == screen_height:
       opponent.bottom = screen_height

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey4')
light_purple = (203, 195, 227)
Cyber_yellow = (255, 201, 0)
red = ((255, 0, 0))


# game rectangles
left_ball = (screen_width / 2) - 15
top_ball = (screen_height / 2)
width_ball = 30
height_ball = 30

# game player

player_left = screen_width - 100
player_top = (screen_height / 2) - 70
width_player = 10
height_player = 140

#opponent 

opponent_left = screen_width - 1200
opponent_top = (screen_height / 2) - 70
width_opponent = 10
height_opponent = 140

#central line
central_line_left = screen_width/2
central_line_top = 0 


ball = pygame.Rect(left_ball, top_ball, width_ball, height_ball)
player = pygame.Rect(player_left, player_top, width_player, height_player)
opponent = pygame.Rect(opponent_left, opponent_top, width_opponent, height_opponent)

# Game variables
ball_speed_x = 10
ball_speed_y = 10
player_speed = 0
opponent_speed = 0

control = True
while control:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
               player_speed -= 40
            if event.key == pygame.K_DOWN:
               player_speed += 40

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_UP:
               player_speed += 40
            if event.key == pygame.K_DOWN:
               player_speed -= 40

    # game logic
    ball_animation()
    player_animation()
    opponent_animation()

    # elements
    screen.fill(bg_color)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, Cyber_yellow, player)
    pygame.draw.rect(screen, red, opponent)
    # Central line

    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width/2, screen_height))

    pygame.display.flip()
    clock.tick(60)
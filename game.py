import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong Game')

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 패들 설정
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
paddle_speed = 5

left_paddle = pygame.Rect(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 30 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 설정
ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 3 * random.choice((1, -1))
ball_speed_y = 3 * random.choice((1, -1))
ball_speed_increase = 0.5

# 점수
left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)
winning_score = 10

# 게임 루프
clock = pygame.time.Clock()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_x = 3 * random.choice((1, -1))
    ball_speed_y = 3 * random.choice((1, -1))

def paddle_ball_interaction(paddle):
    global ball_speed_x, ball_speed_y
    # 충돌 위치에 따라 공의 방향과 속도 조정
    hit_pos = (ball.centery - paddle.centery) / (PADDLE_HEIGHT / 2)
    ball_speed_x *= -1
    ball_speed_y += hit_pos
    ball_speed_x *= 1 + ball_speed_increase
    ball_speed_y *= 1 + ball_speed_increase

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += paddle_speed

    # 공 이동
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 화면 상단/하단에서 튕기기
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # 공이 패들에 닿으면 반사
    if ball.colliderect(left_paddle):
        paddle_ball_interaction(left_paddle)
    if ball.colliderect(right_paddle):
        paddle_ball_interaction(right_paddle)

    # 점수 업데이트 및 리셋
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= SCREEN_WIDTH:
        left_score += 1
        reset_ball()

    # 승리 조건
    if left_score >= winning_score or right_score >= winning_score:
        winner_text = "Left Player Wins!" if left_score >= winning_score else "Right Player Wins!"
        text = font.render(winner_text, True, WHITE)
        screen.fill(BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    # 화면에 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    left_text = font.render(f"{left_score}", True, WHITE)
    right_text = font.render(f"{right_score}", True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(right_text, (SCREEN_WIDTH * 3 // 4, 20))

    pygame.display.flip()
    clock.tick(60)

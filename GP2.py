import pygame
from pygame.locals import *

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 두 개의 사각형 정보
rect1 = pygame.Rect(200, 200, 50, 100)
rect2 = pygame.Rect(300, 300, 80, 60)

# 사각형 이동 속도
speed = 5

# 게임 루프
while True:
    screen.fill((255, 255, 255))

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        rect1.x -= speed
    if keys[K_RIGHT]:
        rect1.x += speed
    if keys[K_UP]:
        rect1.y -= speed
    if keys[K_DOWN]:
        rect1.y += speed

    # 충돌 감지
    collision = rect1.colliderect(rect2)

    # 충돌이 감지된 경우 두 도형을 모두 빨간색으로 변환
    if collision:
        pygame.draw.rect(screen, (255, 0, 0), rect1)
        pygame.draw.rect(screen, (255, 0, 0), rect2)
    else:
        pygame.draw.rect(screen, (0, 255, 0), rect1)
        pygame.draw.rect(screen, (0, 0, 255), rect2)
        
    # 각 사각형의 네 꼭지점 좌표 계산
    vertices1 = [(rect1.topleft, rect1.topright), (rect1.topright, rect1.bottomright), 
                 (rect1.bottomright, rect1.bottomleft), (rect1.bottomleft, rect1.topleft)]
    
    vertices2 = [(rect2.topleft, rect2.topright), (rect2.topright, rect2.bottomright), 
                 (rect2.bottomright, rect2.bottomleft), (rect2.bottomleft, rect2.topleft)]
    
    # 각 꼭지점을 연장하여 선 그리기 (양 방향)
    for vertex in vertices1 + vertices2:
        for i in range(2):  # 양 방향 그리기 위해 반복
            x_diff = vertex[1][0] - vertex[0][0]
            y_diff = vertex[1][1] - vertex[0][1]
            
            # 선의 끝점 좌표 계산
            end_x = vertex[1][0] + x_diff * (-1 if i == 0 else 1) * 10000
            end_y = vertex[1][1] + y_diff * (-1 if i == 0 else 1) * 10000
            
            pygame.draw.line(screen, (255, 255, 0), vertex[0], (end_x, end_y), 2)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
    clock.tick(60)

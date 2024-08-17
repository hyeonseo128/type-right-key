import pygame
import random
import string

# 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Type the Letter Game')

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# 폰트 설정
font = pygame.font.SysFont(None, 74)
small_font = pygame.font.SysFont(None, 36)

def show_start_screen():
    screen.fill(WHITE)
    title_text = font.render('Type the Letter', True, BLACK)
    game_text = font.render('Game', True, BLACK)  # "Game" 텍스트 추가
    start_text = small_font.render('Press ENTER to Start', True, GREEN)
    
    screen.blit(title_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    screen.blit(game_text, (WIDTH // 2 - 100, HEIGHT // 2 + 10))  # "Game" 위치 조정
    screen.blit(start_text, (WIDTH // 2 - 140, HEIGHT // 2 + 70))
    pygame.display.flip()

def main_game():
    clock = pygame.time.Clock()
    running = True
    current_letter = random.choice(string.ascii_uppercase)  # 랜덤 알파벳 생성
    score = 0
    lives = 3  # 목숨 초기화
    start_time = pygame.time.get_ticks()  # 게임 시작 시간

    while running:
        screen.fill(WHITE)

        # 남은 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # 경과 시간 (초)
        remaining_time = 30 - elapsed_time  # 남은 시간 (초)

        # 게임 오버 조건
        if lives <= 0 or remaining_time <= 0:
            running = False

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.unicode.upper() == current_letter:  # 입력된 키가 랜덤 알파벳과 일치하는지 확인
                    score += 1
                    current_letter = random.choice(string.ascii_uppercase)  # 새로운 랜덤 알파벳 생성
                else:
                    lives -= 1  # 목숨 1 감소

        # 랜덤 알파벳 표시
        letter_text = font.render(current_letter, True, BLACK)
        screen.blit(letter_text, (WIDTH // 2 - 30, HEIGHT // 2 - 30))

        # 점수, 목숨, 남은 시간 표시
        score_text = small_font.render(f'Score: {score}', True, BLACK)
        lives_text = small_font.render(f'Lives: {lives}', True, BLACK)
        time_text = small_font.render(f'Time: {remaining_time}', True, BLACK)
        
        # 안내 문구를 오른쪽 위에 출력
        instruction_text1 = small_font.render("Press the keyboard button", True, BLACK)  # 첫 번째 줄
        instruction_text2 = small_font.render("matching the letter on the screen.", True, BLACK)  # 두 번째 줄

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        screen.blit(time_text, (10, 90))
        
        screen.blit(instruction_text1, (WIDTH - instruction_text1.get_width() - 10, 10))  # 첫 번째 줄
        screen.blit(instruction_text2, (WIDTH - instruction_text2.get_width() - 10, 50))  # 두 번째 줄

        pygame.display.flip()
        clock.tick(60)

    # 게임 오버 화면 표시
    screen.fill(WHITE)
    game_over_text = font.render('Game Over!', True, BLACK)
    final_score_text = small_font.render(f'Final Score: {score}', True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
    screen.blit(final_score_text, (WIDTH // 2 - 70, HEIGHT // 2 + 20))
    pygame.display.flip()

    # 잠시 대기
    pygame.time.wait(3000)

def main():
    show_start_screen()  # 시작 화면 표시
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER 키를 누르면 게임 시작
                    main_game()  # 게임으로 전환
                    show_start_screen()  # 게임이 끝나면 다시 시작 화면 표시

    pygame.quit()

if __name__ == '__main__':
    main()

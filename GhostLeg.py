``python
import random

# 참여자 수 입력받기
num_of_players = int(input("참여자 수를 입력하세요: "))

# 사다리 그리기 함수
def draw_ladder(num_of_players):
    ladder = []
    for i in range(num_of_players):
        row = []
        for j in range(num_of_players-1):
            if random.random() < 0.5:
                row.append(True) # 가로선 그리기
            else:
                row.append(False)
        ladder.append(row)
    return ladder

# 상금 또는 벌칙 설정 함수
def set_reward():
    reward = random.choice(["꽝", "1000원", "2000원", "3000원", "꽝"])
    return reward

# 게임 시작
def start_game():
    players = []
    rewards = []
    for i in range(num_of_players):
        name = input("참여자 이름을 입력하세요: ")
        players.append(name)
        rewards.append([])

    ladder = draw_ladder(num_of_players)

    for i in range(num_of_players):
        print("-" * 30)
        print(f"{players[i]} 차례입니다.")
        for j in range(num_of_players-1):
            print(f"{j+1}번째 중간선을 선택하세요.")
            direction = input("왼쪽(l) / 오른쪽(r) / 그냥 직진(s): ")
            if direction == "l":
                if ladder[i][j]:
                    print("상금:", set_reward())
                    rewards[i].append(set_reward())
                    i -= 1 # 왼쪽으로 이동
                    break
            elif direction == "r":
                if ladder[i][j+1]:
                    print("상금:", set_reward())
                    rewards[i].append(set_reward())
                    i += 1 # 오른쪽으로 이동
                    break
            else:
                if not ladder[i][j]:
                    print("상금:", set_reward())
                    rewards[i].append(set_reward())
                    break

    print("=" * 30)
    print("<게임 결과>")
    for i in range(num_of_players):
        print(f"{players[i]}: {sum(rewards[i])}원")

start_game()

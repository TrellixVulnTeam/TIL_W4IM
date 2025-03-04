# tict_8_4 바닥 공사 문제풀이
# 2022-09-23

N = int(input())

dp = [0] * N
# 한 칸일 때 채울 수 있는 경우
# 세로 막대 하나
dp[0] = 1
# 두 칸일 때 채울 수 있는 경우
# 세로 * 2, 가로 * 2, 정사각형
dp[1] = 3

# 이후 부터 N - 1 까지 순회하며
for i in range(2, N):
    # 한 칸 전 꺼에서는 세로 막대 하나 더 추가하는 경우 밖에 없으므로 그냥 더하기
    # 두 칸 전 꺼는 가로 막대 추가하는 경우와 정사각형 추가하는 경우 2가지
    # 세로의 경우 이미 이전에서 고려되었음
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[N-1])
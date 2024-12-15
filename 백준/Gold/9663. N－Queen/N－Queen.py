N = int(input())  # 체스판 크기 (N x N)

# 열, 대각선 관리
columns = [False] * N  # 열 사용 여부
left_diag = [False] * (2 * N - 1)  # 좌 대각선 (row - col)
right_diag = [False] * (2 * N - 1)  # 우 대각선 (row + col)


def backtrack(row):
    """백트래킹 함수: 한 행(row)에 퀸 배치"""
    if row == N:  # 모든 퀸을 배치한 경우
        return 1  # 경우의 수 1 반환

    total = 0
    for col in range(N):  # 현재 행(row)에서 모든 열(col) 탐색
        if not columns[col] and not left_diag[row - col + N - 1] and not right_diag[row + col]:
            # 현재 위치에 퀸 배치 가능
            columns[col] = left_diag[row - col + N - 1] = right_diag[row + col] = True  # 상태 갱신
            total += backtrack(row + 1)  # 다음 행으로 이동
            columns[col] = left_diag[row - col + N - 1] = right_diag[row + col] = False  # 상태 복구
    return total


def solution():
    return backtrack(0)  # 첫 번째 행부터 시작


print(solution())
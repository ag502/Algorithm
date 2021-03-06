from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())

    for i in range(1, N + 1):
        m_permutation(i, N, M, 0, [])


def m_permutation(cur_num, n, m, selected_num, answer):
    # 1. 체크인
    selected_num += 1
    # 2. 목적지
    answer.append(str(cur_num))
    # 3. 인접 노드 순회
    for next_cur in range(1, n + 1):
        # 4. 갈 수 있는지 검사
        if selected_num != m:
            # 5. 간다
            m_permutation(next_cur, n, m, selected_num, answer)

    # 6. 체크 아웃
    if len(answer) == m:
        print(' '.join(answer))
    answer.pop()
    selected_num -= 1


if __name__ == "__main__":
    main()

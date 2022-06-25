'''
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고,
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

첫 번째 줄에는 총 단지수를 출력하시오.
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

'''

def numbering(map: list, complex_num: int, i: int, j: int) -> int: # 단지내 집의 수 반환
    #pass
    if i < 0 or i > len(map)-1 or j < 0 or j > len(map)-1: # 현 위치가 올바른 index가 아닌경우, 종료
        return 0
    if map[i][j] != 1: # 0이거나, 다른 단지에 포함된 경우
        return 0
    map[i][j] = -complex_num # 음수로 마킹

    # 인접한 집 탐색 & 현재 집 개수 추가
    return numbering(map, complex_num, i - 1, j) + numbering(map, complex_num, i + 1, j) + numbering(map, complex_num, i, j - 1) + numbering(map, complex_num, i, j + 1) + 1


N = int(input())
map = []
for idx in range(N):
    tmp_str = input()
    tmp_lst = []
    for c in tmp_str:
        tmp_lst.append(int(c))
    map.append(tmp_lst)

complex_num = 0
house_num = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            complex_num += 1
            h = numbering(map, complex_num, i, j)
            house_num.append(h)

print(complex_num)
house_num.sort()
for n in house_num:
    print(n)


#print(map)
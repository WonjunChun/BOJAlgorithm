'''
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다.
각 보석은 무게 Mi와 가격 Vi를 가지고 있다.
상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다.
가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

모든 숫자는 양의 정수이다.

첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

'''

# 시간초과... 미해결

def jewelry_thief(jewels: list, bags: list) -> int: # 훔칠 수 있는 보석 가격의 합의 최대값 반환
    jewels.sort(key=lambda x:x[1], reverse=True) # 가격 높은 순으로 정렬
    bags.sort() # 담을 수 있는 무게 작은 순으로 정렬
    total_weight = 0

    for j in jewels:
        if bags == []: break # 보석 넣을 가방이 존재하지 않으면, 종료
        for b in range(len(bags)):
            if bags[b] >= j[0]:
                total_weight += j[1]
                bags.pop(b) # 이미 사용한 가방은 목록에서 제거
                break # bags 탐색 중단

    return total_weight


[N, K] = list(map(int, input().split(" ")))
jewels = []
bags = []
for n in range(N):
    jewel = list(map(int, input().split(" ")))
    jewels.append(jewel)

for k in range(K):
    bag = int(input())
    bags.append(bag)

print(jewelry_thief(jewels, bags))

'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
=======================================================
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
'''
def coin(N: int, K: int, Ai: list) -> int:
    #pass
    #print(N, K)
    min = 0 # 동전 개수의 최소값
    Ai.sort(reverse=True) # 제일 큰 단위가 맨앞에 오도록
    #print(Ai)
    for a in Ai:
        if K//a != 0: # a 단위의 동전으로 K값 나타낼수 있으면
            min += K//a # 동전 개수
            K -= (K//a)*a
            #print(K)
        if K == 0:
            return min


[N, K] = list(map(int, input().split(" ")))
Ai = []
for i in range(N):
    Ai.append(int(input()))
print(coin(N, K, Ai))
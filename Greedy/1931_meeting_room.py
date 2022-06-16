'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다.
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고
회의의 시작시간과 끝나는 시간이 주어진다.
시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.
'''
def meeting_room(N: int, meet_info: list) -> int:
    # 이전 회의 끝나는 시간보다 이후의 회의들 중에서
    # 가장 일찍 끝나는 회의 하나씩 append함

    prev_end_time = 0 # 이전 회의가 끝난 시간
    meet_info.sort(key=lambda x: x[0])
    meet_info.sort(key=lambda x: x[1]) #일찍 끝나는 시간 순으로 정렬
    print(meet_info)
    meet_list = []

    for i in range(N):
        if meet_info[i][0] > prev_end_time: # 시작시간이 이전 회의의 끝나는 시간보다 이후이면
            #print(i)
            #print(meet_info[i])
            meet_list.append(meet_info[i])
            prev_end_time = meet_info[i][1]
    #print(meet_list)
    return len(meet_list)

N = int(input())
meet_info = []
for i in range(N):
    meet_info.append(list(map(int, input().split(" "))))
print(meeting_room(N, meet_info))

# 어느 case가 틀렸는지 못찾겠음...
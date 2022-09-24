
import sys
input=sys.stdin.readline
# from collections import Counter 최빈값 풀이1

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

n =  int(input())
nums = []
dic = {}
for i in range(n):
    k = int(input())
    nums.append(k)
    dic[k] = dic.get(k,0)+1
# print(dic) {1: 1, 3: 1, 8: 1, -2: 1, 2: 1}
    # print(nums) [1, 3, 8, -2, 2]
print(round(sum(nums)/ n)) # 산술평균

nums.sort()
print(nums[n//2]) # 중앙값

#최빈값 풀이1
# cnt = Counter(nums).most_common(2)

# if len(nums) > 1:
#     if cnt[0][1] == cnt[1][1]:
#         print(cnt[1][0])
#     else:
#         print(cnt[0][0])
# else:
#     print(cnt[0][0])


#최빈값 풀이2
cc = []
mx = max(dic.values())
# print(mx)
for k,v in dic.items():
    if v == mx:
        cc.append(k)
cc.sort()
if len(cc) == 1:
    print(cc[0])
else:
    print(cc[1])


print(max(nums)-min(nums)) # 범위
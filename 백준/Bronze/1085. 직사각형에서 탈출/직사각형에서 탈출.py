x, y, w, h = map(int, input().split())

# 직사각형 경계선까지 갈 수 있는 거리는 x, y, w-x, h-y 중 최솟값이다.
print(min(x, y, w-x, h-y))

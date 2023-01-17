import sys

n = int(sys.stdin.readline().rstrip())
grade = []

for i in range(1, n + 1):
    person = list(sys.stdin.readline().rstrip().split())
    grade.append((person[0], int(person[1]), int(person[2]), int(person[3])))
    # 이름만 문자열, 나머지는 정수로 넣기

# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
answer = sorted(
    grade, key=lambda student: (-student[1], student[2], -student[3], student[0])
)

for student in answer:
    print(student[0])

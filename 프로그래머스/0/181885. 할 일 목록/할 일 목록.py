def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        print(int(finished[i]))
        if int(finished[i])==0:
            answer.append(todo_list[i])
    return answer
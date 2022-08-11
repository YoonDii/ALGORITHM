for _ in range(3): 
  nums = list(input()) 
  numli = [nums[0]] # 첫번째 숫자 담기
  ans = [1] # 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하기 위해 1을 저장해둠
  cnt = 1 # numli에 숫자가 하나 담겼기 때문에 cnt에 1 저장
  
  for i in range(1, 8): # 숫자는 여덟 자리의 양의 정수기 때문에 7번 반복
    if(numli[len(numli)-1] == nums[i]): # numli에 담겨있는 숫자와 현재 숫자가 같다면
      cnt += 1 # 일을 추가함
    else: # 아니라면
      numli.append(nums[i]) # 그 수를 numli에 추가하고
      ans.append(cnt) # cnt값을 ans에 저장
      cnt = 1 
  
  ans.append(cnt) # ans에 cnt다 담기
  print(max(ans)) # 그 중 가장 큰 값을 출력하기
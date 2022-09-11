while True :
  try :
    n = int(input())
    value = '1'
    while True :
      if int(value) % n == 0 :
        print(len(value))
        break
      value += '1'
  except EOFError :
    break
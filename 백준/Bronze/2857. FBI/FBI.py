noFBI = True
for i in range(1,6):
    name = input()
    # print(name)

    if 'FBI' in name:
        print(i)   
        noFBI = False
if noFBI:
    print("HE GOT AWAY!")
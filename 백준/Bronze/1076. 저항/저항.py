a = input()
b = input()
c = input()

color_ = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
             'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
             'grey': 8, 'white': 9}
 
print((color_[a] * 10 + color_[b]) * (10 ** color_[c]))
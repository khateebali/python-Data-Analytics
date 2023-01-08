from turtle import *

speed('slow')
side = 6
for i in range(side):
    forward(50)
    for i in range(4):
        forward(50)
        left(72)
        
    left(360//6)
mainloop()
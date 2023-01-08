
from turtle import *

speed('slow')
side = 6
for i in range(side):
    forward(50)
    left(360//side)
    for i in range(5):
        forward(25)
        left(72)
        write(i)
    
mainloop()
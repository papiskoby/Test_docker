
from app import *

rand_numb=[1,2]
app.random.randrange = lambda n:rand_numb.pop(0)
#assert play() == 'Hero wins'
r=app.main()
print(r)
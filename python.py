import sys
from itertools import permutations 

l=[]

def split(word): 
    return [char for char in word]  
  
for line in sys.stdin:
    l=split(line)
    l=l[:-1]
    for i in permutations(l): 
        print(''.join(i))
    del l 



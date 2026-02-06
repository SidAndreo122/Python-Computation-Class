# listcomp_vs_genexp.py
# list comprehension vs generator expression
import sys
a = [x for x in range(1000000)] #list comp
b = (x for x in range(1000000))
print('list comp byte size is ',sys.getsizeof(a))
print('generator expression byte size is ',sys.getsizeof(b))

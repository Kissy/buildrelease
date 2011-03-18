
# way1
class Directions:
    up = 0
    down = 1
    left = 2
    right =3
    
print Directions.down

# way2
dirUp, dirDown, dirLeft, dirRight = range(4)

print dirDown

# way3
import collections
dircoll=collections.namedtuple('directions', ('UP', 'DOWN', 'LEFT', 'RIGHT'))
directions=dircoll(0,1,2,3)

print directions.DOWN

# way4
def enum(args, start=0):
    class Enum(object):
        __slots__ = args.split()

        def __init__(self):
            for i, key in enumerate(Enum.__slots__, start):
                setattr(self, key, i)

    return Enum()

e_dir = enum('up down left right')

print e_dir.down

# way5
# some times we need use enum value as string
Directions = {'up':'up','down':'down','left':'left', 'right':'right'}

print Directions['down']

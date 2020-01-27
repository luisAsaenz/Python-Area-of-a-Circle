import math # Have to import math to use anything 'math.'

print('Input radius: ')
radius = int(input())
##print(radius)
if radius > 0:
    radiusSquared = math.pow(radius, 2)
    area = math.pi * radiusSquared
    print('Are of the circle is: ')
    print(area)


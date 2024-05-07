import math

#This program creates n circles and compute if they have intersect points or not.

n = int(input('How many circles are there?'))
coordinate = []
radius = []
for i in range(n):
    x = int(input(f'Tell the x coordinate of the {i+1} circle'))
    y = int(input(f'Tell the y coordinate of the {i+1} circle'))
    r = int(input(f'Tell the radius of the {i+1} circle'))
    coordinate.append([x, y])
    radius.append(r)
intersect = [[]]*n
for i in range(n):
    for j in range(i+1, n):
        distance = math.sqrt((coordinate[i][0]-coordinate[j][0])**2 + (coordinate[i][1]-coordinate[j][1])**2)
        if (radius[i]+radius[j]) >= distance:
            print(f'The {i+1} and {j+1} circles has intersect points')
            intersect[i].append(j+1)
            intersect[j].append(i+1)
counter = 0
intersectCounter = 0
mx = 0
mx_place = []
for i in range(n):
    if len(intersect[i]) == 0:
        counter += 1
    else:
        intersectCounter += 1
    if len(intersect[i]) > mx:
        mx = len(intersect[i])
print(f'{counter} circles has no intersect points with other circles')
print(f'{intersectCounter} circles has intersect points with other circles')
for i in range(n):
    if len(intersect[i]) == mx:
        mx_place.append(i+1)
print(f'These circles has the most circles intersecting them: {mx_place}')
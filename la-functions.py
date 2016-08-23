import math

# my code

def addVector(first_v, second_v):
    result_x = float(first_v[0]) + float(second_v[0])
    result_y = float(first_v[1]) + float(second_v[1])
    return round(result_x, 3), round(result_y,3)

print(addVector([8.218,-9.341],[-1.129,2.111]))

def subtractVector(first_v, second_v):
    result_x = float(first_v[0]) - float(second_v[0])
    result_y = float(first_v[1]) - float(second_v[1])
    return round(result_x, 3), round(result_y,3)

print(subtractVector([7.119,8.215],[-8.223,0.878]))

def scalarMultiply(factor, vector):
    result = list()
    for i in range(len(vector)):
        result.append(round(float(factor) * float(vector[i]),3))
    return result

print(scalarMultiply(7.41,[1.671,-1.012,-0.318]))



class Vector(object):

    def __init__(self, coordinates):
        self.coordinates = coordinates

    # Udacity code

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    # my code

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def direction(self):
        

    def __len__(self)
        return(len(self.coordinates))

    
    # udacity code

    def __str__(self):
        return 'Vector:{}'.format(self.coordinates)

    def __eq__(self,v):
        return self.coordinates == v.coordinates

v = Vector([8.218,-9.341])
w = Vector([-1.129,2.111])
print v.plus(w)

v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print v.minus(w)

v = Vector([1.671,-1.012,-0.318])
print v.times_scalar(7.41)

v = Vector([-0.221,7.437])
print v.magnitude()

v = Vector([8.813,-1.331,-6.247)]
print v.magnitude()


#module containing all class definitions
"""               Define
        Attributes:1.object
                   2.x,y,z - point coordinates
                   3.vector_x,vector_y,vector_z
        Methods    :1.__init__
                    2.__str__
                    3.distance()
                    4.fop() #foot of perpendicular
                    5.image()
                    6.ints() #intersection
                    7.angle_bisector()
"""
import math
class Define:
    def __init__(self,object,point_coordinates,vector = ()):
        if object == "point":
            self.object = object
            self.x,self.y,self.z = point_coordinates
        elif object == "line":
            self.object = "line"
            self.x,self.y,self.z = point_coordinates
            self.vector_x,self.vector_y,self.vector_z = vector
        elif object == "plane":
            self.object = "plane"
            self.x,self.y,self.z = point_coordinates
            self.vector_x,self.vector_y,self.vector_z = vector


    def __str__(self):
        if self.object == "point":
            return f"({self.x} , {self.y} , {self.z})"
        elif self.object == "line":
            return f"(x - {self.x})/{self.vector_x} = (y - {self.y})/{self.vector_y} = (z - {self.z})/{self.vector_z}"
        elif self.object == "plane":
            return f"{self.vector_x}x + {self.vector_y}y + {self.vector_z}z = {self.vector_x*self.x + self.vector_y*self.y + self.vector_z*self.z}"

    def distance(self,other):
        if self.object == "point" and other.object == "point":
            del_x = (self.x - other.x) ** 2
            del_y = (self.y - other.y) ** 2
            del_z = (self.z - other.z) ** 2
            dist = (del_x + del_y + del_z) ** 0.5
            return dist
        if self.object == "line" and other.object == "line":
            line_type = self.check_parallel(other)
            if line_type == "parallel":
                a = self.x - other.x
                b = self.y - other.y
                c = self.z - other.z
                #(a,b,c) is the vector joining two points
                dot_prod = a * self.vector_x + b * self.vector_y + c * self.vector_z
                mag = (self.vector_x ** 2 + self.vector_y ** 2 + self.vector_z ** 2 ) ** 0.5
                horizontal_comp = dot_prod / mag
                dist = (a ** 2 + b ** 2 + c ** 2 - horizontal_comp ** 2) ** 0.5
                return dist
            else:
                 a = self.x - other.x
                 b = self.y - other.y
                 c = self.z - other.z
                 p = self.vector_y * other.vector_z - self.vector_z * other.vector_y
                 q = self.vector_z * other.vector_x - self.vector_x * other.vector_z
                 r = self.vector_x * other.vector_y - self.vector_y * other.vector_x
                 dist = abs((a*p + b*q + c*r) / math.sqrt(p**2 + q**2 + r**2))
                 return dist
        if self.object == "point" and other.object == "line":
            a = self.x - other.x
            b = self.y - other.y
            c = self.z - other.z

            dot_prod = a * other.vector_x + b * other.vector_y + c * other.vector_z
            mag = math.sqrt(other.vector_x ** 2 + other.vector_y ** 2 + other.vector_z ** 2)
            horizontal_comp = dot_prod / mag
            dist = math.sqrt((a ** 2 + b ** 2 + c ** 2) - horizontal_comp ** 2)
            return dist
        
        if self.object == "point" and other.object == "plane":
            a = self.x - other.x
            b = self.y - other.y
            c = self.z - other.z

            dot_prod = a * other.vector_x + b * other.vector_y + c * other.vector_z
            mag = math.sqrt(other.vector_x ** 2 + other.vector_y ** 2 + other.vector_z ** 2)
            vertical_comp = dot_prod / mag

            dist = abs(vertical_comp)
            return dist
        
        if self.object == "plane" and other.object == "plane":
            plane_type = self.check_parallel(other)
            
            if plane_type == "parallel":
                a = self.x - other.x
                b = self.y - other.y
                c = self.z - other.z
                dot_prod = a * other.vector_x + b * other.vector_y + c * other.vector_z
                mag = math.sqrt(other.vector_x ** 2 + other.vector_y ** 2 + other.vector_z ** 2)
                vertical_comp = dot_prod / mag

                dist = abs(vertical_comp)
                return dist
            else:
                return 0
        

    def check_parallel(self,other):
        #if self.object == "line" and other.object == "line":
            if other.vector_x == 0:
                if self.vector_x != 0:
                    return "non-parallel"
                else:
                    if self.vector_y / other.vector_y == self.vector_z / other.vector_z:
                        return "parallel"
                    else:
                        return "non-parallel"
            elif other.vector_y == 0:
                if self.vector_y != 0:
                    return "non-parallel"
                else:
                    if self.vector_x / other.vectorx == self.vector_z / other.vector_z:
                        return "parallel"
                    else:
                        return "non-parallel"
            elif other.vector_z == 0:
                if self.vector_z != 0:
                    return "non-parallel"
                else:
                    if self.vector_x / other.vector_x == self.vector_y / other.vector_y:
                        return "parallel"
                    else:
                        return "non-parallel"
            else:
                if self.vector_x / other.vector_x == self.vector_y / other.vector_y and self.vector_y / other.vector_y == self.vector_z / other.vector_z:
                    return "parallel"
                else:
                    return "non-parallel"
    
    def fop(self,other):
        if self.object == "point" and other.object == "line":
            t = (other.vector_x*self.x+other.vector_y*self.y+other.vector_z*self.z-other.vector_x*other.x-other.vector_y*other.y-other.vector_z*other.z)/(other.vector_x ** 2 + other.vector_y ** 2 + other.vector_z ** 2)
            a = other.x + t * other.vector_x
            b = other.y + t * other.vector_y
            c = other.z + t * other.vector_z
            point = Define("point",(a,b,c))
            return point
        
    def image(self,other):
        if self.object == "point" and other.object == "line":
            foot = self.fop(other)
            a = 2 * foot.x - self.x
            b = 2 * foot.y - self.y
            c = 2 * foot.z - self.z
            point = Define("point",(a,b,c))
            return point


    def ints(self,other):
        if self.object == "line" and other.object == "line":
            if self.distance(other) == 0:
                if  (self.vector_x * other.vector_y - self.vector_y * other.vector_x) != 0:
                     t = (other.vector_x*(self.y - other.y) + other.vector_y*(other.x - self.x)) / (self.vector_x * other.vector_y - self.vector_y * other.vector_x)
                     a = self.x + t * self.vector_x
                     b = self.y + t * self.vector_y
                     c = self.z + t * self.vector_z
                     point = Define("point",(a,b,c))
                     return point
                elif (self.vector_x * other.vector_z - self.vector_z * other.vector_x) != 0:
                     t = (other.vector_x*(self.z - other.z) + other.vector_z*(other.x - self.x)) / (self.vector_x * other.vector_z - self.vector_z * other.vector_x)
                     a = self.x + t * self.vector_x
                     b = self.y + t * self.vector_y
                     c = self.z + t * self.vector_z
                     point = Define("point",(a,b,c))
                     return point
                else:
                    return "two lines coincide"
            else:
                return None
        
        elif self.object == "plane" and other.object == "plane":
            if self.distance(other) == 0:
                if self.check_parallel(other) == "parallel":
                    return "two planes coincide"
                else:
                    d1 = self.x * self.vector_x + self.y * self.vector_y + self.z * self.vector_z
                    d2 = other.x * other.vector_x + other.y * other.vector_y + other.z * other.vector_z
                    x1 = (self.vector_y * d2 - other.vector_y * d1) / (self.vector_x * other.vector_y - self.vector_y * other.vector_x)
                    a = (self.vector_y * other.vector_z - other.vector_y * self.vector_z) / (self.vector_x * other.vector_y - self.vector_y * other.vector_x)
                    y1 = (self.vector_x * d2 - other.vector_x * d1) / (-self.vector_x * other.vector_y + self.vector_y * other.vector_x)
                    b = (self.vector_x * other.vector_z - other.vector_x * self.vector_z) / (-self.vector_x * other.vector_y + self.vector_y * other.vector_x)
                    return f"(x + {x1}) / {a} = (y + {y1}) / {b} = z"
            else:
                return None
            
    def angle_bisector(self,other):
        if self.object == "line" and other.object == "line":
            pass



#For challenge 11,
#create a class called Sphere which takes a numeric value (could be either float or int) representing its radius when it 
#is declared.
#Sphere should have at least three methods:
#get_surface_area, which returns the surface area of the sphere
#get_volume, which returns the volume of the sphere
#set_radius, which changes the radius of the sphere (this should also result in new values being returned from the other 
#two methods).
#Feel free to set __init__ or other methods as necessary to accomplish this task. To ensure you match the test cases 
#exactly, use 3.14 as your approximation for π. The surface area of a sphere is 4*π*r^2; the volume of a sphere is 
#4/3*π*r^3.
import sys
arg1 = float(sys.argv[1])
arg2 = float(sys.argv[2])
class Sphere:
    def __init__(self, rad):
        self.rad = rad
        self.pi = 3.14

    def get_surface_area(self):
        return (4 * self.pi * self.rad ** 2)
    
    def get_volume(self):
        return (4 / 3 * self.pi * self.rad ** 3)

    def set_radius(self, rad):
        self.rad = rad
        return self.get_surface_area
sphere = Sphere(arg1)
print(sphere.get_surface_area())
print(sphere.get_volume())
sphere.set_radius(arg2)
print(sphere.get_surface_area())
print(sphere.get_volume())


# def getSurfArea(rad):
#     pi = 3.14
#     return (4 * pi * rad ** 2)
# print(getSurfArea(5.5))

# def getVolume(rad):
#     pi = 3.14
#     return (4 / 3 * pi * rad ** 3)
# print(getVolume(5.5))
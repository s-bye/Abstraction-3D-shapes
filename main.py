import random
from shapes import Sphere, Cube, Cylinder

def generate_random_shapes(n):
    shapes = []
    for _ in range(n):
        shape_type = random.choice(['sphere', 'cube', 'cylinder'])
        if shape_type == 'sphere':
            radius = random.uniform(1, 10)
            shapes.append(Sphere(radius))
        elif shape_type == 'cube':
            side = random.uniform(1, 10)
            shapes.append(Cube(side))
        elif shape_type == 'cylinder':
            radius = random.uniform(1, 10)
            height = random.uniform(1, 10)
            shapes.append(Cylinder(radius, height))
    return shapes

if __name__ == "__main__":
    shapes = generate_random_shapes(10)

    for i, shape in enumerate(shapes):
        print(f"Shape {i+1}:")
        print(f"Type: {type(shape).__name__}")
        print(f"Volume: {shape.volume():.2f}")
        print(f"Surface Area: {shape.surface_area():.2f}")
        print()

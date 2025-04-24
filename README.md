# 3D Shapes Calculator

This Python application calculates volumes and surface areas of various three-dimensional geometric shapes. It demonstrates object-oriented programming principles including inheritance, abstraction, and polymorphism through a shape class hierarchy.

## Project Overview

The application generates random 3D shapes (spheres, cubes, and cylinders) and calculates their volumes and surface areas using mathematical formulas. It showcases how to implement an abstract base class with concrete implementations for different shape types.

## Project Structure

```
3d-shapes-calculator/
├── main.py            # Entry point that generates and displays random shapes
├── shapes.py          # Contains shape class definitions and calculations
├── .gitignore         # Standard Python gitignore file
└── README.md          # Project documentation (this file)
```

## Classes and Methods

### `Shape3D` (Abstract Base Class)
The foundation for all 3D shapes with required methods:

- `volume()`: Abstract method to calculate a shape's volume
- `surface_area()`: Abstract method to calculate a shape's surface area

### `Sphere` (Extends `Shape3D`)
Represents a spherical shape:

- `__init__(radius)`: Initializes a sphere with the given radius
- `surface_area()`: Returns the surface area using formula 4πr²
- `volume()`: Returns the volume using formula (4/3)πr³

### `Cube` (Extends `Shape3D`)
Represents a cubic shape:

- `__init__(side)`: Initializes a cube with the given side length
- `surface_area()`: Returns the surface area using formula 6s²
- `volume()`: Returns the volume using formula s³

### `Cylinder` (Extends `Shape3D`)
Represents a cylindrical shape:

- `__init__(radius, height)`: Initializes a cylinder with the given radius and height
- `surface_area()`: Returns the surface area using formula 2πr(r + h)
- `volume()`: Returns the volume using formula πr²h

## How to Run

Run the application:

```bash
python main.py
```

## Sample Output

When you run the application, it will generate 10 random shapes and display their properties:

```
Shape 1:
Type: Sphere
Volume: 3923.57
Surface Area: 1203.02

Shape 2:
Type: Cube
Volume: 70.80
Surface Area: 102.68

Shape 3:
Type: Cylinder
Volume: 135.50
Surface Area: 147.78

Shape 4:
Type: Sphere
Volume: 415.65
Surface Area: 269.34

Shape 5:
Type: Sphere
Volume: 1812.90
Surface Area: 719.01

Shape 6:
Type: Sphere
Volume: 2604.55
Surface Area: 915.46

Shape 7:
Type: Cylinder
Volume: 15.14
Surface Area: 36.56

Shape 8:
Type: Cube
Volume: 2.27
Surface Area: 10.38

Shape 9:
Type: Sphere
Volume: 1061.16
Surface Area: 503.12

Shape 10:
Type: Sphere
Volume: 1220.00
Surface Area: 552.15
```

## Screenshots

### Code Execution Output
![Output](https://i.ibb.co/bR7VZQ2F/pycharm64-a-Osmylr-Pjq.png)

## Mathematical Formulas Used

### Sphere
- Volume: (4/3)πr³
- Surface Area: 4πr²

### Cube
- Volume: s³
- Surface Area: 6s²

### Cylinder
- Volume: πr²h
- Surface Area: 2πr(r + h)
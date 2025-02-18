import math

class Vector:
    def __init__(self, *arg):
        self.elements = tuple(arg)

    def __add__(self, vector1):
        if len(self.elements) != len(vector1.elements):
            raise ValueError("Vectors must have the same dimensional space")
        return Vector(*(a + b for a, b in zip(self.elements, vector1.elements)))

    def __sub__(self, vector1):
        if len(self.elements) != len(vector1.elements):
            raise ValueError("Vectors must have the same dimensional space")
        return Vector(*(a - b for a, b in zip(self.elements, vector1.elements)))

    def __mul__(self, vector1):
        if isinstance(vector1, Vector):
            if len(self.elements) != len(vector1.elements):
                raise ValueError("Vectors must have the same dimensional space")
            return sum(a * b for a, b in zip(self.elements, vector1.elements))  # Dot product returns a scalar
        elif isinstance(vector1, (int, float)):
            return Vector(*(k * vector1 for k in self.elements))
        else:
            raise TypeError("Multiplication is only supported with a scalar or another vector (dot product).")

    def __rmul__(self, scalar):
        return self * scalar  # Fix scalar multiplication order

    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.elements))  # Fix magnitude calculation
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(x / mag for x in self.elements))

    def __str__(self):
        return f"Vector {self.elements}"

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)

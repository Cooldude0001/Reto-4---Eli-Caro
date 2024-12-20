from math import degrees, acos, isclose

# Creacion de la clase punto
class Point:
    """Point class used to create points."""
    
    definition: str = """Entidad geometrica abstracta 
    que representa una ubicación en un espacio."""

    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

    def compute_distance(self, point: "Point") -> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

    def __str__ (self):
        return f"({self.x},{self.y})"
  

# Creacion de la clase linea
class Line:
    """Line class used to create lines."""

    def __init__(self, start_point: "Point", end_point: "Point"):
        self.start = start_point
        self.end = end_point
        self.length = self.compute_length()

    def compute_length(self):
        return self.start.compute_distance(self.end) 

    def compute_slope(self):
        # Cambio vertical / cambio horizontal
        return (self.start.y - self.end.y) / (self.start.x - self.end.x)

    def compute_horizontal_cross(self):
        if self.start.y * self.end.y > 0:
            return None
        if self.start.y == self.end.y:
            return None
        x_cross = self.start.x - (self.start.y * (self.end.x - self.start.x)) / (self.end.y - self.start.y)
        return Point(x_cross, 0)

    def compute_vertical_cross(self):
        if self.start.x * self.end.x > 0:
            return None
        if self.start.x == self.end.x:
            return None
        y_cross = self.start.y - (self.start.x * (self.end.y - self.start.y)) / (self.end.x - self.start.x)
        return Point(0, y_cross)
    
    def __str__(self):
        return f"Line instance defined between {self.start} and {self.end} points."


# Creacion de la clase Shape
class Shape:
    """Shape class used to create regular and irregular polygons."""

    def __init__(self, is_regular: "bool", vertices: "list[Point]"):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = self.calculate_edges ()
        self.inner_angles = self.compute_inner_angles ()

    def calculate_edges(self) -> "list[Line]":
        # This list contains the line lengths
        shape_edges = [] 
        
        for index in range(len(self.vertices)):
            start_point = self.vertices [index]
            # To avoid Indexerror exception and make last line between last and start point
            end_point = self.vertices [(index + 1) % len(self.vertices)]
            shape_edges.append(Line(start_point, end_point))
        
        if self.is_regular:
            comparison_length = shape_edges [0].length
            for edge_length in shape_edges:
                if not (isclose(comparison_length, edge_length.length, rel_tol= 1e-9)):
                    raise ValueError("Instance must be regular as specified.")
        
        return shape_edges
    
    def compute_area(self) -> "float":
        pass

    def compute_perimeter(self) -> "float":
        shape_perimeter = 0

        for edges in self.edges:
            shape_perimeter += edges.length
        return shape_perimeter
    
    def compute_inner_angles(self) -> "list":
        pass


# Creación de la clase Rectangle (hereda de Shape)
class Rectangle(Shape):
    """Rectangle class used to create rectangles, inherits methods 
    and attributes from Shape class."""

    def __init__(self, is_regular, vertices):
        if len (vertices) != 4: 
            raise ValueError("Rectangle object must have exactly 4 vertices.")
        super().__init__(is_regular, vertices)

    def compute_area(self):
        width = self.edges[0].length
        length = self.edges[1].length
        return width * length

    def compute_inner_angles(self):
        return [90, 90, 90, 90]


# Creacion de la clase Square (hereda de Rectangle)
class Square(Rectangle):
    """Square class used to create squares, inherits methods 
    and attributes from Rectangle class."""
    
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        
        # all edges must have equal length
        a, b, c, d = (edge.length for edge in self.edges)

        if self.is_regular == True:
            if not (a == b and b == c and c == d and d == a):
                raise ValueError ("Square instance must have the same length in all edges.")
        else:
            raise ValueError("Square instance must be regular.")
        

# Creación de la clase Triangle (hereda de Shape)
class Triangle(Shape):
    """Triangle class used to create triangles, inherits methods
    and attributes from Shape class."""
        
    def __init__(self, is_regular, vertices):
        if len(vertices) != 3:
            raise ValueError("Triangle instance cannot have more than 3 vertices.")
        super().__init__(is_regular, vertices)
    
    def compute_area(self):
        # Heron's formula to calculate any triangle area
        a, b, c = (edge.length for edge in self.edges) # asignation is positional
        semiperimter = (a+b+c)/2
        return (semiperimter*(semiperimter-a)*(semiperimter-b)*(semiperimter-c))**0.5
    
    def compute_inner_angles(self):
        angles = []
        a,b,c = (edge.length for edge in self.edges)
        
        a_angle = degrees(acos(((b**2 + c**2) - a**2)/(2*b*c)))
        b_angle = degrees(acos(((a**2 + c**2) - b**2)/(2*a*c)))
        c_angle = degrees(acos(((a**2 + b**2)- c**2)/(2*b*a)))
        
        angles.append (a_angle) 
        angles.append (b_angle) 
        angles.append (c_angle)
        return angles
    

# Creación de la clase Equilateral (hereda de Triangle)
class Equilateral(Triangle):
    """Equilateral class used to create equilateral triangles, inherits methods
    and attributes from Triangle class."""

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == False:
            raise ValueError("Equilateral instance must be regular.")
        
        # Equilateral triangles must have the same length in all edges
        a, b, c = (edge.length for edge in self.edges)
        
        if not (a == b and b == c):
            raise ValueError ("Equilateral instance must have the same length in all edges.")


# Creación de la clase Isosceles (hereda de Triangle)
class Isosceles(Triangle):
    """Isosceles class used to create isosceles triangles, inherits methods
    and attributes from Triangle class."""

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("Isosceles instance can't be regular.")
        
        # Check if vertices form an Isosceles triangle
        a, b, c = (edge.length for edge in self.edges)
        
        #isosceles condition is a boolean variable that determines if
        #the instance is an isosceles triangle if only 2 lengths are equal
        isosceles_condition = (
            isclose(a, b) and not isclose(b, c) or
            isclose(b, c) and not isclose(c, a) or
            isclose(a, c) and not isclose(a, b)
        )

        if not isosceles_condition:
            raise ValueError("Isosceles instance can't be constructed using the given vertices.")

# Creación de la clase Scalene (hereda de Triangle)
class Scalene(Triangle):
    """Scalene class used to create scalene triangles, inherits methods
    and attributes from Triangle class."""

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("Scalene instance can't be regular.")
        
        # Scalene triangles has different edge lengths
        a, b, c = (edge.length for edge in self.edges)

        # scalene_condition verifies if all edge lengths are different
        scalene_condition = (
            not isclose (a,b) and 
            not isclose (b,c) and 
            not isclose (a,c)
        )

        if not scalene_condition:
            raise ValueError("Scalene instance can't be constructed using the given vertices.")


# Creación de la clase Trirectangle (hereda de Triangle)
class Trirectangle(Triangle):
    """Trirectangle class used to create right triangles, inherits methods
    and attributes from Triangle class."""

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        # check if the shape is regular
        if self.is_regular == True:
            raise ValueError("Trirectangle class cannot be regular")
        
        # Returns true if length of c**2 is equal to a**2 + b**2
        # uses Pytagora's theorem
        
        a, b, c = sorted(edge.length for edge in self.edges)
        # In this case it will evalue if the sum of squares is "more of less"
        # equal to c**2
        if not (c**2 - (10**-9)) < (a**2 + b**2) <= c**2:
            raise ValueError("Trirectangle instance cannot be formed with the given vertices.")
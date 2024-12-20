## Parte 1: Modelado de clases geometricas
### Clases modeladas:

 Point :
Clase que representa un punto en un espacio bidimensional. Tiene atributos  x  y  y  para definir su ubicación. Los métodos incluyen  move  para cambiar la posición del punto,  reset  para reiniciarlo a  (0, 0) ,  compute_distance  para calcular la distancia desde otro punto, y un método  __str__  para representar el punto como una cadena de texto.

 Line :
Clase que representa una línea definida entre dos puntos ( start  y  end ). Tiene métodos para calcular la longitud de la línea, el ángulo con respecto al eje horizontal y vertical, así como el cruce horizontal y vertical. También incluye un método  __str__  para representar la línea como una instancia entre los puntos de inicio y fin.

 Shape :
Clase abstracta que representa una figura geométrica. Incluye métodos para calcular el perímetro y se deben implementar métodos específicos para calcular el área e los ángulos internos. La clase mantiene una lista de vértices y líneas que la conforman.

 Rectangle  (hereda de  Shape ):
Clase específica para crear rectángulos. Verifica que los vértices formen exactamente un rectángulo y proporciona métodos para calcular el área y los ángulos internos (todos son  90 grados ).

 Square  (hereda de  Rectangle ):
Clase específica para crear cuadrados. Verifica que todos los vértices sean iguales en longitud y se asegura de que sea un cuadrado regular antes de calcular el área y los ángulos internos.

 Triangle  (hereda de  Shape ):
Clase específica para crear triángulos. Puede ser regular, isósceles o escaleno. Se utilizan condiciones específicas para verificar si el triángulo cumple con estas características y calcular su área y ángulos internos.

 Equilateral  (hereda de  Triangle ):
Clase para crear triángulos equiláteros. Todos los vértices deben ser iguales y todas las longitudes de los lados deben coincidir para que sea considerado equilátero.

 Isosceles  (hereda de  Triangle ):
Clase para crear triángulos isósceles. Verifica que dos de los vértices tengan la misma longitud, pero el tercero sea diferente.

 Scalene  (hereda de  Triangle ):
Clase para crear triángulos escaleno. Todos los vértices deben tener longitudes diferentes.

 Trirectangle  (hereda de  Triangle ):
Clase para crear triángulos rectángulos. Utiliza el teorema de Pitágoras para verificar que la figura cumpla con esta característica y no sea regular.

## Parte 2: caso del restaurante - _revisitado_
### Clases que conforman el caso del restaurante
MenuItem:
Clase base que representa un elemento del menú, con atributos como nombre, precio y cantidad, tiene métodos para calcular el precio total basado en la cantidad pedida

Subclases de MenuItem:

1. Beverage: Representa bebidas con tamaños como pequeño, mediano o grande.
2. Appetizer: Maneja aperitivos y porciones específicas, como "6 piezas" o "1 plato".
3. MainCourse: Para platos principales, con métodos para añadir acompañamientos (e.g., salsas).

Order:
Clase que administra los pedidos de clientes, perimite añadir elementos al pedido, calcular el precio total, y aplicar descuentos.

Administracion de descuentos:
- Descuento del 10% en bebidas si el pedido incluye un plato principal.
- Descuento del 10% adicional si el pedido tiene tres o más ítems.

Payment:
Payment es una clase que define un método genérico de pago, en este caso por tarjeta y en efectivo.

Subclases de Payment:
CardPayment: Procesa pagos con tarjeta mostrando los últimos dígitos del número de tarjeta.
CashPayment: Permite pagos en efectivo, verificando si hay suficiente dinero entregado y devolviendo el cambio correspondiente.

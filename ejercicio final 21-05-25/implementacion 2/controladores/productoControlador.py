from modelo.producto import Producto

class ProductoControlador:
    def __init__(self):
        self.productos = []
    
    def crear_producto(self, nombre, precio, cantidad):
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)
        return producto
    
    def get_nombre(self, producto):
        return producto._nombre
    
    def get_precio(self, producto):
        return producto._precio
    
    def get_cantidad(self, producto):
        return producto._cantidad
    
    def formato_str(self, producto):
        return f"{producto._nombre} (${producto._precio:.2f})"
    
    def formato_repr(self, producto):
        return f"Producto: [nombre: {producto._nombre}, precio: {producto._precio}, cantidad: {producto._cantidad}]"
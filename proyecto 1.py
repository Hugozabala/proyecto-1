def main():
    print("menu principal")
    print("1. ingreso de producto")
    print("2. inventario")
    print("3. buscar producto")
    print("4. eliminar producto")
    print("5. modificar prpoducto")
    print("6. salir ")

class Producto:
    def __init__(self, codigo,nombre,categoria,precio,stock):
        self.codigo=codigo
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.stock=stock


    def Mostrar(self):
        print(f"Codigo:{self.codigo}- Nombre: {self.nombre}- Categoria: {self.categoria}- Precio:{self.precio}- Stock: {self.stock}")


class Ordenar:
    pass
class Buscar:
    pass
class Inventario:
    def Agregar(self):
        pass




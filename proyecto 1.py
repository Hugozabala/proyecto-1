def main():
    print("menu principal")
    print("1. ingreso de producto")
    print("2. inventario")
    print("3. buscar producto")
    print("4. eliminar producto")
    print("5. modificar prpoducto")
    print("6. salir ")

    op = 0
    while op != 6:
        try:
            op=int(input("ingrese opcion a ejecutar"))
            match op:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    print("fin de programa")
                case _:
                    print("opcion no valida")
        except ValueError:
            print("ingrese opcion valida")



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





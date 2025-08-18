Dic_inventario={}
def main(inve):
    print("Menu principal")
    print("1. Ingreso de producto")
    print("2. Mostrar Inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Modificar producto")
    print("6. Ordenar Inventario")
    print("7. Salir ")

    op = 0
    while op != 6:
        try:
            op=int(input("Ingrese opcion a ejecutar"))
            match op:
                case 1:
                     inven.Agregar()
                case 2:
                     if Dic_inventario:
                        print("\n Inventario actual:")
                        for producto in Dic_inventario.values():
                            producto.Mostrar()
                     else:
                          print(" Inventario vacío.")
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:

                    pass
                case 7:
                    print("Fin de programa")
                case _:
                    print("Opcion no valida")
        except ValueError:
            print("Ingrese opcion valida")
        except Exception:
            print(f"Error: {Exception}")


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
    def quicksort(self, lista, criterio):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]

        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]

        return quick_sort(menores) + iguales + quick_sort(mayores)

class Buscar:
    def Buscar(self):
        pass

class Inventario:
    def Agregar(self):
            try:
                cod = input("Ingrese código del producto: ")
                if cod in Dic_inventario:
                    print(" Ya existe un producto con ese código.")
                    return

                nom = input("Ingrese nombre del producto: ")
                cat = input("Ingrese categoría: ")
                pre = float(input("Ingrese precio del producto: "))
                sto = int(input("Ingrese cantidad del producto: "))

                p = Producto(cod, nom, cat, pre, sto)
                Dic_inventario[cod] = p
                print(" Producto agregado con éxito.")
            except ValueError:
                print("Error: Ingresaste un dato inválido.")

    def actualizar(self, precio=None, stock=None):
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def eliminar(self,codigo=None):
        eli=input("ingrese codigo de producto a eliminar")
        if eli   not in Dic_inventario:
            print("no existe en dicionario")
        else:
            eliminado=Dic_inventario.pop(eli)
            print(f"producto Eliminado{eliminado}")
            print("eliminado con exito")

def Submenu():
    print("Formas de ordenar el inventario")
    print("1. Por Nombre")






inven=Inventario()
main(inven)


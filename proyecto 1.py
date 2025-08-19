Dic_inventario={}
def main():
    inven = Inventario()
    order = Ordenar()
    bus = Buscar()
    print("Menu principal")
    print("1. Ingreso de producto")
    print("2. Listar Inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Modificar producto")
    print("6. Salir ")

    op = 0
    while op != 6:
        try:
            op=int(input("Ingrese opcion a ejecutar"))
            match op:
                case 1:
                     inven.Agregar()
                case 2:
                    Submenu()
                    ordenar=int(input("Ingrese una opción"))
                    lista_nombre = [inventario["nombre"] for inventario in Dic_inventario.values()]
                    lista_stock = [inventario["stock"] for inventario in Dic_inventario.values()]
                    lista_precio = [inventario["precio"] for inventario in Dic_inventario.values()]
                    if ordenar == 1:
                        listaordenada=[order.quicksort(lista_nombre)]
                    elif ordenar == 2:
                        listaordenada=[order.quicksort(lista_precio)]
                    elif ordenar == 3:
                        listaordenada=[order.quicksort(lista_stock)]

                    if not listaordenada:
                        print("\n Inventario actual:")
                        for producto in Dic_inventario.values():
                            producto.Mostrar()
                    else:
                        print(" Inventario vacío.")

                case 3:
                    SubmenuBuscador()
                    buscar= int(input("Ingrese una opción"))
                    valor_a_buscar = input("Ingrese valor a buscar")
                    lista_nombre = [inventario["nombre"] for inventario in Dic_inventario.values()]
                    lista_codigo = list(Dic_inventario.keys())
                    lista_categoria= [inventario["categoria"] for inventario in Dic_inventario.values()]
                    if buscar==1:
                        bus.Buscardor(lista_codigo,buscar,valor_a_buscar)
                    elif buscar==2:
                        bus.Buscardor(lista_nombre, buscar, valor_a_buscar)
                    elif buscar==3:
                        bus.Buscardor(lista_categoria, buscar, valor_a_buscar)

                case 4:
                    inven.eliminar()
                case 5:
                    inven.actualizar()
                case 6:
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
    def quicksort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]

        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]

        return self.quicksort(menores) + iguales + self.quicksort(mayores)

class Buscar:
    def Buscardor(self, lista, criterio, valor):
        resultados = []
        valor = valor.lower().strip()

        for producto in lista:
            if criterio == 1:
                if producto.codigo == valor:
                    resultados.append(producto)
            elif criterio == 2:
                if valor in producto.nombre.lower():
                    resultados.append(producto)
            elif criterio == 3:
                if valor in producto.categoria.lower():
                    resultados.append(producto)

        return resultados

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
    print("2. Por Precio")
    print("3. Por Stock")

def SubmenuBuscador():
    print("Formas de buscar el producto")
    print("1. Por Código")
    print("2. Por Nombre")
    print("3. Por Categoria")


main()


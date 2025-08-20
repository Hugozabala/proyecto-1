Dic_inventario={}
def main():
    inven = Inventario()
    order = Ordenar()
    bus = Buscar()

    op = 0
    while op != 6:
        try:
            print("\nMenu principal")
            print("1. Ingreso de producto")
            print("2. Listar Inventario")
            print("3. Buscar producto")
            print("4. Eliminar producto")
            print("5. Modificar producto")
            print("6. Salir ")
            op=int(input("Ingrese opcion a ejecutar:   "))
            match op:
                case 1:
                     inven.Agregar()

                case 2:
                    if not Dic_inventario:
                        print("\n Inventario vacío.")
                    else:
                        Submenu()
                        ordenar = int(input("Ingrese una opción: "))

                        # listas de atributos a ordenar
                        lista_nombre = [p.nombre for p in Dic_inventario.values()]
                        lista_stock = [p.stock for p in Dic_inventario.values()]
                        lista_precio = [p.precio for p in Dic_inventario.values()]

                        if ordenar == 1:
                            listaordenada = order.quicksort(lista_nombre)
                        elif ordenar == 2:
                            listaordenada = order.quicksort(lista_precio)
                        elif ordenar == 3:
                            listaordenada = order.quicksort(lista_stock)
                        else:
                            print("Opción inválida.")
                            listaordenada = []

                        print("\nInventario ordenado:\n")
                        for valor in listaordenada:
                            for producto in Dic_inventario.values():
                                if (ordenar == 1 and producto.nombre == valor) or \
                                        (ordenar == 2 and producto.precio == valor) or \
                                        (ordenar == 3 and producto.stock == valor):
                                    producto.Mostrar()


                case 3:
                    if not Dic_inventario:
                        print("\nInventario vacío.")
                    else:
                        SubmenuBuscador()
                        buscar = int(input("Ingrese una opción: "))
                        valor_a_buscar = input("Ingrese valor a buscar: ")

                        resultados = bus.Buscardor(list(Dic_inventario.values()), buscar, valor_a_buscar)

                        if resultados:
                            print("\nResultados de la búsqueda:\n")
                            for producto in resultados:
                                producto.Mostrar()
                        else:
                            print("No se encontraron productos con ese criterio.")
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
                agre=int(input("cuantos productos desea ingresar"))
                for a in range(agre):

                     cod = input("Ingrese código del producto: ")
                     if cod in Dic_inventario:
                        print(" Ya existe un producto con ese código.")
                        return

                     nom = input("Ingrese nombre del producto: ")
                     cat = input("Ingrese categoría: ")
                     pre = float(input("Ingrese precio del producto: "))
                     if pre <=0:
                        print("precio invalido")
                     else:
                        sto = int(input("Ingrese cantidad del producto: "))

                     p = Producto(cod, nom, cat, pre, sto)
                     Dic_inventario[cod] = p
                     print(" Producto agregado con éxito.")
            except ValueError:
                print("Error: Ingresaste un dato inválido.")

    def actualizar(self):
        codigo = input("Ingrese el código del producto a actualizar: ")
        if codigo not in Dic_inventario:
            print("No existe un producto con ese código.")
            return

        producto = Dic_inventario[codigo]
        print("\nProducto actual:")
        producto.Mostrar()

        try:
            nuevo_precio = input("Ingrese nuevo precio (deje vacío para no cambiar): ")
            nuevo_stock = input("Ingrese nuevo stock (deje vacío para no cambiar): ")

            if nuevo_precio.strip() != "":
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio > 0:
                    producto.precio = nuevo_precio
                else:
                    print("Precio inválido, no se actualizó.")

            if nuevo_stock.strip() != "":
                nuevo_stock = int(nuevo_stock)
                if nuevo_stock >= 0:
                    producto.stock = nuevo_stock
                else:
                    print("Stock inválido, no se actualizó.")

            print("\nProducto actualizado con éxito:")
            producto.Mostrar()

        except ValueError:
            print("Error: dato inválido, no se realizaron cambios.")



    def eliminar(self,codigo=None):
        eli=input("ingrese codigo de producto a eliminar:  ")
        if eli   not in Dic_inventario:
            print("no existe en dicionario")
        else:
            eli=Dic_inventario.pop(eli)
            print(f"producto Eliminado{eli.nombre}:  ")
            print("eliminado con exito")

def Submenu():
    print("\nFormas de ordenar el inventario")
    print("1. Por Nombre")
    print("2. Por Precio")
    print("3. Por Stock")

def SubmenuBuscador():
    print("\nFormas de buscar el producto")
    print("1. Por Código")
    print("2. Por Nombre")
    print("3. Por Categoria")


main()


"""
Sistema Avanzado de Gestión de Inventario
Autor: Gabriela Yepez

Descripción:
Sistema desarrollado con Programación Orientada a Objetos (POO)
que permite gestionar productos utilizando colecciones y
almacenamiento en archivos JSON para persistencia de datos.
"""

import json
import os


# =====================================================
# CLASE PRODUCTO
# Representa un producto individual del inventario
# =====================================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Convertir objeto a diccionario (para JSON)
    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


# =====================================================
# CLASE INVENTARIO
# Gestiona todos los productos usando un diccionario
# =====================================================
class Inventario:
    def __init__(self, archivo="inventario.json"):
        # Diccionario: clave = ID, valor = objeto Producto
        self.productos = {}
        self.archivo = archivo
        self.cargar_archivo()

    # Añadir producto
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑 Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if p.get_nombre().lower() == nombre.lower()
        ]

        if encontrados:
            for p in encontrados:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
        else:
            print("❌ No se encontró el producto.")

    # Mostrar todos
    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            for p in self.productos.values():
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")

    # Guardar inventario en archivo JSON
    def guardar_archivo(self):
        with open(self.archivo, "w") as f:
            json.dump(
                {id_p: prod.to_dict() for id_p, prod in self.productos.items()},
                f,
                indent=4
            )

    # Cargar inventario desde archivo JSON
    def cargar_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                for id_p, info in datos.items():
                    self.productos[id_p] = Producto(
                        info["id"],
                        info["nombre"],
                        info["cantidad"],
                        info["precio"]
                    )


# =====================================================
# MENÚ INTERACTIVO
# Permite al usuario gestionar el inventario
# =====================================================
def menu():
    inventario = Inventario()

    while True:
        print("\n====== SISTEMA DE INVENTARIO ======")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_archivo()
            print("💾 Inventario guardado. Saliendo...")
            break

        else:
            print("❌ Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()
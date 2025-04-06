import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='55$Ordago$88',
        database='InventarioDB'
    )
    if conn.is_connected():
        print("✅ Conexión exitosa a la base de datos")
except Error as e:
    print(f"❌ Error al conectar a MySQL: {e}")

import mysql.connector
from mysql.connector import Error

# Clase Producto
class Producto:
    def __init__(self, nombre, cantidad, precio, categoria):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

# Clase GestionInventario
class GestionInventario:
    def __init__(self):
        try:
            # Conectar a la base de datos MySQL
            self.conn = mysql.connector.connect(
                host='127.0.0.1',  # O 'localhost'
                user='root',  # Cambia por tu usuario de MySQL
                password='55$Ordago$88',  # Usa la contraseña que configuraste en MySQL
                database='InventarioDB'
            )
            if self.conn.is_connected():
                print("Conexión exitosa a la base de datos")
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def agregar_producto(self, producto):
        try:
            query = "INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)"
            values = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"Producto {producto.nombre} agregado al inventario.")
        except Error as e:
            print(f"Error al agregar producto: {e}")

    def mostrar_productos(self):
        try:
            self.cursor.execute("SELECT * FROM productos")
            productos = self.cursor.fetchall()
            for producto in productos:
                print(producto)
        except Error as e:
            print(f"Error al mostrar productos: {e}")

    def buscar_producto(self, nombre):
        try:
            query = "SELECT * FROM productos WHERE nombre = %s"
            self.cursor.execute(query, (nombre,))
            producto = self.cursor.fetchone()
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")
        except Error as e:
            print(f"Error al buscar producto: {e}")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        try:
            if cantidad:
                query = "UPDATE productos SET cantidad = %s WHERE id = %s"
                self.cursor.execute(query, (cantidad, id))
            if precio:
                query = "UPDATE productos SET precio = %s WHERE id = %s"
                self.cursor.execute(query, (precio, id))
            self.conn.commit()
            print(f"Producto con id {id} actualizado.")
        except Error as e:
            print(f"Error al actualizar producto: {e}")

    def eliminar_producto(self, id):
        try:
            query = "DELETE FROM productos WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.conn.commit()
            print(f"Producto con id {id} eliminado.")
        except Error as e:
            print(f"Error al eliminar producto: {e}")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()
        print("Conexión cerrada.")

def menu():
    inventario = GestionInventario()

    while True:
        print("\n---- Menú de Gestión de Inventario ----")
        print("1. Agregar producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")
            producto = Producto(nombre, cantidad, precio, categoria)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            inventario.mostrar_productos()

        elif opcion == '3':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '4':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '5':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '6':
            inventario.cerrar_conexion()
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()

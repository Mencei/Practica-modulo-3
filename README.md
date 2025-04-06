# Sistema de Gestión de Inventario con Base de Datos

![GitHub language count](https://img.shields.io/github/languages/count/Mencei/Practica-modulo-3?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/Mencei/Practica-modulo-3?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/Mencei/Practica-modulo-3?style=flat-square)

## Descripción

Este proyecto es una práctica desarrollada en el marco del Curso de Formación Avanzada en Backend: Python, Flask y Django (Módulo 3).  
La aplicación **Sistema de Gestión de Inventario con Base de Datos** simula un sistema para administrar productos utilizando una base de datos MySQL.  
A través de un menú interactivo, el usuario puede realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el inventario de productos.

## Funcionalidades

- **Agregar un producto:**  
  Permite añadir un nuevo producto al inventario con atributos como nombre, cantidad, precio y categoría. Se valida que el nombre del producto sea único.

- **Mostrar todos los productos:**  
  Muestra una lista completa de los productos disponibles en el inventario.

- **Buscar un producto:**  
  Permite buscar un producto por su nombre.

- **Actualizar un producto:**  
  Facilita la modificación de información existente, como cantidad o precio.

- **Eliminar un producto:**  
  Permite remover un producto del inventario.

## Requisitos

- **Base de Datos MySQL:**  
  La información del inventario se almacena en una base de datos MySQL.

- **Librería de conexión a MySQL:**  
  Se utiliza la librería `mysql-connector-python` (u otra similar) para conectar y realizar operaciones en la base de datos.

- **Operaciones CRUD:**  
  La aplicación implementa las operaciones de Crear, Leer, Actualizar y Eliminar para la gestión de productos.

- **Gestión de errores:**  
  - Manejo de errores de conexión a la base de datos.  
  - Validación para evitar agregar productos con nombres duplicados.  
  - Control de errores al buscar, actualizar o eliminar productos inexistentes.

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Mencei/Practica-modulo-3.git

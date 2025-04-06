-- Crear la base de datos
CREATE DATABASE InventarioDB;

-- Seleccionar la base de datos
USE InventarioDB;

-- Crear la tabla de productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);
SHOW TABLES;

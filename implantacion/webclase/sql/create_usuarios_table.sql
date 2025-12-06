-- Script para crear la tabla de usuarios
-- Base de datos: oscar

USE oscar;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARBINARY(255) NOT NULL,
    email VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insertar un usuario de prueba (usuario: admin, contraseña: admin123)
-- Hash generado con bcrypt para la contraseña "admin123"
-- Nota: Debes ejecutar este insert después de tener bcrypt funcionando
-- O usar el formulario de registro para crear el primer usuario

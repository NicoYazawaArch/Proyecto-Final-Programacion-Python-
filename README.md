Hostal "La pulpería de Zoilo" 🏨

Sistema de gestión de reservas y estadísticas de ocupación desarrollado en Python. Este proyecto fue creado como parte de un Trabajo Práctico para la carrera de Ingeniria Informática de la Universidad Nacional de Avellaneda (UNDAV).

📋 Descripción

El sistema permite a los administradores del hostal gestionar el ingreso de estadías durante períodos estacionales específicos (Marzo, Junio, Septiembre, Diciembre). El programa se destaca por:

Validación Robusta: No se rompe si el usuario ingresa letras en lugar de números.

Lógica Estacional: Filtra estadías según el trimestre seleccionado.

Reportes Automáticos: Genera estadísticas de ocupación y nivel de uso por tipo de habitación.

🚀 Características Técnicas

Arquitectura Modular: El código está dividido en módulos lógicos (Validaciones, Procesamiento, Reportes) siguiendo el principio de separación de responsabilidades.

Funciones Puras: La lógica de negocio está desacoplada de la interfaz de usuario.

Sin Librerías Externas: Funciona con Python estándar, sin dependencias complejas.

🛠️ Estructura del Proyecto

El proyecto consta de los siguientes módulos .py:

Archivo

Responsabilidad

Main.py

Punto de entrada. Orquesta el flujo del programa y maneja la interacción principal.

Entrada.py

Módulo de seguridad que valida el tipo de dato (evita errores ValueError).

Validaciones.py

Contiene las reglas de negocio (fechas válidas, rangos, habitaciones existentes).

Procesamiento.py

Realiza los cálculos matemáticos y lógica de transformación de datos.

Fechas.py

Funciones auxiliares para lógica de calendario (bisiestos, días del mes).

Reportes.py

Se encarga exclusivamente de formatear y mostrar los datos en consola.

💻 Instalación y Ejecución

Requisitos

Python 3.x instalado.

python Main.py


(Nota: Asegúrate de que todos los archivos .py estén en la misma carpeta para que las importaciones funcionen correctamente).

🧪 Pruebas

El sistema incluye validaciones para:

Años: Rango 2024-2034.

Meses: Solo inicios de trimestre (3, 6, 9, 12).

Fechas: Existencia real en calendario y pertenencia al período elegido.

Habitaciones: Validación contra lista de habitaciones reales del hostal.

✒️ Autor

Estudiante de Ingeniria Informática: Nicolas Corpus - Trabajo Práctico de Programación - [UNDAV]

Este proyecto es de fines académicos.

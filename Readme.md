# Herramientas de Software — Trabajo Práctico

## Massimo Tiziano Bertorello
*Fecha de Entrega:* Lunes 4 de Noviembre de 2024

---

## Resumen del proyecto

Este proyecto tiene como objetivo implementar el análisis léxico, sintáctico y semántico de una versión reducida del lenguaje C. El programa tomará un archivo de código fuente y generará un árbol sintáctico (usando ANTLR), así como una tabla de símbolos y un reporte de errores. Se buscará identificar y reportar errores léxicos, sintácticos y semánticos presentes en el código.

## Funcion

El programa deberá:

1. Leer un archivo de entrada en lenguaje C.
2. Generar un árbol sintáctico correcto en caso de que el código sea válido.
3. Mostrar el contenido de la tabla de símbolos de cada contexto.
4. Realizar un control de errores básicos y generar un reporte de errores.

### Errores que detecta

#### Errores Sintácticos Comunes
- Falta de un punto y coma.
- Falta de apertura de paréntesis.
- Formato incorrecto en lista de declaración de variables.

#### Errores Semánticos Comunes
- Doble declaración del mismo identificador.
- Uso de un identificador no declarado.
- Uso de un identificador sin inicializar.
- Identificador declarado pero no usado.
- Tipos de datos incompatibles.

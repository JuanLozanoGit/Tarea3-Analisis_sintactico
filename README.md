# Tarea 3: Análisis de Asociatividad y Precedencia

1. **Asociatividad por Izquierda:** Verificar que operaciones como la suma (`+`) y resta (`-`) se agrupen de izquierda a derecha.
2. **Asociatividad por Derecha:** Verificar que la potencia (`^`) y la asignación (`=`) se agrupen de derecha a izquierda.
3. **Precedencia:** Confirmar que la multiplicación (`*`) tenga mayor prioridad que la suma (`+`), apareciendo en niveles más profundos del árbol.

## 🛠️ Requisitos
- **Python 3.x**
- **Graphviz** (Instalación en Kali: `sudo apt install graphviz -y`)
- **Librerías:** ```bash
  pip install lark pydot --break-system-packages
  ```

## Instrucciones de Uso

1. **Configurar casos de prueba:**
   Asegúrate de que el archivo `pruebas_asociatividad.txt` contenga las expresiones a evaluar:
   ```text
   2 + 3 + 4      # Asociatividad Izquierda
   2 ^ 3 ^ 4      # Asociatividad Derecha
   x = y = 5      # Asociatividad Derecha
   2 + 3 * 4      # Precedencia (* antes que +)
   ```

2. **Ejecutar el script:**
   ```bash
   python analizador_procedencia.py pruebas_asociatividad.txt
   ```

3. **Revisar resultados:**
   Se generarán imágenes PNG llamadas `resultado_asoc_n.png`. 

## Guía de Interpretación de Resultados

### Asociatividad por Izquierda (Suma)
En el archivo `resultado_asoc_1.png` (`2+3+4`), observarás que el árbol se inclina hacia la **izquierda**. Esto indica que el compilador resuelve primero `(2+3)` y luego suma `4`.

### Asociatividad por Derecha (Potencia)
En el archivo `resultado_asoc_3.png` (`2^3^4`), el árbol se inclina hacia la **derecha**. Esto demuestra que se resuelve primero `(3^4)` y el resultado es el exponente de `2`.

### Precedencia de Operadores
En la expresión `2+3*4`, la multiplicación aparecerá en una rama **más baja** que la suma. En teoría de compiladores, lo que está más cerca de las hojas tiene mayor prioridad de ejecución.

---
**Asignatura:** Compiladores  
**Institución:** Universidad Sergio Arboleda  
**Estudiante:** Juan Lozano
```

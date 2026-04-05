# Tarea3-Analisis_sintactico

Este proyecto analiza cómo la recursividad en las reglas de una Gramática Independiente del Contexto (GIC) determina el orden de evaluación de los operadores.

## Conceptos Implementados

1. **Asociatividad por Izquierda:** Implementada mediante recursión izquierda (`E -> E + num`). Común en operaciones aritméticas básicas para asegurar que se evalúen de izquierda a derecha.
2. **Asociatividad por Derecha:** Implementada mediante recursión derecha (`E -> num ^ E`). Típica en operadores de potencia o asignación simple.
3. **Precedencia:** Organización jerárquica de reglas donde los operadores de mayor prioridad se encuentran más alejados del símbolo inicial (`start`).

## Instrucciones
Ejecutar el script de pruebas para generar las comparativas visuales:
`python analizador_procedencia.py`

## Resultados esperados
- En la suma (`2+3+4`), el árbol crecerá hacia la **izquierda**.
- En la potencia (`2^3^4`), el árbol crecerá hacia la **derecha**.

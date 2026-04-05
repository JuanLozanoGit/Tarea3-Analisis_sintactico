import os
from lark import Lark, tree

def probar_gramatica(nombre_archivo, cadena, tag):
    with open(nombre_archivo, 'r') as f:
        grammar = f.read()
    
    parser = Lark(grammar, start='start', parser='earley')
    try:
        arbol = parser.parse(cadena)
        output = f"ast_{tag}.png"
        tree.pydot__tree_to_png(arbol, output)
        print(f"Gramática {tag}: Procesada. Ver {output}")
    except Exception as e:
        print(f"Error en {tag}: {e}")

if __name__ == "__main__":
    # Prueba de asociatividad izquierda (Suma)
    probar_gramatica("gramatica_izquierda.lark", "2 + 3 + 4", "izquierda")
    
    # Prueba de asociatividad derecha (Potencia)
    probar_gramatica("gramatica_derecha.lark", "2 ^ 3 ^ 4", "derecha")

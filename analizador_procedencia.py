import sys
from lark import Lark, tree

def ejecutar_pruebas(archivo_txt):
    # Gramática completa para asociatividad y precedencia
    grammar = r"""
        ?start: asignacion | expr_suma

        # Asociatividad por Derecha (Asignación)
        asignacion: ID "=" asignacion | ID "=" num
        
        # Jerarquía de operaciones (Asociatividad y Precedencia)
        ?expr_suma: expr_suma ("+" | "-") term  -> suma_izq  // Izquierda
                  | term

        ?term: term ("*" | "/") factor          -> mul_izq   // Izquierda
             | factor

        ?factor: atom "^" factor                -> pot_der   // Derecha
               | atom

        ?atom: num
             | ID
             | "(" expr_suma ")"

        num: /\d+/
        ID: /[a-z]/
        %import common.WS
        %ignore WS
    """
    
    parser = Lark(grammar, start='start', parser='earley')

    try:
        with open(archivo_txt, 'r') as f:
            lineas = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    except FileNotFoundError:
        print(f"Error: No se encontró {archivo_txt}")
        return

    for i, cadena in enumerate(lineas):
        try:
            arbol = parser.parse(cadena)
            nombre = f"resultado_asoc_{i+1}.png"
            tree.pydot__tree_to_png(arbol, nombre)
            print(f"Procesada: {cadena} -> {nombre}")
        except Exception as e:
            print(f"Error en '{cadena}': {e}")

if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else "pruebas_asociatividad.txt"
    ejecutar_pruebas(archivo)

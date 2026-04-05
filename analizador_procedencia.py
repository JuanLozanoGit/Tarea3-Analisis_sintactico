import sys
from lark import Lark, tree

def ejecutar_pruebas(archivo_txt):
    # Gramatica que combina ambas para demostrar la diferencia
    grammar = """
        ?start: asignacion | expr_potencia | expr_suma

        # Asociatividad por Derecha (Asignacion)
        asignacion: ID "=" asignacion | ID "=" num
        
        # Asociatividad por Derecha (Potencia)
        ?expr_potencia: num "^" expr_potencia -> pot_der
                      | num
        
        # Asociatividad por Izquierda (Suma)
        ?expr_suma: expr_suma "+" num -> suma_izq
                  | num

        num: /\d+/
        ID: /[a-z]/
        %import common.WS
        %ignore WS
    """
    
    parser = Lark(grammar, start='start', parser='earley')

    with open(archivo_txt, 'r') as f:
        lineas = [l.strip() for l in f if l.strip() and not l.startswith("#")]

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

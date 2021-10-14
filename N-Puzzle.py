class Nodo:
    def __init__(self, estado, padre):
        self.estado = estado 
        self.padre = padre  

    def ruta_solucion(self):
        lista_estados = []
        count = 1
        nodo_actual = self

        while nodo_actual.padre is not None:
            lista_estados.append(nodo_actual.estado)
            nodo_actual = nodo_actual.padre
        lista_estados.reverse()
        
        for estado in lista_estados:
            print(count)
            print('-------')
            mostrar_estado(estado)
            print('-------')
            print('\n')
            count += 1

        return lista_estados


def mostrar_estado(estado):
    fila = 0
    for n in estado:
        print(n, end=" ")
        fila += 1
        if fila == 3:
            print()
            fila = 0

def move_up(estado):
     new_state = estado[:]
     index = new_state.index(0)
     if index not in [0, 1, 2]:
         temp = new_state[index - 3]
         new_state[index - 3] = new_state[index]
         new_state[index] = temp
         return (new_state)
     else:
         return None

def move_down(estado):
    new_state = estado[:]
    index = new_state.index(0)
    if index not in [6, 7, 8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return (new_state)
    else:
        return None

def move_left(estado):
    new_state = estado[:]
    index = new_state.index(0)
    if index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return (new_state)
    else:
        return None

def move_right(estado):
    new_state = estado[:]
    index = new_state.index(0)
    if index not in [2, 5, 8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return (new_state)
    else:
        return None

def expandir_nodos(nodo):
    nodos_expandidos = []

    nodos_expandidos.append(Nodo(move_up(nodo.estado), nodo))
    nodos_expandidos.append(Nodo(move_down(nodo.estado), nodo))
    nodos_expandidos.append(Nodo(move_right(nodo.estado), nodo))
    nodos_expandidos.append(Nodo(move_left(nodo.estado), nodo))

    nodos_expandidos = [nodo for nodo in nodos_expandidos if nodo.estado != None]
    return nodos_expandidos


def busqueda_anchura(inicial, objetivo):
    nodos = []
    nodos.append(Nodo(inicial, None))

    explorados = set()

    while nodos:
        nodo_actual = nodos.pop(0)

        if tuple(nodo_actual.estado) not in explorados:
            explorados.add(tuple(nodo_actual.estado))
        else:
            continue

        if nodo_actual.estado == objetivo:
            return nodo_actual.ruta_solucion()
        else:
            nodos.extend(expandir_nodos(nodo_actual))

def busqueda_profundidad(inicial, objetivo):
    nodos = []
    nodos.append(Nodo(inicial, None))

    explorados = set()

    while nodos:
        nodo_actual = nodos.pop()

        if tuple(nodo_actual.estado) not in explorados:
            explorados.add(tuple(nodo_actual.estado))
        else:
            continue

        if nodo_actual.estado == objetivo:
            return nodo_actual.ruta_solucion()
        else:
            nodos.extend(expandir_nodos(nodo_actual))


def main():
    estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    estado_inicial = [8, 7, 5, 3, 0, 1, 4, 2, 6]

    # Para busqueda en anchura la funcion "busqueda_anchura"
    # Para busqueda en profundidad la funcion "busqueda_profundidad"
    resultado = busqueda_anchura(estado_inicial, estado_objetivo)
    print('La solucion se encontro en:', len(resultado),'movimientos')
    input()

if __name__ == "__main__":
    main()
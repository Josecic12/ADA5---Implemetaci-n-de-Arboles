class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def mostrar_arbol_acostado(self, nodo, nivel=0):
        if nodo is not None:
            self.mostrar_arbol_acostado(nodo.derecho, nivel + 1)
            print(' ' * 4 * nivel + '->', nodo.valor)
            self.mostrar_arbol_acostado(nodo.izquierdo, nivel + 1)

    def graficar_arbol(self):
        self.mostrar_arbol_acostado(self.raiz)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierdo, valor)
        return self._buscar(nodo.derecho, valor)

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.preorden(nodo.izquierdo)
            self.preorden(nodo.derecho)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=' ')
            self.inorden(nodo.derecho)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierdo)
            self.postorden(nodo.derecho)
            print(nodo.valor, end=' ')

    def eliminar_predecesor(self, valor):
        nodo = self.buscar(valor)
        if nodo:
            predecesor = self._maxValorNodo(nodo.izquierdo)
            if predecesor:
                self.eliminar(predecesor.valor)

    def eliminar_sucesor(self, valor):
        nodo = self.buscar(valor)
        if nodo:
            sucesor = self._minValorNodo(nodo.derecho)
            if sucesor:
                self.eliminar(sucesor.valor)

    def recorrer_por_niveles(self):
        if not self.raiz:
            return
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            print(nodo.valor, end=' ')
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)

    def altura(self, nodo):
        if nodo is None:
            return -1
        else:
            izquierda = self.altura(nodo.izquierdo)
            derecha = self.altura(nodo.derecho)
            return max(izquierda, derecha) + 1

    def contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1
        return self.contar_hojas(nodo.izquierdo) + self.contar_hojas(nodo.derecho)

    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izquierdo) + self.contar_nodos(nodo.derecho)

    def es_completo(self, nodo):
        if nodo is None:
            return True
        cola = [nodo]
        hay_hueco = False
        while cola:
            nodo_actual = cola.pop(0)
            if nodo_actual.izquierdo:
                if hay_hueco:
                    return False
                cola.append(nodo_actual.izquierdo)
            else:
                hay_hueco = True
            if nodo_actual.derecho:
                if hay_hueco:
                    return False
                cola.append(nodo_actual.derecho)
            else:
                hay_hueco = True
        return True

    def es_lleno(self, nodo):
        if nodo is None:
            return True
        altura = self.altura(nodo)
        nodos_esperados = (2 ** (altura + 1)) - 1
        nodos_reales = self.contar_nodos(nodo)
        return nodos_reales == nodos_esperados

    def eliminar_arbol(self):
        self.raiz = None

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            temp = self._minValorNodo(nodo.derecho)
            nodo.valor = temp.valor
            nodo.derecho = self._eliminar(nodo.derecho, temp.valor)
        return nodo

    def _minValorNodo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def _maxValorNodo(self, nodo):
        actual = nodo
        while actual.derecho is not None:
            actual = actual.derecho
        return actual


def menu():
    arbol = Arbol()
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar nodo")
        print("2. Mostrar árbol (acostado)")
        print("3. Buscar nodo")
        print("4. Recorrido PreOrden")
        print("5. Recorrido InOrden")
        print("6. Recorrido PostOrden")
        print("7. Recorrido por niveles")
        print("8. Altura del árbol")
        print("9. Contar hojas")
        print("10. Contar nodos")
        print("11. Eliminar nodo")
        print("12. Eliminar predecesor")
        print("13. Eliminar sucesor")
        print("14. Verificar si es completo")
        print("15. Verificar si es lleno")
        print("16. Eliminar todo el árbol")
        print("17. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 17:
            break

        elif opcion == 1:
            valor = int(input("Valor del nodo: "))
            arbol.insertar(valor)
        elif opcion == 2:
            arbol.graficar_arbol()
        elif opcion == 3:
            valor = int(input("Valor a buscar: "))
            nodo = arbol.buscar(valor)
            print("Nodo encontrado" if nodo else "Nodo no encontrado")
        # Agrega aquí el resto de opciones...

menu()

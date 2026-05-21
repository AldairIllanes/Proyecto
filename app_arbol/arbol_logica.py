class NodoRuta:
    def _init_(self, dato):
        self.dato = dato
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def recorrer(self):
        resultado = [self.dato]

        for hijo in self.hijos:
            resultado.extend(hijo.recorrer())

        return resultado

    def buscar(self, valor):
        if self.dato.lower() == valor.lower():
            return True

        for hijo in self.hijos:
            if hijo.buscar(valor):
                return True

        return False

    def contar_nodos(self):
        contador = 1

        for hijo in self.hijos:
            contador += hijo.contar_nodos()

        return contador

    def calcular_altura(self):
        if not self.hijos:
            return 1

        alturas = []

        for hijo in self.hijos:
            alturas.append(hijo.calcular_altura())

        return 1 + max(alturas)

    def obtener_hijos(self):
        return [hijo.dato for hijo in self.hijos]

    def eliminar_hijo(self, valor):
        for hijo in self.hijos:
            if hijo.dato.lower() == valor.lower():
                self.hijos.remove(hijo)
                return True
            elif hijo.eliminar_hijo(valor):
                return True
        return False


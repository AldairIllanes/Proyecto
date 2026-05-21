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
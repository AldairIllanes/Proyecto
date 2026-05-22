from django.shortcuts import render
from .arbol_logica import NodoRuta

raiz = NodoRuta("Reclamos")
academico = NodoRuta("Académico")
administrativo = NodoRuta("Administrativo")
tecnico = NodoRuta("Técnico")
raiz.agregar_hijo(academico)
raiz.agregar_hijo(administrativo)
raiz.agregar_hijo(tecnico)

academico.agregar_hijo(NodoRuta("Matrícula"))
academico.agregar_hijo(NodoRuta("Notas"))
administrativo.agregar_hijo(NodoRuta("Pagos"))
tecnico.agregar_hijo(NodoRuta("Aula Virtual"))

def inicio(request):
    return render(request, 'index.html')

def ver_arbol(request):
    contexto = {
        'nodos': raiz.recorrer(),
        'total': raiz.contar_nodos(),
        'altura': raiz.calcular_altura()
    }
    return render(request, 'arbol.html', contexto)
    
def buscar_reclamo(request):
    resultado = None
    if request.method == 'POST':
        valor = request.POST.get('buscar')
        if raiz.buscar(valor):
            resultado = f"Sí existe el reclamo: {valor}"
        else:
            resultado = f"No existe el reclamo: {valor}"
    return render(request, 'buscar.html', {
        'resultado': resultado
    })

def registrar_reclamo(request):
    mensaje = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        nuevo_reclamo = NodoRuta(nombre)
        if categoria == 'Academico':
            academico.agregar_hijo(nuevo_reclamo)
        elif categoria == 'Administrativo':
            administrativo.agregar_hijo(nuevo_reclamo)
        elif categoria == 'Tecnico':
            tecnico.agregar_hijo(nuevo_reclamo)
        mensaje = "Reclamo agregado correctamente"
    return render(request, 'registrar.html', {
        'mensaje': mensaje
    })

def detalle_reclamo(request):
    return render(request, 'detalle.html')

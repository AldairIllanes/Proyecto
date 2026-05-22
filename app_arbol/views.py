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

detalle_actual = {}

def inicio(request):
    return render(request, 'index.html')

def ver_arbol(request):
    contexto = {
        'academico': academico.hijos,
        'administrativo': administrativo.hijos,
        'tecnico': tecnico.hijos,
        'total': raiz.contar_nodos(),
        'altura': raiz.calcular_altura()
    }
    return render(request, 'arbol.html', contexto)

def buscar_reclamo(request):
    global detalle_actual
    resultado = None
    if request.method == 'POST':
        valor = request.POST.get('buscar')
        if raiz.buscar(valor):
            resultado = valor
            detalle_actual = {
                'nombre': valor,
                'tipo': 'Administrativo',
                'estado': 'Pendiente',
                'prioridad': 'Alta',
                'descripcion': f'Reclamo relacionado con {valor}',
                'responsable': 'Área de Tesorería',
                'fecha': '22/05/2026'
            }
        else:
            resultado = "No existe el reclamo"
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

def eliminar_reclamo(request):
    mensaje = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if raiz.eliminar_hijo(nombre):
            mensaje = f"Reclamo eliminado: {nombre}"
        else:
            mensaje = f"No se encontró el reclamo: {nombre}"
    return render(request, 'eliminar.html', {
        'mensaje': mensaje
    })

def detalle_reclamo(request):
    return render(request, 'detalle.html', detalle_actual)

def gestion(request):
    contexto = {
        'usuarios': 25,
        'reclamos': raiz.contar_nodos(),
        'categorias': 3
    }
    return render(request, 'gestion.html', contexto)

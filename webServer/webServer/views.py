from django.http import HttpResponse
import datetime
from django.template import Template,Context    
def saludo(request): #primera vista
    nombre = "miguel"
    doc_Externo=open(r"C:\Users\Milkito\Documents\GitHub\creatibotsApp\webServer\webServer\plantilla.html")
    plt = Template(doc_Externo.read())
    doc_Externo.close()
    ctx = Context({"nombre_pesona":"miguel"})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """ <html>
    <body>
    <h1>
    fecha y hora actuales %s
    </h1>
    </body>
    </html>"""%fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request,anio):
    edadActual = 18
    periodo = anio - 2020
    edadFutura = edadActual + periodo
    dc = "<html><body><h2>En el anio %s tendras %s años</h2></body></html>"%(anio,edadFutura)
    return HttpResponse(dc)
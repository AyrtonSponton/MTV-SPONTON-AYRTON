from re import template
from django.http import HttpResponse
from django.template import loader


def Inicio(self):
    Texto="Bienvenido a la Pagina de Incio"
    Titulo={'Titulo':Texto}
    plantilla= loader.get_template("template.html")
    documento= plantilla.render(Titulo)
    return HttpResponse(documento)


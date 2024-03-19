from django.http import HttpResponse
import datetime as dt
from django.template import Template, Context

def saludo(request): #primera vista

    doc_externo = open("C:/Users/Martuki/Desktop/FGGUI/MDDA/MDDA/templates/miplantilla.html")
    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)
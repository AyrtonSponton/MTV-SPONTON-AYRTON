from django.http import HttpResponse
from django.shortcuts import render
from .models import Padre, Madre, Hermana, Novia
from django.http import HttpResponse

def padre(self):
    padre= Padre(nombre="Claudio", Edad=53, color_favorito="Verde", fecha_de_nacimiento="1968-09-14")
    padre.save()
    texto= f"Nombre: {padre.nombre} Edad: {padre.Edad} Color Favorito: {padre.color_favorito} Fecha de Nacimiento: {padre.fecha_de_nacimiento} "
    return HttpResponse(texto)

def madre(self):
    madre= Madre(nombre= "Laura", Edad= 51, color_favorito= "Marron", fecha_de_nacimiento= "1971-04-23")
    madre.save()
    texto= f"Nombre: {madre.nombre} Edad: {madre.Edad} Color Favorito: {madre.color_favorito} Fecha de Nacimiento: {madre.fecha_de_nacimiento} "
    return HttpResponse(texto)

def hermana(self):
    hermana= Hermana(nombre= "Aylen", Edad= 25, color_favorito="Azul", fecha_de_nacimiento= "1996-09-16")
    hermana.save()
    texto= f"Nombre: {hermana.nombre} Edad: {hermana.Edad} Color Favorito: {hermana.color_favorito} Fecha de Nacimiento: {hermana.fecha_de_nacimiento} "
    return HttpResponse(texto)

def novia(self):
    novia= Novia(nombre= "Estefania", Edad= 29, color_favorito="Rojo", fecha_de_nacimiento="1993-03-30")
    novia.save()
    texto= f"Nombre: {novia.nombre} Edad: {novia.Edad} Color Favorito: {novia.color_favorito} Fecha de Nacimiento: {novia.fecha_de_nacimiento} "
    return HttpResponse(texto)
    

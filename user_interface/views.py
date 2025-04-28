from django.shortcuts import render
from django.urls import reverse


def home(request):
    intro = {"name": "Iniciemos", "url": reverse("user_interface:intro")}
    return render(
        request,
        "user_interface/frontpage.html",
        {
            "title": "Sistema de Asesoría Legal Mercantil",
            "intro_url": intro,
        },
    )


def intro(request):
    return render(
        request,
        "user_interface/intro.html",
        {
            "title": "Sistema de Asesoría Legal Mercantil",
            # "intro_url": intro,
        },
    )

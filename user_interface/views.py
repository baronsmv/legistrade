from pprint import pformat

from django.shortcuts import render, reverse

from knowledge_base.recommend import recommend
from user_interface.forms import EmpresaForm
from utils.config_loader import config
from utils.logging_config import logging

logger = logging.getLogger(__name__)

system_name = config["system_name"]
title = system_name
footer = f"2025 {system_name}"


def home(request):
    logger.info("Entrando a la página de inicio (portada).")
    intro = {"name": "Iniciemos", "url": reverse("user_interface:intro")}
    return render(
        request,
        "user_interface/frontpage.html",
        {
            "title": title,
            "intro_url": intro,
        },
    )


def intro(request):
    logger.info("Entrando a la página de introducción.")
    return render(
        request,
        "user_interface/intro.html",
        {"title": title, "footer": footer},
    )


def form(request):
    if request.method == "POST":
        empresa_form = EmpresaForm(request.POST)
        if empresa_form.is_valid():
            datos = empresa_form.cleaned_data
            logger.debug("Los datos de la empresa son:\n" + pformat(datos))
            recomendaciones, table = recommend(datos)
            logger.debug(
                f"Las recomendaciones son:\n{recomendaciones}\n{pformat(table)}"
            )
            return render(
                request,
                "user_interface/recommend.html",
                {
                    "subtitle": "Recomendaciones",
                    "text": recomendaciones,
                    "table": table,
                    "table_title": "Tabla de detalles",
                    "table_columns": ("Concepto", "Detalle"),
                    "footer": footer,
                    "error_message": "No se encontraron recomendaciones. "
                    + "Asegúrate de completar correctamente el formulario.",
                },
            )
        else:
            logger.error("Errores del formulario:\n" + pformat(empresa_form.errors))
    else:
        empresa_form = EmpresaForm()

    return render(
        request,
        "user_interface/form.html",
        {
            "title": title,
            "subtitle": "Características de la empresa",
            "form": empresa_form,
            "footer": footer,
        },
    )

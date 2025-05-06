from knowledge_base.recommend import recommend


def test_recommend():
    example_data = {
        "antiguedad": "Nueva (menos de 4 años)",
        "declara_impuestos": "Sí",
        "ecommerce": "No",
        "emite_cfd": "No",
        "esta_registrada_exportador": "Sí",
        "lleva_contab_elect": "No",
        "propiedad_intelectual": ["Marca", "Patente"],
        "regimen_fiscal": "Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras",
        "regimen_legal": "Asociación en Participación",
        "sector": "Agricultura",
        "seguridad_datos": "Sí",
        "tamano": "Microempresa (menos de 10 empleados)",
        "tiene_experiencia_exportacion": "Sí",
        "tiene_licencias_permisos": "No",
        "tiene_practicas_sostenibles": "No",
        "tiene_responsabilidad_social": "No",
        "tipo_contratos": ["Proveedores", "Trabajadores", "Prestadores"],
        "usa_aviso_privacidad": "No",
        "usa_contratos": "Sí",
    }
    texto, recomendaciones = recommend(example_data)

    # Verifica el tipo de salida de recommend
    assert isinstance(recomendaciones, dict)
    # Verifica que se estén cambiando los nombres de claves
    assert "Régimen Legal" in recomendaciones
    # Verifica que sí se esté guardando el nombre
    assert (
        recomendaciones["Régimen Legal"]["Régimen legal"]
        == "Asociación en Participación"
    )

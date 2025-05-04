import logging

from markdown import markdown

from .dicts import knowledge_base as kb

dict_attrib: dict[str, str] = {
    "regimen_legal": "Régimen Legal",
    "regimen_fiscal": "Régimen Fiscal",
    "sector": "Sector principal",
    "antiguedad": "Años de operación",
    "tamano": "Tamaño de la empresa",
    "usa_contratos": "Uso de contratos escritos",
    "tipo_contratos": "Tipos de contratos usados",
    "ecommerce": "Uso de plataforma de comercio electrónico",
    "usa_aviso_privacidad": "Aviso de privacidad y términos legales",
    "seguridad_datos": "Medidas de seguridad en datos personales",
    "propiedad_intelectual": "Registro de propiedad intelectual",
    "declara_impuestos": "Declaración regular de impuestos",
    "lleva_contab_elect": "Contabilidad electrónica",
    "emite_cfd": "Emisión de CFDI (Comprobante Fiscal Digital por Internet)",
    "tiene_licencias_permisos": "Licencias y permisos",
    "tiene_experiencia_exportacion": "Experiencia en exportación",
    "esta_registrada_exportador": "Registro en el Padrón de Exportadores",
    "tiene_practicas_sostenibles": "Prácticas sostenibles",
    "tiene_responsabilidad_social": "Programas de responsabilidad social",
}

"""
val_attrib: dict[bool, str] = {
    True: "Sí",
    False: "No",
}


def rename(d):
    return {k: val_attrib.get(v, v) for k, v in d.items()}
"""


def text(data):
    t = ""
    return markdown(t)


def recommend(data) -> tuple[str, dict]:
    try:
        return text(data), {
            dict_attrib.get(key, key): value
            for key in dict_attrib.keys()
            if key in kb
            and (
                value := kb[key].get(
                    tuple(data_value)
                    if isinstance((data_value := data.get(key)), list)
                    else data_value
                )
            )
        }
    except Exception as e:
        logging.error(e)
        return "", {}

import logging

from .dicts import knowledge_base as kb

dict_attrib: dict[str, str] = {
    "regimen": "Régimen legal",
    "sector": "Sector principal",
    "antiguedad": "Años de operación",
    "tamano": "Tamaño",
    "usa_contratos": "¿Utiliza contratos escritos?",
    "tipo_contratos": "Tipos de contratos que utiliza",
    "ecommerce": "¿Tiene plataforma de comercio electrónico?",
    "usa_terminos_legales_web": "¿Cuenta con aviso de privacidad y términos legales en su sitio web?",
    "usa_medidas_seguridad": "¿Tiene medidas de seguridad para proteger los datos personales?",
    "propiedad_intelectual": "¿Ha registrado propiedad intelectual?",
    "declara_impuestos": "¿Declara impuestos regularmente?",
    "lleva_contabilidad": "¿Lleva contabilidad electrónica?",
    "regimen_fiscal": "Régimen Fiscal",
    "usa_cfd": "¿Emite Comprobantes Fiscales Digitales (CFD)?",
    "tiene_licencias_permisos": "¿Posee las licencias y permisos requeridos por su actividad económica?",
    "tiene_experiencia_exportacion": "¿Tiene experiencia en exportación?",
    "esta_registrada_exportador": "¿Está registrada en el Padrón de Exportadores?",
    "tiene_practicas_sostenibles": "¿Implementa prácticas sostenibles?",
    "tiene_responsabilidad_social": "¿Tiene programas de responsabilidad social empresarial?",
}

key_attrib: dict[str, str] = {
    # Común
    "características": "Características",
    "financiamiento": "Acceso a financiamiento",
    "derechos": "Derechos",
    "obligaciones_fiscales": "Obligaciones Fiscales",
    "obligaciones_legales": "Obligaciones Legales",
    # Régimen
    "nombre_regimen": "Tipo de régimen",
    "descripción": "Descripción general",
    "mercantil": "Es sociedad mercantil",
    "min_socios": "Número mínimo de socios",
    "capital_minimo": "Capital mínimo requerido",
    "flexibilidad_admin": "Flexibilidad en administración",
    "uso": "Uso común",
    # Sector
    "nombre_sector": "Sector principal",
    # Antiguëdad
    "reputación": "Reputación y credibilidad",
    "adaptabilidad": "Adaptabilidad y cambios",
    "proveedores": "Relaciones con proveedores",
    "innovación": "Innovación",
    # Tamaño
    "rango_empleados": "Número de empleados",
    "estructura": "Estructura organizativa",
    "mercado": "Alcance de mercado",
    "tecnología": "Nivel de adopción tecnológica",
    "regulaciones": "Cumplimiento regulatorio",
    "contrataciones": "Condiciones de contratación",
    # Contratos
    "seguridad_legal": "Seguridad legal",
    "claridad_acuerdos": "Claridad en acuerdos",
    "protección_incumplimientos": "Protección contra incumplimientos",
    "profesionalismo": "Profesionalismo",
    # Tipo de contratos
    "nombre_tipo_contratos": "Tipos de contrato usados",
    "características_contrato": "Características del contrato",
}

val_attrib: dict[bool, str] = {
    True: "Sí",
    False: "No",
}


def rename(d):
    return {key_attrib.get(k, k): val_attrib.get(v, v) for k, v in d.items()}


def recommend(data):
    try:
        return {
            dict_attrib.get(key, key): rename(value)
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
        return {}

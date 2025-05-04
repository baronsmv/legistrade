tiene_experiencia_exportacion = {
    "Sí": {
        "Conocimiento del mercado": "Familiarizada con regulaciones internacionales y tendencias comerciales.",
        "Red de distribución": "Posee contactos y logística para exportaciones eficientes.",
        "Cumplimiento legal": "Conoce y cumple con normas de comercio exterior.",
        "Acceso a clientes globales": "Tiene presencia en mercados internacionales.",
        "Gestión de riesgos": "Anticipa desafíos como fluctuaciones cambiarias y barreras arancelarias.",
        "Expansión del negocio": "Capacidad de crecimiento y diversificación en nuevos países.",
    },
    "No": {
        "Conocimiento del mercado": "Desconocimiento de regulaciones y oportunidades en comercio exterior.",
        "Red de distribución": "Sin infraestructura logística para exportar productos.",
        "Cumplimiento legal": "Riesgo de incumplimiento por falta de experiencia en normativas internacionales.",
        "Acceso a clientes globales": "Limitado a ventas nacionales.",
        "Gestión de riesgos": "Mayor vulnerabilidad ante cambios económicos globales.",
        "Expansión del negocio": "Menos oportunidades de crecimiento fuera del país.",
    },
}

tiene_experiencia_exportacion = {
    k: ({"Experiencia en exportación": k} | v)
    for k, v in tiene_experiencia_exportacion.items()
}

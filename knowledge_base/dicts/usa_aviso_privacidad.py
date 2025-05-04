usa_aviso_privacidad = {
    "Sí": {
        "Cumplimiento legal": "Cumple con regulaciones como GDPR, CCPA o leyes locales.",
        "Confianza del usuario": "Genera mayor confianza y transparencia para los clientes.",
        "Protección de datos": "Define cómo se recopilan, almacenan y utilizan los datos personales.",
        "Riesgo legal": "Minimiza la exposición a sanciones y demandas legales.",
        "Reputación empresarial": "Demuestra compromiso con la privacidad y el respeto a los usuarios.",
        "Experiencia del usuario": "Permite a los visitantes conocer sus derechos y responsabilidades.",
    },
    "No": {
        "Cumplimiento legal": "Puede estar en incumplimiento de leyes de protección de datos.",
        "Confianza del usuario": "Usuarios pueden desconfiar al no encontrar información clara.",
        "Protección de datos": "No establece normas sobre el manejo de información personal.",
        "Riesgo legal": "Mayor posibilidad de sanciones y demandas por falta de transparencia.",
        "Reputación empresarial": "Percepción de descuido o falta de profesionalismo.",
        "Experiencia del usuario": "Los clientes desconocen cómo se manejan sus datos y derechos.",
    },
}

usa_aviso_privacidad = {
    k: ({"Uso de aviso de privacidad y términos legales en su sitio web": k} | v)
    for k, v in usa_aviso_privacidad.items()
}

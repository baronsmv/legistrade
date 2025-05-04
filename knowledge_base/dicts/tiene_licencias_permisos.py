tiene_licencias_permisos = {
    "Sí": {
        "Cumplimiento legal": "Opera dentro del marco regulatorio sin riesgo de sanciones.",
        "Confianza del cliente": "Genera credibilidad y seguridad para consumidores y socios.",
        "Acceso a mercados": "Puede participar en licitaciones, comercio internacional y asociaciones.",
        "Protección financiera": "Evita multas, cierres forzosos y problemas legales.",
        "Reputación empresarial": "Reconocida como negocio legítimo y profesional.",
        "Expansión del negocio": "Facilidad para crecer y acceder a nuevas oportunidades comerciales.",
    },
    "No": {
        "Cumplimiento legal": "Riesgo de sanciones, multas o cierre por operar sin permisos.",
        "Confianza del cliente": "Desconfianza de consumidores y socios comerciales.",
        "Acceso a mercados": "Restricciones para participar en licitaciones y comercio formal.",
        "Protección financiera": "Posibilidad de enfrentar altos costos legales y económicos.",
        "Reputación empresarial": "Riesgo de imagen negativa y problemas de credibilidad.",
        "Expansión del negocio": "Dificultades para crecimiento y acceso a oportunidades.",
    },
}

tiene_licencias_permisos = {
    k: ({"Posesión de licencias y permisos requeridos": k} | v)
    for k, v in tiene_licencias_permisos.items()
}

tiene_practicas_sostenibles = {
    "Sí": {
        "Impacto ambiental": "Reduce la huella de carbono y el consumo de recursos naturales.",
        "Reputación empresarial": "Mejor percepción y compromiso con la sostenibilidad.",
        "Eficiencia operativa": "Optimiza procesos con materiales reciclados y energías renovables.",
        "Cumplimiento normativo": "Adherencia a regulaciones ambientales y certificaciones ecológicas.",
        "Preferencia del consumidor": "Mayor atractivo para clientes concienciados con el medio ambiente.",
        "Ventajas competitivas": "Acceso a mercados verdes y financiamiento sostenible.",
    },
    "No": {
        "Impacto ambiental": "Mayor contaminación y uso excesivo de recursos.",
        "Reputación empresarial": "Riesgo de imagen negativa por falta de compromiso ecológico.",
        "Eficiencia operativa": "Dependencia de procesos tradicionales menos eficientes.",
        "Cumplimiento normativo": "Posibilidad de sanciones por no cumplir regulaciones ambientales.",
        "Preferencia del consumidor": "Menos atractivo para clientes preocupados por el medio ambiente.",
        "Ventajas competitivas": "Limitaciones para acceder a incentivos y mercados sostenibles.",
    },
}

tiene_practicas_sostenibles = {
    k: ({"Implementación de prácticas sostenibles": k} | v)
    for k, v in tiene_practicas_sostenibles.items()
}

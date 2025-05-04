declara_impuestos = {
    "Sí": {
        "Cumplimiento legal": "Cumple con regulaciones fiscales y evita sanciones.",
        "Reputación empresarial": "Genera confianza entre clientes, proveedores e inversionistas.",
        "Acceso a beneficios": "Puede optar por incentivos fiscales y financiamiento.",
        "Estabilidad financiera": "Mantiene registros contables claros y previsión económica.",
        "Riesgo legal": "Menor riesgo de auditorías y penalizaciones gubernamentales.",
        "Expansión del negocio": "Facilidad para crecer y operar sin restricciones legales.",
    },
    "No": {
        "Cumplimiento legal": "En riesgo de incumplimiento y posibles sanciones fiscales.",
        "Reputación empresarial": "Pérdida de credibilidad y confianza en el mercado.",
        "Acceso a beneficios": "No puede acceder a financiamiento ni incentivos fiscales.",
        "Estabilidad financiera": "Mayor dificultad para gestionar recursos y planificar a futuro.",
        "Riesgo legal": "Alta probabilidad de auditorías, multas y problemas legales.",
        "Expansión del negocio": "Limitaciones para crecimiento y acceso a mercados formales.",
    },
}

declara_impuestos = {
    k: ({"Declaración regular de impuestos": k} | v)
    for k, v in declara_impuestos.items()
}

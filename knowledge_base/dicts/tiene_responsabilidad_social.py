tiene_responsabilidad_social = {
    "Sí": {
        "Reputación empresarial": "Mejor percepción pública y confianza de consumidores.",
        "Impacto comunitario": "Contribuye al desarrollo social y ambiental de su entorno.",
        "Fidelización de clientes": "Mayor conexión y lealtad de consumidores comprometidos con valores.",
        "Atracción de talento": "Más atractivo para empleados que buscan propósito en su trabajo.",
        "Cumplimiento normativo": "Alineación con regulaciones y estándares de sostenibilidad.",
        "Ventajas competitivas": "Diferenciación en el mercado por buenas prácticas corporativas.",
    },
    "No": {
        "Reputación empresarial": "Riesgo de imagen negativa por falta de compromiso social.",
        "Impacto comunitario": "Menor contribución al bienestar social y ambiental.",
        "Fidelización de clientes": "Menos atractivo para consumidores con conciencia social.",
        "Atracción de talento": "Menos interés por parte de profesionales que buscan empresas responsables.",
        "Cumplimiento normativo": "Posible incumplimiento de estándares de sostenibilidad.",
        "Ventajas competitivas": "Mayor dificultad para diferenciarse positivamente en el mercado.",
    },
}

tiene_responsabilidad_social = {
    k: ({"Ejercicio de programas de responsabilidad social": k} | v)
    for k, v in tiene_responsabilidad_social.items()
}

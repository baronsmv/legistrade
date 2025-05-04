esta_registrada_exportador = {
    "Sí": {
        "Acceso a mercados": "Puede exportar productos regulados sin restricciones.",
        "Cumplimiento fiscal": "Cumple con los requisitos de comercio exterior.",
        "Confianza comercial": "Mayor credibilidad ante clientes y autoridades.",
        "Facilidades operativas": "Accede a beneficios y procedimientos simplificados.",
        "Expansión internacional": "Posibilidad de crecimiento en mercados globales.",
        "Protección legal": "Menos riesgos legales al operar bajo normas establecidas.",
    },
    "No": {
        "Acceso a mercados": "Limitaciones para exportar ciertos productos.",
        "Cumplimiento fiscal": "Mayor riesgo de incumplimiento y sanciones.",
        "Confianza comercial": "Menor credibilidad y confianza de socios comerciales.",
        "Facilidades operativas": "Trámites más complejos y costos administrativos elevados.",
        "Expansión internacional": "Dificultades para acceder a mercados extranjeros.",
        "Protección legal": "Mayor riesgo de conflictos legales y sanciones.",
    },
}

esta_registrada_exportador = {
    k: ({"Registro en el Padrón de Exportadores": k} | v)
    for k, v in esta_registrada_exportador.items()
}

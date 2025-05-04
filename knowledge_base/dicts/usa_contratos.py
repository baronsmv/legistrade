usa_contratos = {
    "Sí": {
        "Seguridad legal": "Cuenta con respaldo jurídico en caso de disputas.",
        "Claridad en acuerdos": "Los términos están definidos en documentos formales.",
        "Protección contra incumplimientos": "Puede exigir cumplimiento o aplicar sanciones.",
        "Profesionalismo": "Genera confianza y credibilidad en el mercado.",
        "Acceso a financiamiento": "Facilita la obtención de inversión y préstamos.",
    },
    "No": {
        "Seguridad legal": "Depende de acuerdos verbales, difíciles de probar.",
        "Claridad en acuerdos": "Las expectativas pueden ser ambiguas.",
        "Protección contra incumplimientos": "Opciones limitadas para reclamar.",
        "Profesionalismo": "Puede parecer menos estructurada o arriesgada.",
        "Acceso a financiamiento": "Menos atractiva para inversionistas y bancos.",
    },
}

usa_contratos = {
    k: ({"Uso de contratos escritos": k} | v) for k, v in usa_contratos.items()
}

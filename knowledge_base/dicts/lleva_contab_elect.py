lleva_contab_elect = {
    "Sí": {
        "Precisión y eficiencia": "Automatiza cálculos y reduce errores humanos.",
        "Cumplimiento fiscal": "Facilita la declaración de impuestos y reportes financieros.",
        "Acceso a la información": "Datos contables disponibles en tiempo real desde cualquier ubicación.",
        "Seguridad y respaldo": "Protección contra pérdida de datos mediante almacenamiento en la nube.",
        "Análisis financiero": "Generación de reportes detallados para mejor toma de decisiones.",
        "Costos operativos": "Reducción de gastos administrativos y mejora en gestión de recursos.",
    },
    "No": {
        "Precisión y eficiencia": "Mayor riesgo de errores por procesos manuales.",
        "Cumplimiento fiscal": "Mayor dificultad en el control y presentación de impuestos.",
        "Acceso a la información": "Datos almacenados físicamente, menos accesibles y con riesgo de pérdida.",
        "Seguridad y respaldo": "Mayor riesgo de pérdida o deterioro de documentos contables.",
        "Análisis financiero": "Menos herramientas para evaluación financiera eficiente.",
        "Costos operativos": "Gastos más elevados en administración y gestión manual.",
    },
}

lleva_contab_elect = {
    k: ({"Uso de contabilidad electrónica": k} | v)
    for k, v in lleva_contab_elect.items()
}

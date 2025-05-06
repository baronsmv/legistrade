emite_cfd = {
    "Sí": {
        "Cumplimiento fiscal": "Cumple con requisitos del SAT y normativas fiscales.",
        "Credibilidad comercial": "Mayor confianza de clientes y proveedores.",
        "Acceso a deducciones fiscales": "Puede aplicar deducciones y beneficios tributarios.",
        "Facilidad para operar": "Posibilidad de participar en licitaciones y grandes contratos.",
        "Automatización contable": "Integración con sistemas de facturación electrónica.",
        "Evita sanciones": "Minimiza riesgo de multas o problemas legales por evasión fiscal.",
    },
    "No": {
        "Cumplimiento fiscal": "Puede estar en incumplimiento con normativas fiscales.",
        "Credibilidad comercial": "Menor confianza de clientes y proveedores.",
        "Acceso a deducciones fiscales": "Limitaciones para deducciones y beneficios fiscales.",
        "Facilidad para operar": "Menos oportunidades para trabajar con grandes empresas.",
        "Automatización contable": "Mayor carga administrativa y procesos manuales.",
        "Evita sanciones": "Riesgo de multas por no declarar correctamente ingresos.",
    },
}

emite_cfd = {k: ({"Emisión de CFDI": k} | v) for k, v in emite_cfd.items()}

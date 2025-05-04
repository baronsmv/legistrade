seguridad_datos = {
    "Sí": {
        "Protección de datos": "Cifrado, autenticación segura y acceso restringido.",
        "Cumplimiento legal": "Adherencia a normativas como GDPR, CCPA y leyes locales.",
        "Confianza del usuario": "Genera mayor seguridad y lealtad de clientes.",
        "Gestión de riesgos": "Monitoreo constante contra ciberamenazas.",
        "Reputación empresarial": "Buena imagen en el mercado y diferenciación positiva.",
        "Impacto financiero": "Evita multas y pérdidas por brechas de seguridad.",
    },
    "No": {
        "Protección de datos": "Datos expuestos a accesos no autorizados.",
        "Cumplimiento legal": "Riesgo de incumplimiento de normativas y posibles sanciones.",
        "Confianza del usuario": "Menor confianza, posibilidad de fuga de clientes.",
        "Gestión de riesgos": "Mayor vulnerabilidad ante ataques cibernéticos.",
        "Reputación empresarial": "Riesgo de daños a la imagen y credibilidad.",
        "Impacto financiero": "Costos elevados por violaciones de seguridad y pérdida de datos.",
    },
}

seguridad_datos = {
    k: ({"Uso de medidas de seguridad para proteger los datos personales": k} | v)
    for k, v in seguridad_datos.items()
}

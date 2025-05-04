antiguedad = {
    "Nueva (menos de 4 años)": {
        "Obligaciones Fiscales": "Pueden acceder a incentivos fiscales para nuevos negocios",
        "Obligaciones Legales": "Menor exposición a litigios previos",
        "Acceso a financiamiento": "Puede ser difícil sin historial financiero",
        "Reputación y credibilidad": "Deben construir confianza desde cero",
        "Adaptabilidad y cambios": "Mayor flexibilidad para ajustes",
        "Relaciones con proveedores": "Difícil acceso a condiciones favorables",
        "Innovación": "Mayor impulso en la innovación",
    },
    "Intermedia (entre 4 y 10 años)": {
        "Obligaciones Fiscales": "Cumplimiento de normas fiscales más estructuradas",
        "Obligaciones Legales": "Posible acumulación de contratos y obligaciones",
        "Acceso a financiamiento": "Acceso moderado a créditos con historial en crecimiento",
        "Reputación y credibilidad": "Desarrollo de identidad de marca y reconocimiento",
        "Adaptabilidad y cambios": "En fase de expansión y optimización",
        "Relaciones con proveedores": "Construcción de relaciones estratégicas",
        "Innovación": "Balance entre innovación y estabilidad",
    },
    "Establecida (más de 10 años)": {
        "Obligaciones Fiscales": "Sujetos a auditorías y posible mayor carga tributaria",
        "Obligaciones Legales": "Historial legal que puede incluir litigios o responsabilidades adquiridas",
        "Acceso a financiamiento": "Mayor facilidad para obtener financiamiento por estabilidad",
        "Reputación y credibilidad": "Posicionamiento fuerte en el mercado y confianza consolidada",
        "Adaptabilidad y cambios": "Cambios requieren procesos más estructurados",
        "Relaciones con proveedores": "Beneficios por relaciones a largo plazo",
        "Innovación": "Puede ser más tradicional, pero con inversión en nuevas ideas",
    },
}

antiguedad = {
    k: ({"Tipo de empresa según su antigüedad": k} | v) for k, v in antiguedad.items()
}

tamano = {
    "Microempresa (menos de 10 empleados)": {
        "Acceso a financiamiento": "Autofinanciadas o pequeños créditos",
        "Estructura organizativa": "Organización simple, dueño toma decisiones",
        "Alcance de mercado": "Local, poca capacidad de expansión",
        "Nivel de adopción tecnológica": "Uso básico, digitalización limitada",
        "Cumplimiento regulatorio": "Menor carga fiscal, trámites simplificados",
        "Condiciones de contratación": "Relación cercana con empleados, contratos flexibles",
    },
    "Empresa Pequeña (entre 11 y 50 empleados)": {
        "Acceso a financiamiento": "Créditos bancarios o inversionistas pequeños",
        "Estructura organizativa": "Gerencias básicas, propietario aún toma decisiones clave",
        "Alcance de mercado": "Expansión regional, competencia con otros pequeños negocios",
        "Nivel de adopción tecnológica": "Mayor integración digital, sistemas administrativos",
        "Cumplimiento regulatorio": "Más cumplimiento tributario, normativas sectoriales",
        "Condiciones de contratación": "Mayor formalidad en contratación, prestaciones mínimas",
    },
    "Empresa Mediana (entre 51 y 250 empleados)": {
        "Acceso a financiamiento": "Acceso a financiamiento institucional y créditos mayores",
        "Estructura organizativa": "Áreas especializadas, delegación de funciones",
        "Alcance de mercado": "Nacional e internacional, competidores establecidos",
        "Nivel de adopción tecnológica": "Automatización, software empresarial, ERP",
        "Cumplimiento regulatorio": "Cumplimiento estricto de normas fiscales y laborales",
        "Condiciones de contratación": "Contratos formales, prestaciones mayores, sindicatos en algunos casos",
    },
    "Empresa Grande (más de 250 empleados)": {
        "Acceso a financiamiento": "Acceso a mercados de capital y grandes inversionistas",
        "Estructura organizativa": "Departamentos complejos, jerarquías definidas",
        "Alcance de mercado": "Global, expansión internacional y diversificación",
        "Nivel de adopción tecnológica": "Innovación constante, inteligencia artificial, big data",
        "Cumplimiento regulatorio": "Alto nivel de regulación, auditorías y transparencia",
        "Condiciones de contratación": "Normativas estrictas, beneficios completos, representación sindical",
    },
}

tamano = {k: ({"Tipo de empresa según su tamaño": k} | v) for k, v in tamano.items()}

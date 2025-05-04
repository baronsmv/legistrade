from utils.dicts import nombre_tuples

tipo_contratos = {
    (): {
        "Características": (
            "Máxima flexibilidad en acuerdos y operaciones.",
            "Riesgo alto de disputas, falta de respaldo legal y posibles problemas de cumplimiento.",
        ),
    },
    ("Clientes",): {
        "Características": (
            "Establece términos claros de venta y servicio.",
            "Ayuda a gestionar pagos y evitar disputas comerciales.",
        ),
    },
    ("Proveedores",): {
        "Características": (
            "Garantiza la entrega de insumos esenciales.",
            "Permite definir calidad y tiempos de entrega.",
        ),
    },
    ("Trabajadores",): {
        "Características": (
            "Brinda estabilidad laboral y operativa.",
            "Facilita el cumplimiento de derechos y obligaciones.",
        ),
    },
    ("Prestadores",): {
        "Características": (
            "Flexibilidad para contratación especializada.",
            "Evita costos fijos de empleados permanentes.",
        ),
    },
    ("Clientes", "Proveedores"): {
        "Características": (
            "Asegura flujo de ventas y suministro.",
            "Evita interrupciones en la cadena de producción.",
        ),
    },
    ("Clientes", "Trabajadores"): {
        "Características": (
            "Define expectativas claras de servicio.",
            "Mejora atención al cliente y eficiencia.",
        ),
    },
    ("Clientes", "Prestadores"): {
        "Características": (
            "Amplía la oferta de servicios sin contratar empleados.",
            "Ayuda en áreas especializadas como marketing o tecnología.",
        ),
    },
    ("Proveedores", "Trabajadores"): {
        "Características": (
            "Garantiza insumos y fuerza laboral alineada.",
            "Minimiza interrupciones y pérdida de productividad.",
        ),
    },
    ("Proveedores", "Prestadores"): {
        "Características": (
            "Optimiza la gestión de insumos con apoyo externo.",
            "Permite escalar producción sin ampliar plantilla fija.",
        ),
    },
    ("Trabajadores", "Prestadores"): {
        "Características": (
            "Complementa el equipo interno con expertos externos.",
            "Reduce sobrecarga de trabajo y mejora eficiencia.",
        ),
    },
    ("Clientes", "Proveedores", "Trabajadores"): {
        "Características": (
            "Estructura sólida para ventas y producción.",
            "Minimiza riesgos operativos y mejora rendimiento.",
        ),
    },
    ("Clientes", "Proveedores", "Prestadores"): {
        "Características": (
            "Equilibrio entre suministro y servicios externos.",
            "Facilita expansión sin incrementar costos fijos.",
        ),
    },
    ("Clientes", "Trabajadores", "Prestadores"): {
        "Características": (
            "Integración eficiente entre empleados y servicios tercerizados.",
            "Optimiza la atención al cliente y la productividad.",
        ),
    },
    ("Proveedores", "Trabajadores", "Prestadores"): {
        "Características": (
            "Cobertura completa de insumos, equipo y servicios externos.",
            "Reduce costos operativos y mejora tiempos de entrega.",
        ),
    },
    ("Clientes", "Proveedores", "Trabajadores", "Prestadores"): {
        "Características": (
            "Modelo empresarial robusto con estructura completa.",
            "Maximiza la eficiencia operativa y reduce riesgos comerciales.",
        ),
    },
}

tipo_contratos = nombre_tuples(
    tipo_contratos,
    nombre="Contratos usados por la empresa",
    prefijo_opciones="Con",
    si_ninguno="Sin contratos.",
)

tipo_contratos = {
    (): {
        "características_contrato": (
            "Máxima flexibilidad en acuerdos y operaciones.",
            "Riesgo alto de disputas, falta de respaldo legal y posibles problemas de cumplimiento.",
        ),
    },
    ("clientes",): {
        "características_contrato": (
            "Establece términos claros de venta y servicio.",
            "Ayuda a gestionar pagos y evitar disputas comerciales.",
        ),
    },
    ("proveedores",): {
        "características_contrato": (
            "Garantiza la entrega de insumos esenciales.",
            "Permite definir calidad y tiempos de entrega.",
        ),
    },
    ("trabajadores",): {
        "características_contrato": (
            "Brinda estabilidad laboral y operativa.",
            "Facilita el cumplimiento de derechos y obligaciones.",
        ),
    },
    ("prestadores",): {
        "características_contrato": (
            "Flexibilidad para contratación especializada.",
            "Evita costos fijos de empleados permanentes.",
        ),
    },
    ("clientes", "proveedores"): {
        "características_contrato": (
            "Asegura flujo de ventas y suministro.",
            "Evita interrupciones en la cadena de producción.",
        ),
    },
    ("clientes", "trabajadores"): {
        "características_contrato": (
            "Define expectativas claras de servicio.",
            "Mejora atención al cliente y eficiencia.",
        ),
    },
    ("clientes", "prestadores"): {
        "características_contrato": (
            "Amplía la oferta de servicios sin contratar empleados.",
            "Ayuda en áreas especializadas como marketing o tecnología.",
        ),
    },
    ("proveedores", "trabajadores"): {
        "características_contrato": (
            "Garantiza insumos y fuerza laboral alineada.",
            "Minimiza interrupciones y pérdida de productividad.",
        ),
    },
    ("proveedores", "prestadores"): {
        "características_contrato": (
            "Optimiza la gestión de insumos con apoyo externo.",
            "Permite escalar producción sin ampliar plantilla fija.",
        ),
    },
    ("trabajadores", "prestadores"): {
        "características_contrato": (
            "Complementa el equipo interno con expertos externos.",
            "Reduce sobrecarga de trabajo y mejora eficiencia.",
        ),
    },
    ("clientes", "proveedores", "trabajadores"): {
        "características_contrato": (
            "Estructura sólida para ventas y producción.",
            "Minimiza riesgos operativos y mejora rendimiento.",
        ),
    },
    ("clientes", "proveedores", "prestadores"): {
        "características_contrato": (
            "Equilibrio entre suministro y servicios externos.",
            "Facilita expansión sin incrementar costos fijos.",
        ),
    },
    ("clientes", "trabajadores", "prestadores"): {
        "características_contrato": (
            "Integración eficiente entre empleados y servicios tercerizados.",
            "Optimiza la atención al cliente y la productividad.",
        ),
    },
    ("proveedores", "trabajadores", "prestadores"): {
        "características_contrato": (
            "Cobertura completa de insumos, equipo y servicios externos.",
            "Reduce costos operativos y mejora tiempos de entrega.",
        ),
    },
    ("clientes", "proveedores", "trabajadores", "prestadores"): {
        "características_contrato": (
            "Modelo empresarial robusto con estructura completa.",
            "Maximiza la eficiencia operativa y reduce riesgos comerciales.",
        ),
    },
}

tipo_contratos = {
    k: (
        {
            "nombre_tipo_contratos": (
                (f"Con {elemento}." for elemento in k) if k else "Sin contratos."
            )
        }
        | v
    )
    for k, v in tipo_contratos.items()
}

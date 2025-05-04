ecommerce = {
    "Sí": {
        "Alcance y acceso": "Puede vender a clientes globalmente.",
        "Costos operativos": "Menores costos de alquiler y mantenimiento.",
        "Experiencia del cliente": "Compra personalizada con recomendaciones basadas en datos.",
        "Marketing y publicidad": "SEO, redes sociales y anuncios digitales.",
        "Gestión de inventario y logística": "Optimización de envíos y almacén.",
        "Disponibilidad y horarios de venta": "Ventas 24/7 sin restricciones de horario.",
    },
    "No": {
        "Alcance y acceso": "Limitado a la ubicación física de la tienda.",
        "Costos operativos": "Gastos en espacio físico y empleados.",
        "Experiencia del cliente": "Interacción presencial y atención directa.",
        "Marketing y publicidad": "Publicidad tradicional y boca a boca.",
        "Gestión de inventario y logística": "Inventario para ventas en tienda física.",
        "Disponibilidad y horarios de venta": "Limitado a horarios comerciales.",
    },
}

ecommerce = {
    k: ({"Uso de plataforma de comercio electrónico": k} | v)
    for k, v in ecommerce.items()
}

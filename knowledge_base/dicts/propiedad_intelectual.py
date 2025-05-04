propiedad_intelectual = {
    (): {
        "Protección legal": "No tiene protección contra uso indebido.",
        "Ventaja competitiva": "Riesgo de que terceros copien la marca o invención.",
        "Duración": "No aplica.",
        "Uso común": "Negocios informales o sin estrategia de propiedad intelectual.",
    },
    ("Marca",): {
        "Protección legal": "Resguarda el nombre y logotipo de la empresa.",
        "Ventaja competitiva": "Evita que terceros usen la identidad comercial.",
        "Duración": "Renovable cada 10 años.",
        "Uso común": "Empresas que buscan reconocimiento de marca.",
    },
    ("Patente",): {
        "Protección legal": "Resguarda una invención técnica.",
        "Ventaja competitiva": "Impide que otros copien la innovación.",
        "Duración": "Hasta 20 años.",
        "Uso común": "Empresas con productos tecnológicos o farmacéuticos.",
    },
    ("Marca", "Patente"): {
        "Protección legal": "Resguarda tanto la identidad comercial como la innovación.",
        "Ventaja competitiva": "Máxima protección contra copias y competencia desleal.",
        "Duración": "Depende del tipo de registro.",
        "Uso común": "Empresas con productos innovadores y fuerte identidad de marca.",
    },
}

propiedad_intelectual = {
    k: (
        {
            "Registro de propiedad intelectual": (
                value
                if len(
                    value := tuple(
                        (f"De {elemento.lower()}." for elemento in k)
                        if k
                        else "Sin registros."
                    )
                )
                > 1
                else value[0]
            )
        }
        | v
    )
    for k, v in propiedad_intelectual.items()
}

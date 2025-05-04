def nombre_tuples(
    kb: dict, nombre: str, prefijo_opciones: str, si_ninguno: str
) -> dict:
    def procesar_valor(clave):
        if clave:
            resultado = tuple(
                f"{prefijo_opciones} {elemento.lower()}." for elemento in clave
            )
            return resultado[0] if len(resultado) == 1 else resultado
        else:
            return si_ninguno

    return {
        k: {
            nombre: procesar_valor(k),
            **v,
        }
        for k, v in kb.items()
    }

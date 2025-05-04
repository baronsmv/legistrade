from django import forms

from knowledge_base.dicts import knowledge_base as kb


def get_choices(attr: str, key: str = "nombre") -> tuple:
    return tuple((k, v[f"{key}_{attr}"]) for k, v in kb[attr].items())


def bool_choice(label: str, no_aplica: bool = False) -> forms.ChoiceField:
    return forms.ChoiceField(
        label=label,
        choices=((True, "Sí"), (False, "No"))
        + (("None", "No aplica") if no_aplica else ()),
        widget=forms.RadioSelect,
    )


class EmpresaForm(forms.Form):
    # Perfil legal y operativo de la empresa
    regimen = forms.ChoiceField(
        label="Régimen legal",
        choices=get_choices("regimen"),
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el régimen legal bajo el cual opera tu empresa.",
    )
    sector = forms.ChoiceField(
        label="Sector principal",
        choices=get_choices("sector"),
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el sector principal de tu empresa.",
    )
    antiguedad = forms.ChoiceField(
        label="Años de operación",
        choices=[
            ("nueva", "Menos de 4 años."),
            ("intermedia", "Entre 4 y 10 años."),
            ("establecida", "Más de 10 años."),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Indica cuántos años lleva operando tu empresa.",
    )
    tamano = forms.ChoiceField(
        label="Tamaño",
        choices=[
            ("micro", "Menos de 10 empleados."),
            ("pequeña", "Entre 11 y 50 empleados."),
            ("mediana", "Entre 51 y 250 empleados."),
            ("grande", "Más de 250 empleados."),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el número de empleados trabajando en tu empresa.",
    )

    # Obligaciones y derechos contractuales
    usa_contratos = bool_choice("¿Utiliza contratos escritos?")
    tipo_contratos = forms.MultipleChoiceField(
        label="Tipos de contratos que utiliza",
        choices=[
            ("clientes", "Con clientes"),
            ("proveedores", "Con proveedores"),
            ("trabajadores", "Con trabajadores"),
            ("prestadores", "Con prestadores de servicios"),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    # Requisitos en comercio electrónico
    ecommerce = bool_choice("¿Tiene plataforma de comercio electrónico?")
    usa_terminos_legales_web = bool_choice(
        "¿Cuenta con aviso de privacidad y términos legales en su sitio web?"
    )
    usa_medidas_seguridad = bool_choice(
        label="¿Tiene medidas de seguridad para proteger los datos personales?"
    )

    # Protección legal sobre activos intangibles
    propiedad_intelectual = forms.ChoiceField(
        label="¿Ha registrado propiedad intelectual?",
        choices=[
            ("marca", "Marca"),
            ("patente", "Patente"),
            ("ambos", "Ambos"),
            ("ninguno", "Ninguno"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    # Obligaciones fiscales
    declara_impuestos = bool_choice(label="¿Declara impuestos regularmente?")
    lleva_contabilidad = bool_choice(label="¿Lleva contabilidad electrónica?")

    # Información fiscal y contable detallada
    regimen_fiscal = forms.ChoiceField(
        label="Régimen Fiscal",
        choices=[
            ("resico", "Régimen Simplificado de Confianza (RESICO)"),
            ("rif", "Régimen de Incorporación Fiscal (RIF)"),
            ("general", "Régimen General de Ley"),
            ("otra", "Otro"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el régimen fiscal bajo el cual se encuentra registrada tu empresa.",
    )
    usa_cfd = bool_choice(label="¿Emite CFDI?")

    # Licencias y permisos específicos
    tiene_licencias_permisos = bool_choice(
        "¿Posee las licencias y permisos requeridos por su actividad económica?"
    )

    # Internacionalización y comercio exterior
    tiene_experiencia_exportacion = bool_choice("¿Tiene experiencia en exportación?")
    esta_registrada_exportador = bool_choice(
        "¿Está registrada en el Padrón de Exportadores?"
    )

    # Estrategias de sostenibilidad y responsabilidad social
    tiene_practicas_sostenibles = bool_choice("¿Implementa prácticas sostenibles?")
    tiene_responsabilidad_social = bool_choice(
        "¿Tiene programas de responsabilidad social empresarial?"
    )

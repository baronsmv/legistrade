from django import forms

from knowledge_base.dicts import knowledge_base as kb


def get_choices(attr: str) -> tuple:
    return tuple((k, k) for k in kb[attr].keys())


def bool_choice(label: str, no_aplica: bool = False) -> forms.ChoiceField:
    return forms.ChoiceField(
        label=label,
        choices=(("Sí", "Sí"), ("No", "No"))
        + ((None, "No aplica") if no_aplica else ()),
        widget=forms.RadioSelect,
    )


class EmpresaForm(forms.Form):
    # Perfil legal, fiscal y operativo de la empresa
    regimen_legal = forms.ChoiceField(
        label="Régimen legal",
        choices=get_choices("regimen_legal"),
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el régimen legal bajo el cual opera tu empresa.",
    )
    regimen_fiscal = forms.ChoiceField(
        label="Régimen Fiscal",
        choices=get_choices("regimen_fiscal"),
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el régimen fiscal bajo el cual se encuentra registrada tu empresa.",
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
            ("Nueva (menos de 4 años)", "Menos de 4 años"),
            ("Intermedia (entre 4 y 10 años)", "Entre 4 y 10 años"),
            ("Establecida (más de 10 años)", "Más de 10 años"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Indica cuántos años lleva operando tu empresa.",
    )
    tamano = forms.ChoiceField(
        label="Tamaño",
        choices=[
            ("Microempresa (menos de 10 empleados)", "Menos de 10 empleados"),
            ("Empresa Pequeña (entre 11 y 50 empleados)", "Entre 11 y 50 empleados"),
            ("Empresa Mediana (entre 51 y 250 empleados)", "Entre 51 y 250 empleados"),
            ("Empresa Grande (más de 250 empleados)", "Más de 250 empleados"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el número de empleados trabajando en tu empresa.",
    )

    # Obligaciones y derechos contractuales
    usa_contratos = bool_choice("¿Utiliza contratos escritos?")
    tipo_contratos = forms.MultipleChoiceField(
        label="Tipos de contratos que utiliza",
        choices=(
            ("Clientes", "Con clientes"),
            ("Proveedores", "Con proveedores"),
            ("Trabajadores", "Con trabajadores"),
            ("Prestadores", "Con prestadores de servicios"),
        ),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    # Requisitos en comercio electrónico
    ecommerce = bool_choice("¿Tiene plataforma de comercio electrónico?")
    usa_aviso_privacidad = bool_choice(
        "¿Cuenta con aviso de privacidad y términos legales en su sitio web?"
    )
    seguridad_datos = bool_choice(
        label="¿Tiene medidas de seguridad para proteger los datos personales?"
    )

    # Protección legal sobre activos intangibles
    propiedad_intelectual = forms.MultipleChoiceField(
        label="¿Ha registrado propiedad intelectual?",
        choices=(
            ("Marca", "Marca"),
            ("Patente", "Patente"),
        ),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    # Obligaciones fiscales
    declara_impuestos = bool_choice(label="¿Declara impuestos regularmente?")
    lleva_contab_elect = bool_choice(label="¿Lleva contabilidad electrónica?")

    # Información fiscal y contable detallada
    emite_cfd = bool_choice(label="¿Emite CFDI?")

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

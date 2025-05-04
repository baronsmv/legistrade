from django import forms


class EmpresaForm(forms.Form):
    # Perfil legal y operativo de la empresa
    regimen = forms.ChoiceField(
        label="Régimen legal",
        choices=[
            ("sa", "Sociedad Anónima (S.A.)"),
            ("srl", "Sociedad de Responsabilidad Limitada (S. de R.L.)"),
            ("sapi", "Sociedad Anónima Promotora de Inversión (S.A.P.I.)"),
            ("sas", "Sociedad por Acciones Simplificada (S.A.S.)"),
            ("sc", "Sociedad Civil (S.C.)"),
            ("sca", "Sociedad Comandita por Acciones (S. en C.A.)"),
            ("sofom", "Sociedades Financieras de Objeto Múltiple (SOFOM)"),
            ("scoop", "Sociedad Cooperativa"),
            ("ap", "Asociación en Participación"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Selecciona el régimen legal bajo el cual opera tu empresa.",
    )
    sector = forms.ChoiceField(
        label="Sector principal",
        choices={
            "agricultura": "Sector Agrícola",
            "alimentos_bebidas": "Industria de Alimentos y Bebidas",
            "automotriz": "Industria Automotriz",
            "comercio": "Sector Comercial",
            "construcción": "Industria de la Construcción",
            "ecommerce": "Comercio Electrónico",
            "educación": "Sector Educativo",
            "energía": "Sector Energético",
            "entretenimiento_medios": "Industria del Entretenimiento y Medios",
            "farmacéutico": "Industria Farmacéutica",
            "finanzas": "Sector Financiero",
            "ganadería": "Sector Ganadero",
            "importación": "Sector de Importación",
            "industrial": "Industria General",
            "logística_transporte": "Sector de Logística y Transporte",
            "manufactura": "Industria Manufacturera",
            "minería": "Industria Minera",
            "moda_textil": "Industria de Moda y Textiles",
            "pesca": "Sector Pesquero",
            "retail_comercio_menor": "Comercio Minorista",
            "salud": "Sector Salud",
            "seguros_financieros": "Sector de Seguros Financieros",
            "servicios": "Sector de Servicios",
            "silvicultura": "Sector Forestal",
            "tecnología": "Industria Tecnológica",
            "telecomunicaciones": "Sector de Telecomunicaciones",
            "turismo": "Industria del Turismo",
        },
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
    usa_contratos = forms.ChoiceField(
        label="¿Utiliza contratos escritos?",
        choices=[("sí", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
    )
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
    ecommerce = forms.BooleanField(
        label="¿Tiene plataforma de comercio electrónico?", required=False
    )
    usa_terminos_legales_web = forms.ChoiceField(
        label="¿Cuenta con aviso de privacidad y términos legales en su sitio web?",
        choices=[(True, "Sí"), (False, "No"), (None, "No aplica")],
        widget=forms.RadioSelect,
    )
    usa_medidas_seguridad = forms.ChoiceField(
        label="¿¿Tiene medidas de seguridad para proteger los datos personales?",
        choices=[(True, "Sí"), (False, "No"), (None, "No aplica")],
        widget=forms.RadioSelect,
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
    declara_impuestos = forms.BooleanField(
        label="¿Declara impuestos regularmente?", required=False
    )
    lleva_contabilidad = forms.BooleanField(
        label="¿Lleva contabilidad electrónica?", required=False
    )

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
    usa_cfd = forms.BooleanField(label="¿Emite CFDI?", required=False)

    # Licencias y permisos específicos
    tiene_licencias_permisos = forms.BooleanField(
        label="¿Posee las licencias y permisos requeridos por su actividad económica?",
        required=False,
    )

    # Internacionalización y comercio exterior
    tiene_experiencia_exportacion = forms.BooleanField(
        label="¿Tiene experiencia en exportación?",
        required=False,
    )
    esta_registrada_exportador = forms.BooleanField(
        label="¿Está registrada en el Padrón de Exportadores?",
        required=False,
    )

    # Estrategias de sostenibilidad y responsabilidad social
    tiene_practicas_sostenibles = forms.BooleanField(
        label="¿Implementa prácticas sostenibles?",
        required=False,
    )
    tiene_responsabilidad_social = forms.BooleanField(
        label="¿Tiene programas de responsabilidad social empresarial?",
        required=False,
    )

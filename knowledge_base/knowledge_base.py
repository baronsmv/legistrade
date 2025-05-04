knowledge_base = {
    "regimen": {
        "sa": {
            "nombre": "Sociedad Anónima (S.A.)",
            "descripción": "Sociedad Anónima con responsabilidad limitada al capital aportado.",
            "mercantil": True,
            "min_socios": 2,
            "capital_minimo": True,
            "flexibilidad_admin": "Moderada",
            "uso": "Empresas medianas y grandes",
            "derechos": (
                "Emitir acciones para financiamiento",
                "Acceso a mercados bursátiles",
                "Responsabilidad limitada para accionistas",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR e IVA",
                "Declaraciones mensuales y anuales",
                "Contabilidad electrónica",
                "Retención de impuestos a empleados",
            ),
            "obligaciones_legales": (
                "Celebración de asambleas anuales",
                "Registro en el RFC",
                "Depósito de estados financieros",
                "Renovación de matrícula mercantil",
            ),
            "características": (
                "Gobierno corporativo estructurado",
                "Mayor regulación en transparencia financiera",
                "Requiere consejo de administración",
            ),
        },
        "srl": {
            "nombre": "Sociedad de Responsabilidad Limitada (S. de R.L.)",
            "descripción": "Sociedad de Responsabilidad Limitada sin títulos negociables.",
            "mercantil": True,
            "min_socios": 2,
            "capital_minimo": False,
            "flexibilidad_admin": "Alta",
            "uso": "Negocios familiares o pequeños",
            "derechos": (
                "Limitación de responsabilidad de los socios",
                "Flexibilidad en estructura organizativa",
                "No requiere emisión de acciones",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR e IVA",
                "Declaraciones mensuales y anuales",
                "Contabilidad electrónica",
                "Retención de impuestos a empleados",
            ),
            "obligaciones_legales": (
                "Celebración de asambleas anuales",
                "Registro en el RFC",
                "Depósito de estados financieros",
                "Renovación de matrícula mercantil",
            ),
            "características": (
                "Adecuada para pequeñas y medianas empresas",
                "Menos regulación que una S.A.",
                "Cada socio tiene participación proporcional en decisiones",
            ),
        },
        "sapi": {
            "nombre": "Sociedad Anónima Promotora de Inversión (S.A.P.I.)",
            "descripción": "Variante flexible de la S.A. para inversión.",
            "mercantil": True,
            "min_socios": 2,
            "capital_minimo": True,
            "flexibilidad_admin": "Muy flexible",
            "uso": "Empresas con potencial de inversión",
            "derechos": (
                "Facilidad para atraer inversión privada",
                "Permite pactos entre socios sin restricciones estrictas",
                "Puede evolucionar hacia una S.A.B. (Sociedad Anónima Bursátil)",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR e IVA",
                "Declaraciones mensuales y anuales",
                "Contabilidad electrónica",
                "Retención de impuestos a empleados",
            ),
            "obligaciones_legales": (
                "Celebración de asambleas anuales",
                "Registro en el RFC",
                "Depósito de estados financieros",
                "Renovación de matrícula mercantil",
            ),
            "características": (
                "Utilizada por startups y empresas en crecimiento",
                "Ofrece mayor flexibilidad en gobierno corporativo",
                "Regulación intermedia entre S.A. y S.A.B.",
            ),
        },
        "sas": {
            "nombre": "Sociedad por Acciones Simplificada (S.A.S.)",
            "descripción": "Sociedad de una sola persona con un proceso ágil de creación.",
            "mercantil": True,
            "min_socios": 1,
            "capital_minimo": False,
            "flexibilidad_admin": "Alta",
            "uso": "Emprendimientos pequeños",
            "derechos": (
                "Constitución ágil y electrónica",
                "No requiere capital mínimo inicial",
                "Acceso a responsabilidad limitada sin estructura compleja",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR e IVA",
                "Declaraciones mensuales y anuales",
                "Contabilidad electrónica",
            ),
            "obligaciones_legales": (
                "Registro en el RFC",
                "Renovación de matrícula mercantil",
            ),
            "características": (
                "Ideal para emprendedores y pequeñas empresas",
                "Menos burocracia y costos de operación",
                "No puede cotizar en bolsa ni captar inversión pública",
            ),
        },
        "sc": {
            "nombre": "Sociedad Civil (S.C.)",
            "descripción": "Sociedad utilizada para servicios profesionales.",
            "mercantil": False,
            "min_socios": 2,
            "capital_minimo": False,
            "flexibilidad_admin": "Variable",
            "uso": "Servicios profesionales (abogados, consultores, etc.)",
            "derechos": (
                "Flexibilidad en estructura y operación",
                "Uso común en profesiones liberales",
                "No tiene fines de lucro mercantil",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR",
                "Declaraciones anuales",
                "Contabilidad electrónica",
            ),
            "obligaciones_legales": (
                "Registro en el RFC",
                "Renovación de matrícula mercantil",
            ),
            "características": (
                "Responsabilidad ilimitada de los socios en algunos casos",
                "No puede realizar actividades comerciales masivas",
                "Opera como asociación de profesionales con objetivos comunes",
            ),
        },
        "sca": {
            "nombre": "Sociedad Comandita por Acciones (S. en C.A.)",
            "descripción": "Sociedad con socios comanditarios e ilimitados.",
            "mercantil": True,
            "min_socios": 2,
            "capital_minimo": True,
            "flexibilidad_admin": "Moderada",
            "uso": "Empresas con socios inversionistas y gestores activos",
            "derechos": (
                "Posibilidad de tener socios comanditarios sin gestión directa",
                "Acceso a financiamiento mediante emisión de acciones",
                "Socios gestores con control operativo",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR e IVA",
                "Declaraciones mensuales y anuales",
                "Contabilidad electrónica",
                "Retención de impuestos a empleados",
            ),
            "obligaciones_legales": (
                "Celebración de asambleas anuales",
                "Registro en el RFC",
                "Depósito de estados financieros",
                "Renovación de matrícula mercantil",
            ),
            "características": (
                "Combinación de responsabilidad limitada y ilimitada",
                "Modelo menos común en el mercado actual",
                "Regulación más estricta para socios administradores",
            ),
        },
        "sofom": {
            "nombre": "Sociedades Financieras de Objeto Múltiple (SOFOM)",
            "descripción": "Instituciones financieras de crédito.",
            "mercantil": True,
            "min_socios": None,
            "capital_minimo": "Variable",
            "flexibilidad_admin": "Alta",
            "uso": "Instituciones financieras",
            "derechos": (
                "Acceso a financiamiento sin ser bancos",
                "Regulación específica en el sector financiero",
                "Capacidad de otorgar créditos y operar en mercados de capital",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR e IVA",
                "Declaraciones mensuales y anuales",
                "Cumplimiento de regulaciones financieras",
            ),
            "obligaciones_legales": (
                "Debe cumplir con normativas de la CNBV",
                "Registro en el RFC",
                "Cumplimiento de normativas bancarias",
            ),
            "características": (
                "Alta supervisión en prácticas de transparencia",
                "Importante para el crédito empresarial y personal",
            ),
        },
        "scoop": {
            "nombre": "Sociedad Cooperativa",
            "descripción": "Sociedad basada en cooperación y beneficios colectivos.",
            "mercantil": True,
            "min_socios": 5,
            "capital_minimo": False,
            "flexibilidad_admin": "Alta",
            "uso": "Negocios colectivos",
            "derechos": (
                "Administración democrática por los socios",
                "Distribución equitativa de beneficios",
                "Fomento de economía social y solidaria",
            ),
            "obligaciones_fiscales": (
                "Pago de ISR e IVA",
                "Declaraciones mensuales y anuales",
                "Contabilidad electrónica",
            ),
            "obligaciones_legales": (
                "Registro en el RFC",
                "Renovación de matrícula mercantil",
            ),
            "características": (
                "Modelo basado en participación equitativa",
                "Puede ser de producción, consumo o ahorro",
                "Regulación distinta a sociedades mercantiles tradicionales",
            ),
        },
        "ap": {
            "nombre": "Asociación en Participación",
            "descripción": "Acuerdo entre empresarios e inversionistas sin sociedad formal.",
            "mercantil": False,
            "min_socios": 2,
            "capital_minimo": False,
            "flexibilidad_admin": "Alta",
            "uso": "Inversiones y proyectos específicos",
            "derechos": (
                "Socios participan sin figurar en el nombre de la empresa",
                "Permite inversión sin gestión directa",
                "Flexibilidad en acuerdos entre asociados",
            ),
            "obligaciones_fiscales": ("Pago de ISR", "Declaraciones anuales"),
            "obligaciones_legales": ("Registro en el RFC",),
            "características": (
                "No tiene personalidad jurídica propia",
                "Modelo usado en negocios de inversión privada",
                "Regulación flexible en términos de aportación y ganancia",
            ),
        },
    },
    "sector": {
        "agricultura": {
            "características": (
                "Dependencia de factores climáticos",
                "Regulación sobre uso de pesticidas y fertilizantes",
                "Acceso a financiamiento condicionado a prácticas sostenibles",
            ),
            "derechos": (
                "Subsidios y apoyos gubernamentales",
                "Beneficios fiscales en zonas rurales",
                "Acceso preferencial a programas de exportación",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción agrícola",
                "Cumplimiento de normativas de exportación",
                "Declaración de ingresos por cosechas y ventas",
            ),
            "obligaciones_legales": (
                "Regulación sobre condiciones de trabajo en el campo",
                "Normas de seguridad y salud para trabajadores agrícolas",
                "Cumplimiento de leyes sobre contratación temporal",
            ),
        },
        "alimentos_bebidas": {
            "características": (
                "Dependencia de regulaciones sanitarias nacionales",
                "Impacto de políticas de sustentabilidad en producción",
                "Alta competencia en distribución y consumo",
            ),
            "derechos": (
                "Acceso a financiamiento para producción alimentaria",
                "Beneficios fiscales en exportación de productos",
                "Facilidades para comercialización en supermercados",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y venta",
                "Cumplimiento de normativas fiscales sanitarias",
                "Declaración de ingresos por distribución de alimentos",
            ),
            "obligaciones_legales": (
                "Normas de seguridad e higiene alimentaria",
                "Regulación sobre etiquetado y publicidad",
                "Cumplimiento de leyes sobre protección al consumidor",
            ),
        },
        "automotriz": {
            "características": (
                "Alta competencia en el mercado global",
                "Regulación estricta en calidad y certificaciones",
                "Impacto de cambios tecnológicos en movilidad",
            ),
            "derechos": (
                "Acceso a financiamiento para manufactura y exportación",
                "Beneficios fiscales en producción de vehículos",
                "Facilidades para inversión en tecnología automotriz",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y comercialización",
                "Cumplimiento de normativas fiscales en importación y exportación",
                "Declaración de ingresos por venta de autopartes y vehículos",
            ),
            "obligaciones_legales": (
                "Normas de seguridad en fabricación y pruebas",
                "Regulación sobre emisión de contaminantes",
                "Cumplimiento de leyes de comercio internacional",
            ),
        },
        "comercio": {
            "características": (
                "Alta competencia en el mercado",
                "Dependencia de tendencias de consumo",
                "Regulación sobre comercio internacional",
            ),
            "derechos": (
                "Acceso a financiamiento para expansión",
                "Beneficios fiscales en zonas comerciales",
                "Facilidades para importación y exportación",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre ventas y servicios",
                "Cumplimiento de normativas de facturación",
                "Declaración de ingresos y gastos operativos",
            ),
            "obligaciones_legales": (
                "Regulación sobre contratación y condiciones laborales",
                "Normas de protección al consumidor",
                "Cumplimiento de leyes sobre publicidad y competencia",
            ),
        },
        "construcción": {
            "características": (
                "Alta inversión en maquinaria y tecnología",
                "Dependencia de políticas gubernamentales",
                "Regulación estricta en uso de suelo y materiales",
            ),
            "derechos": (
                "Acceso a financiamiento para proyectos de infraestructura",
                "Beneficios fiscales por inversión en vivienda y obras públicas",
                "Prioridad en licitaciones gubernamentales",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre materiales y servicios de construcción",
                "Cumplimiento de normativas fiscales en contrataciones públicas",
                "Declaración de ingresos y gastos operativos",
            ),
            "obligaciones_legales": (
                "Normas estrictas de seguridad en el trabajo",
                "Regulación sobre licencias y permisos de construcción",
                "Cumplimiento de leyes ambientales y de urbanismo",
            ),
        },
        "ecommerce": {
            "características": (
                "Alta dependencia de tecnología y logística",
                "Regulación sobre protección al consumidor digital",
                "Competencia global y adaptación a tendencias",
            ),
            "derechos": (
                "Acceso a mercados internacionales",
                "Beneficios fiscales en plataformas digitales",
                "Facilidades para pagos electrónicos",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre ventas digitales",
                "Cumplimiento de normativas de facturación electrónica",
                "Declaración de ingresos por comercio en línea",
            ),
            "obligaciones_legales": (
                "Regulación sobre teletrabajo y contratación remota",
                "Protección de datos personales de clientes",
                "Normas de seguridad en transacciones digitales",
            ),
        },
        "educación": {
            "características": (
                "Dependencia de inversión pública y privada",
                "Regulación en modelos de enseñanza y certificaciones",
                "Impacto de avances tecnológicos en educación",
            ),
            "derechos": (
                "Acceso a financiamiento para instituciones educativas",
                "Beneficios fiscales en universidades y centros de estudio",
                "Facilidades para inversión en tecnología educativa",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre servicios educativos",
                "Cumplimiento de normativas fiscales en subsidios educativos",
                "Declaración de ingresos por matrícula y cursos",
            ),
            "obligaciones_legales": (
                "Regulación sobre calidad y certificación académica",
                "Normas de seguridad en instalaciones educativas",
                "Cumplimiento de leyes sobre acceso equitativo a educación",
            ),
        },
        "energía": {
            "características": (
                "Dependencia de políticas gubernamentales",
                "Regulación sobre fuentes renovables y fósiles",
                "Impacto en mercados nacionales e internacionales",
            ),
            "derechos": (
                "Acceso a financiamiento para proyectos energéticos",
                "Beneficios fiscales en energías renovables",
                "Prioridad en licencias de exploración y explotación",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre generación y distribución de energía",
                "Cumplimiento de normativas fiscales en producción",
                "Declaración de ingresos por comercialización de energía",
            ),
            "obligaciones_legales": (
                "Regulación ambiental en producción energética",
                "Normativas de seguridad en instalaciones",
                "Cumplimiento de leyes sobre acceso y distribución equitativa",
            ),
        },
        "entretenimiento_medios": {
            "características": (
                "Alta competencia en producción y distribución de contenido",
                "Impacto de regulaciones sobre propiedad intelectual",
                "Dependencia de plataformas digitales y tendencias de consumo",
            ),
            "derechos": (
                "Acceso a financiamiento para producción audiovisual",
                "Beneficios fiscales en industrias creativas",
                "Facilidades para distribución en plataformas digitales",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y distribución",
                "Cumplimiento de normativas fiscales en derechos de autor",
                "Declaración de ingresos por publicidad y regalías",
            ),
            "obligaciones_legales": (
                "Normas sobre propiedad intelectual y derechos de autor",
                "Regulación sobre contenido y censura",
                "Cumplimiento de leyes sobre protección de datos",
            ),
        },
        "farmacéutico": {
            "características": (
                "Alta inversión en investigación y desarrollo",
                "Dependencia de regulaciones sanitarias internacionales",
                "Impacto de políticas gubernamentales en acceso a salud",
            ),
            "derechos": (
                "Acceso a financiamiento para investigación médica",
                "Protección de propiedad intelectual en farmacéuticas",
                "Facilidades para comercialización y distribución de medicamentos",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y venta de fármacos",
                "Cumplimiento de normativas fiscales en exportación",
                "Declaración de ingresos por comercialización médica",
            ),
            "obligaciones_legales": (
                "Regulación estricta en calidad y seguridad",
                "Normas de ética médica y pruebas clínicas",
                "Cumplimiento de leyes sobre acceso equitativo a medicamentos",
            ),
        },
        "finanzas": {
            "características": (
                "Alta regulación gubernamental",
                "Dependencia de estabilidad económica global",
                "Riesgo de crisis financieras y fluctuaciones del mercado",
            ),
            "derechos": (
                "Acceso a mercados internacionales",
                "Protección legal de inversiones",
                "Regulación que permite estabilidad financiera",
            ),
            "obligaciones_fiscales": (
                "Cumplimiento de normativas de lavado de dinero",
                "Pago de impuestos sobre transacciones financieras",
                "Declaración de ingresos y operaciones bancarias",
            ),
            "obligaciones_legales": (
                "Regulación sobre contratación de asesores financieros",
                "Normas de transparencia en relaciones laborales",
                "Cumplimiento de normativas sobre protección al consumidor",
            ),
        },
        "ganadería": {
            "características": (
                "Dependencia de factores climáticos",
                "Regulación sobre uso de antibióticos y alimentación animal",
                "Acceso a financiamiento condicionado a prácticas sostenibles",
            ),
            "derechos": (
                "Acceso a subsidios gubernamentales",
                "Beneficios fiscales por producción agropecuaria",
                "Facilidades para exportación de productos cárnicos",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y comercialización",
                "Cumplimiento de normativas sanitarias en exportación",
                "Declaración de ingresos por venta de ganado",
            ),
            "obligaciones_legales": (
                "Normas de bienestar animal y manejo responsable",
                "Regulación sobre condiciones de trabajo en el campo",
                "Cumplimiento de seguridad y salud ocupacional",
            ),
        },
        "importación": {
            "características": (
                "Dependencia de regulaciones internacionales",
                "Regulación sobre calidad y certificaciones",
                "Impacto de fluctuaciones económicas globales",
            ),
            "derechos": (
                "Acceso a tratados de libre comercio",
                "Beneficios fiscales en zonas aduaneras",
                "Facilidades para logística y distribución",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre importaciones",
                "Cumplimiento de normativas aduaneras",
                "Declaración de ingresos por comercio exterior",
            ),
            "obligaciones_legales": (
                "Regulación sobre contratación en logística",
                "Normas de seguridad en transporte",
                "Cumplimiento de leyes sobre comercio internacional",
            ),
        },
        "industrial": {
            "características": (
                "Alta inversión en maquinaria y tecnología",
                "Regulación ambiental estricta",
                "Dependencia de cadenas de suministro globales",
            ),
            "derechos": (
                "Acceso a financiamiento para manufactura",
                "Beneficios fiscales por inversión en infraestructura",
                "Prioridad en licitaciones públicas",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y exportación",
                "Cumplimiento de normativas ambientales fiscales",
                "Declaración de ingresos y gastos operativos",
            ),
            "obligaciones_legales": (
                "Normativas estrictas de seguridad laboral",
                "Regulación sobre jornadas y condiciones de trabajo",
                "Cumplimiento de normas de capacitación y certificación",
            ),
        },
        "logística_transporte": {
            "características": (
                "Alta dependencia de infraestructura y regulaciones aduaneras",
                "Impacto de costos de combustible y mantenimiento",
                "Regulación sobre emisiones y eficiencia energética",
            ),
            "derechos": (
                "Acceso a financiamiento para infraestructura de transporte",
                "Beneficios fiscales por modernización de flota",
                "Facilidades en tratados de comercio exterior",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre transporte de mercancías",
                "Cumplimiento de normativas fiscales en logística",
                "Declaración de ingresos por operación en transporte",
            ),
            "obligaciones_legales": (
                "Normas de seguridad en transporte y almacenamiento",
                "Regulación sobre contratación de personal de logística",
                "Cumplimiento de leyes sobre comercio internacional",
            ),
        },
        "manufactura": {
            "características": (
                "Alta inversión en maquinaria y tecnología",
                "Regulación ambiental estricta",
                "Dependencia de cadenas de suministro globales",
            ),
            "derechos": (
                "Acceso a financiamiento para producción",
                "Beneficios fiscales por inversión en infraestructura",
                "Prioridad en licitaciones públicas",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y exportación",
                "Cumplimiento de normativas ambientales fiscales",
                "Declaración de ingresos y gastos operativos",
            ),
            "obligaciones_legales": (
                "Normativas estrictas de seguridad laboral",
                "Regulación sobre jornadas y condiciones de trabajo",
                "Cumplimiento de normas de capacitación y certificación",
            ),
        },
        "minería": {
            "características": (
                "Dependencia de demanda internacional de recursos",
                "Regulación estricta en concesiones y explotación",
                "Impacto de políticas ambientales y laborales",
            ),
            "derechos": (
                "Acceso a concesiones para extracción de minerales",
                "Beneficios fiscales en producción minera",
                "Facilidades para exportación de metales y minerales",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre extracción y comercialización",
                "Cumplimiento de normativas fiscales en impacto ambiental",
                "Declaración de ingresos por venta de minerales",
            ),
            "obligaciones_legales": (
                "Normas de seguridad en operaciones mineras",
                "Regulación ambiental en procesos de extracción",
                "Cumplimiento de leyes sobre impacto social y derechos comunitarios",
            ),
        },
        "moda_textil": {
            "características": (
                "Alta competencia en tendencias de moda",
                "Impacto de regulaciones ambientales en textiles",
                "Dependencia de mercados internacionales de producción",
            ),
            "derechos": (
                "Acceso a financiamiento para producción y diseño",
                "Beneficios fiscales en manufactura textil",
                "Facilidades para exportación y comercialización",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre producción y comercialización",
                "Cumplimiento de normativas fiscales en importaciones",
                "Declaración de ingresos por venta de ropa y accesorios",
            ),
            "obligaciones_legales": (
                "Regulación sobre derechos de autor en diseño",
                "Normas de calidad y seguridad en materiales",
                "Cumplimiento de leyes sobre "
                "condiciones laborales en "
                "manufactura",
            ),
        },
        "pesca": {
            "características": (
                "Dependencia de temporadas de pesca",
                "Regulación sobre especies protegidas",
                "Acceso a financiamiento condicionado a prácticas sostenibles",
            ),
            "derechos": (
                "Acceso a permisos de explotación marítima",
                "Subsidios para producción pesquera",
                "Facilidades para exportación de productos marinos",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre captura y comercialización",
                "Cumplimiento de normativas ambientales",
                "Declaración de ingresos por venta de productos pesqueros",
            ),
            "obligaciones_legales": (
                "Regulación sobre condiciones de trabajo en embarcaciones",
                "Normas de seguridad marítima",
                "Cumplimiento de leyes sobre contratación temporal",
            ),
        },
        "retail_comercio_menor": {
            "características": (
                "Alta competencia con grandes cadenas comerciales",
                "Impacto de tendencias de consumo y digitalización",
                "Regulación sobre comercio electrónico y pago digital",
            ),
            "derechos": (
                "Acceso a financiamiento para expansión comercial",
                "Beneficios fiscales en operaciones minoristas",
                "Facilidades para importación y distribución",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre ventas y servicios",
                "Cumplimiento de normativas de facturación electrónica",
                "Declaración de ingresos y gastos operativos",
            ),
            "obligaciones_legales": (
                "Regulación sobre protección al consumidor",
                "Normas sobre calidad y seguridad de productos",
                "Cumplimiento de leyes de competencia y publicidad",
            ),
        },
        "salud": {
            "características": (
                "Alta inversión en tecnología médica",
                "Regulación sobre acceso a medicamentos",
                "Dependencia de avances científicos y tecnológicos",
            ),
            "derechos": (
                "Acceso a fondos de investigación médica",
                "Protección de propiedad intelectual en farmacéuticas",
                "Beneficios fiscales por servicios esenciales",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre productos médicos",
                "Cumplimiento de normativas de facturación en servicios de salud",
                "Declaración de ingresos por tratamientos y procedimientos",
            ),
            "obligaciones_legales": (
                "Normativas estrictas en calidad y seguridad",
                "Supervisión de ética médica",
                "Cumplimiento de normativas sanitarias internacionales",
            ),
        },
        "seguros_financieros": {
            "características": (
                "Dependencia de estabilidad económica global",
                "Regulación sobre tarifas y condiciones de seguros",
                "Impacto de crisis económicas en el sector financiero",
            ),
            "derechos": (
                "Acceso a licencias para operación en mercados financieros",
                "Beneficios fiscales en servicios de seguros",
                "Facilidades para inversión en portafolios de riesgo",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre transacciones financieras",
                "Cumplimiento de normativas fiscales en gestión de riesgos",
                "Declaración de ingresos por inversiones y seguros",
            ),
            "obligaciones_legales": (
                "Regulación sobre transparencia y protección al consumidor",
                "Normas sobre gestión de riesgo y solvencia financiera",
                "Cumplimiento de leyes de lavado de dinero",
            ),
        },
        "servicios": {
            "características": (
                "Alta dependencia de calidad y reputación",
                "Regulación sobre certificaciones y estándares",
                "Adaptación a cambios en demanda y tecnología",
            ),
            "derechos": (
                "Acceso a financiamiento para capacitación",
                "Beneficios fiscales en sectores estratégicos",
                "Facilidades para contratación de personal especializado",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre prestación de servicios",
                "Cumplimiento de normativas de facturación",
                "Declaración de ingresos por servicios profesionales",
            ),
            "obligaciones_legales": (
                "Regulación sobre condiciones de trabajo",
                "Normas de protección al consumidor",
                "Cumplimiento de leyes sobre publicidad y competencia",
            ),
        },
        "silvicultura": {
            "características": (
                "Dependencia de factores climáticos y políticas ambientales",
                "Regulación sobre especies protegidas y sustentabilidad",
                "Alta inversión en certificaciones ecológicas",
            ),
            "derechos": (
                "Acceso a concesiones para explotación forestal",
                "Beneficios fiscales por conservación y reforestación",
                "Facilidades para exportación de productos de madera",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre extracción y comercialización",
                "Cumplimiento de normativas fiscales ambientales",
                "Declaración de ingresos por venta de productos forestales",
            ),
            "obligaciones_legales": (
                "Normas estrictas de conservación ambiental",
                "Regulación sobre tala y reforestación",
                "Cumplimiento de leyes sobre impacto ecológico",
            ),
        },
        "tecnología": {
            "características": (
                "Alta competencia en el mercado",
                "Dependencia de inversión en investigación y desarrollo",
                "Riesgo de ciberseguridad y cumplimiento normativo",
            ),
            "derechos": (
                "Protección de propiedad intelectual",
                "Acceso a incentivos de innovación",
                "Posibilidad de operar globalmente con menos restricciones",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre servicios digitales",
                "Cumplimiento de normativas de facturación electrónica",
                "Declaraciones fiscales periódicas",
            ),
            "obligaciones_legales": (
                "Cumplimiento de normativas de teletrabajo",
                "Protección de datos personales de empleados",
                "Regulación sobre contratación de talento extranjero",
            ),
        },
        "telecomunicaciones": {
            "características": (
                "Alta inversión en tecnología y conectividad",
                "Regulación en monopolios y competencia",
                "Impacto de avances digitales en consumo",
            ),
            "derechos": (
                "Acceso a licencias para operación en redes de comunicación",
                "Beneficios fiscales en infraestructura digital",
                "Facilidades para inversión en conectividad",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre servicios digitales",
                "Cumplimiento de normativas fiscales en telecomunicaciones",
                "Declaración de ingresos por "
                "comercialización de "
                "servicios móviles",
            ),
            "obligaciones_legales": (
                "Regulación sobre privacidad y protección de datos",
                "Normas de calidad en redes y servicios",
                "Cumplimiento de leyes sobre competencia y acceso equitativo",
            ),
        },
        "turismo": {
            "características": (
                "Dependencia de temporadas altas y turismo internacional",
                "Impacto de regulaciones sanitarias y ambientales",
                "Competencia global en destinos turísticos",
            ),
            "derechos": (
                "Acceso a incentivos por promoción turística",
                "Beneficios fiscales por operación en zonas estratégicas",
                "Facilidades para inversión en hoteles y servicios turísticos",
            ),
            "obligaciones_fiscales": (
                "Pago de impuestos sobre hospedaje y entretenimiento",
                "Cumplimiento de normativas fiscales en servicios turísticos",
                "Declaración de ingresos por turismo internacional",
            ),
            "obligaciones_legales": (
                "Regulación sobre calidad y seguridad en establecimientos",
                "Normativas de protección al consumidor",
                "Cumplimiento de leyes sobre conservación del patrimonio",
            ),
        },
    },
    "antigüedad": {
        "nueva": {
            "obligaciones_fiscales": "Pueden acceder a incentivos fiscales para nuevos negocios",
            "obligaciones_legales": "Menor exposición a litigios previos",
            "financiamiento": "Puede ser difícil sin historial financiero",
            "reputación": "Deben construir confianza desde cero",
            "adaptabilidad": "Mayor flexibilidad para ajustes",
            "proveedores": "Difícil acceso a condiciones favorables",
            "innovación": "Mayor impulso en la innovación",
        },
        "intermedia": {
            "obligaciones_fiscales": "Cumplimiento de normas fiscales más estructuradas",
            "obligaciones_legales": "Posible acumulación de contratos y obligaciones",
            "financiamiento": "Acceso moderado a créditos con historial en crecimiento",
            "reputación": "Desarrollo de identidad de marca y reconocimiento",
            "adaptabilidad": "En fase de expansión y optimización",
            "proveedores": "Construcción de relaciones estratégicas",
            "innovación": "Balance entre innovación y estabilidad",
        },
        "establecida": {
            "obligaciones_fiscales": "Sujetos a auditorías y posible mayor carga tributaria",
            "obligaciones_legales": "Historial legal que puede incluir litigios o responsabilidades adquiridas",
            "financiamiento": "Mayor facilidad para obtener financiamiento por estabilidad",
            "reputación": "Posicionamiento fuerte en el mercado y confianza consolidada",
            "adaptabilidad": "Cambios requieren procesos más estructurados",
            "proveedores": "Beneficios por relaciones a largo plazo",
            "innovación": "Puede ser más tradicional, pero con inversión en nuevas ideas",
        },
    },
    "tamano": {
        "micro": {
            "financiamiento": "Autofinanciadas o pequeños créditos",
            "estructura": "Organización simple, dueño toma decisiones",
            "mercado": "Local, poca capacidad de expansión",
            "tecnologia": "Uso básico, digitalización limitada",
            "regulaciones": "Menor carga fiscal, trámites simplificados",
            "contrataciones": "Relación cercana con empleados, contratos flexibles",
        },
        "pequeña": {
            "financiamiento": "Créditos bancarios o inversionistas pequeños",
            "estructura": "Gerencias básicas, propietario aún toma decisiones clave",
            "mercado": "Expansión regional, competencia con otros pequeños negocios",
            "tecnologia": "Mayor integración digital, sistemas administrativos",
            "regulaciones": "Más cumplimiento tributario, normativas sectoriales",
            "contrataciones": "Mayor formalidad en contratación, prestaciones mínimas",
        },
        "mediana": {
            "financiamiento": "Acceso a financiamiento institucional y créditos mayores",
            "estructura": "Áreas especializadas, delegación de funciones",
            "mercado": "Nacional e internacional, competidores establecidos",
            "tecnologia": "Automatización, software empresarial, ERP",
            "regulaciones": "Cumplimiento estricto de normas fiscales y laborales",
            "contrataciones": "Contratos formales, prestaciones mayores, sindicatos en algunos casos",
        },
        "grande": {
            "financiamiento": "Acceso a mercados de capital y grandes inversionistas",
            "estructura": "Departamentos complejos, jerarquías definidas",
            "mercado": "Global, expansión internacional y diversificación",
            "tecnologia": "Innovación constante, inteligencia artificial, big data",
            "regulaciones": "Alto nivel de regulación, auditorías y transparencia",
            "contrataciones": "Normativas estrictas, beneficios completos, representación sindical",
        },
    },
    "usa_contratos": {
        True: {
            "seguridad_legal": "Cuenta con respaldo jurídico en caso de disputas.",
            "claridad_acuerdos": "Los términos están definidos en documentos formales.",
            "protección_incumplimientos": "Puede exigir cumplimiento o aplicar sanciones.",
            "profesionalismo": "Genera confianza y credibilidad en el mercado.",
            "financiamiento": "Facilita la obtención de inversión y préstamos.",
        },
        False: {
            "seguridad_legal": "Depende de acuerdos verbales, difíciles de probar.",
            "claridad_acuerdos": "Las expectativas pueden ser ambiguas.",
            "protección_incumplimientos": "Opciones limitadas para reclamar.",
            "profesionalismo": "Puede parecer menos estructurada o arriesgada.",
            "financiamiento": "Menos atractiva para inversionistas y bancos.",
        },
    },
    "tipo_contratos": {
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
    },
}


if __name__ == "__main__":
    from pprint import pprint

    pprint(knowledge_base["sector"].keys())

# Definir emociones
all_emotions = {
        "Agradables": ["Amor", "Alegría"],
        "Desagradables": ["Miedo", "Enojo", "Asco", "Envidia",
                          "Celos", "Vergüenza", "Culpa", "Tristeza",
                          "Desprecio", "Ansiedad"],
    }

# Info sobre emociones
diccionario_emociones = {
    "Amor": {
        "emoji": "❤️",
        "impulso_accion": "Dar cosas, dedicar tiempo, buscar proximidad.",
        "si_justificada": "Cuando contribuye positivamente al bienestar y crecimiento mutuo, basado en el respeto, reciprocidad y apoyo emocional.",
        "no_justificada": "Cuando existe abuso emocional o físico.",
        "acciones_si_justificada": "Fomentar la comunicación abierta, el respeto mutuo y el apoyo emocional.",
        "acciones_no_justificada": "Establecer límites saludables, considerar el autocuidado y, en situaciones extremas como abuso, buscar ayuda profesional o distanciamiento según sea necesario.",
    },

    "Alegría": {
        "emoji": "😄",
        "impulso_accion": "Sonreír, celebrar, compartir momentos felices, saltar.",
        "si_justificada": "Cuando surge de experiencias positivas y contribuye al bienestar emocional, en equilibrio con otras emociones.",
        "no_justificada": "Cuando se usa como un mecanismo de evitación o negación de emociones difíciles.",
        "acciones_si_justificada": "Practicar la atención plena en momentos felices, compartir positividad con otros, cultivar la gratitud de manera equilibrada.",
        "acciones_no_justificada": "Explorar y validar otras emociones presentes, usar la alegría como una herramienta para construir resiliencia emocional."
   },

    "Miedo": {
        "emoji": "😨",
        "impulso_accion": "Evitar cosas, escapar, gritar, pedir ayuda.",
        "si_justificada": "Cuando señala peligros reales y ayuda a la autoprotección.",
        "no_justificada": "Cuando es desproporcionado o basado en temores irracionales.",
        "acciones_si_justificada": "Validar el miedo, desarrollar habilidades para afrontar, buscar apoyo para enfrentar la amenaza real.",
        "acciones_no_justificada": "Explorar y cuestionar los pensamientos irracionales, desarrollar habilidades para la gestión del miedo."
    },

    "Enojo": {
        "emoji": "😡",
        "impulso_accion": "Golpear, lastimar, gritar, tirar cosas, explotar.",
        "si_justificada": "Cuando señala límites personales y motiva acciones positivas.",
        "no_justificada": "Cuando es destructiva, desproporcionada o dirigida injustamente.",
        "acciones_si_justificada": "Validar el enojo, comunicar de manera asertiva, buscar soluciones constructivas.",
        "acciones_no_justificada": "Explorar la causa subyacente, practicar la tolerancia a la frustración, aprender estrategias de regulación emocional."
    },

    "Asco": {
        "emoji": "🤢",
        "impulso_accion": "Alejarse, vomitar, dar arcadas, deseo de destruir algo, sensación de querer sacarse algo.",
        "si_justificada": "Cuando señala situaciones peligrosas o poco saludables.",
        "no_justificada": "Cuando se proyecta sin justificación en personas o situaciones.",
        "acciones_si_justificada": "Identificar situaciones riesgosas, establecer límites saludables, practicar la aceptación.",
        "acciones_no_justificada": "Explorar prejuicios o sesgos, practicar la compasión y empatía."
    },

    "Envidia": {
        "emoji": "😒",
        "impulso_accion": "Sentirse competitivo/a o motivado/a a mejorar.",
        "si_justificada": "Cuando sirve como motivación positiva para el crecimiento personal.",
        "no_justificada": "Cuando genera resentimiento y amargura.",
        "acciones_si_justificada": "Utilizar la envidia como motivación, establecer metas realistas, practicar la gratitud.",
        "acciones_no_justificada": "Explorar las propias metas y logros, desarrollar la autoaceptación y la autoestima."
    },
    "Celos": {
        "emoji": "😠",
        "impulso_accion": "Aferrarse, querer conservar lo que tienes, confrontación inmediata, la vigilancia excesiva, la invasión de la privacidad y la expresión emocional intensa.",
        "si_justificada": "Cuando hay una amenaza real para la relación.",
        "no_justificada": "Cuando se basa en inseguridades no fundamentadas.",
        "acciones_si_justificada": "Comunicar abiertamente, construir confianza, trabajar en la autoestima.",
        "acciones_no_justificada": "Explorar inseguridades subyacentes, practicar la aceptación de uno mismo y de los demás."
    },

    "Vergüenza": {
        "emoji": "😳",
        "impulso_accion": "Evitación, taparse la cara, el silencio repentino o achicar la postura.",
        "si_justificada": "Cuando se reconoce un error y se busca la mejora personal.",
        "no_justificada": "Cuando es paralizante y no contribuye al aprendizaje.",
        "acciones_si_justificada": "Aprender de la experiencia, disculparse cuando sea necesario, buscar apoyo para el crecimiento personal.",
        "acciones_no_justificada": "Explorar creencias irracionales, practicar la autocompasión y el perdón hacia uno mismo."
    },

    "Culpa": {
        "emoji": "😔",
        "impulso_accion": "Reparar, pedir disculpas reiterarivas, aislarse, castigarse.",
        "si_justificada": "Cuando se reconoce la responsabilidad de un error y se busca la reparación.",
        "no_justificada": "Cuando es desproporcionada o basada en expectativas poco realistas.",
        "acciones_si_justificada": "Hacer reparaciones, aprender y crecer, practicar el perdón hacia uno mismo y hacia los demás.",
        "acciones_no_justificada": "Explorar expectativas poco realistas, practicar la aceptación y la autorresponsabilidad."
    },

    "Tristeza": {
        "emoji": "😢",
        "impulso_accion": "Llorar, aislamiento, evasión, culparte, anhelar lo perdido.",
        "si_justificada": "Cuando surge como respuesta a pérdidas y desafíos.",
        "no_justificada": "Cuando es abrumadora y persistente sin causa evidente.",
        "acciones_si_justificada": "Permitir la expresión emocional, buscar apoyo, practicar la autocompasión.",
        "acciones_no_justificada": "Explorar las causas subyacentes, buscar apoyo profesional, desarrollar habilidades de afrontamiento."
    },

    "Desprecio": {
        "emoji": "😤",
        "impulso_accion": "Querer que lo que despreciamos se aleje de nosotros, expresiones faciales negativas, comentarios despectivos, evitación social o desvinculación emocional.",
        "si_justificada": "Cuando se fundamenta en comportamientos inaceptables y se dirige a la conducta en lugar de la persona.",
        "no_justificada": "Cuando se utiliza como un mecanismo de defensa sin base real.",
        "acciones_si_justificada": "Comunicar de manera asertiva, establecer límites saludables, practicar la empatía.",
        "acciones_no_justificada": "Explorar prejuicios o sesgos, practicar la aceptación y la tolerancia."
    },

    "Ansiedad": {
        "emoji": "😰",
        "impulso_accion": "Evitación, comportamientos compulsivos, reacciones emocionales intensas o decisiones apresuradas en un intento de aliviar la incomodidad momentánea.",
        "si_justificada": "Cuando señala peligros reales y motiva acciones preventivas.",
        "no_justificada": "Cuando es desproporcionada o basada en temores irracionales.",
        "acciones_si_justificada": "Desarrollar habilidades de afrontamiento, buscar apoyo, abordar la fuente de la ansiedad.",
        "acciones_no_justificada": "Explorar y cuestionar los pensamientos irracionales, practicar la relajación y la atención plena."
    },
}
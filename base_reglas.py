reglas = [
    {
        "id": "R1",
        "nombre": "Gripe",
        "condiciones_and": ["fiebre", "tos", "cansancio"],
        "condiciones_or": ["dolor_muscular", "escalofrios", "dolor_cabeza"],
        "conclusion": "Gripe",
        "descripcion": "El paciente probablemente tiene GRIPE",
        "prioridad": 2,
        "recomendacion": "Reposo, líquidos y paracetamol. Visita al médico si persiste más de 5 días."
    },
    {
        "id": "R2",
        "nombre": "Resfriado Común",
        "condiciones_and": ["estornudos", "dolor_garganta"],
        "condiciones_or": ["tos", "dolor_cabeza", "cansancio"],
        "conclusion": "Resfriado",
        "descripcion": "El paciente probablemente tiene RESFRIADO COMÚN",
        "prioridad": 1,
        "recomendacion": "Reposo, vitamina C y mucha agua. Suele pasar en 7-10 días."
    },
    {
        "id": "R3",
        "nombre": "COVID-19",
        "condiciones_and": ["fiebre", "tos", "dificultad_respirar"],
        "condiciones_or": ["perdida_olfato", "perdida_gusto", "cansancio"],
        "conclusion": "COVID-19",
        "descripcion": "El paciente probablemente tiene COVID-19",
        "prioridad": 3,
        "recomendacion": "Aislamiento inmediato y prueba PCR. Busca atención médica urgente si hay dificultad severa para respirar."
    },
    {
        "id": "R4",
        "nombre": "Alergia",
        "condiciones_and": ["estornudos", "ojos_llorosos", "picazon_nariz"],
        "condiciones_or": ["dolor_cabeza", "tos"],
        "conclusion": "Alergia",
        "descripcion": "El paciente probablemente tiene ALERGIA",
        "prioridad": 1,
        "recomendacion": "Antihistamínicos y evitar el alérgeno. Consulta al médico para identificar la causa."
    },
    {
        "id": "R5",
        "nombre": "Gastroenteritis",
        "condiciones_and": ["nauseas", "diarrea"],
        "condiciones_or": ["vomito", "dolor_cabeza", "cansancio"],
        "conclusion": "Gastroenteritis",
        "descripcion": "El paciente probablemente tiene GASTROENTERITIS",
        "prioridad": 2,
        "recomendacion": "Hidratación constante con suero oral. Dieta blanda. Médico si dura más de 2 días."
    },
    {
        "id": "R6",
        "nombre": "Angina",
        "condiciones_and": ["dolor_garganta", "fiebre"],
        "condiciones_or": ["dolor_cabeza", "cansancio"],
        "conclusion": "Angina",
        "descripcion": "El paciente probablemente tiene ANGINA",
        "prioridad": 2,
        "recomendacion": "Antibióticos recetados por médico. No automedicarse."
    },
    {
        "id": "R7",
        "nombre": "Bronquitis",
        "condiciones_and": ["tos", "dificultad_respirar", "cansancio"],
        "condiciones_or": ["fiebre", "dolor_pecho"],
        "conclusion": "Bronquitis",
        "descripcion": "El paciente probablemente tiene BRONQUITIS",
        "prioridad": 2,
        "recomendacion": "Reposo, inhaladores si es necesario. Consulta médica obligatoria."
    },
    {
        "id": "R8",
        "nombre": "Neumonía",
        "condiciones_and": ["fiebre", "dificultad_respirar", "dolor_pecho", "cansancio"],
        "condiciones_or": ["tos", "sudoracion"],
        "conclusion": "Neumonia",
        "descripcion": "El paciente probablemente tiene NEUMONÍA",
        "prioridad": 3,
        "recomendacion": "URGENTE: Atención médica inmediata. Puede requerir hospitalización."
    },
    {
        "id": "R9",
        "nombre": "Intoxicación Alimentaria",
        "condiciones_and": ["nauseas", "vomito", "diarrea"],
        "condiciones_or": ["fiebre", "dolor_cabeza"],
        "conclusion": "Intoxicacion Alimentaria",
        "descripcion": "El paciente probablemente tiene INTOXICACIÓN ALIMENTARIA",
        "prioridad": 2,
        "recomendacion": "Hidratación urgente. Si hay sangre en heces o fiebre alta, ir a urgencias."
    },
    {
        "id": "R10",
        "nombre": "Agotamiento",
        "condiciones_and": ["cansancio", "dolor_cabeza", "dolor_muscular"],
        "condiciones_or": ["sudoracion", "escalofrios"],
        "conclusion": "Agotamiento",
        "descripcion": "El paciente probablemente tiene AGOTAMIENTO FÍSICO",
        "prioridad": 1,
        "recomendacion": "Descanso, hidratación y alimentación balanceada."
    }
]
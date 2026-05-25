import json
import os
from datetime import datetime

ARCHIVO_HISTORIAL = "historial.json"

def guardar_consulta(sintomas_activos, conclusiones, explicaciones):
    historial = cargar_historial()

    consulta = {
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "sintomas": sintomas_activos,
        "diagnosticos": conclusiones,
        "detalles": [
            {
                "regla": e["regla"],
                "nombre": e["nombre"],
                "recomendacion": e["recomendacion"]
            } for e in explicaciones
        ]
    }

    historial.append(consulta)

    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)

def cargar_historial():
    if not os.path.exists(ARCHIVO_HISTORIAL):
        return []
    with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as f:
        return json.load(f)

def limpiar_historial():
    if os.path.exists(ARCHIVO_HISTORIAL):
        os.remove(ARCHIVO_HISTORIAL)
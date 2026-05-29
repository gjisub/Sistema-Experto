def ejecutar_motor(hechos, reglas):
    conclusiones = []
    explicaciones = []
    reglas_ordenadas = sorted(reglas, key=lambda r: r["prioridad"], reverse=True)

    for regla in reglas_ordenadas:
        cumple_and = all(hechos.get(c, False) for c in regla["condiciones_and"])

        cumple_or = any(hechos.get(c, False) for c in regla["condiciones_or"]) if regla["condiciones_or"] else True

        if cumple_and:
            hechos_and_usados = [c for c in regla["condiciones_and"] if hechos.get(c)]
            hechos_or_usados = [c for c in regla["condiciones_or"] if hechos.get(c)]

            conclusiones.append(regla["conclusion"])
            explicaciones.append({
                "regla": regla["id"],
                "nombre": regla["nombre"],
                "conclusion": regla["descripcion"],
                "prioridad": regla["prioridad"],
                "hechos_and": hechos_and_usados,
                "hechos_or": hechos_or_usados,
                "recomendacion": regla["recomendacion"]
            })

    return conclusiones, explicaciones
def calcular_certeza(explicacion, total_sintomas_activos):
    sintomas_usados = len(explicacion["hechos_and"]) + len(explicacion["hechos_or"])
    if total_sintomas_activos == 0:
        return 0
    return round((sintomas_usados / total_sintomas_activos) * 100, 1)
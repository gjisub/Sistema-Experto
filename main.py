import customtkinter as ctk
from base_hechos import hechos
from base_reglas import reglas
from motor import ejecutar_motor, calcular_certeza
from historial import guardar_consulta, cargar_historial, limpiar_historial
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

SINTOMAS_NOMBRES = {
    "fiebre": "Fiebre",
    "tos": "Tos",
    "dolor_cabeza": "Dolor de cabeza",
    "cansancio": "Cansancio / Fatiga",
    "estornudos": "Estornudos",
    "dolor_garganta": "Dolor de garganta",
    "nauseas": "Náuseas",
    "dificultad_respirar": "Dificultad para respirar",
    "dolor_muscular": "Dolor muscular",
    "escalofrios": "Escalofríos",
    "perdida_olfato": "Pérdida de olfato",
    "perdida_gusto": "Pérdida de gusto",
    "diarrea": "Diarrea",
    "vomito": "Vómito",
    "ojos_llorosos": "Ojos llorosos",
    "picazon_nariz": "Picazón en la nariz",
    "dolor_pecho": "Dolor en el pecho",
    "sudoracion": "Sudoración excesiva"
}

#inicio del sistema con la p-bienvenida 
class Bienvenida(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Experto")
        self.geometry("500x320")
        self.resizable(False, False)

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="¡Bienvenido!",
                     font=ctk.CTkFont(size=34, weight="bold")).pack(pady=(0, 10))

        ctk.CTkLabel(frame, text="Sistema Experto para Diagnóstico\nde Enfermedades Comunes",
                     font=ctk.CTkFont(size=15),
                     text_color="gray",
                     justify="center").pack(pady=(0, 35))

        ctk.CTkButton(frame, text="Ingresar →",
                      width=180, height=45,
                      font=ctk.CTkFont(size=14, weight="bold"),
                      command=self.abrir_app).pack()

    def abrir_app(self):
        self.destroy()
        app = App()
        app.mainloop()

#PRINCIPAL 
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Experto — Diagnóstico Médico")
        self.geometry("900x650")
        self.resizable(True, True)

        self.checks = {}

        self.tabview = ctk.CTkTabview(self, width=880)
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)

        self.tab_diagnostico = self.tabview.add("🩺 Diagnóstico")
        self.tab_historial = self.tabview.add("📋 Historial")
        self.tab_info = self.tabview.add("ℹ️ Acerca del sistema")

        self.build_diagnostico()
        self.build_historial()
        self.build_info()

    # ── TAB DIAGNÓSTICO ──────────────────────────────────────
    def build_diagnostico(self):
        tab = self.tab_diagnostico

        ctk.CTkLabel(tab, text="Sistema Experto de Diagnóstico Médico",
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(15, 2))
        ctk.CTkLabel(tab, text="Selecciona los síntomas que presentas:",
                     text_color="gray").pack(pady=(0, 10))

        frame_sintomas = ctk.CTkScrollableFrame(tab, height=250)
        frame_sintomas.pack(padx=15, fill="x")

        sintomas = list(SINTOMAS_NOMBRES.items())
        for i in range(0, len(sintomas), 3):
            fila = ctk.CTkFrame(frame_sintomas, fg_color="transparent")
            fila.pack(fill="x", pady=2)
            for j in range(3):
                if i + j < len(sintomas):
                    key, nombre = sintomas[i + j]
                    var = ctk.BooleanVar(value=False)
                    self.checks[key] = var
                    ctk.CTkCheckBox(fila, text=nombre, variable=var,
                                    width=230).pack(side="left", padx=8)

        frame_btns = ctk.CTkFrame(tab, fg_color="transparent")
        frame_btns.pack(pady=10)

        ctk.CTkButton(frame_btns, text="🔍 Diagnosticar",
                      command=self.diagnosticar, width=160).pack(side="left", padx=8)
        ctk.CTkButton(frame_btns, text="🔄 Limpiar",
                      command=self.limpiar_checks,
                      fg_color="gray", width=120).pack(side="left", padx=8)

        self.resultado_box = ctk.CTkTextbox(tab, height=220, font=ctk.CTkFont(size=13))
        self.resultado_box.pack(padx=15, pady=(5, 10), fill="both", expand=True)
        self.resultado_box.configure(state="disabled")

    def diagnosticar(self):
        for key, var in self.checks.items():
            hechos[key] = var.get()

        sintomas_activos = [k for k, v in hechos.items() if v]
        conclusiones, explicaciones = ejecutar_motor(hechos, reglas)

        self.resultado_box.configure(state="normal")
        self.resultado_box.delete("1.0", "end")

        if not conclusiones:
            self.resultado_box.insert("end", "⚠ No se encontró diagnóstico claro con los síntomas seleccionados.\n")
            self.resultado_box.insert("end", "Consulta a un médico para una evaluación profesional.\n")
        else:
            self.resultado_box.insert("end", f"✅ Diagnóstico completado — {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            self.resultado_box.insert("end", f"Síntomas seleccionados: {', '.join(sintomas_activos)}\n")
            self.resultado_box.insert("end", "─" * 55 + "\n\n")

            for exp in explicaciones:
                certeza = calcular_certeza(exp, len(sintomas_activos))
                prioridad_txt = ["", "🟡 Baja", "🟠 Media", "🔴 Alta"][exp["prioridad"]]

                self.resultado_box.insert("end", f"[{exp['regla']}] {exp['conclusion']}\n")
                self.resultado_box.insert("end", f"     Prioridad: {prioridad_txt}   |   Certeza: {certeza}%\n")
                self.resultado_box.insert("end", f"     Síntomas clave (AND): {', '.join(exp['hechos_and'])}\n")
                if exp["hechos_or"]:
                    self.resultado_box.insert("end", f"     Síntomas adicionales (OR): {', '.join(exp['hechos_or'])}\n")
                self.resultado_box.insert("end", f"     💊 Recomendación: {exp['recomendacion']}\n\n")

            guardar_consulta(sintomas_activos, conclusiones, explicaciones)
            self.resultado_box.insert("end", "─" * 55 + "\n")
            self.resultado_box.insert("end", "⚠ Este sistema no reemplaza la consulta médica profesional.\n")

        self.resultado_box.configure(state="disabled")

    def limpiar_checks(self):
        for var in self.checks.values():
            var.set(False)
        self.resultado_box.configure(state="normal")
        self.resultado_box.delete("1.0", "end")
        self.resultado_box.configure(state="disabled")

    # ── TAB HISTORIAL ─────────────────────────────────────────
    def build_historial(self):
        tab = self.tab_historial

        ctk.CTkLabel(tab, text="Historial de Consultas",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(15, 5))

        frame_btns = ctk.CTkFrame(tab, fg_color="transparent")
        frame_btns.pack(pady=5)

        ctk.CTkButton(frame_btns, text="🔄 Actualizar",
                      command=self.cargar_historial_ui, width=130).pack(side="left", padx=6)
        ctk.CTkButton(frame_btns, text="🗑 Limpiar historial",
                      command=self.limpiar_historial_ui,
                      fg_color="#c0392b", width=150).pack(side="left", padx=6)

        self.historial_box = ctk.CTkTextbox(tab, font=ctk.CTkFont(size=13))
        self.historial_box.pack(padx=15, pady=10, fill="both", expand=True)
        self.cargar_historial_ui()

    def cargar_historial_ui(self):
        historial = cargar_historial()
        self.historial_box.configure(state="normal")
        self.historial_box.delete("1.0", "end")

        if not historial:
            self.historial_box.insert("end", "No hay consultas registradas aún.\n")
        else:
            for i, consulta in enumerate(reversed(historial), 1):
                self.historial_box.insert("end", f"Consulta #{i} — {consulta['fecha']}\n")
                self.historial_box.insert("end", f"  Síntomas: {', '.join(consulta['sintomas'])}\n")
                self.historial_box.insert("end", f"  Diagnósticos: {', '.join(consulta['diagnosticos'])}\n")
                for d in consulta["detalles"]:
                    self.historial_box.insert("end", f"    [{d['regla']}] {d['nombre']}: {d['recomendacion']}\n")
                self.historial_box.insert("end", "─" * 50 + "\n")

        self.historial_box.configure(state="disabled")

    def limpiar_historial_ui(self):
        limpiar_historial()
        self.cargar_historial_ui()

    # ── TAB INFO ──────────────────────────────────────────────
    def build_info(self):
        tab = self.tab_info

        ctk.CTkLabel(tab, text="Acerca del Sistema Experto",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(20, 10))

        info = """
Este sistema experto fue desarrollado como proyecto de la materia
de Sistemas Expertos.

─────────────────────────────────────────────────────
🧠 COMPONENTES DEL SISTEMA:

  • Base de hechos:
    Almacena los síntomas ingresados por el usuario.
    Se representa como un diccionario Python con 18 síntomas.

  • Base de reglas:
    Contiene 10 reglas con lógica AND/OR y niveles de prioridad.
    Cubre: Gripe, Resfriado, COVID-19, Alergia, Gastroenteritis,
    Angina, Bronquitis, Neumonía, Intoxicación Alimentaria y Agotamiento.

  • Motor de inferencia:
    Aplica encadenamiento hacia adelante (forward chaining).
    Evalúa condiciones AND (obligatorias) y OR (complementarias).
    Ordena resultados por prioridad (1=baja, 2=media, 3=alta).
    Calcula porcentaje de certeza por diagnóstico.

  • Explicación de resultados:
    Muestra qué síntomas activaron cada regla.
    Indica nivel de prioridad y recomendación médica.
    Guarda historial en archivo JSON local.

─────────────────────────────────────────────────────
⚠ ADVERTENCIA:
Este sistema es educativo y no reemplaza la consulta médica.
        """

        box = ctk.CTkTextbox(tab, font=ctk.CTkFont(size=13))
        box.pack(padx=15, pady=10, fill="both", expand=True)
        box.insert("end", info)
        box.configure(state="disabled")


if __name__ == "__main__":
    bienvenida = Bienvenida()
    bienvenida.mainloop()
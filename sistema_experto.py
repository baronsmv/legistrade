from experta.fact import Fact
from experta.engine import KnowledgeEngine
from experta.rule import Rule


class Sintoma(Fact):
    pass


class DiagnosticoSalud(KnowledgeEngine):
    @Rule(Sintoma(fiebre=True, tos=True, dolor_cabeza=True))
    def diagnosticar_covid(self):
        print("Posible diagnóstico: COVID-19")

    @Rule(Sintoma(fiebre=True, tos=True, dolor_cabeza=False))
    def diagnosticar_gripe(self):
        print("Posible diagnóstico: Gripe")

    @Rule(Sintoma(fiebre=False, tos=True, dolor_cabeza=False))
    def diagnosticar_resfriado(self):
        print("Posible diagnóstico: Resfriado común")

    @Rule(Sintoma(fiebre=False, tos=False, dolor_cabeza=False))
    def sin_sintomas(self):
        print("No presenta síntomas. ¡Todo bien!")


if __name__ == "__main__":
    # Inicialización del motor de inferencia (instancia de DiagnosticoSalud)
    motor = DiagnosticoSalud()

    # Solicitud de variables
    fiebre, tos, dolor_cabeza = (
        input(f"¿Tiene {sintoma}? (s/n): ").lower() == "s"
        for sintoma in ("fiebre", "tos", "dolor de cabeza")
    )

    # Acción del motor de inferencia
    motor.reset()
    motor.declare(Sintoma(fiebre=fiebre, tos=tos, dolor_cabeza=dolor_cabeza))
    motor.run()

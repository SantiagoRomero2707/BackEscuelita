from datetime import time
import strawberry


@strawberry.type
class Horario:
    id: int
    dias: str
    inicio_jornada: time
    final_jornada: time
    habitacion: str
    edificio: str


@strawberry.input
class HorarioInput:
    dias: str
    inicio_jornada: time
    final_jornada: time
    habitacion: str
    edificio: str

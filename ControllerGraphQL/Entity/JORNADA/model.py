from datetime import time
import strawberry


@strawberry.type
class Jornada:
    id: int
    dia: int
    incio: time
    final: time
    IPS_ID_FK: int


@strawberry.input
class JornadaInput:
    dia: int
    incio: time
    final: time
    IPS_ID_FK: int


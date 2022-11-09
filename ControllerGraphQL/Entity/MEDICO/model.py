import strawberry


@strawberry.type
class Medico:
    id: int
    nombre_medico: str
    apellidos_medico: str
    licencia: str
    especialidad: str
    cargo: str
    persona_id: int
    IPS_FK: int


@strawberry.input
class MedicoInput:
    nombre_medico: str
    apellidos_medico: str
    licencia: str
    especialidad: str
    cargo: str
    persona_id: int
    IPS_FK: int


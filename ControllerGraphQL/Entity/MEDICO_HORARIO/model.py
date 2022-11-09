import strawberry


@strawberry.type
class MedicoHorario:
    Medico_ID: int
    Medico_Horario_PK: str
    Horario_id_fk: int


@strawberry.input
class MedicoHorarioInput:
    Medico_Horario_PK: str
    Horario_id_fk: int

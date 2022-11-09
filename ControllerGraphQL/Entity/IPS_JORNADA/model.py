import strawberry


@strawberry.type
class IPSJornada:
    IPS_ID: int
    Jornada_ID_FK: int
    IPS_Jornada_ID: str


@strawberry.input
class IPSJornadaInput:
    Jornada_ID_FK: int
    IPS_Jornada_ID: str


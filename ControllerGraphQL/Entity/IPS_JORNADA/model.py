import strawberry


@strawberry.type
class IPSJornada:
    IPS_Jornada_ID: str
    IPS_ID: int
    Jornada_ID_FK: str


@strawberry.input
class IPSJornadaInput:
    IPS_Jornada_ID: str
    IPS_ID: int


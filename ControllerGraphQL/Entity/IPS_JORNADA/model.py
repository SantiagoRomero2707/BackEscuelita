import strawberry


@strawberry.type
class IPSJornada:
    IPS_Jornada_ID: int
    IPS_ID_FK: int
    Jornada_ID_FK: int
    ips_jornadacol: str


@strawberry.input
class IPSJornadaInput:
    IPS_ID_FK: int
    Jornada_ID_FK: int
    ips_jornadacol: str



import strawberry


@strawberry.type
class IPSServicio:
    IPS_Servicio_PK: str
    IPS_ID: int
    Servicio_ID_FK: int


@strawberry.input
class IPSServicioInput:
    IPS_Servicio_PK: str
    IPS_ID: int
    Servicio_ID_FK: int


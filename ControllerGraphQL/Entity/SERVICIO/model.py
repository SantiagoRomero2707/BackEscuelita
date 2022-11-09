import strawberry


@strawberry.type
class Servicio:
    id: int
    nombre_servicio: str
    tarifa: float

@strawberry.input
class ServicioInput:
    nombre_servicio: str
    tarifa: float


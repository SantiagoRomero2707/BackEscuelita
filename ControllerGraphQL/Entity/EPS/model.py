import strawberry


@strawberry.type
class EPS:
    id: str
    nombre: str
    telefono: str
    NIT: str
    tipo: str


@strawberry.input
class EPSInput:
    nombre: str
    telefono: str
    NIT: str
    tipo: str

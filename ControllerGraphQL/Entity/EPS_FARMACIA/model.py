import strawberry


@strawberry.type
class EPSFarmacia:
    id_EPS_Farmacia: int
    EPS_ID_FK: int
    Farmacia_ID_FK: int

@strawberry.input
class EPSFarmaciaInput:
    EPS_ID_FK: int
    Farmacia_ID_FK: int


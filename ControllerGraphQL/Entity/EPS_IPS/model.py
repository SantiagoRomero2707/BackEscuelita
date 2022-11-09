import strawberry


@strawberry.type
class EPSIPS:
    EPS_IPS_PK: str
    EPS_ID: int
    IPS_ID_FK: int


@strawberry.input
class EPSIPSInput:
    EPS_IPS_PK: str
    EPS_ID: int
    IPS_ID_FK: int

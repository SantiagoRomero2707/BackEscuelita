class selectField:    
    # Primary keys
    def pkvalue(value):
        if value == 20:
            PK = ['NIT_Cliente']
            return PK
        elif value == 26:
            PK = ['CC_TRABAJ']
            return PK
        elif value == 31:
            PK = ['DOCUMENT']
            return PK
        elif value == 33:
            PK = ['DOCUMENT']
            return PK
        elif value == 34:
            PK = ['GEN_DESCP']
            return PK
        else:
            PK = ''
            return PK

    # Foreing Keys
    def fkvalue(value):
        if value == 19:
            FK = ['ID_DEPA','ID_PAIS','ID_CIUDAD','ID_CLIENTE','ID_FUENENERGIA','ID_Amb_Oper',
                'ID_INCIDENT','ID_DIRECT','ID_COORD']
            return FK
        elif value == 23:
            FK = ['ID_Proyecto','CC_Trabajador','ID_INCVIAL','ID_PARTC','ID_CAURAIZ','ID_FacT','ID_FacP',
                'ID_COND_INSE','ID_ActInse','ID_Enfermedad','ID_NATULES','ID_TIPOLOGIA' ]
            return FK
        elif value == 24:
            FK = ['ID_INCIDENTE','ID_AUTO','ID_Clima','ID_TipoVia','ID_CondicionVia','ID_LUZVIA','ID_CLASEVIA','ID_ASEGURADORA']
            return FK
        elif value == 31:
            FK = ['ID_GEN','ID_CENTROCOS','ID_CARGO']
            return FK
        elif value == 32:
            FK = ['ID_TIPOAUTO','ID_ESTADO']
            return FK
        elif value == 33:
            FK = ['ID_ROL']
            return FK
        elif value == 34:
            FK = ['COD_EVEN']
            return FK
        elif value == 35:
            FK = ['ID_DEPA','ID_PAIS']
            return FK
        elif value == 36:
            FK = ['ID_MODULO','Evento','DescripEvento','Documento']
            return FK
        else: 
            FK = ''
            return FK


    @staticmethod
    def joinfields(nom_table):
        A = selectField.pkvalue(nom_table)
        B = selectField.fkvalue(nom_table)
        if A == '':
            list = B
            return list
        elif B == '':
            list = A
            return list
        else:
            list = A + B
            return list
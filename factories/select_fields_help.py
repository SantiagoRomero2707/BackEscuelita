class selectModelConsulting:    
    # Entidades fuerte
    def EntityStrong(value):
        # GENERAL AMBIENTE OPERACIONAL			
        # GENERAL ASEGURADORA			
        # GENERAL CAUSA BÁSICA ACTO INSEGURO			
        # GENERAL CAUSA BASICA CONDICIÓN INSEGURA			
        # GENERAL CAUSA FACTORES DEL TRABAJO			
        # GENERAL CAUSA FACTORES PERSONALES			
        # GENERAL CAUSA RAÍZ			
        # GENERAL CENTRO DE COSTOS			
        # GENERAL CLASE DE LA VIA			
        # GENERAL CLIMA			
        # GENERAL CONDICIÓN LUZ			
        # GENERAL CONDICION VIA			
        # GENERAL ENFERMEDADES			
        # GENERAL FUENTE DE ENERGÍA			
        # GENERAL GENERO			
        # GENERAL NATURALEZA DE LA LESIÓN			
        # GENERAL PAÍS			
        # GENERAL PARTE DEL CUERPO LESIONADA 			
        # GENERAL PROYECTO CLIENTE			
        # GENERAL TIPO VIA			
        # GENERAL TIPOLOGIA			
        # REGISTRO ROL DE USUARIO			
        # SISTEMA EVENTO DEL SISTEMA			
        # SISTEMA MODULO DEL SISTEMA			
        # VIAL ESTADO DEL AUTOMÓVIL			
        # VIAL TIPO DE AUTOMÓVIL			

        if value == 'ID_AMB_OPE':
            PK = ['NIT_Cliente']
            return print('PAIS')
        elif value == 'ID_DEPA':
            PK = ['CC_TRABAJ']
            return 'DEPARTAMENTO'
        else:
            PK = ''
            return print("PK")

    # Entidades débiles 
    def EntityWeak(value):
        # GENERAL CARGO DEL TRABAJADOR			
        # GENERAL CIUDAD			
        # GENERAL DEPARTAMENTO 			
        # GENERAL PROYECTO			
        # GENERAL TRABAJADOR			
        # PROYECTO INCIDENTE			
        # PROYECTO INCIDENTE VIAL			
        # PROYECTO INCIDENTE VIAL AUTOMÓVIL			
        # REGISTRO DE USUARIOS			
        # SISTEMA AUDITORIA			
        # SISTEMA DESCRIPCIÓN EVENTO			

        if value == 'ID_AMB_OPE':
            PK = ['NIT_Cliente']
            return print('PAIS')
        elif value == 'ID_DEPA':
            PK = ['CC_TRABAJ']
            return 'DEPARTAMENTO'
        elif value == 'ID_COORD':
            PK = ['GEN_DESCP']
            return 'Coordinador'
        else:
            PK = ''
            return print("PK")


selectModelConsulting.Consulta('ID_PAIS')
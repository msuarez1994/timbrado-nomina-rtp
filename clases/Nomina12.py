from clases.Funciones import *

class Nomina12():
    def __init__(self):
        self.IDNOMINA = ""				             #VARCHAR2 (30 BYTE)
        self.IDCOMPROBANTE = "" 			         #VARCHAR2 (30 BYTE)
        self.RFCRECEPTOR = ""		                 #VARCHAR2 (39 BYTE)
        self.NOMBRERECEPTOR = ""   		             #VARCHAR2 (900 BYTE)
        self.TIPONOMINA = "" 			             #VARCHAR2 (3 BYTE)
        self.FECHAPAGO = "" 			             #VARCHAR2 (30 BYTE)
        self.FECHAINICIALPAGO = ""   		         #VARCHAR2 (30 BYTE)
        self.FECHAFINALPAGO = ""		             #VARCHAR2 (30 BYTE)
        self.NUMDIASPAGADOS = ""		             #NUMBER (10)
        self.TOTALPERCEPCIONES = ""		             #NUMBER (14,2)
        self.TOTALDEDUCCIONES = "" 		             #NUMBER (14,2)
        self.TOTALOTROSPAGOS = ""        		     #NUMBER (14,2)
        self.CURP = "" 					             #VARCHAR2 (54 BYTE)
        self.NUMSEGURIDADSOCIAL = "" 	             #VARCHAR2 (45 BYTE)
        self.ANTIGUEDAD = ""     			         #VARCHAR2 (45 BYTE)
        self.TIPOCONTRATO = ""       			     #VARCHAR2 (6 BYTE)
        self.SINDICALIZADO = ""           		     #VARCHAR2 (6 BYTE)
        self.TIPOJORNADA = ""         			     #VARCHAR2 (6 BYTE)
        self.TIPOREGIMEN = ""   			         #VARCHAR2 (6 BYTE)
        self.NUMEMPLEADO = ""   			         #VARCHAR2 (30 BYTE)
        self.DEPARTAMENTO = ""      			     #VARCHAR2 (750 BYTE)
        self.PUESTO  = ""  				             #VARCHAR2 (300 BYTE)
        self.RIESGOPUESTO = ""       			     #VARCHAR2 (6 BYTE)
        self.PERIODICIDADPAGO = ""           		 #VARCHAR2 (300 BYTE)
        self.BANCO = "" 				             #VARCHAR2 (9 BYTE)
        self.CUENTABANCARIA = ""         		     #VARCHAR2 (54 BYTE)
        self.SALARIOBASECOTAPOR = ""             	 #NUMBER (14,2)
        self.SALARIODIARIOINTEGRADO = ""             #NUMBER (14,2)
        self.CLAVEENTFED = "" 	                     #VARCHAR2 (9 BYTE)
        self.IDUSUARIO = "FACTURAX"                  #VARCHAR2 (60 BYTE)
        self.FEC_ULT_ACTUALIZACION = ""	             #DATE
        self.COMENT = "" 				             #VARCHAR2 (300 BYTE)
        self.SERIE = ""	                             #VARCHAR2 (75 BYTE)
        self.SECT_PRES = "" 	                     #NUMBER
        self.N_SECT_PRES = "" 	                     #VARCHAR2 (900 BYTE)
        self.UNIDAD_ADM = ""	                     #NUMBER
        self.N_UNIDAD_ADM = ""                       #VARCHAR2 (900 BYTE)
        self.ZONA_PAGADORA = "" 			         #NUMBER
        self.NUM_PLAZA = "" 				         #NUMBER
        self.UNIVERSO = ""                           #VARCHAR2 (6 BYTE)
        self.NIVEL_SALARIAL = ""                     #NUMBER (4)
        self.COD_PUESTO_CVE_ACT = ""                 #VARCHAR2 (30 BYTE)
        self.GRADO = ""	                             #NUMBER
        self.N_PUESTO_ACT_ASOC_PROG = ""             #VARCHAR2 (900 BYTE)
        self.SINDICATO = ""  	                     #NUMBER
        self.COMISION_SIND = "" 	  	             #VARCHAR2 (60 BYTE)
        self.TIPO_CONTRATACION_SUBPROG = "" 		 #VARCHAR2 (90 BYTE)
        self.PERIODO_PAGO = "" 					     #VARCHAR2 (300 BYTE)
        self.LEY_CUMPLEANIOS = "" 				     #VARCHAR2 (180 BYTE)
        self.AVISOS = "" 						     #VARCHAR2 (750 BYTE)
        self.NUM_CUENTA = "" 					     #VARCHAR2 (60 BYTE)
        self.INICIO_DE_LAB = "" 			         #VARCHAR2 (600 BYTE)
        self.TURNO_LAB = "" 					     #VARCHAR2 (600 BYTE)
        self.CODIGO_CONASA = "" 				     #VARCHAR2 (600 BYTE)
        self.N_CODIGO_CONASA = "" 				     #VARCHAR2 (600 BYTE)
        self.FG = "" 						         #DATE
        self.ST = "" 							     #NUMBER
        self.PERIODO_CONTRATACION = "" 			     #VARCHAR2 (90 BYTE)
        self.TIPO_NOMINA = "" 					     #NUMBER (1)
        self.FECHAINICIOREALLABORAL = ""       		 #VARCHAR2 (60 BYTE)
        self.DEDUCCIONESAD = "" 				     #NUMBER (14,2)
        self.CEDULAPROF = "" 					     #VARCHAR2 (90 BYTE)
        self.FOLIO_CFDI = ""					     #VARCHAR2 (150 BYTE)
        self.VERSION = "" 						     #VARCHAR2 (15 BYTE)
        self.FECHATIMBRADO = "" 				     #DATE
        self.SELLOCFD = "" 						     #VARCHAR2 (4000 BYTE)
        self.NOCERTIFICADOSAT = "" 				     #VARCHAR2 (150 BYTE)
        self.SELLOSAT = "" 						     #VARCHAR2 (4000 BYTE)
        
    def setIDNOMINA(self,IDNOMINA):
        self.IDNOMINA = validarDato(IDNOMINA)
    def setIDCOMPROBANTE(self,IDCOMPROBANTE):
        self.IDCOMPROBANTE = validarDato(IDCOMPROBANTE)
    def setRFCRECEPTOR(self,RFCRECEPTOR):
        self.RFCRECEPTOR =  validarDato(RFCRECEPTOR)
    def setNOMBRERECEPTOR(self,NOMBRERECEPTOR):
        self.NOMBRERECEPTOR = validarDato(NOMBRERECEPTOR)
    def setTIPONOMINA(self,TIPONOMINA):
        self.TIPONOMINA = validarDato(TIPONOMINA)
    def setFECHAPAGO(self,FECHAPAGO):
        self.FECHAPAGO = formatFecha(validarDato(FECHAPAGO))
    def setFECHAINICIALPAGO(self,FECHAINICIALPAGO):
        self.FECHAINICIALPAGO = formatFecha(validarDato(FECHAINICIALPAGO))
    def setFECHAFINALPAGO(self,FECHAFINALPAGO):
        self.FECHAFINALPAGO = formatFecha(validarDato(FECHAFINALPAGO))
    def setNUMDIASPAGADOS(self,NUMDIASPAGADOS):
        self.NUMDIASPAGADOS = validarDato(NUMDIASPAGADOS)
    def setTOTALPERCEPCIONES(self,TOTALPERCEPCIONES):
        self.TOTALPERCEPCIONES = validarCifra(validarDato(TOTALPERCEPCIONES))
    def setTOTALDEDUCCIONES(self,TOTALDEDUCCIONES):
        self.TOTALDEDUCCIONES = validarCifra(validarDato(TOTALDEDUCCIONES))
    def setTOTALOTROSPAGOS(self,TOTALOTROSPAGOS):
        self.TOTALOTROSPAGOS = validarCifra(validarDato(TOTALOTROSPAGOS))
    def setCURP(self,CURP):
        self.CURP = validarDato(CURP)
    def setNUMSEGURIDADSOCIAL(self,NUMSEGURIDADSOCIAL):
        self.NUMSEGURIDADSOCIAL = validarDato(NUMSEGURIDADSOCIAL)
    def setANTIGUEDAD(self,ANTIGUEDAD):
        self.ANTIGUEDAD = validarDato(ANTIGUEDAD)
    def setTIPOCONTRATO(self,TIPOCONTRATO):
        self.TIPOCONTRATO = validarDato(TIPOCONTRATO)
    def setSINDICALIZADO(self,SINDICALIZADO):
        self.SINDICALIZADO = validarDato(SINDICALIZADO)
    def setTIPOJORNADA(self,TIPOJORNADA):
        self.TIPOJORNADA = validarDato(TIPOJORNADA)
    def setTIPOREGIMEN(self,TIPOREGIMEN):
        self.TIPOREGIMEN = validarDato(TIPOREGIMEN)
    def setNUMEMPLEADO(self,NUMEMPLEADO):
        self.NUMEMPLEADO = validarDato(NUMEMPLEADO)
    def setDEPARTAMENTO(self,DEPARTAMENTO):
        self.DEPARTAMENTO = validarDato(DEPARTAMENTO)
    def setPUESTO(self,PUESTO):
        self.PUESTO = validarDato(PUESTO)
    def setRIESGOPUESTO(self,RIESGOPUESTO):
        self.RIESGOPUESTO = validarDato(RIESGOPUESTO)
    def setPERIODICIDADPAGO(self,PERIODICIDADPAGO):
        self.PERIODICIDADPAGO = validarDato(PERIODICIDADPAGO)
    def setBANCO(self,BANCO):
        self.BANCO = validarDato(BANCO)
    def setCUENTABANCARIA(self,CUENTABANCARIA):
        self.CUENTABANCARIA = validarDato(CUENTABANCARIA)
    def setSALARIOBASECOTAPOR(self,SALARIOBASECOTAPOR):
        self.SALARIOBASECOTAPOR = validarCifra(validarDato(SALARIOBASECOTAPOR))
    def setSALARIODIARIOINTEGRADO(self,SALARIODIARIOINTEGRADO):
        self.SALARIODIARIOINTEGRADO = validarCifra(validarDato(SALARIODIARIOINTEGRADO))
    def setCLAVEENTFED(self,CLAVEENTFED):
        self.CLAVEENTFED = validarDato(CLAVEENTFED)
    def setN_UNIDAD_ADM(self,N_UNIDAD_ADM):
        self.N_UNIDAD_ADM = validarDato(N_UNIDAD_ADM)
    def setCOD_PUESTO_CVE_ACT(self,COD_PUESTO_CVE_ACT):
        self.COD_PUESTO_CVE_ACT = validarDato(COD_PUESTO_CVE_ACT)
    def setN_PUESTO_ACT_ASOC_PROG(self,N_PUESTO_ACT_ASOC_PROG):
        self.N_PUESTO_ACT_ASOC_PROG = validarDato(N_PUESTO_ACT_ASOC_PROG)
    def setTIPO_CONTRATACION_SUBPROG(self,TIPO_CONTRATACION_SUBPROG):
        self.TIPO_CONTRATACION_SUBPROG = validarDato(TIPO_CONTRATACION_SUBPROG)
    def setPERIODO_PAGO(self,PERIODO_PAGO):
        self.PERIODO_PAGO = validarDato(PERIODO_PAGO)
    def setFECHAINICIOREALLABORAL(self,FECHAINICIOREALLABORAL):
        self.FECHAINICIOREALLABORAL = formatFecha(validarDato(FECHAINICIOREALLABORAL))
    def setDEDUCCIONESAD(self,DEDUCCIONESAD):
        self.DEDUCCIONESAD = validarDato(DEDUCCIONESAD)
    def setSERIE(self,SERIE):
        self.SERIE = validarDato(SERIE)
 
        
    def getinfo(self,opc):
        if opc:
            resp  = str(self.IDNOMINA) + "," + str(self.IDCOMPROBANTE) + "," + str(self.RFCRECEPTOR) + "," + str(self.NOMBRERECEPTOR) + "," + str(self.TIPONOMINA) + "," + str(self.FECHAPAGO) + "," + str(self.FECHAINICIALPAGO) + "," + str(self.FECHAFINALPAGO) + "," + str(self.NUMDIASPAGADOS) + "," + str(self.TOTALPERCEPCIONES) + "," + str(self.TOTALDEDUCCIONES) + "," + str(self.TOTALOTROSPAGOS) + "," + str(self.CURP) + "," + str(self.NUMSEGURIDADSOCIAL) + "," + str(self.ANTIGUEDAD) + "," + str(self.TIPOCONTRATO) + "," + str(self.SINDICALIZADO) + "," + str(self.TIPOJORNADA) + "," + str(self.TIPOREGIMEN) + "," + str(self.NUMEMPLEADO) + "," + str(self.DEPARTAMENTO) + "," + str(self.PUESTO) + "," + str(self.RIESGOPUESTO) + "," + str(self.PERIODICIDADPAGO) + "," + str(self.BANCO) + "," + str(self.CUENTABANCARIA) + "," + str(self.SALARIOBASECOTAPOR) + "," + str(self.SALARIODIARIOINTEGRADO) + "," + str(self.CLAVEENTFED) + "," + str(self.IDUSUARIO) + "," + str(self.FEC_ULT_ACTUALIZACION) + "," + str(self.COMENT) + "," + str(self.SERIE) + "," + str(self.SECT_PRES) + "," + str(self.N_SECT_PRES) + "," + str(self.UNIDAD_ADM) + "," + str(self.N_UNIDAD_ADM) + "," + str(self.ZONA_PAGADORA) + "," + str(self.NUM_PLAZA) + "," + str(self.UNIVERSO) + "," + str(self.NIVEL_SALARIAL) + "," + str(self.COD_PUESTO_CVE_ACT) + "," + str(self.GRADO) + "," + str(self.N_PUESTO_ACT_ASOC_PROG) + "," + str(self.SINDICATO) + "," + str(self.COMISION_SIND) + "," + str(self.TIPO_CONTRATACION_SUBPROG) + "," + str(self.PERIODO_PAGO) + "," + str(self.LEY_CUMPLEANIOS) + "," + str(self.AVISOS) + "," + str(self.NUM_CUENTA) + "," + str(self.INICIO_DE_LAB) + "," +  str(self.TURNO_LAB) + "," + str(self.CODIGO_CONASA) + "," + str(self.N_CODIGO_CONASA) + "," + str(self.FG) + "," + str(self.ST) + "," + str(self.PERIODO_CONTRATACION) + "," + str(self.TIPO_NOMINA) + "," + str(self.FECHAINICIOREALLABORAL) + "," + str(self.DEDUCCIONESAD) + "," + str(self.CEDULAPROF) + "," + str(self.FOLIO_CFDI) + "," + str(self.VERSION) + "," + str(self.FECHATIMBRADO) + "," + str(self.SELLOCFD) + "," + str(self.NOCERTIFICADOSAT) + "," + str(self.SELLOSAT) + "\n"
            return resp;
        else: 
            return str(self.__dict__)
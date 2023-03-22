from clases.Funciones import *

class Percepcion():
    def __init__(self):
        self.IDPERCEPCION = ""            #NUMBER
        self.IDPERCEPCIONES = ""          #NUMBER
        self.IDNOMINA = ""                #VARCHAR2 (30 BYTE)
        self.TIPOPERCEPCION = ""          #VARCHAR2 (9 BYTE)
        self.CLAVE = ""                   #VARCHAR2 (45 BYTE)
        self.CONCEPTO = ""                #VARCHAR2 (300 BYTE)
        self.IMPORTEGRAVADO = ""          #NUMBER (14,2)
        self.IMPORTEEXENTO = ""           #NUMBER (14,2)
        self.IMPORTETOTAL = ""            #NUMBER (14,2)
        self.FEC_IMPUTACION = ""          #DATE
        self.FEC_PAGO = ""                #DATE
        self.FEC_INICIO_P = ""            #DATE
        self.FEC_FIN_P = ""               #DATE
        self.IDUSUARIO = "FACTURAX"               #VARCHAR2 (60 BYTE)
        self.FG = ""                      #DATE
        self.ST = ""                      #NUMBER
        self.SERIE = ""                   #VARCHAR2 (75 BYTE)
        
    def setIDPERCEPCION(self,IDPERCEPCION):
            self.IDPERCEPCION = validarDato(IDPERCEPCION)
    def setIDPERCEPCIONES(self,IDPERCEPCIONES):
            self.IDPERCEPCIONES = validarDato(IDPERCEPCIONES)
    def setIDNOMINA(self,IDNOMINA):
            self.IDNOMINA = validarDato(IDNOMINA)
    def setTIPOPERCEPCION(self,TIPOPERCEPCION):
            self.TIPOPERCEPCION = validarDato(TIPOPERCEPCION)
    def setCLAVE(self,CLAVE):
            self.CLAVE = validarDato(CLAVE)
    def setCONCEPTO(self,CONCEPTO):
            self.CONCEPTO = validarDato(CONCEPTO)
    def setIMPORTEGRAVADO(self,IMPORTEGRAVADO):
            self.IMPORTEGRAVADO = validarCifra(validarDato(IMPORTEGRAVADO))
    def setIMPORTEEXENTO(self,IMPORTEEXENTO):
            self.IMPORTEEXENTO = validarCifra(validarDato(IMPORTEEXENTO))
    def setIMPORTETOTAL(self,IMPORTETOTAL):
            self.IMPORTETOTAL = validarCifra(validarDato(IMPORTETOTAL))
    def setFEC_IMPUTACION(self,FEC_IMPUTACION):
            self.FEC_IMPUTACION = formatFecha(validarDato(FEC_IMPUTACION))
    def setFEC_PAGO(self,FEC_PAGO):
            self.FEC_PAGO = formatFecha(validarDato(FEC_PAGO))
    def setFEC_INICIO_P(self,FEC_INICIO_P):
            self.FEC_INICIO_P = formatFecha(validarDato(FEC_INICIO_P))
    def setFEC_FIN_P(self,FEC_FIN_P):
            self.FEC_FIN_P = formatFecha(validarDato(FEC_FIN_P))
    			
    def getinfo(self,opc):
        if opc:
            resp  = self.IDPERCEPCION+ "," + self.IDPERCEPCIONES+ "," + self.IDNOMINA+ "," + self.TIPOPERCEPCION+ "," + self.CLAVE+ "," + self.CONCEPTO+ "," + self.IMPORTEGRAVADO+ "," + self.IMPORTEEXENTO+ "," + self.IMPORTETOTAL+ "," + self.FEC_IMPUTACION+ "," + self.FEC_PAGO+ "," + self.FEC_INICIO_P+ "," + self.FEC_FIN_P+ "," + self.IDUSUARIO+ "," + self.FG+ "," + self.ST+ "," + self.SERIE + "\n"
            return resp;
        else:
            return str(self.__dict__)
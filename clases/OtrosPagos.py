from clases.Funciones import *

class OtrosPagos():
    def __init__(self):
        self.IDOTROPAGO = ""                      #NUMBER
        self.IDNOMINA = ""                        #VARCHAR2 (30 BYTE)
        self.TIPOOTROPAGO = ""                    #VARCHAR2 (9 BYTE)
        self.CLAVE = ""                           #VARCHAR2 (45 BYTE)
        self.CONCEPTO = ""                        #VARCHAR2 (300 BYTE)
        self.IMPORTE = ""                         #NUMBER (14,2)
        self.SUBSIDIOCAUSADO = ""                 #NUMBER (14,2)
        self.SALDOAFAVOR = ""                     #NUMBER (14,2)
        self.ANIO = ""                            #NUMBER (4)
        self.REMANENTESALDOAFAVOR = ""            #NUMBER (14,2)
        self.IDUSUARIO = "FACTURAX"               #VARCHAR2 (60 BYTE)
        self.FG = ""                              #DATE
        self.ST = ""                              #NUMBER
    
    def setIDOTROPAGO(self,IDOTROPAGO):
        self.IDOTROPAGO = validarDato(IDOTROPAGO)
    def setIDNOMINA(self,IDNOMINA):
        self.IDNOMINA = validarDato(IDNOMINA)
    def setTIPOOTROPAGO(self,TIPOOTROPAGO):
        self.TIPOOTROPAGO = validarDato(TIPOOTROPAGO)
    def setCLAVE(self,CLAVE):
        self.CLAVE = validarDato(CLAVE)
    def setCONCEPTO(self,CONCEPTO):
        self.CONCEPTO = validarDato(CONCEPTO)
    def setIMPORTE(self,IMPORTE):
        self.IMPORTE = validarCifra(validarDato(IMPORTE))
    def setSUBSIDIOCAUSADO(self,SUBSIDIOCAUSADO):        
        self.SUBSIDIOCAUSADO = validarCifra(validarDato(SUBSIDIOCAUSADO))
    def setSALDOAFAVOR(self,SALDOAFAVOR):
        self.SALDOAFAVOR = validarCifra(validarDato(SALDOAFAVOR))
    def setANIO(self,ANIO):
        self.ANIO = validarDato(ANIO)
    def setREMANENTESALDOAFAVOR(self,REMANENTESALDOAFAVOR):
        self.REMANENTESALDOAFAVOR = validarDato(REMANENTESALDOAFAVOR)
    			
    def getinfo(self,opc):
        if opc:
            resp  = self.IDOTROPAGO+ "," + self.IDNOMINA+ "," + self.TIPOOTROPAGO+ "," + self.CLAVE+ "," + self.CONCEPTO+ "," + self.IMPORTE+ "," + self.SUBSIDIOCAUSADO+ "," + self.SALDOAFAVOR+ "," + self.ANIO+ "," + self.REMANENTESALDOAFAVOR+ "," + self.IDUSUARIO+ "," + self.FG+ "," + self.ST + "\n"
            return resp;
        else:
            return str(self.__dict__)
from clases.Funciones import *

class Deduccion():
    def __init__(self):
        self.IDDEDUCCION = ""              #NUMBER
        self.IDDEDUCCIONES = ""            #NUMBER
        self.IDNOMINA = ""                 #VARCHAR2 (30 BYTE)
        self.TIPODEDUCCION = ""            #VARCHAR2 (9 BYTE)
        self.CLAVE = ""                    #VARCHAR2 (45 BYTE)
        self.CONCEPTO = ""                 #VARCHAR2 (300 BYTE)
        self.IMPORTE = ""                  #NUMBER (14,2)
        self.FEC_IMPUTACION = ""           #DATE
        self.FEC_PAGO = ""                 #DATE
        self.TIPO_PRESTAMO = ""            #VARCHAR2 (12 BYTE)
        self.SUBTIPO_PRESTAMO = ""         #VARCHAR2 (12 BYTE)
        self.IDUSUARIO = "FACTURAX"        #VARCHAR2 (60 BYTE)
        self.FG = ""                       #DATE
        self.ST = ""                       #NUMBER
        self.SERIE = ""                    #VARCHAR2 (75 BYTE)
        self.IMPORTEGRAVADO = ""           #NUMBER (10,2)
        self.IMPORTEEXENTO = ""            #NUMBER (10,2)
        
    def setIDDEDUCCION(self,IDDEDUCCION):
        self.IDDEDUCCION = validarDato(IDDEDUCCION)
    def setIDDEDUCCIONES(self,IDDEDUCCIONES):
            self.IDDEDUCCIONES = validarDato(IDDEDUCCIONES)
    def setIDNOMINA(self,IDNOMINA):
            self.IDNOMINA = validarDato(IDNOMINA)
    def setTIPODEDUCCION(self,TIPODEDUCCION):
            self.TIPODEDUCCION = validarDato(TIPODEDUCCION)
    def setCLAVE(self,CLAVE):
            self.CLAVE = validarDato(CLAVE)
    def setCONCEPTO(self,CONCEPTO):
            self.CONCEPTO = validarDato(CONCEPTO)
    def setIMPORTE(self,IMPORTE):
            self.IMPORTE = validarCifra(validarDato(IMPORTE))
    def setFEC_IMPUTACION(self,FEC_IMPUTACION):
            self.FEC_IMPUTACION = formatFecha(validarDato(FEC_IMPUTACION))
    
        
    			
    def getinfo(self,opc):
        if opc:
            resp  =  self.IDDEDUCCION + "," + self.IDDEDUCCIONES + "," + self.IDNOMINA + "," + self.TIPODEDUCCION + "," + self.CLAVE + "," + self.CONCEPTO + "," + self.IMPORTE + "," + self.FEC_IMPUTACION + "," + self.FEC_PAGO + "," + self.TIPO_PRESTAMO + "," + self.SUBTIPO_PRESTAMO + "," + self.IDUSUARIO + "," + self.FG + "," + self.ST + "," + self.SERIE + "," + self.IMPORTEGRAVADO + "," + self.IMPORTEEXENTO +"\n"
            return resp;
        else:
            return str(self.__dict__)
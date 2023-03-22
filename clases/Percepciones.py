from clases.Funciones import *

class Percepciones():
    def __init__(self):
        self.IDPERCEPCIONES = ""                  #NUMBER
        self.IDNOMINA = ""                        #VARCHAR2 (30 BYTE)
        self.TOTALSUELDOS = ""                    #NUMBER (14,2)
        self.TOTALSEPARACIONINDEM = ""            #NUMBER (14,2)
        self.TOTALJUBILACIONPENSIONRE = ""        #NUMBER (14,2)
        self.TOTALGRAVADO = ""                    #NUMBER (14,2)
        self.TOTALEXENTO = ""                     #NUMBER (14,2)
        self.TOTALUNAEXHIBICION = ""              #NUMBER (14,2)
        self.INGRESOACUMULABLEPEN = ""            #NUMBER (14,2)
        self.INGRESONOACUMULABLEPEN = ""          #NUMBER (14,2)
        self.TOTALPAGADO = ""                     #NUMBER (14,2)
        self.NUMANIOSSERVICIO = ""                #NUMBER
        self.ULTIMOSUELDOMENSORD = ""             #NUMBER (14,2)
        self.INGRESOACUMULABLEINDEM = ""          #NUMBER (14,2)
        self.INGRESONOACUMULABLEINDEM = ""        #NUMBER (14,2)
        self.IDUSUARIO = "FACTURAX"               #VARCHAR2 (60 BYTE)
        self.FG = ""                              #DATE
        self.ST = ""                              #NUMBER
        self.TOTALPARCIALIDAD = ""                #NUMBER (14,2)
        self.MONTODIARIO = ""                     #NUMBER (14,2)
        
    def setIDPERCEPCIONES(self,IDPERCEPCIONES):
        self.IDPERCEPCIONES = validarDato(IDPERCEPCIONES)
    def setIDNOMINA(self,IDNOMINA):
        self.IDNOMINA = validarDato(IDNOMINA)
    def setTOTALSUELDOS(self,TOTALSUELDOS):
        self.TOTALSUELDOS = validarCifra(validarDato(TOTALSUELDOS))
    def setTOTALSEPARACIONINDEM(self,TOTALSEPARACIONINDEM):
        self.TOTALSEPARACIONINDEM = validarCifra(validarDato(TOTALSEPARACIONINDEM))
    def setTOTALJUBILACIONPENSIONRE(self,TOTALJUBILACIONPENSIONRE):
        self.TOTALJUBILACIONPENSIONRE = validarCifra(validarDato(TOTALJUBILACIONPENSIONRE))
    def setTOTALGRAVADO(self,TOTALGRAVADO):
        self.TOTALGRAVADO = validarCifra(validarDato(TOTALGRAVADO))
    def setTOTALEXENTO(self,TOTALEXENTO):
        self.TOTALEXENTO = validarCifra(validarDato(TOTALEXENTO))
    def setTOTALUNAEXHIBICION(self,TOTALUNAEXHIBICION):
        self.TOTALUNAEXHIBICION = validarCifra(validarDato(TOTALUNAEXHIBICION))
    def setINGRESOACUMULABLEPEN(self,INGRESOACUMULABLEPEN):
        self.INGRESOACUMULABLEPEN = validarCifra(validarDato(INGRESOACUMULABLEPEN))
    def setINGRESONOACUMULABLEPEN(self,INGRESONOACUMULABLEPEN):
        self.INGRESONOACUMULABLEPEN = validarCifra(validarDato(INGRESONOACUMULABLEPEN))
    def setTOTALPAGADO(self,TOTALPAGADO):
        self.TOTALPAGADO = validarCifra(validarDato(TOTALPAGADO))
    def setNUMANIOSSERVICIO(self,NUMANIOSSERVICIO):
        self.NUMANIOSSERVICIO = validarDato(NUMANIOSSERVICIO)
    def setULTIMOSUELDOMENSORD(self,ULTIMOSUELDOMENSORD):
        self.ULTIMOSUELDOMENSORD = validarDato(ULTIMOSUELDOMENSORD)
    def setINGRESOACUMULABLEINDEM(self,INGRESOACUMULABLEINDEM):
        self.INGRESOACUMULABLEINDEM = validarDato(INGRESOACUMULABLEINDEM)
    def setINGRESONOACUMULABLEINDEM(self,INGRESONOACUMULABLEINDEM):
        self.INGRESONOACUMULABLEINDEM = validarDato(INGRESONOACUMULABLEINDEM)
    def setTOTALPARCIALIDAD(self,TOTALPARCIALIDAD):
        self.TOTALPARCIALIDAD = validarDato(TOTALPARCIALIDAD)
    def setMONTODIARIO(self,MONTODIARIO):
        self.MONTODIARIO = validarDato(MONTODIARIO)
    def getIDNOMINA(self):
        return self.IDNOMINA
    def getID(self):
        return self.IDPERCEPCIONES
    			
    def getinfo(self,opc):
        if opc:
            resp  = self.IDPERCEPCIONES + "," +self.IDNOMINA + "," +self.TOTALSUELDOS + "," +self.TOTALSEPARACIONINDEM + "," +self.TOTALJUBILACIONPENSIONRE + "," +self.TOTALGRAVADO + "," +self.TOTALEXENTO + "," +self.TOTALUNAEXHIBICION + "," +self.INGRESOACUMULABLEPEN + "," +self.INGRESONOACUMULABLEPEN + "," +self.TOTALPAGADO + "," +self.NUMANIOSSERVICIO + "," +self.ULTIMOSUELDOMENSORD + "," +self.INGRESOACUMULABLEINDEM + "," +self.INGRESONOACUMULABLEINDEM + "," +self.IDUSUARIO + "," +self.FG + "," +self.ST + "," +self.TOTALPARCIALIDAD + "," +self.MONTODIARIO + "\n"
            return resp;
        else:
            return str(self.__dict__)
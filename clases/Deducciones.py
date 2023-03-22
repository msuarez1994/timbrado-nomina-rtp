from clases.Funciones import *

class Deducciones():
    def __init__(self):
        self.IDDEDUCCIONES = ""                   #NUMBER
        self.IDNOMINA = ""                        #VARCHAR2 (30 BYTE)
        self.TOTALOTRASDEDUCCIONES = ""           #NUMBER (14,2)
        self.TOTALIMPUESTOSRETENIDOS = ""         #NUMBER (14,2)
        self.IDUSUARIO = "FACTURAX"               #VARCHAR2 (60 BYTE)
        self.FG = ""                              #DATE
        self.ST = ""                              #NUMBER
        
    def setIDDEDUCCIONES(self,IDDEDUCCIONES):
        self.IDDEDUCCIONES = validarDato(IDDEDUCCIONES)
    def setIDNOMINA(self,IDNOMINA):
        self.IDNOMINA = validarDato(IDNOMINA)
    def setTOTALOTRASDEDUCCIONES(self,TOTALOTRASDEDUCCIONES):
        self.TOTALOTRASDEDUCCIONES = validarCifra(validarDato(TOTALOTRASDEDUCCIONES))
    def setTOTALIMPUESTOSRETENIDOS(self,TOTALIMPUESTOSRETENIDOS):
        self.TOTALIMPUESTOSRETENIDOS = validarCifra(validarDato(TOTALIMPUESTOSRETENIDOS))
    def setIDUSUARIO(self,IDUSUARIO):
        self.IDUSUARIO = validarDato(IDUSUARIO)
    def setFG(self,FG):
        self.FG = validarDato(FG)
    def setST(self,ST):
        self.ST = validarDato(ST)
    def getIDNOMINA(self):
        return self.IDNOMINA
    def getID(self):
        return self.IDDEDUCCIONES
    			
    def getinfo(self,opc):
        if opc:
            resp  = self.IDDEDUCCIONES+ "," + self.IDNOMINA+ "," + self.TOTALOTRASDEDUCCIONES+ "," + self.TOTALIMPUESTOSRETENIDOS+ "," + self.IDUSUARIO+ "," + self.FG+ "," + self.ST + "\n"
            return resp;
        else:
            return str(self.__dict__)
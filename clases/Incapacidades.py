from clases.Funciones import *

class Incapacidades():
    def __init__(self):
        self.IDINCAPACIDAD = ""			 #NUMBER
        self.IDNOMINA = ""			 	 #VARCHAR2 (30 BYTE)
        self.DIASINCAPACIDAD = ""		 #NUMBER
        self.TIPOINCAPACIDAD = ""		 #VARCHAR2 (6 BYTE)
        self.IMPORTEMONETARIO = ""		 #NUMBER (14,2)
        self.IDUSUARIO = "FACTURAX"		 #VARCHAR2 (60 BYTE)
        self.FG = ""			 	     #DATE
        self.ST = ""			 		 #NUMBER
        
    def setIDINCAPACIDAD(self,IDINCAPACIDAD):
        self.IDINCAPACIDAD = validarDato(IDINCAPACIDAD)
    def setIDNOMINA(self,IDNOMINA):
    	self.IDNOMINA = validarDato(IDNOMINA)
    def setDIASINCAPACIDAD(self,DIASINCAPACIDAD):
    	self.DIASINCAPACIDAD = validarDato(DIASINCAPACIDAD)
    def setTIPOINCAPACIDAD(self,TIPOINCAPACIDAD):
    	self.TIPOINCAPACIDAD = validarDato(TIPOINCAPACIDAD)
    def setIMPORTEMONETARIO(self,IMPORTEMONETARIO):
    	self.IMPORTEMONETARIO = validarCifra(validarDato(IMPORTEMONETARIO))
    			
    def getinfo(self,opc):
        if opc:
            resp  = self.IDINCAPACIDAD+ "," + self.IDNOMINA+ "," + self.DIASINCAPACIDAD+ "," + self.TIPOINCAPACIDAD+ "," + self.IMPORTEMONETARIO+ "," + self.IDUSUARIO+ "," + self.FG+ "," + self.ST +"\n"
            return resp;
        else:
            return str(self.__dict__)
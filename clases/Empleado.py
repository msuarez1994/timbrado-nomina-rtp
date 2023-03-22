class Empleado():
    def __init__(self, rfc, nempleado):
        self.rfc = rfc
        self.nempleado = nempleado
    
    def setRFC(self,RFC):
        self.rfc = RFC
    def setNEMPLEADO(self,NEMPLEADO):
        self.nempleado = NEMPLEADO
        
    def getRFC(self):
        return self.rfc
    def getNEMPLEADO(self):
        return self.nempleado
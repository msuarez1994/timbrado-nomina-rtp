from clases.Funciones import *

class Comprobante():
    def __init__(self):
        self.IDCOMPROBANTE = ""              #VARCHAR2 (30 BYTE)
        self.IDNOMINA = ""                   #VARCHAR2 (30 BYTE)
        self.VERSION = "1.2"                 #VARCHAR2 (15 BYTE)
        self.SERIE = ""                      #VARCHAR2 (450 BYTE)
        self.FOLIO = ""                      #VARCHAR2 (120 BYTE)
        self.FECHA = ""                      #DATE
        self.FORMADEPAGO = ""                #VARCHAR2 (600 BYTE)
        self.SUBTOTAL = ""                   #NUMBER (14,2)
        self.DESCUENTO = ""                  #NUMBER (14,2)
        self.TOTAL = ""                      #NUMBER (14,2)
        self.METODODEPAGO = ""               #VARCHAR2 (900 BYTE)
        self.TIPODECOMPROBANTE = ""          #VARCHAR2 (30 BYTE)
        self.MONEDA = ""                     #VARCHAR2 (75 BYTE)
        self.LUGAREXPEDICION = ""            #VARCHAR2 (900 BYTE)
        self.RFCEMISOR = ""                  #VARCHAR2 (39 BYTE)
        self.NOMBREEMISOR = ""               #VARCHAR2 (900 BYTE)
        self.REGIMENFISCALEMISOR = ""        #VARCHAR2 (900 BYTE)
        self.CURPEMISOR = ""                 #VARCHAR2 (54 BYTE)
        self.REGISTROPATRONAL = ""           #VARCHAR2 (90 BYTE)
        self.RFCPATRONORIGEN = ""            #VARCHAR2 (39 BYTE)
        self.ORIGENRECURSO = ""              #VARCHAR2 (300 BYTE)
        self.CANTIDAD = ""                   #NUMBER (14,2)
        self.DESCRIPCION = ""                #VARCHAR2 (3000 BYTE)
        self.VALORUNITARIO = ""              #NUMBER (14,2)
        self.IMPORTE = ""                    #NUMBER (14,2)
        self.PARA  = ""                      #VARCHAR2 (750 BYTE)
        self.CC = ""                         #VARCHAR2 (750 BYTE)
        self.CCO = ""                        #VARCHAR2 (750 BYTE)
        self.PROCESADO = ""                  #NUMBER
        self.ESTATUS = ""                    #NUMBER
        self.ID_UNIDAD_ADM = ""              #NUMBER
        self.IDUSUARIO = ""                  #VARCHAR2 (60 BYTE)
        self.FG = ""                         #DATE
        self.ST = ""                         #NUMBER
        self.MONTORECURSOPROPIO = ""         #NUMBER (14,2)
        self.IDSUCURSAL = ""                 #VARCHAR2 (60 BYTE)
        self.CONDICIONESDEPAGO = ""          #VARCHAR2 (300 BYTE)
        self.TIPORELACION = ""               #VARCHAR2 (300 BYTE)
        self.UUID = ""                       #VARCHAR2 (300 BYTE)
        self.USODECFDI = ""                  #VARCHAR2 (300 BYTE)
        self.CLAVEPRODSERV = ""              #NUMBER
        self.NOIDENTIFICACION = ""           #VARCHAR2 (300 BYTE)
        self.CLAVEUNIDAD = ""                #VARCHAR2 (150 BYTE)
        self.BASE = ""                       #NUMBER (14,2)
        self.IMPUESTO = ""                   #NUMBER (14,2)
        self.TIPOFACTOR = ""                 #NUMBER (14,2)
        self.TASAOCUOTA = ""                 #NUMBER (14,2)
        self.UUIDSUCURSAL = ""               #VARCHAR2 (108 BYTE)     
        self.EXPORTACION = ""                
        self.obj_objetos = ""                
    
    def setIDCOMPROBANTE(self,IDCOMPROBANTE):
        self.IDCOMPROBANTE = validarDato(IDCOMPROBANTE)
    def setIDNOMINA(self,IDNOMINA):
        self.IDNOMINA = validarDato(IDNOMINA)
    def setSERIE(self,SERIE):
        self.SERIE = validarDato(SERIE)
    def setFOLIO(self,FOLIO):
        self.FOLIO = validarDato(FOLIO)
    def setFECHA(self,FECHA):
        self.FECHA = formatFecha(validarDato(FECHA))
    def setFORMADEPAGO(self,FORMADEPAGO):
        self.FORMADEPAGO = validarDato(FORMADEPAGO)
    def setSUBTOTAL(self,SUBTOTAL):
        self.SUBTOTAL = validarCifra(validarDato(SUBTOTAL))
    def setDESCUENTO(self,DESCUENTO):
        self.DESCUENTO = validarCifra(validarDato(DESCUENTO))
    def setTOTAL(self,TOTAL):
        self.TOTAL = validarCifra(validarDato(TOTAL))
    def setMETODODEPAGO(self,METODODEPAGO):
        self.METODODEPAGO = validarDato(METODODEPAGO)
    def setTIPODECOMPROBANTE(self,TIPODECOMPROBANTE):
        self.TIPODECOMPROBANTE = validarDato(TIPODECOMPROBANTE)
    def setMONEDA(self,MONEDA):
        self.MONEDA = validarDato(MONEDA)
    def setLUGAREXPEDICION(self,LUGAREXPEDICION):
        self.LUGAREXPEDICION = validarDato(LUGAREXPEDICION)
    def setRFCEMISOR(self,RFCEMISOR):
        self.RFCEMISOR = validarDato(RFCEMISOR)
    def setNOMBREEMISOR(self,NOMBREEMISOR):
        self.NOMBREEMISOR = validarDato(NOMBREEMISOR)
    def setREGIMENFISCALEMISOR(self,REGIMENFISCALEMISOR):
        self.REGIMENFISCALEMISOR = validarDato(REGIMENFISCALEMISOR)
    def setREGISTROPATRONAL(self,REGISTROPATRONAL):
        self.REGISTROPATRONAL = validarDato(REGISTROPATRONAL)
    def setORIGENRECURSO(self,ORIGENRECURSO):
        self.ORIGENRECURSO = validarDato(ORIGENRECURSO)
    def setCANTIDAD(self,CANTIDAD):
        self.CANTIDAD = validarCifra(validarDato(CANTIDAD))
    def setDESCRIPCION(self,DESCRIPCION):
        self.DESCRIPCION = validarDato(DESCRIPCION)
    def setVALORUNITARIO(self,VALORUNITARIO):
        self.VALORUNITARIO = validarCifra(validarDato(VALORUNITARIO))
    def setIMPORTE(self,IMPORTE):
        self.IMPORTE = validarCifra(validarDato(IMPORTE))
    def setPARA(self,PARA):
        self.PARA = validarDato(PARA)
    def setCC(self,CC):
        self.CC = validarDato(CC)
    def setCCO(self,CCO):
        self.CCO = validarDato(CCO)
    def setMONTORECURSOPROPIO(self,MONTORECURSOPROPIO):
        self.MONTORECURSOPROPIO = validarCifra(validarDato(MONTORECURSOPROPIO))
    def setTIPORELACION(self,TIPORELACION):
        self.TIPORELACION = validarDato(TIPORELACION)
    def setUUID(self,UUID):
        self.UUID = validarDato(UUID)
    def setUSODECFDI(self,USODECFDI):
        self.USODECFDI = validarDato(USODECFDI)
    def setCLAVEPRODSERV(self,CLAVEPRODSERV):
        self.CLAVEPRODSERV = validarDato(CLAVEPRODSERV)
    def setCLAVEUNIDAD (self,CLAVEUNIDAD):
        self.CLAVEUNIDAD  = validarDato(CLAVEUNIDAD)
    			
    def setEXPORTACION (self,EXPORTACION):
        self.EXPORTACION  = validarDato(EXPORTACION)
    			
    def setobj_objetos (self,obj_objetos):
        self.obj_objetos  = validarDato(obj_objetos)
    def getinfo(self,opc):
        if opc:
            resp  = str(self.IDCOMPROBANTE) + "," + str(self.IDNOMINA) + "," + str(self.VERSION) + "," + str(self.SERIE) + "," + str(self.FOLIO) + "," + str(self.FECHA) + "," + str(self.FORMADEPAGO) + "," + str(self.SUBTOTAL) + "," + str(self.DESCUENTO) + "," + str(self.TOTAL) + "," + str(self.METODODEPAGO) + "," + str(self.TIPODECOMPROBANTE) + "," + str(self.MONEDA) + "," + str(self.LUGAREXPEDICION) + "," + str(self.RFCEMISOR) + "," + str(self.NOMBREEMISOR) + "," + str(self.REGIMENFISCALEMISOR) + "," + str(self.CURPEMISOR) + "," + str(self.REGISTROPATRONAL) + "," + str(self.RFCPATRONORIGEN) + "," + str(self.ORIGENRECURSO) + "," + str(self.CANTIDAD) + "," + str(self.DESCRIPCION) + "," + str(self.VALORUNITARIO) + "," + str(self.IMPORTE) + "," + str(self.PARA) + "," + str(self.CC) + "," + str(self.CCO) + "," + str(self.PROCESADO) + "," + str(self.ESTATUS) + "," + str(self.ID_UNIDAD_ADM) + "," + str(self.IDUSUARIO) + "," + str(self.FG) + "," + str(self.ST) + "," + str(self.MONTORECURSOPROPIO) + "," + str(self.IDSUCURSAL) + "," + str(self.CONDICIONESDEPAGO) + "," + str(self.TIPORELACION) + "," + str(self.UUID) + "," + str(self.USODECFDI) + "," + str(self.CLAVEPRODSERV) + "," + str(self.NOIDENTIFICACION) + "," + str(self.CLAVEUNIDAD) + "," + str(self.BASE) + "," + str(self.IMPUESTO) + "," + str(self.TIPOFACTOR) + "," + str(self.TASAOCUOTA) + "," + str(self.UUIDSUCURSAL)+ "," + str(self.EXPORTACION) + "," + str(self.obj_objetos) + "\n"
            return resp;
        else:
            return str(self.__dict__)
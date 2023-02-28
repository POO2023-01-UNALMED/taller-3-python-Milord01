class TV:
    __numTV=0
    def __init__(self,marca,estado):
        self.__marca=marca
        self.__canal=1
        self.__precio=500
        self.__estado=estado
        self.__volumen=1
        self.__control=None
        TV.__numTV+=1
    def setMarca(self,marca):
        self.__marca=marca
    def getMarca(self):
        return self.__marca

    def setControl(self,control):
        self.__control=control
    def getControl(self):
        return self.__control
    
    def setPrecio(self,precio):
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    
    def setVolumen(self,volumen):
        if self.__estado==True and volumen>=0 and volumen<7:
          self.__volumen=volumen
    def getVolumen(self):
        return self.__volumen
    
    def setCanal(self,canal):
        if self.__estado==True and canal>=1 and canal<120:
          self.__canal=canal
    def getCanal(self):
        return self.__canal

    def setEstado(self,estado):
        self.__estado=estado
    def getEstado(self):
        return self.__estado
    
    @classmethod
    def setNumTV(cls, numTV):
        cls.__numTV=numTV
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    def turnOn(self):
        self.__estado=True
    def turnOff(self):
        self.__estado=False
    
    def volumenUp(self):
        self.__volumen+=1
    def volumenDown(self):
        self.__volumen-=1

    def canalUp(self):
        self.__canal+=1
    def canalDown(self):
        self.__canal-=1


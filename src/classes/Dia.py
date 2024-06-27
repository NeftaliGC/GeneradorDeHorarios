from datetime import datetime

class Dia:

    def __init__(self, dia, __horarioInicio, __horarioFin):
        self.__dia = dia
        self.__horarioInicio = datetime.strptime(__horarioInicio, '%H:%M').time()
        self.__horarioFin = datetime.strptime(__horarioFin, '%H:%M').time()

    def getDia(self):
        return self.__dia

    def getHorarioInicio(self):
        return self.__horarioInicio

    def getHorarioFin(self):
        return self.__horarioFin
    
    def __str__(self):
        return f'{self.__dia} {self.__horarioInicio} {self.__horarioFin}'
        
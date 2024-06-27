class Curso:
    def __init__(self, nombre, grupo, profesor, salon, dias=[]):
        self.__nombre = nombre
        self.__grupo = grupo
        self.__profesor = profesor
        self.__salon = salon
        self.__dias = dias

    def __str__(self):
        str = f'{self.__nombre} {self.__grupo} {self.__profesor} {self.__salon}'
        for dia in self.__dias:
            str += f' {dia}'
        return str

    def getNombre(self):
        return self.__nombre

    def getDias(self):
        return self.__dias

    def compare(self, curso):
        solapado = False

        for dia in self.__dias:
            for dia2 in curso.getDias():
                if dia.getDia() == dia2.getDia():
                    if dia2.getHorarioInicio() >= dia.getHorarioInicio() and dia2.getHorarioInicio() <= dia.getHorarioFin():
                        solapado = True
                        break
            if solapado:
                break

        return solapado
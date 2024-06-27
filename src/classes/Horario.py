class Horario:

    def __init__(self):
        self.__cursos = []

    def addCurso(self, curso):
        if not self.__cursos:
            self.__cursos.append(curso)
        else:

            for c in self.__cursos:
                if c.getNombre() == curso.getNombre():
                    return False

                if c.compare(curso):
                    return False
                    
            self.__cursos.append(curso)

    def getCursos(self):
        return self.__cursos
    
    def __str__(self):
        str = ''
        for curso in self.__cursos:
            str += f'{curso}\n'
        return str
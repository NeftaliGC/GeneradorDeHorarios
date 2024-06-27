from classes.Curso import Curso
from classes.Dia import Dia
from classes.Reader import Reader
import re

def main():
    reader = Reader('src/data/horarios.csv')
    reader.read()
    horarios = reader.getData()
    
    cursos = []

    for horario in horarios:
        horario = horario.split(',')
        curso = None
        dias = []
        dia = horario[3]
        dia = re.findall(r'\"(.*?)\"|\S+', dia)
        for i in dia:
            sepi = i.split(' ')
            
            temDay = Dia(sepi[0], sepi[1], sepi[2])
            dias.append(temDay)

            curso = Curso(horario[0], horario[1], horario[2], sepi[3], dias)

            cursos.append(curso)

    for curso in cursos:
        print(curso)

if __name__ == "__main__":
    main()
from classes.Curso import Curso
from classes.Dia import Dia
from classes.Reader import Reader
from classes.Horario import Horario
import re
import os
from classes.InterfazGrafica import InterfazGrafica
categorias = []

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

    """ for curso in cursos:
        print(curso) """

    establecerCategorias(cursos)
    horarios = []

    for categoria in categorias:
        horariosGenerados = generar_combinaciones(cursos, horarios, categoria)
        for horario in horariosGenerados:
            horarios.append(horario)


    #Crear un txt con los horarios en un solo archivo
    with open('src/data/horarios.txt', 'w') as file:
        for i, horario in enumerate(horarios):
            file.write(f'Horario {i+1}\n{horario}\n\n')
    InterfazGrafica.run(horarios[0])

def generar_combinaciones(cursos, horarios, categoria):

    allCursosOfCategory = []
    Horarios = []
    for curso in cursos:
        if curso.getNombre() == categoria:
            allCursosOfCategory.append(curso)
        
    for curso in allCursosOfCategory:
        temoHorario = Horario()
        temoHorario.addCurso(curso)
        for curso in cursos:
            temoHorario.addCurso(curso)

        Horarios.append(temoHorario)

    return Horarios
            

def establecerCategorias(cursos):
    for curso in cursos:
        if categorias == []:
            categorias.append(curso.getNombre())
        else:
            if curso.getNombre() not in categorias:
                categorias.append(curso.getNombre())

if __name__ == "__main__":
    main()
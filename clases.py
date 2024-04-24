#Programacion orientada a objetos

#clases

class Profesor:
    def __init__(self, el_nombre, email_prof):
        self.__nombre__ = el_nombre
        self.__email__ = email_prof

    def give_nombre(self): #funcion que si es llamada devuelve el nombre
        return self.__nombre__

class Alumno:
    def __init__(self,nombre_alumno):
        self.__nombre__ = nombre_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def mentoria (self, profesor):
        self.__mentor__ = profesor

    def falta(self): #suma una falta al alumno que llame a esta funcion
        self.__inasistencias__ += 1

    def libre (self): #a partir de las 5 faltas el alumno esta libre
        if self.__inasistencias__ > 5:
            return "ALUMNO LIBRE"
        else:
            return "OK"
        
    def dieta (self, dieta):
        self.__dieta__ = dieta
    
    def vegano (self):
        self.__dieta__ = "vegano"

profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

print(profe_elio.give_nombre()) #devuelve el nombre
print(profe_gabi.give_nombre()) #devuelve el nombre

alumno_juan = Alumno("Juan")
alumno_maria = Alumno("Maria")

alumno_juan.falta() #cada vez que se ejectua la funcion falta, se suma una falta
alumno_juan.falta() #cada vez que se ejectua la funcion falta, se suma una falta
alumno_juan.falta() #cada vez que se ejectua la funcion falta, se suma una falta
alumno_juan.falta() #cada vez que se ejectua la funcion falta, se suma una falta 

print(alumno_juan.libre()) #Al ejecutar la funcion libre se avisa si el alumno esta libre

alumno_juan.falta() #cada vez que se ejectua la funcion falta, se suma una falta

print(alumno_juan.libre()) #Al ejecutar la funcion libre se avisa si el alumno esta libre
print(alumno_maria.libre())#Al ejecutar la funcion libre se avisa si el alumno esta libre

alumno_maria.dieta("vegetariana")
print(alumno_maria.__dieta__)
alumno_juan.vegano()
print(alumno_juan.__dieta__)

alumno_juan.mentoria(profe_elio)

print(alumno_juan.__mentor__)

#LOS ATRIBUTOS se anotan con doble undercore __atributo__
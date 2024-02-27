from tabulate import tabulate
alumno = {}

def AddStudent(alumnos:dict):
    id = input('Ingrese el id : ')
    nombre = input('Ingrese el nombre : ')
    edad = int(input(f'Ingrese la edad de {nombre} : '))
    email = input(f'Ingrese el email de {nombre}: ')
    alumno = {
        'id':id,
        'nombre':nombre,
        'edad':edad,
        'email':email,
    }
    alumnos.update({id:alumno})
    print(alumnos)
    
def SearchStudents(alumnos:dict):
    id = input('Ingrese numero de id del estudiante: ')
    data = alumnos.get(id,False)
    if type(data) == dict:
        print(data)
    elif type(data) == bool and data == False:
        print('El estudiante no existe')
        
def LitData(alumnos:dict):
    info = []
    for key,value in alumnos.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))

def ValidateStudent(alumnos : dict)-> bool:
    return bool(alumnos.get(id,''))

def DelStudent(alumnos : dict):
    id = input('Ingrese numero de id del estudiante: ')
    if (ValidateStudent(alumnos,id)):
        alumnos.pop(id)
    else:
        print(f'El estudiante con id {id} no esta registrado') 
        
def DelByName(alumnos : dict):
    nombre = input('Ingrese nombre del estudiante: ')
    for key,value in alumnos.items():
        if(nombre in value['nombre']):
            alumnos.pop(key)
            break

def AddGrades(alumnos: dict):
    notas = {
        'parciales' : [],
        'quices' : [],
        'trabajos' : []
    }
    id_alumno = input('Ingrese el ID del alumno al que desea asignar las notas: ')
    estudiante = alumnos.get(id_alumno)
    if estudiante:
        estudiante['calificaciones'] = notas
        estudiante['calificaciones']['parciales'] = input('Ingrese las notas de parciales separadas por comas: ').split(',')
        estudiante['calificaciones']['quices'] = input('Ingrese las notas de quices separadas por comas: ').split(',')
        estudiante['calificaciones']['trabajos'] = input('Ingrese las notas de trabajos separadas por comas: ').split(',')
        LitData(alumnos)
    else:
        print(f"No se encontró ningún alumno con el ID '{id_alumno}'.")


        



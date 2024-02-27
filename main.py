import modulos.gestorAlumnos as st
import os
if __name__ == '__main__':
    alumnos = {}
    while True: 
        st.AddStudent(alumnos)
        # st.SearchStudents(alumnos)
        st.AddGrades(alumnos)
        # st.LitData(alumnos)
        # st.DelStudent(alumnos)
        # st.DelByName(alumnos)
        print('¿Desea continuar? (S/N)')
        respuesta = input().upper()
        if respuesta == 'N':
            break   
    
    
    

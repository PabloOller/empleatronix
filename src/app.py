import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title('EMPLEATRONIX')

st.write('Todos los datos sobre los empleados en una aplicación.')
employees = pd.read_csv('data/employees.csv')
st.dataframe(employees)

st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker('Elige un color para las barras', '#3475B3')
with col2:
    mostrarNombres = st.toggle('Mostrar el nombre')
with col3:
    mostrarSalarios = st.toggle('Mostrar el sueldo en la barra')

names = employees['full name']
salaries = employees['salary']

fig, ax = plt.subplots()

if mostrarNombres == False:
       ax.set_yticks([])

# Mostrar salarios en las barras si el toggle correspondiente está activado
if mostrarSalarios:
   bars = ax.barh(names, salaries, color=color)
   for bar, salary in zip(bars, salaries):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{salary} €', va='center', ha='left', fontsize=10, color='black')


ax.barh(names, salaries, color=color)
plt.xlim(0,4500)


st.pyplot(fig)


st.write("Por Pablo Oller Pérez")
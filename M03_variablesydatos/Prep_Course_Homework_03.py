#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

entero = 10
print("El numero entero es: ", entero)
# In[7]:




# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# In[3]:





# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(entero))
# In[8]:





# 4) Crear una variable que contenga tu nombre
nombre = "Sebastián Cruz"
# In[2]:




# 5) Crear una variable que contenga un número complejo
complejo = 3j
# In[3]:





# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(complejo)
# In[4]:





# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416
pi_redondeado = round(pi, 4)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
var1 = True
var2 = True

print (var1 == var2 )



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(var1))
print(type(var2))
# In[5]:





# 10) Asignar a una variable, la suma de un número entero y otro decimal
suma = 10 + 3.1416
# In[1]:





# 11) Realizar una operación de suma de números complejos

suma1 = 3j + 75j
# In[2]:





# 12) Realizar una operación de suma de un número real y otro complejo

suma2 = 3.1416 + 3j
# In[4]:





# 13) Realizar una operación de multiplicación

producto = 5 * 5 
# In[5]:





# 14) Mostrar el resultado de elevar 2 a la octava potencia
print (2**8)
# In[6]:




# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print (cociente)
# In[8]:





# 16) De la división anterior solamente mostrar la parte entera
cociente = 27 // 4 
print (cociente)
# In[9]:





# 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print (resto)
# In[1]:





# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
operacion = 4 * 6 + 3
print(operacion)
# In[2]:





# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
concatenacion = "1. " + "Ciudad " + "de " "Mexico "
print(concatenacion)

# In[3]:





# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
var1 = "2"
var2 = 2
print(var1 == var2)

''' Esto ocuere por que  no son iguales ya que uno es un valor entero y el otro en un string'''

# In[4]:





# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
var3 = int(var1)
print (var3 == var2)
# In[11]:





# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

'''La razón por la que el código a = float('3,8') arroja un error es porque el carácter de coma , no es un delimitador 
   válido para representar un número decimal en Python. El delimitador correcto para los números decimales en Python es el punto ..'''

# Forma correcta de convertir un número decimal
a = float('3.8')  # Es usar punto para decimales
print(type(a))  

# In[12]:





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.
numero = 3
numero -= 1
print (numero)
# In[15]:





# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print (1<<2)

'''El sistema binario utiliza solo dos dígitos, 0 y 1, para representar números. Cada posición en una secuencia de bits (binarios) 
   tiene un peso que es una potencia de 2. Por ejemplo, el número binario 10 (en base 2) es equivalente al número decimal 2, ya que el 
   dígito más significativo es una potencia de 2 elevada a 1 (2^1) y el menos significativo es una potencia de 2 elevada a 0 (2^0)'''
# In[29]:





# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# print (2 + '2')

''' La operación 2 + '2' no está permitida en Python porque intenta sumar un número entero (int) y una cadena de texto (str). 
    Python no permite la concatenación entre estos dos tipos de datos de manera directa porque no tiene un comportamiento claro qué hacer con el resultado.
    
    El resultado depende del tipo de los operandos. Python permite el operador '+' para sumar números y para concatenar cadenas, pero no entre diferentes tipos, 
    porque esto puede ser confuso.'''

# In[23]:






# 26) Realizar una operación válida entre valores de tipo entero y string
entero = 3
texto = " es un número entero"
resultado = str(entero) + texto  
print(resultado)


# In[30]:




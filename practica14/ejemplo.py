import re

#patron para buscar un codigo postal de 5 digitos al principio de una cadena utilizando match

# pattern = re.compile(r"^\d{5}")

# text = "12345 san Miguel, san miguel"
# resultado = pattern.match(text)

# if resultado :
#     print(f"Coniciedencia encontrada {resultado.group()}")

# else:
#     print("No hay conicendias")

# /////////////////////////////////////////////////////////////////////////////////////

# PATRON PARA ENCONTRAR UNA PALABRA QUE LLEVE "PYTHON"

# pattern = re.compile(r"\bpython\w*" , re.IGNORECASE)

# text = "python es un lenguaje de programacion poderoso"
# resultado = pattern.search(text)

# if resultado:
#     print(f"Coincidencia encontrada en cualquier lugar de : {resultado.group()}")
# else:
#     print("No hay coincidencias encontradas")

# /////////////////////////////////////////////////////////////////////////////////////

# PATRON PARA BUSCAR TODAS LAS PALABRAS DE 2 LETRAS

# pattern = re.compile(r"\b\w{2}\b")

# text = "hola, soy un text con algunas palabras cortas"
# resultado = pattern.findall(text)

# print("Todas las coicidencias encontradas: ")
# for palabra in resultado:
#     print(palabra)

# /////////////////////////////////////////////////////////////////////////////////////

# PATRON PARA ENCONTRAR TODAS LAS DIRECCIONES DE CORREO EN UN TEXTO

pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

text = "Contacto conmigo en correo@example.com o en otro.correo@dominio.com"
resultado = pattern.finditer(text)

print("Direcciones de correo electronico encontrados: ")
for match in resultado:
    print(match.group())
texto = "hola Mundo"
print(texto.upper())
print(texto.lower())
print(texto.find("Mun"))
print(texto.find("mun"))
nuevoTexto = texto.replace("Mun","prueba")
print(texto, nuevoTexto)
print("Mundo" in texto)
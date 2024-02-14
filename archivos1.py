from io import open

archivo_texto = open('nombres.txt', 'r',)

# archivo_texto.write('\n datos en el archivo')
# archivo_texto.close()

for linea in archivo_texto.readlines():
    print(linea.rstrip())

archivo_texto.close()

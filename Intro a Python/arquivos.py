# arq = open('arquivo.txt', 'w')
#
# texto = '''
#     Aprendendo python
#     Gledson CArvalho
# '''
# with open('arquivo.txt', 'w') as f:
#     f.write(texto)
#     f.close()

with open('dataset.txt', 'r') as f:
    lista = f.read().splitlines()
    print(len(lista))

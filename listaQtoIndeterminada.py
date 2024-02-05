lista = [] # Lista zerada
# Uso loop while para adicionar quantas indormações desejar
while True:
    nome = input('Digite um novo nome (ou sair para finalizar)').lower()
    lista.append(nome) # Adiciona dados inseridos
   
    if nome.lower() == 'sair': # Comando para sair do programa
        break
        
lista.remove('sair') # Remove o 'sair', já que é um comando que acaba sendo adicionado a lista
print(lista)
print('CADASTRO FINALIZADO')
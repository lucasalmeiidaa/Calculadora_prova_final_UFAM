#Verificador de nota UFAM: Você precisa de nota final?
print("\n\n################### VERIFICADOR DE NOTA FINAL ###################")

#Número de provas parciais na matéria.
numero_provas = int(input("\n\nQuantas provas parciais a matéria tem?\n"))

#Variável que armazena as notas separadas por vírgular
notas = input("\nInsira as notas separadas por vírgula sem espaço ({}):\n"
    .format("use pontos para decimais"))
#Transforma as notas em lista
notas_str = notas.split(",")

#Loop se a qtd de notas repassadas não for igual à qtd de notas informadas
while len(notas_str) is not numero_provas:
    print("\n# Você precisa insesir o mesmo número de notas que de provas. #")
    numero_provas = int(input("\nQuantas provas parciais a matéria tem?\n"))
    notas = input("\nInsira as notas separadas por vírgula:\n")
    notas_str = notas.split(",")

#Transforma em float os elementos da lista de notas
notas_str = list(map(float, notas_str))

#Cáculo de acordo com as regras da UFAM (CADA UNIVERSIDADE TEM A SUA)
media_exercicios = (sum(notas_str)/numero_provas)

if media_exercicios >= 8.0:
    print("\nVocê passou sem final!! Parabéns!\n")
elif media_exercicios >= 7.5 and media_exercicios < 8.0:
    print("\nVocê passou sem final, porém com a média {}"
        .format((media_exercicios * 2)/3))
elif media_exercicios < 7.5:
    #Calcula-se quanto falta para atingir a média
    pf = 15 - (media_exercicios * 2)
    print("\nVocê ainda precisa de {} na final.".format(pf))

input("\nAperte enter para fechar...") #Para fechar prompt do .exe

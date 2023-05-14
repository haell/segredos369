# Título do programa e descrição das curiosidades
def titulo_quadro():
    segredo = '{:-^82}'.format("> SEGREDO 3 6 9 <")
    print(segredo)
    barra = '\033[32m|\033[m'
    traço = '\033[32m-\033[m'*80
    print(f"""{barra}{traço}{barra}
{barra} Sempre que multiplicamos um número, maior que 9, por 3, 6 ou 9                 {barra}
{barra} e depois somamos os algarismos do resultado, sempre resultará em 3, 6 ou 9.    {barra}
{barra}{traço}{barra}
{barra} Outra curiosidade é que, cada vez que aumentamos o número em +1, esse cálculo  {barra}
{barra} acaba trazendo um padrão nos resultados.                                       {barra}
{barra}{traço}{barra}
{barra} O padrão se mantém imutável: 3, 6 e 9, depois 6, 3 e 9, e por último 9, 9 e 9. {barra}
 {traço}
""")

# Chamando cabeçalho
titulo_quadro()

# Definição da função que calcula a soma dos dígitos de um número
def soma_produto(produto_da_multiplicação):
    soma = 0
    while produto_da_multiplicação > 0: 
        soma += produto_da_multiplicação % 10
        produto_da_multiplicação //= 10
    return soma

# Loop para receber o número digitado pelo usuário. Deve ser inteiro e maior que 9.5+9526
chave = False
while chave == False:
    num = input("Digite um número INTEIRO maior que 9: ")
    if num.isnumeric() == True:
        if int(num) <= 9:
            print("\033[36m\nValor baixo!\033[m\n")
        elif int(num) > 9:
            chave = True
    else:
        print("\033[31mn\nValor inválido!\033[m\n")        

# Verifica se o número é diferente de zero e executa o cálculo
if int(num) != 0:
    segredo = (3, 6, 9)
    for n in segredo:
        # Multiplica o número digitado por 3, 6 e 9
        produto_da_multiplicação = n*int(num)
        print(f"{n} X {int(num)} = {produto_da_multiplicação}")
        
        # Calcula a soma dos dígitos do resultado da multiplicação
        resultado = soma_produto(produto_da_multiplicação)
        print(f"Soma dos dígitos: {resultado}")
        
        # Verifica se a soma dos dígitos é maior que 9 e calcula novamente se for o caso
        if resultado > 9:
            resultado = soma_produto(resultado)
            print(f"Soma dos dígitos do resultado: {resultado}")
            if resultado > 9:
                resultado = soma_produto(resultado)
                print(f"Soma dos dígitos do resultado do resultado: {resultado}")
        print(" ")
else:
    print("Fim do Programa!")

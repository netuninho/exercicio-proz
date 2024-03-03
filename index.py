import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                print("Ano de nascimento fora do intervalo válido. Por favor, tente novamente.")
            else:
                return ano_nascimento
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    
    print(f"Olá, {nome_completo}!")
    print(f"Você completou ou completará {idade} anos em 2024.")

if __name__ == "__main__":
    main()

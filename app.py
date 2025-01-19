import os

def exibir_nome_programa():
    print('Calculadora de Gorjeta')

def valor_da_conta():
    valor_conta = float(input('Qual é o valor total da compra? R$ '))
    return valor_conta

def escolher_gorjeta():
    while True:
        print('Escolher gorjeta:')
        print('[1] 15%')
        print('[2] 18%')
        print('[3] 20%')
        print('[4] 0% (não oferecer gorjeta)')
        try:
            escolha_gorjeta = int(input('Quanto gostaria de dar de gorjeta? '))
            if escolha_gorjeta in [1, 2, 3, 4]:  # Se a opção for válida, sai do loop
                return escolha_gorjeta
            else:
                print("\nOpção inválida! Tente novamente.\n")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número de 1 a 4.")


def calcular_gorjeta(valor_conta, escolha_gorjeta):
    if escolha_gorjeta == 1:
        return valor_conta * 0.15
    elif escolha_gorjeta == 2:
        return valor_conta * 0.18
    elif escolha_gorjeta == 3:
        return valor_conta * 0.20
    elif escolha_gorjeta == 4:
        return 0
    
def main():
    os.system('cls')  
    exibir_nome_programa()  
    
    valor_conta = valor_da_conta()  
    escolha_gorjeta = escolher_gorjeta()  
    
    gorjeta = calcular_gorjeta(valor_conta, escolha_gorjeta)  
    
    
    total = valor_conta + gorjeta
    
    
    print(f'\nValor da conta: R$ {valor_conta:.2f}')
    print(f'Gorjeta escolhida: R$ {gorjeta:.2f}')
    print(f'Total a pagar: R$ {total:.2f}')


if __name__ == "__main__":
    main()

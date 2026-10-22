#Valor do produto de acordo com as formas de pagamento disponíveis
print('-=-' * 25)
valor = float(input('Valor do produto: R$'))
pagamento = int(input('\n1- À vista no dinheiro/cheque \n2- À vista no cartão \n3- 2x no cartão \n4- 3x ou mais no cartão \n\nQual a forma de pagamento escolhida: '))
print('-=-' * 25)
if pagamento == 1:
    print('O valor total a ser pago será de \033[1;32mR${:.2f}\033[m'.format(valor - (valor * 0.1)))
elif pagamento == 2:
    print('O valor total a ser pago será de \033[1;32mR${:.2f}\033[m'.format(valor - (valor * 0.05)))
elif pagamento == 3:
    print('O valor total a ser pago será de \033[1;32mR${:.2f}\033[m'.format(valor))
    print('Pagamento em duas parcelas de \033[1;32mR${:.2f}\033[m'.format(valor / 2))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas == 2:
        print('O valor total a ser pago será de \033[1;32mR${:.2f}\033[m'.format(valor))
        print('Pagamento em duas parcelas de \033[1;32mR${:.2f}\033[m'.format(valor / 2))
    else:
        mensal = (valor + (valor * 0.2)) / parcelas
        print('O valor total a ser pago COM JUROS será de \033[1;32mR${:.2f}\033[m'.format(valor + (valor * 0.2)))
        print('As parcelas serão de \033[1;32mR${:.2f}\033[m em {:.0f} vezes'.format(mensal, parcelas))
else:
    print('\033[1;31mOpção inválida\033[m')
print('-=-' * 25)
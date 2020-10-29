#CADASTRO (em modo de lista)
codigo_produtos = ['001', '002', '003']
nome_produtos = ['BONE NEW ERA SNAPBACK PRETO - TAM REGULAVEL', 'TENIS NIKE AIR MAX 90 - TAM 41', 'BIQUINI DE PRAIA ROSA - TAM M']
preco_produtos = [50.00, 399.99, 25.99]

#TERMINAL (tela do cliente)
nome_loja = ("Magazine do Marcao")
print("                                          ")
print("MAGAZINE DO MARCAO - E-COMMERCE DE QUALIDADE")
print("                                          ")
nome_cliente = input("POR FAVOR, NOS DIGA SEU NOME:")
email_cliente = input("QUAL O SEU E-MAIL?:")
print("Olá Sr(a). " + nome_cliente + ", oque você deseja comprar hoje?")
print("Temos disponíveis os seguintes produtos:"
produto = input("DIGITE O CODIGO DO PRODUTO: ")
codigo_produto_checkout = codigo_produtos.index(produto)
print("VOCÊ ESCOLHEU: " + nome_produtos[codigo_produto_checkout] + " ")
preco = preco_produtos[codigo_produto_checkout]
impostos = (preco * 0.1)
total = (preco + impostos)
print("Estamos processando sua compra...")
print("Calculando impostos...")
print("-------------------------------")
print("TOTAL: R$ " + str(total) + " ")
print("-------------------------------")
print("                               ")
import random
random_id = random.sample(range(100,500 ), 1)
print('O código de sua compra foi: ' + str(random_id)+ ', utilize esse ID único para qualquer troca posterior na loja.')
print("                ")
print("Obrigado por comprar na " + nome_loja + ", volte sempre!")


#CONFIRMAÇÃO (envia um email confirmando a compra para a equipe de logistica separar o produto)


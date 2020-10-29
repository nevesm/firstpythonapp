#CADASTRO (em modo de lista)
codigo_produtos = ['001', '002', '003', '004', '005', '006']
nome_produtos = ['BONÉ NEWERA SNAPBACK|PRETO|TAM REGULAVEL| COD: 001', 'TENIS NIKE AIR MAX 90|AZUL|TAM 41| COD: 002', 'BIQUINI DE PRAIA|ROSA|TAM M| COD: 003', 'SHORT DE PRAIA|AZUL-MARINHO|TAM 46| COD: 004', 'CALÇA JEANS|PRETA|TAM 48| COD: 005', 'CHINELO HAVAIANAS|BRANCO|TAM 39| COD: 006']
preco_produtos = [48.80, 399.99, 25.99, 27.00, 40.50, 32.00]

#TERMINAL (tela do cliente)
nome_loja = ("Magazine do Marcao")
print("                                          ")
print("MAGAZINE DO MARCAO - E-COMMERCE DE QUALIDADE")
print("                                          ")
nome_cliente = input("Por favor, nos diga seu nome: ")
email_cliente = input(nome_cliente + " Por favor, digite seu e-mail: ")
print("Olá Sr(a). " + nome_cliente + ", oque você deseja comprar hoje? Temos os seguintes produtos disponíveis:")
print(" ")
print(*nome_produtos, sep = "\n")
print(" ")
produto = input("Digite o código do produto correspondente: ")
if produto in codigo_produtos:
 codigo_produto_checkout = codigo_produtos.index(produto)
 print("Você escolheu: " + nome_produtos[codigo_produto_checkout] + " ")
 import time
 time.sleep(2)  # Sleep for 2 seconds
else:
  print("Produto não encontrado, escolha outro... (Sua conexão será fechada na proxima tentativa errada)")
  produto = input("Digite o código do produto correspondente: ")
  codigo_produto_checkout = codigo_produtos.index(produto)
  print("Você escolheu: " + nome_produtos[codigo_produto_checkout] + " ")

confirmacao = input("Deseja continuar sua compra? Digite 'Sim' para COMPRAR: ")
if confirmacao == str("Sim"):
 preco = preco_produtos[codigo_produto_checkout]
 impostos = (preco * 0.1)
 total = (preco + impostos)

else :
 print("Sua compra foi cancelada, por favor escolha outro produto... (Sua conexão será fechada na proxima tentativa errada)")
 produto = input("Digite o código do produto correspondente: ")
 codigo_produto_checkout = codigo_produtos.index(produto)
 print("Você escolheu: " + nome_produtos[codigo_produto_checkout] + " ")
 confirmacao = input("Deseja continuar sua compra? Digite 'Sim' para COMPRAR: ")

if confirmacao == str("Sim"):
 preco = preco_produtos[codigo_produto_checkout]
 impostos = (preco * 0.1)
 total = (preco + impostos)
 print("Estamos processando sua compra...")

else : print("Sua compra foi cancelada, fechando conexão!")


time.sleep(1)  # Sleep for 1 seconds

print("O valor do produto é: R$ " + ("%.2f" % preco))
time.sleep(1)  # Sleep for 1 seconds
print("Calculando impostos...")
time.sleep(1)  # Sleep for 1 seconds
print("Você está pagando: R$ " + ("%.2f" % impostos) + " em impostos.")
time.sleep(2)  # Sleep for 2 seconds
print(" ")
print("-------------------------------")
print("TOTAL: R$ " + ("%.2f" % total) + " ")
print("-------------------------------")
print("                               ")
import random
id_compra = random.sample(range(100,500 ), 1)
print('O código de sua compra foi: ' + str(id_compra)+ ', utilize esse ID único para qualquer troca posterior na loja.')
print("                ")
print("Fique tranquilo, enviamos um e-mail para: " +email_cliente + " com o resumo da sua compra!")
print("Obrigado por comprar na " + nome_loja + ", volte sempre!")


#CONFIRMAÇÃO (Envia um e-mail para o cliente confirmando a compra)

from mail import sender_email
from mail import password
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart("alternative")
message["Subject"] = "Compra efetuada! - PEDIDO: " + str(id_compra) + " - Magazine do Marcao"
message["From"] = sender_email
message["To"] = email_cliente

# Create the plain-text and HTML version of your message
text = "Olá, você acabou de comprar no nosso site https://magazinedomarcao.azurewebsites.net\n" \
       "Se você recebeu este e-mail significa que tudo ocorreu corretamente!\n"\
       "O seu " + nome_produtos[codigo_produto_checkout] + " já está sendo preparado para envio, agora é só aguardar!!\n"\
       "Seu código de compra é: " + str(id_compra) + " utilize para qualquer assunto relacionado à esse pedido.\n"
'OFF: Obrigado por testar meu app :)\n' \
 \
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, email_cliente, message.as_string()
    )
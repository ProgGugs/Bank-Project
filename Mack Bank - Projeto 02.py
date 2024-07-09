# Bibliotecas
import random
import smtplib 
import email.message
# Variáveis de controle
valor_inicial = 0
valor_saldo = 0
cadastro_unico = 0
recuperacao_unica = 0
contador_senha = 2
# Listas de controle 
lista_saque = []
lista_deposito = []

# Definição da função de menu
def menu():
  print("MACK BANK – ESCOLHA UMA OPÇÃO")
  print("(1) CADASTRAR CONTA CORRENTE")
  print("(2) DEPOSITAR")
  print("(3) SACAR")
  print("(4) CONSULTAR SALDO")
  print("(5) CONSULTAR EXTRATO")
  print("(6) FINALIZAR")
  opcao = int(input("SUA OPÇÃO: "))
  # Validação se o número digitado faz parte das opções disponíveis
  global cadastro_unico 
  while cadastro_unico == 0:
    while opcao != 1:
      if opcao > 1 and opcao <= 6:
        print ("Cadastro ainda não foi realizado")
        opcao = int(input("SUA OPÇÃO: "))
      elif not(opcao >= 1 and opcao <= 6):
        print ("Este número não pertence as opções acima")
        opcao = int(input("SUA OPÇÃO: "))
    cadastro_unico = cadastro_unico + 1
    cadastro()
 
  if opcao == 1:
      print("Cadastro já realizado!")
      menu()
  elif opcao == 2:
      deposito()
  elif opcao == 3:
      saque()
  elif opcao == 4:
      saldo()
  elif opcao == 5:
      extrato()
  elif opcao == 6:
      finalizacao()
  else: 
     print ("Este número não pertence as opções acima")
     menu()

# Definindo a função do menu limitado
def menu_limitado():
  print("MACK BANK – ESCOLHA UMA OPÇÃO")
  print("(1) CADASTRAR CONTA CORRENTE")
  print("(2) DEPOSITAR")
  print("(3) SACAR")
  print("(4) CONSULTAR SALDO")
  print("(5) CONSULTAR EXTRATO")
  print("(6) FINALIZAR")
  print ("(7) RECUPERAR ACESSO")
  opcao = int(input("SUA OPÇÃO: "))
  # Validação se o número digitado faz parte das opções disponíveis
  # O usuário será direcionado para a função correspondente a sua escolha
  # Porém com algumas limitações
  global recuperacao_unica
  if opcao >= 1 and opcao <= 7:
    if opcao == 1:
      print("Cadastro já realizado!")
      menu_limitado()
    elif opcao == 2:
      deposito()
    elif opcao == 3:
      print("Não é possível realizar saques no momento!")
      menu_limitado()
    elif opcao == 4:
      print("Não é possível consultar saldo no momento!")
      menu_limitado()
    elif opcao == 5:
      print("Não é possível consultar o extrato no momento!")
      menu_limitado()
    elif opcao == 6:
      finalizacao()
    elif opcao == 7:
      while recuperacao_unica == 0:
        recuperacao_unica = recuperacao_unica + 1
        recuperar_acesso()
      print("Não é possível recuperar a senha!")
      menu_limitado()
    else: 
      print ("Este número não pertence as opções acima")
      menu_limitado()


# Definição da função de cadastro da conta
def cadastro():
  print("MACK BANK – CADASTRO DE CONTA")

  # Lista de controle do cadastro é definida dentro da função "cadastro"
  # como global para podermos utilizar seus elementos em outras funções
  global lista_cadastro
  lista_cadastro = []

  # Usando o "import random", serão gerados 4 números aleatórios para o número da conta
  num_conta = []
  for i in range (4):
    num = random.randrange (0,9)
    num = str(num)
    num_conta.append (num)
  num_conta_str = ''.join(num_conta)
  print("NÚMERO DA CONTA:", num_conta_str)

  lista_cadastro.append (num_conta_str)

  nome = input("NOME DO CLIENTE: ")
  # O nome não pode ser uma string vazia ou conter um único caracter de espaço
  while nome == "" or nome == " ":
    print ("É necessário o preenchimento do nome!")
    nome = input("NOME DO CLIENTE: ")

  lista_cadastro.append(nome)

  telefone = input("TELEFONE: ")
  # O telefone não pode ser uma string vazia ou conter um único caracter de espaço
  while telefone == "" or telefone == " ":
    print ("É necessário o preenchimento do telefone!")
    telefone = input("TELEFONE: ")

  lista_cadastro.append(telefone)

  email = input("EMAIL: ")
  # O email não pode ser uma string vazia ou conter um único caracter de espaço
  while email == "" or email == " ":
    print ("É necessário o preenchimento do email!")
    email = input("EMAIL: ")

  lista_cadastro.append(email)

  # A variável "valor_inicial" é definida dentro da função "cadastro"
  # como global para podermos utilizar seu valor em outras funções
  global valor_inicial
  valor_inicial = float(input("SALDO INICIAL: "))
  # O saldo inicial não pode ser menor que 1000 reais
  while valor_inicial < 1000:
    print ("Saldo inicial inválido!\nO valor não pode ser menor que 1000 reais")
    valor_inicial = float(input("SALDO INICIAL: "))

  global valor_saldo
  valor_saldo = valor_inicial

  lista_cadastro.append(valor_inicial)

  global limite_credito
  limite_credito = float(input("LIMITE DE CRÉDITO: "))
  # O limite de crédito não pode ser negativo
  while limite_credito < 0:
    print ("Limite de crédito inválido!")
    limite_credito = float(input("LIMITE DE CRÉDITO: "))

  lista_cadastro.append(limite_credito)

  global senha
  senha = input("SENHA: ")
  # A senha não pode ser menor ou maior que 6 dígitos
  while len(senha) != 6:
    print("Senha inválida!\nO número da senha deve conter exatamente 6 caracteres")
    senha = input("SENHA: ")

  lista_cadastro.append(senha)

  repita_senha = input("REPITA A SENHA: ")
  # A confirmação da senha não pode ser diferente da senha cadastrada
  while repita_senha != senha:
    print("Senha diferente")
    repita_senha = input("REPITA A SENHA: ")
  
  # Essas são algumas perguntas com respostas únicas que servirão para uma futura recuperação de senha
  print("PERGUNTAS PARA FUTURA RECUPERAÇÃO DE ACESSO")
  pergunta1 = input("QUAL É SUA CIDADE NATAL: ")
  pergunta2 = input("QUAl SUA COR FAVORITA: ")
  pergunta3 = input("EM QUE ESCOLA VOCÊ COMPLETOU O ENSINO MÉDIO: ")

  lista_cadastro.append(pergunta1)
  lista_cadastro.append(pergunta2) 
  lista_cadastro.append(pergunta3)

  input("CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU: ")
  menu() # Chama a função "menu"

# Definicção da função de depósito
def deposito():
  conta = input("INFORME O NÚMERO DA CONTA: ")
  # Validação do número da conta digitado
  if conta == lista_cadastro[0]: 
    print ("NOME DO CLIENTE:", lista_cadastro[1])
  else: 
    while conta != lista_cadastro[0]:
      print ("Número da conta não condiz com o cadastrado")
      conta = input("INFORME O NÚMERO DA CONTA: ")
    print("NOME DO CLIENTE:", lista_cadastro[1])

  valor_deposito = float(input("VALOR DO DEPÓSITO: "))
  while valor_deposito <= 0:
    print ("Valor de depósito inválido\nO depósito não pode ser menor ou igual a 0")
    valor_deposito = float(input("VALOR DO DEPÓSITO: "))

  # Incrementa o valor do depósito no "valor_saldo" de todos os depósitos
  # E na "lista_deposito" de controle de todos os depósitos feitos
  global valor_saldo
  valor_saldo = valor_saldo + valor_deposito 
  global lista_deposito
  lista_deposito.append (valor_deposito)
  print("DEPÓSITO REALIZADO COM SUCESSO!")
  if contador_senha != 0:
     menu() # Chama a função "menu"
  else:
    menu_limitado()


# Definicção da função de saque
def saque():
  # Variáveis globais que serão utlizadas
  global valor_saldo
  global lista_saque
  global limite_credito
  conta = input("INFORME O NÚMERO DA CONTA: ")
  if conta == lista_cadastro[0]:
      print("NOME DO CLIENTE:", lista_cadastro[1])
  else:
      while conta != lista_cadastro[0]:
          print("Número da conta não condiz com o cadastrado")
          conta = input("INFORME O NÚMERO DA CONTA: ")
      print("NOME DO CLIENTE:", lista_cadastro[1])
  informe_senha = input("INFORME SENHA: ")
# Validação do saque será acionada, caso a senha esteja correta
  if informe_senha == senha:
    valor_saque = float(input("VALOR DO SAQUE: "))
    while valor_saque <= 0 or valor_saque > (valor_saldo + limite_credito):
      print("Valor de saque inválido!\nO saque não pode ser igual ou menor que 0\nE não pode exceder seu saldo e limite de crédito")
      valor_saque = float(input("VALOR DO SAQUE: "))
    if valor_saque > valor_saldo:
      limite_credito = limite_credito - (valor_saque - (valor_saldo))
      valor_saldo = 0
      print ("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")

      lista_saque.append(valor_saque)

      print("SAQUE REALIZADO COM SUCESSO!")
    else:
      valor_saldo = valor_saldo - valor_saque

      lista_saque.append(valor_saque)

      print ("SAQUE REALIZADO COM SUCESSO!")
  else:
# Caso a senha seja digitada errada, o usuário terá mais duas tentativas
    global contador_senha
    contador_senha = 2
    while contador_senha != 0:
      print("A senha inválida!\nVocê ainda possui {} tenativas".format(contador_senha))
      informe_senha = input("INFORME SENHA: ")
# Se a senha digitada novamente for a correta, o mesmo bloco de código de validação do saque será acionada
      if informe_senha == senha:
       valor_saque = float(input("VALOR DO SAQUE: "))
       while valor_saque <= 0  or valor_saque > (valor_saldo + limite_credito):
        print("Valor de saque inválido!\nO saque não pode ser igual ou menor que 0\nE não pode exceder seu saldo e limite de crédito")
        valor_saque = float(input("VALOR DO SAQUE: "))
       if valor_saque > valor_saldo:
        limite_credito = limite_credito - (valor_saque - (valor_saldo))
        valor_saldo = 0
        print (limite_credito)
        print ("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")

        lista_saque.append(valor_saque)

        print("SAQUE REALIZADO COM SUCESSO!")
        break
       else:
        valor_saldo = valor_saldo - valor_saque
        lista_saque.append(valor_saque)
        print("SAQUE REALIZADO COM SUCESSO!")
        break
      else:
       contador_senha = contador_senha - 1
# Controle de menus, caso a senha excedeu o limite de 3 tentativas
  if contador_senha == 0:
    print("Conta bloqueada para SAQUES e CONSULTAS de SALDO e EXTRATO ")
    menu_limitado()
  else: 
    menu()

# Definindo a função de consulta de saldo
def saldo():
  conta = input("INFORME O NÚMERO DA CONTA: ")
  if conta == lista_cadastro[0]:
    print("NOME DO CLIENTE:", lista_cadastro[1])
  else:
    while conta != lista_cadastro[0]:
       print("Número da conta não condiz com o cadastrado")
       conta = input("INFORME O NÚMERO DA CONTA: ")
    print("NOME DO CLIENTE:", lista_cadastro[1])
  informe_senha = input("INFORME SENHA: ")
  global contador_senha
  contador_senha = 2  # Tentativas restantes
  while informe_senha != senha and contador_senha > 0:
      print(f"Senha inválida! Você ainda possui {contador_senha} tentativas")
      informe_senha = input("INFORME SENHA: ")
      contador_senha -= 1
  if informe_senha == senha:
      print("SALDO: R$", valor_saldo)
      print("LIMITE DE CRÉDITO: R$", limite_credito)
      menu()
  else:
      print("Você excedeu a quantidade de tentativas")
      print("Conta bloqueada para SAQUES e CONSULTAS de SALDO e EXTRATO")
      menu_limitado()

# Definindo a função de consulta de extrato
def extrato():
  conta = input("INFORME O NÚMERO DA CONTA: ")
  if conta == lista_cadastro[0]:
      print("NOME DO CLIENTE:", lista_cadastro[1])
  else:
      while conta != lista_cadastro[0]:
          print("Número da conta não condiz com o cadastrado")
          conta = input("INFORME O NÚMERO DA CONTA: ")
      print("NOME DO CLIENTE:", lista_cadastro[1])
  informe_senha = input("INFORME SENHA: ")
  if informe_senha == senha:
      print("LIMITE DE CREDITO: R$", limite_credito)
      print("ÚLTIMAS OPERAÇÕES")
      for i in range(len(lista_deposito)):
        print("DEPÓSITOS: R$", lista_deposito[i])
      for i in range(len(lista_saque)):
        print("SAQUES: R$", lista_saque[i])
      print("SALDO: R$", valor_saldo)
  else:
      global contador_senha
      contador_senha = 2
      while contador_senha != 0:
          print("Senha inválida! Você ainda possui {} tentativas".format(contador_senha))
          informe_senha = input("INFORME SENHA: ")
          if informe_senha == senha:
             print("LIMITE DE CREDITO: R$", limite_credito)
             print("ÚLTIMAS OPERAÇÕES: ")
             for i in range(len(lista_deposito)):
                print("DEPÓSITOS: ", lista_deposito[i])
             for i in range(len(lista_saque)):
                print("SAQUES: ", lista_saque[i])
             print("SALDO: R$", valor_saldo)
             break
          contador_senha -= 1
      if contador_senha == 0:
          print("Você excedeu a quantidade de tentativas")
          print("Conta bloqueada para SAQUES e CONSULTAS de SALDO e EXTRATO")
          menu_limitado()
      else:
        menu()

def finalizacao():
  print("MACK BANK – AGRADECEMOS A PREFERÊNCIA!")
  print ("Programa desenvolvido por:\nGustavo Emerick dos Santos e Samuel Wenceslau Cardoso")
  exit()
  
def enviar_email():  
    corpo_email = """
    <p>Este é um email automático, não é necessário responder</p>
    <p>Sua nova senha de acesso é: 019473, faça de tudo para não esquecer dessa vez!</p>
    """
# Formatação do e-mail
    msg = email.message.Message()
    msg['Subject'] = "Recuperação de Senha"
    msg['From'] = 'gustavao784@gmail.com'
    msg['To'] = lista_cadastro[3]
    password = 'njwpckyeskbnirho' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

# Requisitos do Google para maior segurança
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

# Credenciais de Login
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# Definindo a função de recuperação de acesso
def recuperar_acesso():
  conta = input("INFORME O NÚMERO DA CONTA: ")
  # Validação do número da conta digitado
  if conta == lista_cadastro[0]: 
    print ("NOME DO CLIENTE:", lista_cadastro[1])
  else: 
    while conta != lista_cadastro[0]:
      print ("Número da conta não condiz com o cadastrado")
      conta = input("INFORME O NÚMERO DA CONTA: ")
    print("NOME DO CLIENTE:", lista_cadastro[1])

# Validação de recuperação de senha
  acertos = 0
  print("Agora responda as 3 perguntas de recuperação de senha\nSe houver 2 erros de resposta dentre as 3 perguntas\nNão será possível recuperar senha...")
  pergunta1 = input("QUAL É SUA CIDADE NATAL: ")
  if pergunta1 == lista_cadastro[-3]:
    acertos = acertos + 1
  pergunta2 = input("QUAl SUA COR FAVORITA: ")
  if pergunta2 == lista_cadastro[-2]:
    acertos = acertos + 1
  pergunta3 = input("EM QUE ESCOLA VOCÊ COMPLETOU O ENSINO MÉDIO: ")
  if pergunta3 == lista_cadastro[-1]: 
    acertos = acertos + 1
  if acertos <= 1:
    print("Não foi possível recuperar a senha, sua conta será bloqueada por tempo INDETERMINADO")
    menu_limitado()
  else:
    email = input("INFORME EMAIL CADASTRADO PARA RECUPEREAÇÃO DA SENHA: ")
    while email != lista_cadastro[3]:
      print("Este não é o email cadastrado")
      email = input("INFORME EMAIL CADASTRADO PARA RECUPEREAÇÃO DA SENHA: ")
    enviar_email()
    global senha
    senha = "019473"
    lista_cadastro[-4] = senha
    print("SENHA RECUPERADA COM SUCESSO!")
    global contador_senha
    contador_senha = 2
    menu()

# Início do código
menu()

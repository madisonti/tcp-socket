import socket


def cabecalho ():
   print('')
   print('')


   print('Olá! Este código faz uma requisição diretamente a uma URL alvo')
   print('')
   print('acessa uma porta, retornando a resposta de uma requisição ao servidor alvo.')
   print('')
   print('Digite sua URL: www.google.com / Digite a porta: 80')


   print('')
   print('')




cabecalho()




  
url = input("Digite sua URL: ")
porta = int(input("Digite a porta: "))


try:
  
   cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




   cliente.connect((url, porta))


  
   requisicao = f"GET / HTTP/1.1\r\nHost: {url}\r\n\r\n".encode('utf-8')
   cliente.send(requisicao)


  
   resposta = cliente.recv(4096)


   print('Resultado é:')
   print(resposta.decode('utf-8'))


except ValueError:
   print("Erro: A porta deve ser um número inteiro.")


except socket.gaierror:
   print("Erro: URL inválida ou não encontrada podera verificar o url tente o ping no cmd + url alvow.")


except ConnectionRefusedError:
   print("Erro: Conexão recusada. Verifique se o servidor está ativo podera usa o exemplo: ping 192.000.00.0  => ip alvo no cmd'.")
  
except Exception as m:
   print(f"Erro inesperado: {m}")
finally:
  
   try:
       cliente.close()
   except:
       pass

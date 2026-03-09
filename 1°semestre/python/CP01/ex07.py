#Peça um nome de usuário e uma senha. Se o usuário for "admin" e a senha "1234", exiba “Acesso permitido”; caso contrário, “Acesso negado”.

usuario_correto = "admin"
senha_correta = "1234"

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        print(f"Acesso negado.")

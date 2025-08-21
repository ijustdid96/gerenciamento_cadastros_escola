student_informations = []
suma = "K"
while True:
 print("    MENU PRINCIPAL    ")
 print("(1) Gerenciar estudantes.")
 print("(2) Gerenciar professores.")
 print("(3) Gerenciar disciplinas.")
 print("(4) Gerenciar turmas.")
 print("(5) Gerenciar matrículas.")
 print("(6) Sair.")
 while True:
  try:
    option = int(input("Digite a opção desejada: "))
  except ValueError:
     print("Valor inválido")
  except:
     print("Outro tipo de erro ocorreu!")
  else:
       break
 if option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6:
     print("A OPÇÃO SELECIONADA É INEXISTENTE!")
     continue
 if option == 2 or option == 3 or option == 4 or option == 5:
     print("EM DESENVOLVIMENTO...")
     continue
 if option == 6:
        break
 suma = "j"
 if option == 1:
    suma = "ESTUDANTES"
 while True:
  if option == 1:
         print( "(" + suma + ") MENU DE OPERAÇÕES")
         print("(1) INCLUIR.")
         print("(2) LISTAR.")
         print("(3) EDITAR.")
         print("(4) EXCLUIR.")
         print("(5) VOLTAR AO MENU PRINCIPAL.")
         try:
             opr = int(input("Digite a operação desejada: "))
         except ValueError:
             print("Valor inválido")
         except:
             print("Outro tipo de erro ocorreu!")
         if opr != 1 and opr != 2 and opr != 3 and opr != 4 and opr != 5:
             print("A OPÇÃO DIGITADA É INVÁLIDA.")
         if opr == 5:
             break
         if opr == 1:
             suma = "INCLUIR."
         if  opr == 2:
             suma = "LISTAR."
         if opr == 3:
             suma = "EDITAR."
         if opr == 4:
             suma = "EXCLUIR"
         print("OPERAÇÃO SELECIONADA (" + suma + ")")
         if opr == 1:
          while True:
           student_data = {}
           student_code = int(input("digite o código do estudante: "))
           if student_code in student_data.values():
              print("Este código de estudante já esta cadastrado.")
              if input("Deseja alterar o registro? ") == "s":
                  continue
           student_name = input("Digite o primeiro e o segundo nome do estudante: ")
           if student_name in student_data.values():
               print("Este nome já esta cadastrado.")
               if input("Deseja alterar o registro? ") == "s":
                   continue
           student_id = int(input("Digite o cpf do estudante: "))
           if student_id in student_data.values():
              print("Este cpf já esta cadastrado.")
              if input("Deseja alterar o registro? ") == "s":
                  continue
           student_data["codigo"] = student_code
           student_data["nome"] = student_name
           student_data["cpf"] = student_id
           student_informations.append(student_data)
           if input("Deseja cadastrar um novo estudante(s/n)? ") == "n":
               break
           print("Dados cadastrados com sucesso.")
         if opr == 2:
             if len(student_informations) == 0:
                 print("Não há dados cadastrados no sistema.")
             elif len(student_informations) > 0:
              for i in student_informations:
               print(i)
         if opr == 3:
             add = int(input("Digite o código do estudante: "))
             for student_data in student_informations:
                 if student_data["codigo"] == add:
                     student_data["código"] = int(input("Digite o código do estudante: "))
                     student_data["nome"] = input("Digite o nome do estudante: ")
                     student_data["cpf"] = int(input("Digite o cpf do estudante: "))
         if opr == 4:
            delete_student = None
            delete = int(input("Digite o código do estudante: "))
            for student_data in student_informations:
                if student_data["codigo"] == delete:
                 delete_student = student_data
                 student_informations.remove(student_data)
print("Sua sessão foi encerrada.")

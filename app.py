from Tarefas import CriarTarefa,ExibirQtdTarefa, ConsultarTarefaPorID
QtdTarefa = 0
ListaDeTarefas = []
#Fim das variáveis.
while(True):
    Acao = input("O que você quer fazer? ")
    # print(Acao)
    # print(Acao.lower())
    if Acao.lower() == "criar":
        print("Criando uma tarefa")
        QtdTarefa= CriarTarefa(QtdTarefa,ListaDeTarefas) # Foi uma criada uma var e o valor dela corresponde ao return do Criar Tarefa.

    elif Acao.lower() == "detalhe":
        print("Consultando tarefa")
        ExibirQtdTarefa(ListaDeTarefas,QtdTarefa)

    elif Acao.lower() == "sair":
        print("Você saiu")
        break

    elif Acao.lower() == "consulta":
        TarefaID = int(input("Qual Tarefa ID você quer consultar ?"))
        print(ConsultarTarefaPorID(ListaDeTarefas,TarefaID))
        
    else: 
        print("Digite uma ação válida ")



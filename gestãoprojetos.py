# ===============================
# Sistema de Gestão de Projetos de Extensão
# UFCD:  Programação em Python
# ===============================

projetos = {}
nomes_projetos = set()


def adicionar_projeto():
    print("\n=== Adicionar Novo Projeto ===")
    nome = input("Nome do projeto: ").strip()
    
    if nome in nomes_projetos:
        print("Projeto já existe. Escolha outro nome.")
        return
    
    try:
        inscricoes = int(input("Número de inscrições: "))
        duracao = int(input("Duração em horas: "))
        valor = float(input("Valor por inscrição: "))
    except ValueError:
        print("Erro: insira valores numéricos válidos.")
        return

    projetos[nome] = {
        'inscricoes': inscricoes,
        'duracao': duracao,
        'valor': valor
    }
    nomes_projetos.add(nome)
    print(f"Projeto '{nome}' adicionado com sucesso.")


def ver_detalhes():
    print("\n=== Ver Detalhes de um Projeto ===")
    nome = input("Nome do projeto: ").strip()
    
    if nome in projetos:
        dados = projetos[nome]
        print(f"Projeto: {nome}")
        print(f"Inscrições: {dados['inscricoes']}")
        print(f"Duração: {dados['duracao']} horas")
        print(f"Valor por inscrição: €{dados['valor']:.2f}")
    else:
        print("Projeto não encontrado.")


def listar_projetos():
    print("\n=== Lista de Projetos ===")
    if not projetos:
        print("Nenhum projeto registrado.")
        return
    for nome in nomes_projetos:
        print(f"- {nome}")


def remover_projeto():
    print("\n=== Remover Projeto ===")
    nome = input("Nome do projeto a remover: ").strip()
    
    if nome in projetos:
        projetos.pop(nome)
        nomes_projetos.remove(nome)
        print(f"Projeto '{nome}' removido com sucesso.")
    else:
        print("Projeto não encontrado.")


def calcular_receita_total():
    print("\n=== Receita Total Esperada ===")
    total = 0.0
    for dados in projetos.values():
        receita = dados['inscricoes'] * dados['valor']
        total += receita
    print(f"Receita total esperada: €{total:.2f}")


def menu():
    while True:
        print("\n==== Sistema de Gestão de Projetos ====")
        print("1. Adicionar Novo Projeto")
        print("2. Ver Detalhes de um Projeto")
        print("3. Listar Todos os Projetos")
        print("4. Remover um Projeto")
        print("5. Calcular Receita Total")
        print("6. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            adicionar_projeto()
        elif escolha == '2':
            ver_detalhes()
        elif escolha == '3':
            listar_projetos()
        elif escolha == '4':
            remover_projeto()
        elif escolha == '5':
            calcular_receita_total()
        elif escolha == '6':
            print("A encerrar o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

import os

# Caminho do arquivo onde as tarefas serão salvas
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Carrega as tarefas do arquivo."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Salva as tarefas no arquivo."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def list_tasks(tasks):
    """Exibe a lista de tarefas."""
    if not tasks:
        print("\nNenhuma tarefa encontrada.")
        return
    print("\nSuas tarefas:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    """Adiciona uma nova tarefa."""
    task = input("Digite a nova tarefa: ").strip()
    if task:
        tasks.append(task)
        print(f"\nTarefa '{task}' adicionada com sucesso!")
    else:
        print("\nA tarefa não pode ser vazia.")

def remove_task(tasks):
    """Remove uma tarefa pelo número."""
    try:
        list_tasks(tasks)
        index = int(input("\nDigite o número da tarefa a ser removida: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"\nTarefa '{removed}' removida com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nEntrada inválida. Por favor, insira um número.")

def main():
    """Função principal do programa."""
    print("Bem-vindo ao Gerenciador de Tarefas!")
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")

        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("\nSaindo... Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
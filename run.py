import subprocess

from main import cardsol_solver

subprocess.run("clear")
print(
    """
                   WELCOME TO CARDSOL USER INTERFACE 
                   help: enter 'run' to start optimization or 'exit' to quit cardsol
           """
)

while True:

    command = input("cardsol$ ")

    if command == "exit":
        break
    elif command == "run":
        n = int(input("numvar: "))
        cardsol_solver(n)
    else:
        continue

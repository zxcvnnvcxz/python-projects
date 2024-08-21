# from functions import get_todos, write_todos
import functions as f
import time as t

now = t.strftime("%b %d %Y, %H:%M:%S")
print("It is", now)

FILEPATH = './Files/todos.txt'
user_prompt = "Type add or show, edit, complete, or exit: "
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = f.get_todos()

        todos.append(todo + "\n")

        f.write_todos(todos)

    elif user_action.startswith('show'):
        todos = f.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = f.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            f.write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please enter a number.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no todo with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")

print("Bye")

import functions
import FreeSimpleGUI as sG
import time
import os

if not os.path.exists("./todos.txt"):
    with open("./todos.txt", "w") as file:
        pass

sG.theme("DarkPurple4")

clock = sG.Text('', key="clock")
label = sG.Text("Type in a to-do")
input_box = sG.InputText(tooltip="Enter todo", key="todo")
add_button = sG.Button("Add", key='Add', mouseover_colors='LightBlue2',
                       tooltip="Add Todo")

list_box = sG.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sG.Button("Edit")
complete_button = sG.Button("Complete")
exit_button = sG.Button("Exit")
output_label = sG.Text(key="output", text_color="red")

window = sG.Window('My To-Do App',
                   layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button, output_label]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=500)
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].strip() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip() + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                # window["output"].update(value="Please select an item first.")
                sG.popup("Please select an item first.", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                window["output"].update(value="Please select an item first.")
            except ValueError:
                window["output"].update(value="No item.")

        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0].strip())
            except IndexError:
                window["output"].update(value="No item.")
        case "Exit":
            break

        case sG.WIN_CLOSED:
            break

    window["clock"].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))


window.close()
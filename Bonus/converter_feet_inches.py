from convert9 import convert

import FreeSimpleGUI as gui

label1 = gui.Text("Enter feet: ")
label2 = gui.Text("Enter inches: ")

input_box1 = gui.Input(key="feet")
input_box2 = gui.Input(key="inches")

convert_button = gui.Button("Convert")
output_label = gui.Text(key="output")

window = gui.Window('Converter',
                    layout=[
                        [label1, input_box1],
                        [label2, input_box2],
                        [convert_button, output_label]
                    ])

while True:
    event, values = window.read()
    print(event, values)
    feet = int(values["feet"])
    inches = int(values["inches"])
    converted_number = str(convert(feet, inches)) + "m"
    window["output"].update(value=converted_number)
    match event:
        case gui.WIN_CLOSED:
            break

window.read()
window.close()
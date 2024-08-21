# File Zipper titled Window
# Select files to compress: # Choose Button, opens up file explorer, multi-select
# Select destination folder: # Choose Button, open up a directory
# Compress Button

import FreeSimpleGUI as gui

label1 = gui.Text("Enter feet: ")
label2 = gui.Text("Enter inches ")
input_box1 = gui.Input()
input_box2 = gui.Input()
compress = gui.Button("Convert")
compress_button = gui.Button("Compression was completed!")

window = gui.Window('File Zipper',
                    layout=[
                        [label1, input_box1],
                        [label2, input_box2],
                        [compress]
                    ])

window.read()
window.close()
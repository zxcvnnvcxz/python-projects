# File Zipper titled Window
# Select files to compress: # Choose Button, opens up file explorer, multi-select
# Select destination folder: # Choose Button, open up a directory
# Compress Button

import FreeSimpleGUI as gui

label1 = gui.Text("Select Files to compress: ")
label2 = gui.Text("Select Destination Folder: ")
input_box1 = gui.Input()
input_box2 = gui.Input()
choose_files = gui.FilesBrowse("Choose")
choose_location = gui.FolderBrowse("Choose")
compress = gui.Button("Compress")
compress_button = gui.Button("Compression was completed!")

window = gui.Window('File Zipper',
                    layout=[
                        [label1, input_box1, choose_files],
                        [label2, input_box2, choose_location],
                        [compress]
                    ])

while True:
    event, values = window.read()
    filepaths = values["Choose"]

window.read()
window.close()
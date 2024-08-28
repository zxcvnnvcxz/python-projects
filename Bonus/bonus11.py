from zip_creator import make_archive
import FreeSimpleGUI as gui

label1 = gui.Text("Select Files to compress: ")
label2 = gui.Text("Select Destination Folder: ")

input_box1 = gui.Input()
input_box2 = gui.Input()

choose_files = gui.FilesBrowse("Choose", key="files")
choose_location = gui.FolderBrowse("Choose", key="folder")

compress = gui.Button("Compress")
compress_button = gui.Button("Compression was completed!")
output_label = gui.Text(key="output", text_color = "yellow")

window = gui.Window('File Zipper',
                    layout=[
                        [label1, input_box1, choose_files],
                        [label2, input_box2, choose_location],
                        [compress, output_label]
                    ])

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")
    match event:
        case gui.WIN_CLOSED:
            break


window.close()


import zipfile


def extract_archive(archivepath,
                    dest_dir='/home/zxcv/Documents/Study/app1/pythonProject/Files/dest'):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/home/zxcv/Documents/Study/app1/pythonProject/Files/compressed.zip")

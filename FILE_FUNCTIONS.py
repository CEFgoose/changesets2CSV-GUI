from PyQt5.QtWidgets import *


def import_editor_json(main):
    files = QFileDialog.getOpenFileNames(main, main.filters, main.importDirectory, main.select_filters)[0]
    main.userFile=files[0]
    print(main.userFile)
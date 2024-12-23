from cx_Freeze import setup, Executable

# pip install cx_Freeze

# python setup.py build

setup(
    name = "имя",
    version = "0.1",
    description = "описание",
    # если приложение консольное то пишем - base=None
    # если приложение с графическим интерфейсом то пишем - base='Win32GUI'
    executables = [Executable("main.py" , base="Win32GUI" , icon="icon_py.ico")]
)

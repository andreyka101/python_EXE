from cx_Freeze import setup, Executable

# pip install cx_Freeze

# python setup.py build

setup(
    name = "hello",
    version = "0.1",
    description = "126525e fefef efe",
    # если приложение консольное то пишем - base=None
    # если приложение с графическим интерфейсом то пишем - base='Win32GUI'
    executables = [Executable("main.py" , base="Win32GUI" , icon="icon_py.ico")]
)

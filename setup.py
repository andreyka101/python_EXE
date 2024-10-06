from cx_Freeze import setup, Executable
# python setup.py build
# https://jenyay.net/Programming/Cxfreeze

setup(
    name = "убей меня",
    version = "0.1",
    description = "убей меня АААААА",
    # если приложение консольное то пишем - base=None
    # если приложение с графическим интерфейсом то пишем - base='Win32GUI'
    executables = [Executable("main.py", base=None, icon="il_fullxfull.4526746696_j9bu.ico")]
)





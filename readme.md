# создание EXE для python

устанавливаем cx_Freeze

``` bash
pip install cx_Freeze
```
создаем файл

``` bash
setup.py
```
в него пишем :

``` python
from cx_Freeze import setup, Executable

setup(
    name = "имя",
    version = "0.1",
    description = "описание",
    # если приложение консольное то пишем - base=None
    # если приложение с графическим интерфейсом то пишем - base='Win32GUI'
    executables = [Executable("main.py" , base="Win32GUI" , icon="icon_py.ico")]
)
```
<br/>
компилируем в exe

``` bash
python setup.py build
```




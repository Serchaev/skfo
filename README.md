# skfo

## Project setup only Linux
```
pip install -r req.txt
pip install nvidia-cublas-cu11 nvidia-cudnn-cu11

export LD_LIBRARY_PATH=`python3 -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))'`

pip install TTS
```
Для использования, необходимо создать в корне проекта папки work/, work/{назание_видео}, work/{назание_видео}/segments, my/, my/cloning. Итоговое видео будет лежать с тем же назанием в корне проекта.

В файле main необходимо передать путь к файлу, название файла (без расширения), язык.
Cписок названия целевых языков находится в файле config.txt
Для синтеза также необходимо указать язык в файле tts
Cписок названия целевых языков для синтеза находится в файле config2.txt

При первом прогоне будет скачано чуть больше 15 гигабайт моделей.

ссылка на яндекс диск - https://disk.yandex.ru/d/avi_XEyyYvPHAA



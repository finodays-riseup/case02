# case02 #
[Папка на Google Drive](https://drive.google.com/drive/folders/12OqkVQ42YCYHQQMJnAuJe5E4IsUGdgD9)

## Зависимости ##
```shell
pip install -r requirements.txt
```
## Модели ##
Модели сериализуются `pickle`. Пути к моделям определяются в `config/__init__.py`.
## Запуск ##
```shell
python -m api >>api.log 2>&1 &
./run_ui.py
```

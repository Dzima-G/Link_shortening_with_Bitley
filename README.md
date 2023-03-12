# Сокращение ссылок с помощью Битли

Приложение сокращает URL, выводит количество кликов по сокращенному URL.

### Как установить

Приложение работает из консольной утилиты. объясните пользователю, откуда брать ключи, куда их класть и как они выглядят]

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомедуется использовать [vittualenv/venv] (https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Применение
 Приложение работает из консольной утилиты.
```
\Link_shortening_with_Bitley> python main.py https://dvmn.org/
Битлинк: bit.ly/3yy3FM6
```
Отправьте параметры `-h` помощь.
```
\Link_shortening_with_Bitley> python main.py -h
usage: main.py [-h] url

Сокращает url и выводит количество кликов по сокращенному url

positional arguments:
  url         Ваш url

options:
  -h, --help  show this help message and exit
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

# Bookmarks Manager

## Опис проєкту
Bookmarks Manager — це простий веб-додаток для управління закладками. Користувачі можуть додавати, редагувати, видаляти закладки, а також організовувати їх за категоріями.

## Встановлення та запуск

### 1. Клонування репозиторію
```bash
git clone <https://github.com/derkachhhh/Bookmarks.git>
cd bookmarks_manager
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Create superuser
```bash
python manage.py createsuperuser
```
5. Run the server
```bash
python manage.py runserver
```
# <p style="text-align: center; color: red; font-size: 5rem;"> Django-CMS </p>

## <p style="text-align: center"> Installation </p>

1. `python3 -m venv .venv` erstellt eine virtuelle umgebung
2. `source .venv/bin/activate` (linux/macOS) `.venv\Scripts\activate` (Windows) aktiviert die virtuelle Umgebung
3. `pip install --upgrade pip` akutalisiert PIP
4. `pip install django-cms` installiert den Django Content-Manager

## <p style="text-align: center"> erstellen eines Projekts </p>

1.  `djangocms myproject` erstellt ein neues Projekt mit dem Namen "myproject"
2.  `pip install djangocms-frontend` um Bootstrap 5 zu verwenden
    - folgendes muss in den INSTALLED_APPS hinzu gefügt werden(ist vorhanden, aber prüfen):
      ```python
      'easy_thumbnails',
      'djangocms_frontend',
      'djangocms_frontend.contrib.accordion',
      'djangocms_frontend.contrib.alert',
      'djangocms_frontend.contrib.badge',
      'djangocms_frontend.contrib.card',
      'djangocms_frontend.contrib.carousel',
      'djangocms_frontend.contrib.collapse',
      'djangocms_frontend.contrib.content',
      'djangocms_frontend.contrib.grid',
      'djangocms_frontend.contrib.icon',
      'djangocms_frontend.contrib.image',
      'djangocms_frontend.contrib.jumbotron',
      'djangocms_frontend.contrib.link',
      'djangocms_frontend.contrib.listgroup',
      'djangocms_frontend.contrib.media',
      'djangocms_frontend.contrib.tabs',
      'djangocms_frontend.contrib.utilities',
      ```
3.  `cd myproject` um in den Projekt Ordner zu gelangen
4.  `CMS_CONFIRM_VERSION4 = True` überprüfe ob dass in der **settings.py** vorhanden ist
5.  run `python manage.py migrate`
6.  füge `"sekizai.context_processors.sekizai"` überprüfe ob es in der settings.py vorhanden ist (installed_apps und templates)
7.  `python -m manage runserver` um den Server zu starten

## <p style="text-align: center"> App erstellen </p>

- run `python manage.py startapp newApp`
- füge sie in den `ÌNSTALLED_APPS` hinzu:
  ```python
  INSTALLED_APPS = [
  ...
  'myapp',
  'djangocms_text_ckeditor',
  ...
  ]
  ```

## <p style="text-align: center"> Templates richtig erstellen </p>

## <p style="text-align: center"> Bilder einfügen </p>

1. Installiere `pip install djangocms-picture`
2. danach muss es auch in der `INSTALLED_APPS` in der **settings.py** registriert werden `djangocms_picture`
3. jetzt muss man erneut eine migration ausführen `python manage.py migrate`
4. danach kann man Bilder in der Django admin hochladen

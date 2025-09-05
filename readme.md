# Diario IA

Diario IA es una aplicación web de diario personal que permite a los usuarios crear, editar y eliminar entradas de diario, con la opción de ingresar texto mediante reconocimiento de voz. El proyecto está orientado a la práctica de desarrollo web con Python y Flask, integrando tecnologías modernas y una interfaz amigable.

## Tecnologías implementadas

- **Python 3**
- **Flask** (framework web)
- **Flask-SQLAlchemy** (ORM para SQLite)
- **HTML5 y CSS3** (interfaz y estilos)
- **Reconocimiento de voz** (speech recognition, mediante un módulo Python personalizado)
- **SQLite** (base de datos local)

## Características principales

- Registro e inicio de sesión de usuarios
- Creación, edición y eliminación de entradas de diario
- Visualización de todas las entradas
- Entrada de texto por voz (speech-to-text)
- Interfaz moderna y responsiva

## Instalación y ejecución

1. **Clona el repositorio:**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Diario-IA
   ```

2. **Instala las dependencias:**

   Se recomienda usar un entorno virtual. Puedes instalar las dependencias con pipenv:

   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```
   O usando pip y el archivo `Pipfile`/`Pipfile.lock`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicializa la base de datos:**

   Abre un intérprete de Python y ejecuta:
   ```python
   from main import db
   db.create_all()
   ```
   Esto creará el archivo `diary.db` en la carpeta `instance/`.

4. **Ejecuta la aplicación:**

   ```bash
   python main.py
   ```
   La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Notas adicionales

- El reconocimiento de voz requiere un micrófono y permisos en el navegador.
- Puedes personalizar los estilos en `static/css/style.css`.
- Las plantillas HTML están en la carpeta `templates/`.

## Estructura del proyecto

```
Diario-IA/
├── main.py
├── speech.py
├── Pipfile / Pipfile.lock
├── instance/
│   └── diary.db
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
├── templates/
│   ├── index.html
│   ├── card.html
│   ├── create_card.html
│   ├── login.html
│   └── registration.html
└── ...
```

## Licencia

Este proyecto es educativo y de libre uso.

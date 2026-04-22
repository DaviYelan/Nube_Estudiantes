# School CRUD — Django

CRUD de estudiantes y libros con Django + Bootstrap 5.

## Instalación local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Variables de entorno para producción

| Variable        | Descripción                       |
|-----------------|-----------------------------------|
| `SECRET_KEY`    | Clave secreta Django              |
| `DEBUG`         | `False` en producción             |
| `ALLOWED_HOSTS` | Dominio separado por espacios     |

## Despliegue en Railway

1. Sube el código a GitHub
2. Conecta Railway con el repositorio
3. Agrega las variables de entorno
4. Railway detecta el `Procfile` y despliega automáticamente

"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

# Auto-crear superusuario 'karma' al iniciar en Render
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='karma').exists():
        User.objects.create_superuser('karma', 'karmacastillo2017@gmail.com', '12345')
        print("Superusuario 'karma' creado automáticamente.")
except Exception as e:
    print(f"Nota auto-superuser: {e}")

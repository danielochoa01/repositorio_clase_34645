# Renderizar HTML

1. Primero, en la raiz de nuestro proyecto creamos una carpeta llamada ```templates```
    |-- Proyecto1
    |   |-- __init__.py
    |   |-- settings.py
    |   |-- urls.py
    |   -- wsgi.py
    |-- templates
    -- manage.py
2. En nuestro archivo __settings.py__, buscamos la lista ```TEMPLATES``` y en ```DIRS = []``` ponemos lo siguiente:
    ```DIRS = [BASE_URL, 'templates']```
3. En nuestro archivo ```views.py```, importamos el modulo render:
```from django.shortcuts import render```
4. Utilizamos render de la siguiente forma:
    ```
    def prueba_render(request):
        return render(response, 'plantilla a renderizar')
    ```
5. Incluimos nuestra vista en el archivo __urls.py__

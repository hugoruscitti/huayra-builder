# huayra-builder

huayra-builder es una aplicación web que permite
automatizar la generación de paquetes .deb
para la distribución huayra.

## Dependencias generales

Deberías tener instalado pip, virtualenv y redis.


## ¿Cómo instalar la aplicación?

El primer paso es crear un entorno virtual para
python y luego instalar las dependencias
así:

```
virtualenv venv
source venv/bin/activate
```

y una vez dentro del virtualenv, instalar las depenencias:

```
pip install -r requirements.txt
```

y por último, compilar la aplicación ember:

```
make compilar
```

Nota: Si estás usando fish mirá estas instrucciones antes:

- https://github.com/adambrenecki/virtualfish


# ¿Cómo iniciar la aplicación?

Dentro del entorno virtual, el único paso para inicializar
todo debería ser este comando:

```
honcho start
```

honcho es similar a foreman, lee el archivo Procfile y ejecuta
todos los componentes que ahí encuentre.


# Notas y otras observaciones

Luego iniciá un servidor redis, lo usa la
aplicación para intercambiar mensajes entre
flask y celery.

  redis-server

y luego iniciá celery:

  venv/bin/celery worker -A app.celery --loglevel=info

  (o bien make celery)


Por último, para ver en funcionamiento las tareas:

  venv/bin/celery -A app.celery events


Luego compilar la aplicación ember:

  make iniciar


Para finalizar:

  make ejecutar

y visitar http://localhost:5000

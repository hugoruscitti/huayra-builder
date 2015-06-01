# huayra-builder

huayra-builder es una aplicación web que permite
automatizar la generación de paquetes .deb
para la distribución huayra.

## Dependencias generales

Deberías tener instalado pip, virtualenv, npm, bower, emberjs y redis. En Debian o Huayra se pueden instalar así:

```
sudo apt-get install redis-server python-pip nodejs nodejs-legacy
sudo pip install virtualenv
sudo npm install -g bower ember-cli
```


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

Por último, tendrías que visitar la siguiente URL con el
navegador:

- http://localhost:5000


# Notas y otras observaciones

Esta aplicación usa 3 componentes principales, un servidor
web (que atiende en el puerto 5000 por omisión), un gestor
de tareas celery y una aplicación web desarrollada con emberjs.

Si querés ver el funcionamineto de las tareas podés ejecutar
este comando:

  venv/bin/celery -A app.celery events

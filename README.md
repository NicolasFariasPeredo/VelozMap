# VelozMap 🚀

**VelozMap** es una herramienta de escaneo de puertos/servicios desarrollada en Python utilizando **Nmap**. Su objetivo principal es permitir a los usuarios realizar escaneos de red con configuraciones específicas de Nmap a través de una interfaz sencilla y eficiente. VelozMap ofrece tres modos de escaneo: **discreto**, **medio** y **rápido**, adaptándose a las necesidades del usuario según la situación.

## Descripción

**VelozMap** permite ejecutar escaneos de red con diferentes niveles de agresividad y rapidez, dependiendo del modo elegido:

- **Modo Discreto**: Escaneo extremadamente lento y sigiloso, ideal para situaciones donde se requiere evitar la detección.
- **Modo Medio**: Escaneo equilibrado en cuanto a velocidad y sigilo, adecuado para la mayoría de los casos.
- **Modo Rápido**: Escaneo rápido y agresivo, utilizado cuando se necesita obtener resultados rápidos sin importar tanto la discreción.

## Requisitos

- Python 3.x
- Nmap (instalado en el sistema)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/velozmap.git
   cd velozmap

## Uso

Ejecuta el script `escaneo.py` con el modo de escaneo que desees y la IP o rango de IPs que quieras escanear:

```bash
python3 escaneo.py {discreto|medio|rapido} <IP>```


## Licencia MIT

Este proyecto está licenciado bajo la **Licencia MIT**. A continuación se detalla el texto de la licencia: MIT License

Copyright (c) [2025] [Nicolás Farias Peredo]

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y los archivos de documentación asociados (el "Software"), para usarlo sin restricciones, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y para permitir a las personas a las que se les proporcione el Software hacer lo mismo, bajo las siguientes condiciones:

El aviso de copyright y este permiso deberán incluirse en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITÁNDOSE A LAS GARANTÍAS DE COMERCIABILIDAD, APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES POR CUALQUIER RECLAMO, DAÑO O OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRA ACCIÓN, QUE SURJA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO O CUALQUIER OTRO TIPO DE ACCIONES EN EL SOFTWARE.

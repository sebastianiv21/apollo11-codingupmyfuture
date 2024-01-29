## Tabla de Contenido

- [Contexto del Proyecto](#-apollo-11-sistema-de-simulación-y-monitoreo-para-misiones-espaciales) 
  1. [Descripción del Proyecto](#descripción-del-proyecto) 
  2. [Objetivo](#objetivo)
  3. [Equipo de especialistas](#-equipo-de-especialistas)
  4. [Centro de operaciones](#-centro-de-operaciones-cabo-cañaveral)
- [Desarrollo del proyecto](#desarrollo-del-proyecto)
  1. [Requerimientos](#-requerimientos-del-proyecto)
  2. [Instrucciones de uso](#-instrucciones-de-uso)


# <p align="center">🚀 Apollo-11: Sistema de Simulación y Monitoreo para Misiones Espaciales</p>


<p align="center"> <img src="docs/build/html/_static/imageapollo.png" width="300" height="300"> </p>


## <p align="center">Descripción del Proyecto</p>

Desarrollado por la NASA, este sistema implementa un monitoreo basado en la transmisión de archivos con intervalos de 20 segundos, con el objetivo de proporcionar un control detallado sobre el estado operativo de cada componente clave para detectar tempranamente posibles anomalías. Esto facilita la toma de acciones preventivas tanto en el espacio como en la Tierra.


## <p align="center">Objetivo</p>

La adopción de esta tecnología avanzada es crucial para asegurar la seguridad de astronautas y turistas en futuras misiones espaciales. Además, la capacidad de monitoreo en tiempo real proporcionada por este sistema ofrece una ventaja significativa, permitiendo una respuesta inmediata ante cualquier situación imprevista. Esto, a su vez, mejora la eficiencia y la efectividad de los siguientes proyectos espaciales:

1. 📡 **OrbitOne**: Modernizar la flota de satélites representa un avance significativo para mejorar el rendimiento y expandir las comunicaciones, no solo optimizando la cobertura, sino también mejorando considerablemente la calidad de las transmisiones y la recopilación de datos.

<p align="center"><img src="docs/build/html/_static/Orbitone.png" width="200" height="200"> </p>


2. 🌕 **ColonyMoon**: Destinado a establecer una colonia lunar, con la finalidad de redefinir de manera significativa la narrativa de la exploración espacial. Más allá de la notoriedad asociada con la presencia humana en nuestro satélite natural, la colonia propuesta se vislumbra como un laboratorio espacial singular para experimentación avanzada, así como una base estratégica para futuras incursiones espaciales más allá de nuestro sistema solar.

<p align="center"><img src="docs/build/html/_static/Colonymoon.png" width="200" height="200"></p>

3. 🌋 **VacMars**: Al hacer que Marte sea accesible para los turistas, se establecería una nueva era de colaboración público-privada en la exploración espacial, creando una sinergia entre los intereses comerciales y la investigación científica.

<p align="center"><img src="docs/build/html/_static/Vacmars.png" width="200" height="200"></p>

4. 🌌 **GalaxyTwo**: La exploración de otras galaxias representa un salto gigantesco en nuestro entendimiento del universo, no solo se centraría en la expansión del conocimiento científico, sino que también podría inspirar nuevas formas de colaboración internacional en la búsqueda de respuestas a las preguntas fundamentales sobre el origen y la naturaleza del cosmos.

<p align="center"><img src="docs/build/html/_static/Galaxytwo.png" width="200" height="200"></p>

## <p align="center">💻 Equipo de especialistas</p>

|  Nombres |  Apellidos | Cargo  |
| :------------: | :------------: | :------------: |
| Luis Sebastian  |  Ibarra Villamil | Ingeniero de Sistemas Espaciales  |
| Leonardo Alfonso  |  Cometa Trujillo | Ingeniero de Software Espacial  |
| Alvaro Jose  | Polania Alvarez | Ingeniero de Comunicaciones Espaciales  |

## <p align="center">🏢 Centro de operaciones: Cabo Cañaveral</P>

<p align="center"><img src="docs/build/html/_static/Cañaveral.jpg "width="200" height="200"></p>

Ubicado en la costa este de Florida, Estados Unidos, es reconocido por ser la sede del Centro Espacial Kennedy (CEK), una instalación fundamental para la exploración espacial. A lo largo de los años, ha contribuido significativamente al desarrollo de la exploración espacial, siendo crucial en el programa Apolo y en el lanzamiento de misiones del transbordador espacial que facilitaron la construcción y mantenimiento de la Estación Espacial Internacional (EEI). 

# <p align="center">Desarrollo del proyecto</P>

## <p align="center">📜 Requerimientos del proyecto</P>

### <p align="center"> 1. Instalación de Python </P>

Para instalar Python, sigue estos sencillos pasos:

1. Dirígete a la página oficial de Python en [https://www.python.org/](https://www.python.org/).

2. Haz clic en el botón "Downloads" en el menú de navegación.

3. Selecciona la versión de Python que prefieras. 

:bulb: **Tip:** Generalmente, se recomienda la última versión.

4. Descarga el instalador adecuado para tu sistema operativo (Windows, macOS o Linux).

5. Ejecuta el instalador y sigue las instrucciones en pantalla.

:bulb: **Tip:** Puedes verificar la instalación abriendo una terminal y escribiendo el siguiente comando:

```bash
`python --version`.
```

### <p align="center"> 2. Validación de Pyp</P>

:warning: **Atención:** Asegúrate de tener Python instalado en tu sistema, debido que Pip generalmente se incluye automáticamente con las versiones mas actualizadas. 

1. Para verificar si ya tienes pip instalado, abre la terminal y ejecuta el siguiente comando:

```bash
pip --version
```

:memo: **Nota:** Si el comando no es reconocido, significa que pip no está instalado y por ello necesitas proceder con los siguientes pasos para su instalación.

2. Dirígete al sitio web oficial de pip en https://pip.pypa.io/en/stable/installation/. Aquí encontrarás la información actualizada sobre cómo instalar pip en diferentes sistemas operativos.

3.  En la página de instalación, encontrarás un enlace o un script de instalación adecuado para tu sistema operativo. Haz clic derecho sobre el enlace y selecciona "Guardar enlace como..." para descargar el script en tu máquina.

:bulb: **Tip:** Para asegurarte de que pip se ha instalado correctamente, ejecuta el siguiente comando en la terminal:

```bash
pip --version
```

### <p align="center"> 3. Instalación de GIT</P>

1. Dirígete a la página oficial de Git en https://git-scm.com/ para descargar el instalador correspondiente a tu sistema operativo. En la página principal, encontrarás enlaces de descarga para Windows, macOS y opciones para sistemas basados en Linux.

2. Una vez en la página oficial, sigue las instrucciones específicas de descarga e instalación para tu sistema operativo. Estas instrucciones te guiarán a través del proceso de instalación, asegurándote de obtener la versión más reciente y compatible de Git.

:bulb: **Tip:** Después de completar la instalación, verifica que Git se ha instalado correctamente ejecutando el siguiente comando en tu terminal o símbolo del sistema:

```bash
git --version
```

### <p align="center"> 4. Instalación de Poetry</P>

Para instalar Poetry, sigue los siguientes pasos:

1. Dirígete a la página oficial de Poetry en [https://python-poetry.org/](https://python-poetry.org/).

2. En la sección de instalación, encontrarás instrucciones detalladas para la instalación en diferentes sistemas operativos, para ello sigue las indicaciones específicas para tu entorno.

:bulb: **Tip:** Una vez completada la instalación, puedes verificar que Poetry se haya instalado correctamente ejecutando el siguiente comando en tu terminal:

    ```bash
    poetry --version
    ```
## <p align="center">📜 Instrucciones de uso</P>

1. Para obtener el programa, clona el repositorio desde el siguiente enlace: [https://github.com/sebastianiv21/apollo11](https://github.com/sebastianiv21/apollo11).

2. Accede a la ruta del programa y dirígete al archivo config_app.yaml. Este archivo contiene las configuraciones esenciales del programa, las cuales puedes personalizar según tus necesidades. A continuacion tienes un ejemplo del contenido del archivo:

```yaml

# ciclo_simulacion: periodicidad de ejecucion en segundos
ciclo_simulacion: 20

# cantidad de archivos generados en cada ejecucion
cantidad_archivos_generados:
  - minimo: 1
  - maximo: 100

formato_fecha_archivo: "%d%m%Y%H%M%S"

estado_dispositivo:
  - excellent
  - good
  - warning
  - faulty
  - killed
  - unknown
```
3. Abre una consola o terminal y ubícate en la carpeta que contiene la aplicación. Luego, ejecuta el siguiente comando:

```bash
python app.py ciclo_simulacion periodicidad_ejecucion
```
4. Asegúrate de proporcionar los siguientes argumentos:

- **ciclo_simulacion:** Indica la cantidad de ciclos requeridos.

- **periodicidad_ejecucion:** Intervalo de tiempo entre cada ciclo, expresado en segundos.

# Juego de Memoria "CodePairs"

¡Bienvenido al desafío de memorización de logotipos tecnológicos! En este juego, pondrás a prueba tu memoria al encontrar pares de cartas que representan logotipos famosos en el mundo de la tecnología.                                                      


![subcat-730](https://github.com/Luiss2080/ProyectoFinal/assets/149401326/5467d295-cf87-4770-97bd-7d3b9cf28a71)

## Información del Proyecto

- **Universidad:** Universidad Privada Domingo Savio
- **Facultad:** Ingeniería
- **Título del Proyecto:** CodePairs    
- **Asignatura:** Programación I    
- **Estudiantes:** Carlos Eduardo Salvatierra Chávez, Luis Mario Rocha Vela, Jesús Enrique Salas Espinoza.
- **Docente:** Zambrana Chacón Jaime.

## Resumen

CodePairs, un emocionante juego de memoria desarrollado en Python utilizando la poderosa biblioteca Pygame, desafía a los jugadores a sumergirse en el fascinante mundo de los logotipos tecnológicos. Con un temporizador de 2 minutos, los participantes deben encontrar pares para acumular puntos, enfrentando la presión del tiempo. La interfaz de usuario clara presenta un tablero vibrante de logotipos, mientras que varios sonidos acompañan cada movimiento, desde voltear las cartas hasta las elecciones correctas o incorrectas. CodePairs no es solo un juego; es una herramienta educativa que familiariza a los jugadores con los logotipos relevantes en tecnología. Este proyecto cuidadosamente estructurado y documentado representa la síntesis perfecta de creatividad, habilidades de programación y aprendizaje interactivo. ¡Sumérgete en el desafío de CodePairs y descubre el fascinante universo de los logotipos tecnológicos!

## Abstract

CodePairs, an exciting memory game developed in Python using the powerful Pygame library, challenges players to immerse themselves in the fascinating world of technological logos. With a 2-minute timer, participants must find pairs to accumulate points, facing the pressure of time. The clear user interface presents a vibrant board of logos, while various sounds accompany each move, from flipping cards to the correct or incorrect choices. CodePairs is not just a game; it is an educational tool that acquaints players with relevant logos in technology. This carefully structured and documented project represents the perfect synthesis of creativity, programming skills, and interactive learning. Dive into the challenge of CodePairs and discover the fascinating universe of technological logos!

# Desarrollo

## Marco Teórico

En esta sección, se abordarán los conceptos clave relacionados con las tecnologías utilizadas en el desarrollo del juego.

### 1. Visual Studio Code

Visual Studio Code es un entorno de desarrollo integrado (IDE) de código abierto y gratuito desarrollado por Microsoft. Se destaca por su interfaz de usuario minimalista, su capacidad de personalización y su amplia gama de extensiones. En el proyecto CodePairs, Visual Studio Code se utilizó como el entorno principal para escribir, editar y depurar el código del juego.

### 2. Python

Python es un lenguaje de programación de alto nivel conocido por su sintaxis clara y legible. Es ampliamente utilizado en el desarrollo de aplicaciones y juegos debido a su versatilidad y facilidad de aprendizaje. En CodePairs, Python fue la piedra angular para la implementación de la lógica del juego y la interacción con la biblioteca Pygame.

### 3. Pygame

Pygame es una biblioteca de juegos en Python que facilita el desarrollo de videojuegos 2D. Proporciona módulos para el manejo de gráficos, eventos, sonido y otros elementos esenciales en el desarrollo de juegos. CodePairs se benefició de Pygame para la creación de la interfaz de usuario, la gestión de eventos y la integración de elementos multimedia.

### 4. Manejo de Imágenes en Pygame

El manejo de imágenes es fundamental en un juego de memoria que implica cartas con logotipos. Pygame simplifica esta tarea al proporcionar funciones para cargar, mostrar y manipular imágenes. En CodePairs, se implementó un sistema eficiente para gestionar las imágenes de los logotipos y su presentación en el tablero de juego.

### 5. Sonido en Pygame

La integración de sonidos en un juego mejora significativamente la experiencia del usuario. Pygame ofrece capacidades para reproducir efectos de sonido y música de fondo. CodePairs aprovechó estas funciones para proporcionar una experiencia auditiva envolvente, desde sonidos al voltear cartas hasta pistas musicales que acompañan el juego.

### 6. Cronómetro

El cronómetro en CodePairs es esencial para agregar un componente de desafío al juego. Se implementó un sistema de cronometraje utilizando la biblioteca time de Python. Este cronómetro cuenta regresiva comienza automáticamente al iniciar el juego, brindando a los jugadores un límite de tiempo para completar el desafío de memorización.

### 7. Sistema de Puntaje

El sistema de puntaje en CodePairs motiva a los jugadores a encontrar pares de cartas de manera rápida y precisa. Cada par correcto suma puntos al puntaje total del jugador. Se diseñó un sistema de puntaje eficiente que se actualiza en tiempo real a medida que los jugadores avanzan en el juego.

Estos elementos del marco teórico fueron fundamentales para el desarrollo exitoso de CodePairs, brindando una base sólida y herramientas eficientes para la implementación de un juego de memoria interactivo y educativo.


## Proyecto

### Instalación de Librerías y Versiones

En el desarrollo de CodePairs, se requiere la instalación de las siguientes librerías y versiones específicas para garantizar la compatibilidad y el correcto funcionamiento del juego:

- **pygame**
  - Versión: (la versión que estás utilizando, si no especificaste una versión, simplemente coloca "Última versión")
  - Descripción: Pygame es una biblioteca de juegos en Python que facilita el desarrollo de videojuegos 2D. Proporciona módulos para el manejo de gráficos, eventos, sonido y otros elementos esenciales en el desarrollo de juegos.

- **sys**
  - Versión: (la versión que estás utilizando, si no especificaste una versión, simplemente coloca "Última versión")
  - Descripción: Este módulo proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y funciones que interactúan fuertemente con el intérprete.

- **math**
  - Versión: (la versión que estás utilizando, si no especificaste una versión, simplemente coloca "Última versión")
  - Descripción: Este módulo proporciona funciones matemáticas.

- **time**
  - Versión: (la versión que estás utilizando, si no especificaste una versión, simplemente coloca "Última versión")
  - Descripción: Este módulo proporciona diversas funciones relacionadas con el tiempo, como herramientas de medición de tiempo y manipulación de fechas.

- **random**
  - Versión: (la versión que estás utilizando, si no especificaste una versión, simplemente coloca "Última versión")
  - Descripción: Este módulo implementa generadores de números pseudoaleatorios para diversas distribuciones.

- **os**
  - Versión: (la versión que estás utilizando, si no especificaste una versión, simplemente coloca "Última versión")
  - Descripción: Este módulo proporciona una interfaz para interactuar con el sistema operativo, permitiendo acceder a archivos y directorios.



### Diseño

El diseño de CodePairs se centró en proporcionar una experiencia de usuario atractiva y funcional. Algunos aspectos clave del diseño incluyen:

1. **Interfaz de Usuario Intuitiva:**
   - Se diseñó una interfaz de usuario clara y fácil de entender, con un tablero que muestra los logotipos tecnológicos y un temporizador visible.

2. **Elementos Visuales Atractivos:**
   - Los logotipos tecnológicos seleccionados son visualmente atractivos y reconocibles, lo que contribuye a la experiencia del juego.

3. **Sonidos Inmersivos:**
   - Se incorporaron efectos de sonido para mejorar la interactividad, incluyendo sonidos al voltear cartas, aciertos y errores.

4. **Sistema de Puntaje Motivador:**
   - El sistema de puntaje se diseñó para motivar a los jugadores a encontrar pares de cartas de manera eficiente, sumando puntos con cada elección correcta.



### Funcionalidades Más Importantes

Durante el desarrollo de CodePairs, se implementaron diversas funcionalidades para enriquecer la experiencia del juego:

1. **Temporizador de Juego:**
   - Se incorporó un cronómetro que cuenta regresiva, proporcionando a los jugadores un límite de tiempo de 2 minutos para completar el juego.

2. **Gestión de Imágenes:**
   - El juego incluye un sistema eficiente para cargar, mostrar y gestionar las imágenes de los logotipos presentes en las cartas del juego.

3. **Sonido Interactivo:**
   - Se añadieron efectos de sonido para cada acción relevante en el juego, creando una experiencia auditiva envolvente.

4. **Sistema de Puntaje Dinámico:**
   - El sistema de puntaje se actualiza en tiempo real a medida que los jugadores encuentran pares de cartas, ofreciendo una retroalimentación inmediata.


![e39742a6-3e7c-4a8b-a723-9528c7c47b85](https://github.com/Luiss2080/ProyectoFinal/assets/149401326/a3f20301-01aa-4b9a-b361-bca91b4a1c12) ![7267b87b-d84a-4186-917a-d9ad04dc3cfe](https://github.com/Luiss2080/ProyectoFinal/assets/149401326/f62b51d5-0f4c-4e14-984a-14708629b630)


### Información del Juego

#### Reglas del Juego:

1. **Cronómetro:**
   - Tienes 2 minutos para completar el juego.
   - El cronómetro se inicia automáticamente cuando comienzas el juego.

2. **Interfaz de Usuario:**
   - El juego muestra un tablero de cartas con los logotipos tecnológicos.
   - Se presenta un cronómetro en cuenta regresiva.

3. **Sonidos:**
   - **Fondo:**
     - Música de fondo que crea una atmósfera envolvente durante el juego.
   - **Movimiento de Cartas:**
     - Sonido al voltear y mover las cartas para una experiencia interactiva.
   - **Elección Correcta:**
     - Agradable sonido de éxito al encontrar un par correcto.
   - **Elección Incorrecta:**
     - Sonido indicativo cuando se elige un par incorrecto.

4. **Puntajes:**
   - Al encontrar cartas pares identicas vas sumando púntos 

5. **Fin del Juego:**
   - Al finalizar el tiempo tendrás la opción de iniciar juego nuevamente


   ### Ejecución del Juego:

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala la biblioteca Pygame ejecutando `pip install pygame`.
3. Descarga el código fuente del juego.
4. Ejecuta el juego usando `python main.py`.


#### Estrategias para Ganar:

1. *Planificación:*
   - Antes de hacer clic, observa todas las cartas y planifica tu estrategia.
   - Recuerda la ubicación de las cartas para encontrar los pares de manera eficiente.

2. *Enfoque y Concentración:*
   - Mantén un enfoque constante y evita distracciones para mejorar tu rendimiento.
   - La concentración es clave para recordar la ubicación de los logotipos.

3. *Velocidad y Precisión:*
   - Encuentra los pares rápidamente para acumular más puntos.
   - La precisión al elegir las cartas correctas también es esencial.

#### Consejos para una Experiencia Óptima:

1. *Auriculares Recomendados:*
   - Disfruta de la experiencia completa del juego utilizando auriculares para sumergirte en los sonidos envolventes.

2. *Ambiente Tranquilo:*
   - Juega en un entorno tranquilo para facilitar la concentración y la inmersión.

3. *Descansos Breves:*
   - Si juegas durante períodos prolongados, toma descansos cortos para mantener la agudeza mental.



### Código Fuente

Puedes acceder al código fuente del juego en el siguiente enlace: https://github.com/Luiss2080/ProyectoFinal/blob/main/README.md




# Conclusiones

Este proyecto, CodePairs, representa el resultado de un esfuerzo colaborativo y creativo centrado en el desarrollo de un juego de memoria con un enfoque tecnológico. A lo largo de este proceso, se han extraído conclusiones significativas que destacan los logros alcanzados y las lecciones aprendidas. A continuación, se presentan las principales conclusiones:

## Desarrollo y Aplicación de Conocimientos

La ejecución de CodePairs no solo representó un desafío técnico, sino también una oportunidad para aplicar y consolidar los conocimientos adquiridos en programación y desarrollo de juegos. La complejidad del juego permitió la implementación de conceptos teóricos en un entorno práctico, fortaleciendo nuestra comprensión de la materia y mejorando nuestras habilidades en Python y Pygame.

## Colaboración y Trabajo en Equipo

El trabajo colaborativo fue esencial para el éxito del proyecto. La asignación de roles y responsabilidades, junto con una comunicación efectiva entre los miembros del equipo, contribuyó significativamente a la fluidez del desarrollo. Esta experiencia refuerza la importancia del trabajo en equipo en proyectos de esta envergadura.

## Solución Creativa de Problemas

El desarrollo de CodePairs planteó diversos desafíos que requerían soluciones creativas. Desde la gestión del tiempo hasta la integración de elementos visuales y sonoros, cada problema se abordó con ingenio y cooperación. Esta capacidad para resolver problemas de manera creativa es una habilidad transferible valiosa que llevamos más allá de este proyecto.

## Aprendizaje Continuo

El proyecto no solo fue un hito en términos de desarrollo, sino también un punto de partida para un aprendizaje continuo. La investigación y comprensión de las herramientas utilizadas, así como la adaptación a nuevos problemas durante el desarrollo, destacaron la importancia de la adaptabilidad y la disposición para aprender en entornos de programación complejos.
"# CodeAirs-" 

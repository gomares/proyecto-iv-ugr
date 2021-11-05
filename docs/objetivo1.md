## Objetivo 1: Estructura general y planificación del proyecto
En esta documentación se puede encontrar los perfiles de usuario iniciales junto con la planificación de milestones iniciales del proyecto.


## Perfiles de Usuarios
 
 -  **Aficionado del fútbol de un equipo:** Se describe al usuario como Felipe Castillo, de 35 años de edad. Especialmente es aficionado de un equipo de fútbol desde muy chico y siempre mira sus partidos todas las semanas. Apostar le parece divertido, por lo que cada semana pone un poco de dinero extra en la apuesta del partido de su equipo.  Felipe quiere poder obtener información estadísticas previa particularmente de su equipo, así como el historial reciente de los partidos que ha jugado. Finalmente, quiere obtener una recomendación de apuesta para el siguiente partido de su club de toda la vida.
 
 -  **Aficionado del fútbol apostador:** Se describe al usuario como Javier Reyes, de 28 años de edad. Le gusta bastante los deportes pero más allá le gusta apostar y ganarle a la casa. Cree que ganar en  las apuestas del fútbol son cuestión de estrategia e investigación. Por ello, cada semana busca la mejor apuesta y más segura intentando ganar dinero. Javier quiere poder obtener información estadísticas previa de partidos del fin de semana que viene y también obtener información sobre el historial reciente de los resultados entre dichos equipos. Javier quiere obtener una recomendación de apuesta para un partido y también le gustaría obtener una serie de recomendaciones de las mejores apuestas que puede realizar en un fin de semana.

## Historias de Uusario
|ID | Historia de Usuario| 
|--|--|
|[HU1](https://github.com/sorozcov/proyecto-iv-ugr/issues/5)|[HU4] Aficionado del fútbol apostador-1|
|[HU2](https://github.com/sorozcov/proyecto-iv-ugr/issues/6)| [HU5] Aficionado del fútbol apostador-2|

## Milestones

|ID | Milestone | Descripción | Estado|
|--|--|--|--|

|[M1](https://github.com/sorozcov/proyecto-iv-ugr/milestone/2)| Desarrollo de Clases Base|
Este milestone pretende el desarrollo de las clases básicas para llevar a cabo el proyecto. En este caso la clase más importante es la clase que puede leer datos de un JSON y puede almacenar los datos importantes de todos los partidos. La misma clase debe poder filtar y obtener información en los mismos datos. Se desarrolla otra clase básica que será el algoritmo predictivo el cual guardará referencia a los datos entrenados y sus propias funciones de entrenamiento y predicción.| No Iniciado
|[M2](https://github.com/sorozcov/proyecto-iv-ugr/milestone/3)| Predicción de Resultados| En este punto se puede acceder a la información de un partido y el usuario puede visualizar dicha información. A partir de lo anterior, se puede generar un algoritmo de predicción basado en la implementación de un arbol de decisión y atributos de partidos pasados tales como tiros de esquina , número de faltas, penales, posesión y más importante goles en su historial de los equipos participantes. El usuario podrá probar dicho algoritmo al escoger un partido. | No Iniciado
|[M3](https://github.com/sorozcov/proyecto-iv-ugr/milestone/4)| Comparación y Predicción Mejor Apuesta Posible | Este milestone pretende realizar un algoritmo sencillo para calcular cuál es la mejor apuesta a la que puede acceder un usuario de un partido o ya bien de una serie de partidos. Para ello, se utilizaría el algoritmo ya completado en M2 y se generaría una forma de calcular las ganancias a partir del porcentaje de acierto de las predicciones junto con el pago de la apuesta antes de iniciar el partido. El usuario ahora podrá probar #6.| No Iniciado


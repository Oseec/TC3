

Descripción

Los algoritmos genéticos están inspirados en la teoría de la evolución de las especies, la cual establece que en una población de una especie determinada, los individuos mejor adaptados son los que logran sobrevivir y reproducirse.

El objetivo del proyecto consiste en implementar un algoritmo genético que sea capaz de buscar el camino óptimo entre dos puntos en un tablero, evadiendo cualquier obstáculo que pueda encontrarse.

Se debe generar una población de indivuos capaces de moverse en el tablero, un espacio a la vez y solo con movimientos verticales y horizontales. En el transcurso de su recorrido se puede encontrar obstáculos, que si los toca (cae directamente en el obstáculo) el individuo muere. El usuario, podría, dado el caso, de introducir el adn de un individuo, de tal forma que a partir de este se genere el resto de la población. La forma y codificación del ADN debe ser definido por su grupo

Un ejemplo de una posible implementación, es ser codificar la secuencia de movimientos en un string con la forma "DAIIIBII..." donde la D es derecha, A es arriba, I es izquierda y b es abajo. El espécimen se moverá de acuerdo con la secuencia: derecha, arriba, tres movimientos a la izquierda, uno hacia abajo y dos movimientos a la izquierda. Las estrategias de selección, cruce y mutación, y la función de fitness se dejan a su creatividad.

Para la segunda estrategia, pueden cambiar elementos de la prueba, como agregar "premios" en todo el tablero, de tal forma que los especímenes no solo tengan el objetivo de hacer el recorrido, sino de obtener la mayor cantidad de recompensas. También pueden probar haciendo pequeños cambios en el tablero ya sea en su forma o en los obstáculos mismos, o agregarle algún tipo de sentidos sensoriales mínimos que le aporte información a cada individuo sobre su entorno. 

La implementación de estas alternativas y sus resultados, deben ser detallados en el artículo científico que debe presentar a partir de sus experimentos. 


Interfaz gráfica

El proyecto debe ser implementado en javascript, utilizando tecnologías WEB para su visualización y animación. El usuario debe ser capaz de introducir el tamaño del tablero y la cantidad de obstáculos que se puede encontrar. Estos obstáculos pueden ocupar más de un campo y deben distribuirse por todo el espacio de forma aleatoria.

El pograma debe permitir observar todos los individuos de la población, saber si alguno de ellos muere y ser capaz de saber si alguno de ellos se encicla. El usuario puede ingresar la cantidad de individuos para cada generación, el porcentaje de selección y la cantidad de los individuos 

Se pueden introducir los parámetros necesarios para la ejecución de las estrategias diseñadas por usted, así como información relevante que puede ser utilizada como datos experimentales para su paper.

Evaluación

Criterio 1. implementación del algoritmo genético base  30%
Criterio 2. Algoritmo Genético estrategia 2             30%
Criterio 3. Funcionalidad y parametrización             10%
Criterio 4. Interfaz Gráfica y experiencia de usuario   20%
Criterio 5. Estética                                    10%

La evaluación del paper se realizará de forma separada, que se le informara en su mo

Aclaraciones y correcciones
En esta sección se detallará, en versiones posteriores del documento, los cambios, aclaraciones o correcciones realizadas a esta especificación.

26 de abril de 2022 Explicación y entrega inicial de la especificación del proyecto.


Entrega

La entrega se debe realizar antes de las 10:00 pm del día de mayo del 2022 en un archivo zip mediante el TecDigital.
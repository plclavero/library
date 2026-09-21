# Diplomatura Superior y de Vinculación en Fundamentos de Programación Asistida por IA (UNAJ)

## Curso 1: Introducción al Pensamiento Computacional y la Programación Estructurada

## Trabajo Integrador

### 1. Consigna

Se solicita el desarrollo de un programa que gestione un conjunto de registros correspondientes a un dominio de libre elección (por ejemplo, turnos de un centro de salud, fuentes para un informe de investigación, control de stock o inscripciones a un curso, entre otros posibles).

El programa debe incluir los siguientes elementos:

- Variables con al menos tres tipos de datos distintos, y un mensaje construido con f-string.
- Una clase que modele el registro principal del dominio elegido, con sus atributos correspondientes y al menos un método que calcule o transforme información a partir de esos atributos.
- Una segunda clase, independiente de la anterior, que modele otro elemento del mismo dominio, también con sus propios atributos y al menos un método.
- Una jerarquía de clases compuesta por una clase base y dos subclases que hereden de ella con `super().__init__()` (ver el material de POO de la Clase 6), donde cada subclase agregue al menos un atributo propio y un método propio o redefinido respecto de la clase base.
- Listas de objetos que organicen los registros de cada una de las clases anteriores.
- Una estructura de manejo de excepciones que valide el dato correspondiente antes de crear cada objeto, de manera que un dato inválido no interrumpa la ejecución del programa.
- Una estructura condicional que clasifique la información según un criterio propio del dominio elegido.
- Una estructura repetitiva que recorra alguna de las listas de objetos y calcule al menos dos valores de interés distintos.
- Al menos cinco funciones, cada una con una responsabilidad clara y definida.

Se recomienda desarrollar el trabajo en Python, lenguaje utilizado a lo largo del curso. Es posible utilizar otro lenguaje, siempre que el programa cumpla con los mismos requisitos funcionales y que la estructura de los datos quede documentada con claridad, de forma independiente del lenguaje elegido.

Se admite el uso de herramientas de inteligencia artificial como apoyo durante el desarrollo del trabajo, en tanto quien lo presente pueda explicar el funcionamiento de cada parte del código entregado.

### 2. Formato de entrega

La entrega es asincrónica y no requiere instancia de defensa en clase. Consta de lo siguiente:

1. Código correspondiente al programa desarrollado.
2. Elegir uno de los siguientes formatos:

   A. Documento breve, que describa el dominio elegido y el funcionamiento general del programa.

   B. Video de entre tres y cinco minutos que muestre el programa en funcionamiento y explique el criterio utilizado para organizar el código en funciones y en la clase definida.

**Nombre:** [David Zuluaga Ceballos]

### Parte 1 — Analizar el algoritmo antes de comprar hardware

Hay que encontrar primero que todo la causa raiz, si sabemos que el algoritmo esta diseñado con cierto patrón, que es un poco mas desactualizado y no cumple con lo requerido, insertion sort no es eficiente en tiempo de ejecución para 1'200.000 registros. Con lo que dices podemos deducir que Tamiza cumple su objetivo de ordenar correctamente pero incumple el rango de tiempo, que algo funcione correctamente no quiere decir que sea lo mas productivo.

Duplicar la velocidad del servidor puede resolver hasta cierta parte, pero insertion sort tiene una ecuacion cuadratica, lo que nos indica que si el numero de registros se duplica, los recursos necesarios no van a ser solo el doble tambien, si no que sera cuadriplicado. Un servidor que sea mas rapido solo mejora un poco comparado con lo anterior, pero un buen algoritmo le gana a un mejor servidor. Esto sin contar que es mucho mas alto el costo de, cada vez que incremente los registros, aumentar la capacidad del servidor, comparado con la inversion del algortimo que seria unica.

El siaweb del itm hace 1 o 2 años, en las asesorias de matricula para elegir materias de los estudiantes, siempre generaba una sesion demasiado lenta por el alto volumen de estudiantes: eran 26mil en la sesion al mismo tiempo. Esto hacia que muchos estudiantes perdieramos el cupo en materias o grupos que necesitabamos por la alta demora en las peticiones. Lo que yo experimenté en el software fue una mejora muy grande, ya que en el momento es muchisimo mejor y no causa problema al momento de hacer la asesoria, y ese numero en la sesion ha incrementado a aproximadamente 30mil.


### Parte 2 — Responsabilidad ambiental y ética de la implementación

Analizando un poco mas la situacion y adentrandonos en temas un poco mas algidos: ¿que pasa en el tema ambiental con un servidor encenndido mas tiempo durante muchos años? El gasto energetico que se genera se va llendo en una cadena, porque por ejemplo en nuestro pais la mayor productora de energia es el agua, basado en las hidroelectricas, entonces ademas del gasto energetico se le suma el desgaste hidrico.

Ademas, como el algoritmo es ineficiente en tiempos, tambien puede generar mas daños basados en su mal procesamiento, ya que si hay mejores algortimos, mejores alternativas, lo pasado va quedando obsoleto. Es muy probable que como el algoritmo no termine a tiempo, no queden bien ordenados los pacientes y que dejen a uno de riesgo alto para el final, o que ni siquiera quede en la lista prioritaria. El costo en ese escenario lo asume el paciente con su salud o hasta con su vida, y ustedes como institucion lo asumen en su reputación y hasta en cargos legales. Estos son de los peores escenarios, pero pueden existir.

No solo se convierte en perjuicio, como lo indique antes, para los pacientes, si no tambien para los operadores del centro: trabajan con una lista incompleta y eso los pone en una posicion de decidir sin herramientas, y eso se les puede culpar a ellos por algo que no depende de su trabajo. Vamos viendo como una sola decision repercute en tantos ambitos y en tantas personas sin culpa alguna.

Desde una vista de profesionales se debe tener una responsabilidad etica y moral: productos realizados con excelente calidad desde un principio, cubriendo todos los posibles escenarios. No basta solo con que termine a tiempo, si no que no hayan errores silenciosos, que se genere un trabajo limpio, correcto y puntual. En este ambito no se corren los mismos riesgos que en un error de facturacion o algo similar, que solo es un problema de dinero; aqui estamos hablando de daños irreparables en la salud o hasta perder una vida.
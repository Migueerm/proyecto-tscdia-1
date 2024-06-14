# EduTarea SRL
**Integrantes**

| Nombre y  Apellido  |    DNI    | Correo eléctronico        | Link Git Hub |
|---------------------|-----------|---------------------------|--------------
| Melania Ligorria    | 38412646  | melanialigorria@gmail.com | https://github.com/mel-ligorria
| Miguel Rojas        | 39215582  | rojas.miguel018@gmail.com | https://github.com/Migueerm/ejercitacion-ispc
| Florencia Andrada   | 44788525  | florenciacarolina031@gmail.com | https://github.com/Flor3ncia-Andr4d4
| Carlota Olmedo      | 41711170  | carlota_olmedo@hotmail.com| https://github.com/caolmedo
| Guadalupe Mendoza   | 45934026  | despontinguadalupe@gmail.com |https://github.com/Guadamendoza/SolucionesPracticas 


**Objetivo del Proyecto**

EduTarea SRL, especialistas en aplicaciones móviles de gestión de tareas, se dedica a desarrollar soluciones innovadoras para la organización y gestión académica. Nuestra principal aplicación será EduTarea, estará diseñada para ayudar a los estudiantes a organizar y gestionar sus materias y tareas de manera eficiente. Con el objetivo de mejorar la productividad y facilitar el seguimiento del progreso académico, EduTarea permitirá a los estudiantes mantenerse al día con sus responsabilidades de forma integral.

**Características Principales**

**Gestión de Materias:**
- Permite a los estudiantes agregar, editar y eliminar materias.
- Cada materia incluye detalles como el nombre del curso, el profesor, el horario de clases y la ubicación del aula.
  
**Organización de Tareas:**
- Los estudiantes pueden añadir tareas para cada materia, especificando la fecha de entrega, el nivel de prioridad y las instrucciones.
- Las tareas pueden ser categorizadas (por ejemplo, actividades, proyectos, exámenes) para facilitar su organización.

**Recordatorios y Notificaciones:**
- Configuración de recordatorios para fechas de entrega y eventos importantes.
- Notificaciones push para alertar a los estudiantes sobre próximas tareas y plazos.

**Calendario Integrado:**
- Un calendario visual donde los estudiantes pueden ver todas sus tareas y eventos en un solo lugar.
- Sincronización con calendarios externos como Google Calendar para una mayor integración.
  
**Seguimiento del Progreso:**
- Los estudiantes pueden marcar tareas como completadas y ver su progreso general.
- Gráficos y estadísticas que muestran el rendimiento académico y el cumplimiento de tareas.
  
**Colaboración y Compartir:**
- Funciones para compartir tareas y notas con compañeros de clase.
- Espacios de discusión para colaboración en proyectos grupales.

**Interfaz Amigable:**
- Diseño intuitivo y fácil de usar, adaptado a las necesidades de los estudiantes.
- Personalización de temas y colores para una experiencia de usuario más agradable.


**Análisis y Diseño**
**Análisis de Requisitos del Usuario:**
-Investigación de Usuarios:
Para comprender las necesidades y preferencias de los estudiantes en cuanto a la gestión de tareas, llevamos a cabo una exhaustiva investigación que incluyó encuestas, entrevistas y análisis de mercado. A través de estas actividades, pudimos obtener información valiosa sobre los comportamientos y hábitos de los estudiantes en relación con la gestión de sus tareas académicas.

Nuestros hallazgos indican que la mayoría de los estudiantes valoran la capacidad de organizar sus tareas de manera eficiente, establecer fechas límite claras y recibir recordatorios o notificaciones para mantenerse al tanto de sus responsabilidades académicas. Además, muchos estudiantes expresaron la necesidad de una aplicación que les permita gestionar no solo tareas individuales, sino también proyectos más grandes con múltiples sub-tareas y fechas de vencimiento.

Segmentación de Usuarios:durante nuestro proceso de investigación, identificamos varios grupos demográficos de usuarios con diferentes necesidades y preferencias en lo que respecta a la gestión de tareas. Estas segmentaciones incluyen:
1. Estudiantes de Secundaria: este grupo de usuarios tiende a estar más enfocado en tareas individuales y asignaciones escolares. Valoraron especialmente la capacidad de establecer fechas límite claras y recibir recordatorios para evitar la procrastinación.
2. Estudiantes Universitarios: los estudiantes universitarios tienen una carga de trabajo más variada y compleja, que incluye proyectos de investigación, exámenes y trabajos grupales. Para este grupo, la capacidad de organizar proyectos más grandes en tareas más pequeñas y colaborar con compañeros de clase es esencial.
3. Estudiantes Postgraduados: este segmento de usuarios a menudo está más orientado hacia la investigación y proyectos a largo plazo. Valoraron la capacidad de establecer metas a largo plazo y desglosarlas en tareas más pequeñas, así como la integración con herramientas de gestión de referencias bibliográficas.
   
Al comprender las necesidades específicas de cada segmento de usuarios, podemos diseñar una aplicación que se adapte mejor a sus requisitos individuales y ofrezca una experiencia más personalizada y satisfactoria para cada grupo.Nuestro objetivo es que el sistema de gestión de tareas está diseñado para mejorar la organización y la productividad de los usuarios en el ámbito educativo, brindándoles una herramienta eficaz y fácil de usar para gestionar sus responsabilidades académicas.

**Estructura del Diseño**

- Datos de Entrada:
	Para agregar una tarea en una categoría:
		○ Descripción de la tarea.
		○ Categoría a la que pertenece la tarea (opción de crear una nueva categoría si no existe).
  
	Para marcar una tarea como completa:
		○ ID de la tarea que se desea marcar como completa.
  
	Para modificar el estado de una tarea:
		○ ID de la tarea que se desea modificar.
		○ Nuevo estado de la tarea (pendiente, completa u observada).
  
	Para listar las tareas:
		○ Opción para filtrar por categoría (opcional).
  
	Para listar las categorías:
No requiere datos de entrada adicionales.


- Proceso:
	Agregar una Tarea en una Categoría:
		○ Verificar si la categoría especificada existe.
		○ Si la categoría no existe, ofrecer la opción de crearla.
		○ Crear una nueva tarea con la descripción y categoría proporcionadas.
		○ Agregar la tarea a la lista de tareas.
  
	Marcar como Completa la Tarea:
		○ Buscar la tarea por su ID.
		○ Cambiar el estado de la tarea a "completa".
  
	Modificar el Estado de la Tarea:
		○ Buscar la tarea por su ID.
		○ Actualizar el estado de la tarea al nuevo estado especificado.
  
	Listar las Tareas:
		○ Mostrar todas las tareas almacenadas.
		○ Opcionalmente, filtrar las tareas por categoría si se especifica.
  
	Lista de Categorías:
		○ Mostrar todas las categorías disponibles almacenadas en la lista.

- Salida:
Confirmaciones de acciones realizadas con éxito (por ejemplo, tarea agregada, tarea marcada como completa, etc.).
Listados de tareas y categorías según las solicitudes del usuario.
Mensajes de error en caso de que ocurran problemas durante el proceso.





# MODULARIZACIÓN - Aplicación EduTarea

**Descripción general**
Esta aplicación permite gestionar tareas, permitiendo al usuario crear, modificar y listar tareas con diferentes estados y categorías. La aplicación está modularizada para facilitar el mantenimiento y la escalabilidad.

**MODULO 1**
**index.py:**
Este fragmento de código es un programa de gestión de tareas que interactúa con los módulos 
tareas y categorías, los cuales contienen funciones relacionadas con las operaciones de tareas y 
categorías respectivamente.

 Importación de módulos:
• Las líneas import tareas y import categorias importan los módulos tareas y 
categorias, respectivamente. Estos módulos contienen funciones 
relacionadas con las operaciones de tareas y categorías en el programa.

 Definición de funciones de ayuda:
• La función mostrar_bienvenida() está diseñada para imprimir un mensaje 
de bienvenida cuando el programa se inicia. Esto proporciona una 
introducción amigable al usuario al comenzar a usar la aplicación.

• La función mostrar_menu() imprime un menú de opciones disponible para 
el usuario. Esto permite que el usuario vea todas las operaciones que 
puede realizar dentro del programa.


**• Modulos_Educategorias.py:** 
Este archivo Python contiene una serie de funciones que están diseñadas para manejar diferentes opciones relacionadas con las categorías. Cada función está relacionada con una
operación específica que se puede realizar en las categorías del sistema. 
Descripción de cada función:

 ingreso_categoria(): Esta función está relacionada con la operación de ingreso de 
una nueva categoría. Cuando se llama a esta función, imprime un mensaje indicando 
que se ha seleccionado la opción de ingreso de categoría.

 listar_categoria(): Esta función está diseñada para listar las categorías existentes. Al 
llamar a esta función, se imprime un mensaje indicando que se ha seleccionado la 
opción de listar categorías.

 modificar_categoria(): Esta función está relacionada con la operación de modificar 
una categoría existente. Al llamar a esta función, se imprime un mensaje indicando 
que se ha seleccionado la opción de modificar categorías.

 eliminar_categoria(): Esta función se encarga de eliminar una categoría. Al llamar a 
esta función, se imprime un mensaje indicando que se ha seleccionado la opción de 
eliminar categorías.

 salir(): Esta función es para salir del programa o del menú de categorías. Al llamar a 
esta función, se imprime un mensaje indicando que se ha seleccionado la opción de 
salir.








**Módulo_2.py**
Este código es un fragmento del gestor de tareas simple, permitiendo a los usuarios modificar el estado de las tareas y listar todas las tareas existentes. El uso de una lista para almacenar las tareas y las funciones específicas para manipular estas tareas facilita la gestión y el mantenimiento del código.

1. **Comprueba si la lista de tareas está vacía**:
   - La función verifica si la variable `lista_tareas` no contiene ninguna tarea.
   - Si `lista_tareas` está vacía, imprime "No hay tareas para mostrar."

2. **Muestra el listado de tareas**:
   - Si hay tareas en `lista_tareas`, imprime un encabezado "Listado de Tareas:".
   - Recorre cada tarea en `lista_tareas` utilizando un bucle `for`.

3. **Imprime los detalles de cada tarea**:
   - Para cada tarea en la lista, imprime los detalles de la tarea en un formato específico:
     - `ID`: Identificador de la tarea.
     - `Descripción`: Descripción de la tarea.
     - `Estado`: Estado de la tarea (por ejemplo, completada o pendiente).
     - `Categoría`: Categoría a la que pertenece la tarea.

4. **Uso de formato de cadena**:
   - Utiliza una f-string para formatear la salida de cada tarea, mostrando sus atributos (`id`, `descripcion`, `estado`, `categoria`).

El código que has compartido implementa una lista de tareas y dos funciones principales para gestionar estas tareas. Aquí está la descripción de cada componente y función:

### Componentes del código

1. **lista_tareas**:  Es una lista vacía que almacenará las tareas en forma de diccionarios. Cada tarea tendrá las siguientes claves: `id`, `descripcion`, `estado` y `categoria`.

### Funciones del código

### `ingreso_categoria()`:  
Incluye funciones para ingresar categorías y listar las categorías existentes. El usuario debe ingresar el nombre de una categoria que luego sera guardada en una lista "lista_categoria"

  ### `ingreso_tarea()`:
  1. Permite al usuario **ingresar una tarea** y **almacenarla en una lista** “lista_tareas”.   A su vez le permite ingresar 
 la categoría de la tarea, y en el caso de que no exista dicha categoría el usuario tiene la opción de crearla.
 2. Tambien solicita que ingrese la **descripion de la tarea**. Se intrduce un ID de la tarea y luego se crea un diccionario con los siguientes campos: ID, descripcion, estado y categoria.
3. Finalmente se **añade a la lista** de tareas y se le **notifica** al usuario que su tarea fue añadida con exito.
  
- ### `marcar_tarea_completa()`:
  1. Se le solicita al usuario que **ingrese el ID** de la tarea que desea marcar como completa.
  2. Luego la funcion **recorre la lista** de tareas ("lista_tareas") para ver si se encuentra el ID de la tarea ingresada, 
  3.Si se encuentra el estado de la tarea se muestra como **"tarea completa"**, se **notifica** al usuario y la funcion finaliza, por el contrario, si el ID  no fue encontrado se le **notifica** al usuario que la tarea no fue encontrada.  
####  `modificar_estado_tarea()`
Esta función permite al usuario modificar el estado de una tarea específica basada en su ID. A continuación se detalla el proceso:

1. **Entrada del ID de la tarea**: solicita al usuario que ingrese el ID de la tarea que desea modificar.
2. **Búsqueda de la tarea**: busca en `lista_tareas` la tarea cuyo ID coincida con el ingresado.
3. **Verificación de la existencia de la tarea**:
   - Si la tarea existe:
     - Muestra las opciones de estado disponibles: Pendiente, Realizada, Observada.
     - Solicita al usuario que seleccione el nuevo estado ingresando el número correspondiente.
     - Actualiza el estado de la tarea si la opción ingresada es válida.
     - Informa al usuario sobre la actualización del estado.
   - Si la tarea no existe:
     - Informa al usuario que la tarea no fue encontrada.

#### `listar_tareas()`
Esta función lista todas las tareas almacenadas en `lista_tareas` con sus detalles:

1. **Verificación de tareas**:
   - Si no hay tareas en `lista_tareas`, informa al usuario que no hay tareas para mostrar.
   - Si hay tareas:
     - Muestra el listado de tareas con sus detalles (ID, descripción, estado y categoría).



**modulo_3.py** 
Esta parte del código define distintas funciones de salida de acuerdo a las acciones que se realicen previamente, de acuerdo a las selecciones realizadas en los módulos 1 y 2. 

Descripción de la salida de cada función:
bienvenida(): Esta funcion realiza un mensaje de bienvenida. 
menu(): Esta funcion indica la ejecución del menú, recuperando las distintas opciones.
opcion_invalida(): Esta funcion indica que la opción es inválida
salir_programa(): Esta funcion indica que se está saliendo del programa
operacion_cancelada(): Esta funcion indica que la operación fue cancelada.
error_inesperado(error): Esta funcion indica que hubo un error inesperado. 
categoria_anadida(nombre_categoria): Esta funcion indica que se añadió una categoría
categoria_ya_existe(nombre_categoria):Esta funcion indica que la categoría ingresada ya existe.
categoria_modificada(nombre_original, nuevo_nombre): Esta función indica que se modificó un nombre de una categoría.
categoria_no_existe(nombre_categoria): Esta funcion indica que la categoría no existe. 
categoria_eliminada(nombre_categoria): Esta funcion indica que se eliminó una categoría
tarea_anadida(): Esta función indica que se agregó una tarea con éxito. 
tarea_no_encontrada(id_tarea): Esta funcion indica que la tarea no ha sido encontrada.
tarea_eliminada(id_tarea): Esta funcion indica que la tarea ha sido eliminada. 
tarea_actualizada(id_tarea, nuevo_estado): Esta funcion indica que el estado de la tarea ha sido actualizado un nuevo estado, recuperando el ID y el Estado.
tarea_listada(id_tarea, descripcion, estado, categoria): Esta funcion indica la descripción de la tarea listada, recuperando el ID, Descripción, Estado y Categoría
no_hay_categorias(): Esta funcion indica que no hay categorías para mostrar.
no_hay_tareas(): Esta funcion indica que no hay tareas para mostrar.


**Guía del contenido de nuestro repositorio GitHub**

**Readme**

**En nuestro archivo readme, se describen los integrantes del grupo, presentación y objetivo del proyecto y la explicación de la modularización de nuestra aplicación.**


  1 USO DE LA APLICACIÓN  
Para ingresar una nueva tarea, el usuario sigue estos pasos:
Selecciona la opción 1 del menú principal.
Ingresa la categoría de la tarea requerida.
En caso de que la categoría no exista previamente, se ofrece la opción de crearla.
Luego, proporciona una descripción detallada de la tarea.
Se registra la tarea en el sistema con un ID único, la descripción proporcionada, el estado inicial "pendiente", y la categoría seleccionada.

Listar Tareas:
Para listar todas las tareas registradas, sigue estos pasos:

Selecciona la opción 2 del menú principal.
El programa muestra todas las tareas en la lista, incluyendo detalles como su ID, descripción, estado y categoría.
Antes de mostrar las tareas, verifica si la lista está vacía. En caso afirmativo, se muestra un mensaje indicando que no hay tareas para mostrar.

Modificar Estado de Tarea:
Para actualizar el estado de una tarea existente, realiza lo siguiente:
Selecciona la opción 3 del menú principal.
Ingresa el ID de la tarea que desea modificar.
Una vez encontrada la tarea, se presentan opciones para cambiar su estado a "Pendiente", "Realizada" o "Observada", según la preferencia del usuario.
El estado de la tarea se actualiza inmediatamente después de la selección.

Ingresar Categoría:
Para ingresar una nueva categoría el usuario debe hacer lo siguiente: 
Selecciona la opción 5 del menú principal. 
Ingresa el nombre de la categoría deseada.
Si la categoría no existe previamente, se añade al sistema

Listar categorias: 
Para ver todas las categorías existentes seguir los siguientes pasos: 
Selecciona la opción 6 del menú.
Se mostrará un listado con todas las categorías registradas en el sistema.
Si no hay categorías registradas, se mostrará un mensaje indicando que no hay categorías para mostrar.

Modificar categoría:
Para cambiar el nombre de una categoria existente
Selecciona la opción 7 del menú principal.
Ingresa el nombre actual de la categoría que deseas modifica
Proporciona el nuevo nombre para la categoría
La categoría se actualizará con el nuevo nombre y recibirás una confirmación.

### Base de datos

Dentro de esta carpeta, hemos incluido varios archivos esenciales para comprender y trabajar con nuestra base de datos. Primero, tenemos un archivo SQL que contiene la estructura completa de la base de datos, detallando todas las tablas, columnas, y relaciones necesarias. Luego, encontrarán otro archivo con las inserciones de datos, que les permitirá poblar la base de datos con información de prueba. Además, hemos agregado un archivo con diversas consultas SQL que pueden ser útiles para analizar y extraer datos de la base de datos de EduTareas.
- **Archivos Crud:** Cada tabla de la base de datos tiene su propio archivo Python dedicado a las operaciones CRUD (Crear,Leer, Actualizar y Eliminar). A su vez cada uno de estos archivos incluye menús interactivos para facilitar la gestión de datos. 
- **Archivo de consultas INNER JOIN:** un archivo específico que contiene consultas complejas utilizando INNER JOIN para extraer datos relacionados entre diferentes tablas de nuestra base de datos.
Para facilitar aún más la comprensión de la estructura de nuestra base de datos, también hemos incluido dos diagramas: el diagrama Crow’s Foot y el diagrama entidad-relación. Estos diagramas proporcionan una representación visual de las tablas y las relaciones entre ellas, haciendo que sea más fácil entender cómo se organiza y se conecta toda la información.

A continuacion una explicacion del funcionamiento de los archivos.py CRUD e INNER JOIN: 
Archivos CRUD: 
**CRUD_tarea.py:**
- def obtener_conexion (): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- def crear_tabla():
inserta una nueva tarea en la tabla ‘tarea’
Si se genero correctamente imprime un mensaje exitoso (“tarea creada correctamente”)
- def leer_tareas():
Recupera todas las tareas de la tabla tarea y las imprime.
Si no se encuentran tareas, imprime un mensaje indicando esto,(“no se econtraron tareas”)
 def actualizar tarea():
Actualiza los detalles de una tarea específica identificada por ID_Tarea.
Si falta algún dato esencial, imprime un mensaje de error.
Imprime un mensaje confirmando la actualización de la tarea.
- def borrar_tarea():
Elimina una tarea específica de la tabla tarea identificada por ID_Tarea.
Si no se proporciona un ID_Tarea, imprime un mensaje de error.
Confirma la transacción y cierra la conexión.
Imprime un mensaje confirmando la eliminación de la tarea (tarea,(ID_tarea) eliminada correctamente)
- def mostrar_menu():
Muestra las opciones disponibles para gestionar las tareas (crear, leer, actualizar, borrar, salir).
- def ejecutar_opcion_tareas ():
Dependiendo de la opción seleccionada por el usuario, llama a la función correspondiente para crear, leer, actualizar o borrar una tarea.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_recordatorio.py:**
def obtener_conexion(): 
Establece la conexión con la base de datos Imprime un mensaje si la conexión es exitosa.
- def crear_recordatorio():
Inserta un nuevo recordatorio en la tabla recordatorio con los siguientes detalles (Mensaje, Fecha, Hora, Descripcion, ID_Tarea).
Imprime un mensaje confirmando la creación del recordatorio. (“recordatorio creado correctamente”)
- def leer_recordatorio():
Recupera todos los recordatorios de la tabla recordatorio y los imprime.
Si no se encuentran recordatorios, imprime un mensaje indicando esto (“no se encontraron recordatorios”)
- def actualizar_recordatorio():
Actualiza los detalles de un recordatorio específico identificado por ID_Recordatorio.
Si falta algún dato esencial, imprime un mensaje de error.
Imprime un mensaje confirmando la actualización del recordatorio.
- def Borrar_Recordatorio():
Elimina un recordatorio específico de la tabla recordatorio identificado por ID_Recordatorio.
Imprime un mensaje confirmando la eliminación del recordatorio.
- def mostrar_menu(): 
Muestra las opciones disponibles para gestionar los recordatorios (crear, leer, actualizar, borrar, salir).
- def ejecutar_opcion_recordatorios(): 
Dependiendo de la opción seleccionada por el usuario, llama a la función correspondiente para crear, leer, actualizar o borrar un recordatorio.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_profesor.py:**
- def obtener_conexion(): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- def crear_profesor()
Inserta un nuevo profesor en la tabla profesor con los detalles (ID_Profesor, Nombre_Apellido, Correo_electronico).
Imprime un mensaje confirmando la creación del profesor.(“profesor(ID_profesor) creado correctamente”)
- def leer_Profesores()
Recupera todos los registros de profesores de la tabla profesor y los imprime.
Si no se encuentran registros, imprime un mensaje indicando esto.
- def Actualizar_profesor(): 
Actualiza los detalles de un profesor específico identificado por ID_Profesor.
Si falta algún dato esencial, imprime un mensaje de error.
Imprime un mensaje confirmando la actualización del profesor.
- def borrar_profesor()
Elimina un registro de profesor específico de la tabla profesor identificado por ID_Profesor.
Imprime un mensaje confirmando la eliminación del profesor
- def mostrar_menu_profesores(): 
Muestra las opciones disponibles para gestionar los registros de profesores (crear, leer, actualizar, borrar, salir).
- def ejecutar_opcion_profesores()
Dependiendo de la opción seleccionada por el usuario, llama a la función correspondiente para crear, leer, actualizar o borrar un registro de profesor.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_materia.py**
Lista de Días Válidos:
Se define una lista DIAS_VALIDOS que contiene los nombres de los días de la semana (lunes,martes, miercoles, jueves, viernes) utilizados para validar los días ingresados al crear o actualizar una materia.
- def obtener_conexion(): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- def crear_materia():
Valida que el día ingresado esté en la lista de días válidos.
Inserta una nueva materia en la tabla materia con los detalles (Nombre, ID_Profesor, Ubicacion, Dias, Horario).
Imprime "Materia creada correctamente".
- def leer_materias():
Recupera todos los registros de materias de la tabla materia y los imprime.
Si no se encuentran registros, imprime "No se encontraron materias".
Cierra la conexión e imprime "Lectura de materias realizada correctamente".
- def actualizar_materia():
Verifica que el ID_Materia esté presente y que los días ingresados sean válidos.
Construye una lista de valores a actualizar y verifica que al menos un campo adicional a ID_Materia se vaya a actualizar.
Construye y ejecuta la consulta SQL de actualización.
Imprime ("Materia actualizada correctamente".)
- def borrar_materia():
Elimina un registro de materia específico de la tabla materia identificado por ID_Materia.
Imprime "Materia borrada correctamente".
- def mostrar_menu_materias():
Muestra las opciones disponibles para gestionar los registros de materias (crear, leer, actualizar, borrar, salir).
- ejecutar_opcion_materias():
Dependiendo de la opción seleccionada por el usuario, llama a la función correspondiente para crear, leer, actualizar o borrar un registro de materia.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_inscripciones.py**
- def obtener_conexion(): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- def crear_inscripcion():
Inserta una nueva inscripción en la tabla inscripcion con los detalles (ID_Estudiante, ID_Curso, Fecha_Inscripcion, Nota_Final).
Imprime "Inscripción creada correctamente".
- def leer_inscripciones():
Recupera todos los registros de inscripciones de la tabla inscripcion y los imprime.
Si no se encuentran registros, imprime "No se encontraron inscripciones".
Cierra la conexión e imprime "Lectura de inscripciones realizada correctamente".
- actualizar_inscripcion():
Verifica que todos los campos estén presentes (ID_Estudiante, ID_Curso, Fecha_Inscripcion, Nota_Final).
Construye y ejecuta la consulta SQL de actualización.
Imprime "Inscripción actualizada correctamente".
- borrar_inscripcion():
Elimina un registro de inscripción específico de la tabla inscripcion identificado por ID_Estudiante y ID_Curso.
Imprime "Inscripción borrada correctamente".
- def mostrar_menu_inscripciones():
Muestra las opciones disponibles para gestionar los registros de inscripciones (crear, leer, actualizar, borrar, salir).
- def ejecutar_opcion_inscripciones():
Dependiendo de la opción seleccionada por el usuario, llama a la función correspondiente para crear, leer, actualizar o borrar un registro de inscripción.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_evento.py**
- def obtener_conexion(): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- def crear_evento():
Inserta un nuevo evento en la tabla evento con los detalles proporcionados (ID_Evento, Fecha, ID_Calendario).
Imprime "Evento creado correctamente".
- def leer_eventos():
Recupera todos los registros de eventos de la tabla evento y los imprime.
Si no se encuentran registros, imprime "No se encontraron eventos".
Cierra la conexión e imprime "Lectura de eventos realizada correctamente".
- def actualizar_evento():
Verifica que todos los campos estén presentes (ID_Evento, Fecha, ID_Calendario).
Construye y ejecuta la consulta SQL de actualización.
Imprime "Evento actualizado correctamente".
- def borrar_evento():
Elimina un registro de evento específico de la tabla evento identificado por ID_Evento.
Imprime "Evento borrado correctamente".
Menú Interactivo:
- def mostrar_menu_eventos():
Muestra las opciones disponibles para gestionar los registros de eventos (crear, leer, actualizar, borrar, salir).
- def ejecutar_opcion_eventos():
Dependiendo de la opción seleccionada por el usuario, llama a la función correspondiente para crear, leer, actualizar o borrar un registro de evento.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_estudiante.py**
- def obtener_conexion(): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- def crear_estudiante():
Inserta un nuevo registro de estudiante en la tabla estudiante con los detalles (id_estudiante, nombre_apellido, fecha_nacimiento, edad, correo_electronico, telefono).
- def leer_estudiantes():
Recupera todos los registros de estudiantes de la tabla estudiante y los imprime.
Si no se encuentran registros, imprime "No se encontraron estudiantes”.
- def actualizar_estudiante):
Verifica que todos los campos estén presentes (ID_Estudiante, Nombre_Apellido, Fecha_nacimiento, Edad, Correo_electronico, Telefono).
ejecuta la actualizacion. 
- def borrar_estudiante():
Elimina un registro de estudiante específico de la tabla estudiante identificado por ID_Estudiante.
- def mostrar_menu_estudiantes):
Muestra las opciones disponibles para gestionar los registros de estudiantes (crear, leer, actualizar, borrar, salir).
def ejecutar_opcion_estudiantes):
Dependiendo de la opción seleccionada por el usuario, llama a la función correspondiente para crear, leer, actualizar o borrar un registro de estudiante.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_curso_profesor_py**
- def obtener_conexion(): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- def crear_curso_profesor(): 
Inserta un nuevo registro de curso asignado a un profesor en la tabla curso_profesor con los detalles(ID_Curso, ID_Profesor, Año_academico, Semestre).
Imprime "Curso de profesor creado correctamente".
- def leer_cursos_profesor():
Recupera todos los registros de cursos asignados a profesores de la tabla curso_profesor y los imprime.
Si no se encuentran registros, imprime "No se encontraron cursos de profesor".
Cierra la conexión y confirma la lectura exitosa.
- def actualizar_curso_profesor ():
Verifica que todos los campos estén presentes (ID_Curso, ID_Profesor, Año_academico, Semestre).
ejecuta la actualizacion
Imprime "Curso de profesor actualizado correctamente".
- def borrar_curso_profesor):
Elimina un registro de curso asignado a un profesor específico de la tabla curso_profesor identificado por ID_Curso.
Imprime "Curso de profesor borrado correctamente".
- Menú Interactivo:
- def mostrar_menu_cursos_profesor ():
Muestra las opciones disponibles para gestionar los registros de cursos asignados a profesores (crear, leer, actualizar, borrar, salir).
def ejecutar_opcion_cursos_profesor():llama a la función correspondiente para crear, leer, actualizar o borrar un registro de curso asignado a un profesor.
Solicita al usuario los datos necesarios para realizar la operación.
Maneja la opción de salir del programa.

**CRUD_curso.py:**
- def obtener_conexion(): 
Establece la conexión con la base de datos
Imprime un mensaje si la conexión es exitosa.
- Función crear_curso()
con los siguientes detalles (ID_Curso, Nombre_Curso, Descripcion_Curso) Inserta un nuevo curso en la tabla curso de la base de datos.
Imprime "Curso creado correctamente" después de que la operación de inserción haya sido exitosa.
- def leer_cursos():
Recupera todos los cursos existentes desde la tabla curso y los imprime.
Si no se encuentran cursos en la tabla, imprime "No se encontraron cursos."
Después de imprimir los cursos (si hay), imprime "Lectura de cursos realizada correctamente".
- def actualizar_curso
Actualiza los datos de un curso (ID_Curso, Nombre_Curso=None, Descripcion_Curso=None):
específico en la tabla curso con los siguientes detalles
Imprime "Curso actualizado correctamente" después de que la operación de actualización haya sido exitosa.
- Función borrar_curso(ID_Curso):
Elimina un curso específico de la tabla curso.
Imprime "Curso borrado correctamente" después de que la operación de eliminación haya sido exitosa.

**CRUD_calendario.py:**
- def crear_calendario
Inserta un nuevo registro de calendario en la tabla calendario con los siguientes detalles(ID_Calendario, Tipo, Fecha, ID_Profesor) .
Imprime "Calendario creado correctamente" después de que la operación de inserción haya sido exitosa.
- Función leer_calendarios():
Recupera todos los registros de calendarios desde la tabla calendario.
Imprime cada calendario encontrado o imprime "No se encontraron calendarios" si la tabla está vacía.
Después de imprimir los calendarios (si hay), imprime "Lectura de calendarios realizada correctamente".
- def actualizar_calendario()
Actualiza los datos de un calendario específico en la tabla calendario.
Verifica que los campos requeridos (ID_Calendario, Tipo y Fecha) estén presentes antes de ejecutar la actualización.
Imprime "Calendario actualizado correctamente" después de que la operación de actualización haya sido exitosa.
- def borrar_calendario()
Elimina un calendario específico de la tabla calendario basado en el ID_Calendario proporcionado.
Imprime "Calendario borrado correctamente" después de que la operación de eliminación haya sido exitosa.

**Consultas_join.py**
- Función leer_datos_con_join_inscripcion_estudiante():
Realiza una consulta que combina datos de la tabla inscripcion y estudiante usando INNER JOIN.
Imprime los resultados en formato de tabla utilizando tabulate.
Imprime un mensaje de error si ocurre algún problema durante la ejecución de la consulta.
- Función leer_datos_con_join_inscripcion_cursos():
Realiza una consulta que combina datos de la tabla inscripcion y curso usando INNER JOIN.
Imprime los resultados en formato de tabla utilizando tabulate.
Imprime un mensaje de error si ocurre algún problema durante la ejecución de la consulta.
- Función leer_datos_con_join_nombre_profesor():
Realiza una consulta que combina datos de la tabla curso_profesor y profesor usando INNER JOIN.
Imprime los resultados en formato de tabla utilizando tabulate.
Imprime un mensaje de error si ocurre algún problema durante la ejecución de la consulta.
- Función leer_datos_con_join_materias_con_tareas():
Realiza una consulta que combina datos de la tabla tarea_materia y tarea usando INNER JOIN.
Imprime los resultados en formato de tabla utilizando tabulate.
Imprime un mensaje de error si ocurre algún problema durante la ejecución de la consulta.
- Función leer_datos_con_join_mails():
Realiza una consulta que combina datos de la tabla estudiante y estudiante_compartir usando INNER JOIN.
Imprime los resultados en formato de tabla utilizando tabulate.
Imprime un mensaje de error si ocurre algún problema durante la ejecución de la consulta.


 **Aplicación Python:** Se encuentran todos los archivos.py de nuestra aplicación. GUADA
Archivo index.py: 
Código fuente de EduTareas. Está compuesto por varios módulos y funciones que se encargan de realizar distintas operaciones relacionadas con las tareas. Dentro de él podemos encontrar la inicialización de las variables y las funciones, la llamada a dichas variables y funciones, el proceso y finalmente la salida de la información.  
Modulo_Educategorias.py: 
En este archivo se definen las funciones específicas para gestionar categorías dentro de la aplicación. Sirve para:
-Ingreso a una nueva categoría.
-Listado de todas las categorías existentes.
-Modificación de una categoría existente.
-Eliminación de una categoría.
-Salida de la gestión de categorías.
Modulo_Edutarea.py:
En este archivo se definen funciones específicas para gestionar tareas dentro de la aplicación. Sirve para: 
-Ingreso de una nueva tarea.
-Listado de todas las tareas existentes.
-Modificación de una tarea existente.
-Eliminación de una tarea.
-Marcado de una tarea como completa.







### **Wiki**

La Wiki de nuestro repositorio proporciona información detallada y respuestas a preguntas clave relacionadas con los aspectos legales y éticos del proyecto EduTareas SRL. A continuación, se ofrece una breve descripción de las temáticas que encontrarán en la Wiki:
1. **Conformación legal del grupo:** descripción de cómo el grupo se constituye como una entidad legal, incluyendo la estructura de la empresa, los socios, el CEO y los empleados. Detalles sobre los contratos que se establecerán y las cláusulas principales de dichos contratos.
2. **Matriculación Profesional:** identificación de las personas que deben matricularse a nivel provincial para ejercer la profesión.Consecuencias legales a nivel provincial para los miembros del grupo que no completen el trámite de matriculación.
3. **Divulgación de datos internos:** procedimientos legales que deben seguirse si un integrante del grupo divulga datos de la base de datos interna.
4. **Reutilización del código para fines personales:** acciones legales que deben tomarse si un integrante del grupo reutiliza el código para fines personales, según la Legislación de la Provincia de Córdoba y el Código Penal Argentino. Medidas a seguir en caso de reutilización del código a nivel internacional.
5. **Adulteración de la Base de Datos:** instrumentos legales que respaldan a la empresa si la base de datos es adulterada externamente a nivel nacional. procedimientos legales y respaldo si la base de datos es adulterada a nivel internacional.
6. **Negligencia de los Programadores:** instrumentos legales a los que se acude en caso de negligencia por parte de los programadores y la persona responsable de hacerlo.
7. **Reemplazo del sistema por otro proveedor:** directrices éticas para actuar ante el cliente y los colegas si el cliente decide reemplazar el sistema por otro proveedor.
8. **Registro Nacional de Software:** pasos necesarios para que el programa sea parte del Registro Nacional de Software.
9. **Replicación del código:** cómo la Ley de Propiedad Intelectual puede proteger al software si el código es replicado.
10. **Seguridad y protección de datos:** implementación de medidas de seguridad según la Ley de Protección de Datos Personales.
11. **Denuncia por divulgación de datos personales:** legislación a la que un usuario puede recurrir en caso de denunciar a la empresa por divulgación de sus datos personales y cómo la empresa puede respaldarse jurídicamente.
Estas temáticas están diseñadas para proporcionar una guía completa y detallada sobre los aspectos legales y éticos que deben considerarse al utilizar y gestionar el sistema EduTareas SRL. La Wiki actúa como un recurso fundamental para garantizar el cumplimiento de todas las regulaciones pertinentes y para asegurar que las operaciones del grupo se lleven a cabo de manera legal y ética.

**Rquisistos, instalación y base de datos**

En primer lugar, si una persona desea hacer uso de la aplicación deberá asegurarse de tener instalado: Python, MySQL workbench y preferentemente un IDE como Visual Studio Code.
Una vez instalado esos programas deberá instalar en el IDE la biblioteca de Python “mysql-connector-python” desde una nueva terminal. Nos permite conectar Python a nuestra base de datos de MySQL.
Para utilizar nuestra aplicación, la persona deberá clonar nuestro repositorio “ proyecto-tscdia-1” o descargarlo ya que contiene el código de EduTareas, deberá importar la base de datos y luego en el IDE importar “mysql-connecor-python” y configurarlo de la siguiente manera para conectarse a nuestra base de datos:
import mysql.connector config = { 'user': 'root, o el nombre de usuario configurado',
 'password': 'contraseña del usuario',
'host': '127.0.0.1',
'port': 3306,
'database': 'edutareas'
Y finalmente necesitará ejecutar nuestro código principal.
 


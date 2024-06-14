# EduTarea SRL
**Integrantes**

| Nombre y  Apellido  |    DNI    | Correo eléctronico        | Link Git Hub |
|---------------------|-----------|---------------------------|--------------
| Melania Ligorria    | 38412646  | melanialigorria@gmail.com | https://github.com/mel-ligorria
| Miguel Rojas        | 39215582  | rojas.miguel018@gmail.com | https://github.com/Migueerm/ejercitacion-ispc
| Florencia Andrada   | 44788525  | florenciacarolina031@gmail.com | https://github.com/Flor3ncia-Andr4d4
| Carlota Olmedo      | 41711170  | carlota_olmedo@hotmail.com| https://github.com/caolmedo
| Guadalupe Mendoza   | 45934026  | despontinguadalupe@gmail.com |https://github.com/Guadamendoza/SolucionesPracticas 
| Guadalupe Barrozo   | 40203672  | gbarrozosanchez@gmail.com | https://github.com/Guadalupe-S

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

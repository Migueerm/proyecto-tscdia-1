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


# MODULARIZACIÓN - Aplicación EduTarea

**Descripción general**
Esta aplicación permite gestionar tareas, permitiendo al usuario crear, modificar y listar tareas con diferentes estados y categorías. La aplicación está modularizada para facilitar el mantenimiento y la escalabilidad.


**Módulo 2**
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

1. **lista_tareas**: Es una lista vacía que almacenará las tareas en forma de diccionarios. Cada tarea tendrá las siguientes claves: `id`, `descripcion`, `estado` y `categoria`.

### Funciones del código

#### 1. `modificar_estado_tarea()`
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

#### 2. `listar_tareas()`
Esta función lista todas las tareas almacenadas en `lista_tareas` con sus detalles:

1. **Verificación de tareas**:
   - Si no hay tareas en `lista_tareas`, informa al usuario que no hay tareas para mostrar.
   - Si hay tareas:
     - Muestra el listado de tareas con sus detalles (ID, descripción, estado y categoría).



**Módulo 3** 
Esta parte del código define distintas funciones de salida de acuerdo a las acciones que se realicen previamente, de acuerdo a las selecciones realizadas en los módulos 1 y 2. 

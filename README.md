CRUD Manipulación Lista de Clientes.
Este README proporciona una explicación detallada de la aplicación Flask, incluyendo sus rutas y el uso de la API.

Introducción

Esta aplicación Flask está diseñada para administrar la información de clientes a través de una interfaz web y proporciona una API para acceder y manipular los datos de los clientes. Se integra con una base de datos en el backend utilizando el módulo model y expone varias rutas para diferentes operaciones.

Inicio
Instale las dependencias necesarias ejecutando:

pip install flask flask_httpauth

Ejecute la aplicación Flask con:

python app.py

Acceda a la aplicación a través de su navegador navegando a http://localhost:5000.

Rutas y Uso de la API:
Autenticación
    Ruta: /api/login
    Método: GET
    Uso: Esta ruta está protegida mediante Autenticación Básica HTTP. Utilice el nombre de usuario y la contraseña para acceder a las rutas de la API.
Listado y Creación de Clientes
    Ruta: /api/clientes
    Métodos: GET, POST
    Uso:
        GET: Obtiene una lista de todos los clientes desde la base de datos y devuelve datos JSON que contienen los detalles del cliente.
        POST: Crea un nuevo registro de cliente en la base de datos en función de los datos proporcionados en el cuerpo JSON de la solicitud.
    
Detalles del Cliente, Actualización y Eliminación
    Ruta: /api/clientes/<int:id>
    Métodos: GET, PUT, DELETE
    Uso:
        GET: Recupera los detalles de un cliente específico según el ID de cliente proporcionado.
        PUT: Actualiza los detalles de un cliente específico según el ID de cliente proporcionado y los datos en el cuerpo JSON de la solicitud.
        DELETE: Elimina un cliente específico según el ID de cliente proporcionado.

Lógica de Interfaz de Usuario
    Ruta: /

    Métodos: GET
    Uso: Muestra una interfaz de usuario que lista todos los clientes y sus detalles. Utiliza la función show_user_list para renderizar los datos.

    Ruta: /add_user:

    Métodos: GET, POST
    Uso: Proporciona una interfaz de usuario para agregar un nuevo cliente. Acepta datos de formulario a través de una solicitud POST para crear un nuevo cliente.

    Ruta: /edit_user/<int:user_id>:

    Métodos: GET, POST
    Uso: Proporciona una interfaz de usuario para editar los detalles de un cliente específico. Permite la actualización y eliminación de registros de clientes.

Manejo de Errores
    404 No Encontrado: Se implementa un controlador de errores para manejar el caso cuando no se encuentra un recurso. Devuelve una respuesta JSON con el mensaje de error.
Conclusión
    Esta aplicación Flask ofrece una interfaz fácil de usar para administrar la información de los clientes y proporciona una API para acceder de manera programática a los datos de los clientes. Puede interactuar con la aplicación a través de las rutas proporcionadas y realizar operaciones como listar clientes, agregar nuevos clientes, actualizar detalles de clientes y eliminar clientes. La estructura modular de la aplicación permite una fácil expansión y personalización para adaptarse a sus requisitos específicos.
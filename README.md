# Nombre del proyecto Entrega Final

Comision: 54140

Alumno: Castro Luis Martin

Proyecto: Animalix

## Explicacion breve del proyecto en cuanto a funcion

WEB Django con patron MVT

Incluye:
        1.💫 Readme con la explicación del proyecto
        2.💫 Video de no más de 10 minutos
    🕵️ Estructura interna:
        1.💫 una o más aplicaciones creadas
        2.💫 dos modelos con campos de texto, número, fecha
        3.💫 vista de listado de registros de un modelo
        4.💫 vista del detalle de un registro de un modelo
        💫 vista para crear un registro de un modelo
        💫 vista para eliminar un registro de un modelo
        💫 about/ que hable sobre el creador del proyecto
    🕵️ Lógica de usuarios:
        💫 login de usuario
        💫 registro de usuario
        💫 administrador: puede realizar CRUD sobre los modelos
        💫 administrador: subir una imagen de perfil para un usuario
    🕵️ Flujo del proyecto
        💫 Ingresar a la web app desde la ruta base ‘/’ y direccionar a “home”
        💫 navegar entre las diferentes URL sin tener que usar la “barra del navegador”

## Explicacion breve tecnica: urls, modelos, plantillas

El proyecto es un foro donde se registran usuarios y se suben fotos de animales de todo tipo.

Se utilizo una App llamada colaborador para los modelos "Colaborador" e "Imagen".

Se organiza de forma tal en la que sin logearse se puedan ver los "listados" y al logearse se puedan modificar.

Cada modelo tiene su CRUD y plantilla respectiva a cada una de las funcionalidades.

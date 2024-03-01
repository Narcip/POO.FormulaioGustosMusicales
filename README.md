Queremos hacer una base de datos de nuestros amigos y sus gustos musicales, así que vamos a crear un formulario para pedirles una serie de datos a través de nuestra tablet,
ya que nuestro programa está ejecutándose en local... pero resulta que la parte de la pantalla donde se ponen las mayúsculas se ha estropeado por lo que solo pueden escribir en minúsculas, 
así que debemos tratar la información que nos entre por teclado para que se guarde de forma correcta. En lo que respecta a los datos personales, les preguntaremos:

Nombre y apellidos (en mayúsculas, la primera letra de cada palabra)
DNI
Población (en mayúsculas, la primera letra de cada palabra)
País (Todo en mayúsculas)
Como no nos fiamos mucho de nuestros compañeros, hay ciertos campos, como el DNI, que tendremos que comprobar que han puesto la letra y no solo el número, 
además de asegurarnos que han introducido un valor alfanumérico de 9 caracteres.

Por otra parte, queremos saber cuál es su canción favorita, a qué grupo pertenece y cuál es el estilo musical que interpretan. Para que destaque más, 
el estilo debería guardarse todo en mayúsculas.

Ambas informaciones deben ir en clases diferentes pero, para relacionarlo todo y facilitarnos la programación de filtros en un futuro; 
deberemos crear una clase que herede de ambas y definir un método para mostrar por pantalla -de la forma más clara posible- los datos introducidos por nuestro compañero.

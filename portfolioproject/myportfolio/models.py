from django.db import models

# Create your models here.
# myportfolio/models.py

# Modelo para las categorías de los proyectos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para las tecnologías utilizadas en los proyectos
class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para los proyectos del portafolio
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='proyectos/')
    descripcion = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia)
    link_sitio = models.URLField(max_length=200)
    link_repositorio = models.URLField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
#models.py   archivo
#Modelos del formulario

class Contacto(models.Model):
    # Definición del campo 'nombre' como un campo de caracteres con una longitud máxima de 100 caracteres.
    nombre = models.CharField(max_length=100)
    # Definición del campo 'email' como un campo de correo electrónico, que valida automáticamente el formato del correo.
    email = models.EmailField()
    # Definición del campo 'mensaje' como un campo de texto largo, adecuado para almacenar mensajes largos.
    mensaje = models.TextField()
    # Definición del campo 'fecha' como un campo de fecha y hora que se establece automáticamente con la fecha y hora actuales al crear un nuevo registro.
    fecha = models.DateTimeField(auto_now_add=True)
    # Método especial que define cómo se representará el objeto Contacto como una cadena.
    def __str__(self):
        # Devuelve el nombre del contacto como representación en cadena del objeto.
        return self.nombre
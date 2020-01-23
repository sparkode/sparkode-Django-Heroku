from django.db import models

# Create your models here.
#tabla en la que se guardarán los nombres de los tecnológicos y sus claves
class Tecnologico(models.Model):
   Nombre = models.CharField(max_length=40)
   ClavePlantel = models.CharField(max_length=20)

#tabla de los usuarios
class Usuario(models.Model):
   NombreUsuario = models.CharField(max_length=25)
   Nombre = models.CharField(max_length=20)
   ApellidoPaterno = models.CharField(max_length=30)
   ApellidoMaterno = models.CharField(max_length=30)
   Password = models.CharField(max_length=15)
   Email = models.EmailField()
   FechaNacimiento = models.DateField()
   Nivel = models.CharField(max_length=2)
   Progreso = models.IntegerField()
   IdTecnologico = models.ForeignKey(Tecnologico, on_delete=models.CASCADE)
   Foto = models.ImageField(upload_to="perfil", null = True)

  
#Aquí le añadí 3 campos extras, en el cual guardará la cantidad de ejercicios que se le mostrarán al usuario
class Aprendizaje(models.Model):
   Visual = models.FloatField()
   Auditivo = models.FloatField()
   Kinestesico = models.FloatField()
   CantidadVisuales = models.IntegerField()
   CantidadAuditivos = models.IntegerField()
   CantidadKinestesicos = models.IntegerField()
   IdUsuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

#para tener mayor control sobre lo que se le muestra al usuario, se guardan los temas que tiene la plataforma
class Temas(models.Model):
   Nombre = models.CharField(max_length=60)
   Numero=models.IntegerField()
   NSubtemas=models.IntegerField()

#Esta tabla relaciona al usuario con el tema, guardando la evaluación del usuario en dicho tema
class TemaUsuario(models.Model):
   IdUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
   IdTema=models.ForeignKey(Temas, on_delete=models.CASCADE)
   Evaluacion = models.FloatField(null= True,blank=True)

#se almacenan los subtemas para mayor control
class SubTemas(models.Model):
   Nombre = models.CharField(max_length=60)
   Numero=models.IntegerField()
   NEjercicios=models.IntegerField()
   IdTemas = models.ForeignKey(Temas, on_delete=models.CASCADE)

#Aquí se almacenarán los ejercicios y sus calificaciones, el campo fecha va a almacenar fecha y hora para poder 
# controlar a donde dirigir al usuario cuando le de en "continuar", los campos R... no sé qué hacer con ellos :v a ver que sale
class Ejercicio(models.Model):
   IdUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
   IdSubtema=models.ForeignKey(SubTemas, on_delete=models.CASCADE)
   IdTem = models.IntegerField(null = True, blank= True)
   Nombre=models.CharField(max_length=20,null=True,blank=True)
   Tipo = models.CharField(max_length=25)
   Evaluacion = models.FloatField(null = True)
   Fecha=models.DateTimeField(null=True, blank=True)
   R1=models.CharField(max_length=40,null=True,blank=True)
   R2=models.CharField(max_length=40,null=True,blank=True)
   R3=models.CharField(max_length=40,null=True,blank=True)
   R4=models.CharField(max_length=40,null=True,blank=True)
   R5=models.CharField(max_length=40,null=True,blank=True)
   R6=models.CharField(max_length=40,null=True,blank=True)

#Esta tabla guarda los ejercicios resueltos
class EjercicioR(models.Model):
   IdTem = models.ForeignKey(Temas, on_delete=models.CASCADE)
   IdSub = models.ForeignKey(SubTemas, on_delete=models.CASCADE)
   Descripcion = models.CharField(max_length=20,null=True,blank=True)
   NEjer = models.IntegerField()
   Tipo = models.CharField(max_length=20)
   RP1 = models.CharField(max_length=40,null=True,blank=True)
   RP2 = models.CharField(max_length=40,null=True,blank=True)
   RP3 = models.CharField(max_length=40,null=True,blank=True)
   RP4 = models.CharField(max_length=40,null=True,blank=True)
   RP5 = models.CharField(max_length=40,null=True,blank=True)
   RP6 = models.CharField(max_length=40,null=True,blank=True)
   RP7 = models.CharField(max_length=40,null=True,blank=True)
   RP8 = models.CharField(max_length=40,null=True,blank=True)
   RP9 = models.CharField(max_length=40,null=True,blank=True)
   RP10 = models.CharField(max_length=40,null=True,blank=True)

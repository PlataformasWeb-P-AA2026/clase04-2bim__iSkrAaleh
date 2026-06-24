from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre, 
                self.apellido,
                self.cedula)

    def obtener_numero_telefonicos(self):
        return self.numeros_telefonicos.count()

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)

    def obtener_operadora(self):
        # si el teléfono empieza con 099
        if self.telefono.startswith('099'):
            return "Movistar"
        # si el teléfono empieza con 098
        elif self.telefono.startswith('098'):
            return "Claro"
        # si empieza con 09 pero no fue ni 099 ni 098
        elif self.telefono.startswith('09'):
            return "Otra operadora"
        # en caso de que sea un teléfono fijo u otro formato
        else:
            return "Desconocida"

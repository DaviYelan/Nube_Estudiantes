from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Fecha de inscripción")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=150, verbose_name="Autor")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Estudiante",
    )

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} — {self.author}"

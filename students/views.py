from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student, Book
from .forms import StudentForm, BookForm


# ── Estudiantes ────────────────────────────────────────────────────────────────

def student_list(request):
    students = Student.objects.prefetch_related("books").all()
    return render(request, "students/student_list.html", {"students": students})


def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Estudiante creado correctamente.")
        return redirect("student_list")
    return render(request, "students/student_form.html", {"form": form, "title": "Nuevo estudiante"})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, "Estudiante actualizado.")
        return redirect("student_list")
    return render(request, "students/student_form.html", {"form": form, "title": "Editar estudiante"})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.warning(request, "Estudiante eliminado.")
        return redirect("student_list")
    return render(request, "students/confirm_delete.html", {"object": student, "type": "estudiante"})


# ── Libros ─────────────────────────────────────────────────────────────────────

def book_list(request):
    books = Book.objects.select_related("student").all()
    return render(request, "students/book_list.html", {"books": books})


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Libro creado correctamente.")
        return redirect("book_list")
    return render(request, "students/book_form.html", {"form": form, "title": "Nuevo libro"})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, "Libro actualizado.")
        return redirect("book_list")
    return render(request, "students/book_form.html", {"form": form, "title": "Editar libro"})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.warning(request, "Libro eliminado.")
        return redirect("book_list")
    return render(request, "students/confirm_delete.html", {"object": book, "type": "libro"})

from django.db import models

# Create your models here.
class Faculty(models.Model):
    # se crea una clase llamada Faculty que equivale a una tabla el modelo
    faculty_id = models.CharField(max_length=10, primary_key=True)
    faculty_name = models.CharField(max_length=200, null=False)
    faculty_description = models.TextField()
    faculty_imagen = models.ImageField(
        upload_to='faculties/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.faculty_id

class Department(models.Model):
    department_id = models.CharField(max_length=5, primary_key=True)
    department_name = models.CharField(max_length=200, null=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department_imagen = models.ImageField(
            upload_to='departments/',
            blank=True,
            null=True
        )
    

    def __str__(self):
        return self.department_id

class Program(models.Model):
    program_id = models.CharField(max_length=10,primary_key= True)
    program_name = models.CharField(max_length=200, null=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.program_id

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10, primary_key= True)
    teacher_name = models.CharField(max_length=100, null=False)
    teacher_age = models.PositiveIntegerField()
    teacher_email = models.EmailField(null=True)
    teacher_phone = models.CharField(max_length=10)
    teacher_gender = models.CharField(max_length=2)
    teacher_heigth = models.DateTimeField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_id

class Commune(models.Model):
    commune_id = models.CharField(max_length=10, primary_key=True)
    commune_name = models.CharField(max_length=45, null= False)

    def __str__(self):
        return self.commune_id

class Neighborhood(models.Model):
    neighborhood_id = models.CharField(max_length=10, primary_key=True)
    neighborhood_name = models.CharField(max_length=100, null=False)
    commune = models.ForeignKey(Commune,on_delete=models.CASCADE)

    def __str__(self):
        return self.neighborhood_id

class Student(models.Model):
    student:id = models.CharField(max_length=10, primary_key=True)
    student_name = models.CharField(max_length=100, null= False)
    studenet_gender = models.PositiveIntegerField()
    student_email = models.EmailField(null=True)
    student_phone = models.CharField(max_length=10)
    student_date_of_birth = models.DateField()
    student_state = models.BooleanField(True)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)
    neighborhood= models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id

class Subject(models.Model):
    subject_id = models.CharField(max_length=10, primary_key=True)
    subject_name = models.CharField(max_length=100, null=False)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.subject_id

class Score(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    score1 = models.DecimalField(max_digits=4, decimal_places=2)
    score2 = models.DecimalField(max_digits=4, decimal_places=2)
    score3 = models.DecimalField(max_digits=4 , decimal_places=2)
    final_score = models.DecimalField(max_digits=4 , decimal_places=2)
    
    ESTADOS_NOTA = [
    ('Pendiente', 'Pendiente'),
    ('Aprobada', 'Aprobada'),
    ('Reprobada', 'Reprobada'),
]
    state = models.CharField(
        max_length=10,
        choices=ESTADOS_NOTA,
        default='Pendiente'
    )
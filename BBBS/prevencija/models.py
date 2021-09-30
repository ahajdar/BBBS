# Create your models here.

from django.db import models
import uuid

GENDER_MALE = 0
GENDER_FEMALE = 1
SAD = 0
UNDECIDED = 1
HAPPY = 2
STATUS_DA = 1
STATUS_NE = 0

GENDER_CHOICES = [(GENDER_MALE, 'Muško'), (GENDER_FEMALE, 'Žensko')]
SATISFACTION_CHOICES = [(SAD, ':('), (UNDECIDED, ':/'), (HAPPY, ':)')]
STATUS_CHOICES = [(STATUS_DA, 'Aktivan'), (STATUS_NE, 'Neaktivan')]
PROGRAM_CHOICES = [(STATUS_DA, 'U programu'), (STATUS_NE, 'Nije u programu')]


class BaseModel(models.Model):
    """
    The base model which all models should inherit from.
    Provides basic fields which are useful for all models.
    """

    id = models.UUIDField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    repr_fields = ['id']

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        return super().save(*args, **kwargs)

    def __repr__(self) -> str:
        """
        Generic way of handling `__repr__` representations by using `self.repr_fields`.
        """

        field_values = [
            f'`{getattr(self, field)}`'
            for field in self.repr_fields
        ]
        class_name = self.__class__.__name__

        return '{class_name}({field_values})'.format(
            class_name=class_name,
            field_values=', '.join(field_values),
        )


class Coordinator(BaseModel):
    def __str__(self) -> str:
        return str(self.first_name) + " " + str(self.last_name)

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    education = models.CharField(
        max_length=50,
        blank=True,
    )

    gender = models.IntegerField(choices=GENDER_CHOICES, null=False, blank=True, default=GENDER_MALE)

    email = models.EmailField(blank=True)

    phone = models.CharField(
        default='-',
        max_length=20,
    )

    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=True, default=STATUS_DA)

    class Meta:
        verbose_name_plural = "Koordinatori"


class Department(BaseModel):
    def __str__(self) -> str:
        return str(self.name)

    name = models.CharField(
        max_length=50,
    )

    education = models.CharField(
        max_length=50,
        blank=True,
    )

    city = models.CharField(
        max_length=50,
        blank=True,
    )

    email = models.EmailField(blank=True)

    phone = models.CharField(
        default='-',
        max_length=20,
    )

    class Meta:
        verbose_name_plural = "Institucije"


class Volunteer(BaseModel):
    """
    The default Volunteer model, extended to represent customers as well as staff users.
    """

    def __str__(self) -> str:
        return str(self.first_name) + " " + str(self.last_name)

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    education = models.CharField(
        max_length=50,
        blank=True,
    )

    gender = models.IntegerField(choices=GENDER_CHOICES, null=False, blank=True, default=GENDER_MALE)

    email = models.EmailField(blank=True)

    phone = models.CharField(
        default='-',
        max_length=20,
    )

    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=True, default=STATUS_DA)

    class Meta:
        verbose_name_plural = "Volonteri"


class Child(BaseModel):
    def __str__(self) -> str:
        return str(self.child_code)

    child_code = models.CharField(
        max_length=50,
    )

    status = models.IntegerField(choices=PROGRAM_CHOICES, null=False, blank=True, default=STATUS_DA)

    class Meta:
        verbose_name_plural = "Djeca"


class VolunteerReport(BaseModel):
    def __str__(self) -> str:
        return str(self.volunteer) + " (" + str(self.date_completed) + ")"

    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES, null=True, blank=True)
    report = models.TextField(max_length=1000, null=True, blank=True)
    completed = models.BooleanField()

    class Meta:
        verbose_name_plural = "Volonterski izvještaji"


class Mapping(BaseModel):
    def __str__(self) -> str:
        return str(self.volunteer) + " (" + str(self.date_completed) + ")"

    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Organizacija volonetera"

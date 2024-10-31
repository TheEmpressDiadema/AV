from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def gen_directory_path(instance, filename: str) -> str:
    return "gen_{0}/{1}".format(instance.name, filename)

def car_directory_path(instance, filename: str) -> str:
    return "car_{0}/{1}".format(instance.car.vin, filename)

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Наименование марки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return f"Марка id:{self.pk}, имя:{self.name}, создано:{self.created}, изменено:{self.updated}"

class CarModel(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Наименование Модели')
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Марка', related_name="car_models")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return f"Модель id:{self.pk}, имя:{self.name}, марка:{self.brand.name}, создано:{self.created}, изменено:{self.updated}"

class Gen(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, verbose_name='Наименование Поколения')
    model = models.ForeignKey(to='CarModel', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Модель', related_name='gens')
    image = models.ImageField(upload_to=gen_directory_path, blank=False, null=False, verbose_name='Фото поколения')
    release_start = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(3000)
        ],
        verbose_name='Начало выпуска'
    )
    release_end = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[
        MinValueValidator(1900),
        MaxValueValidator(3000)
        ],
        verbose_name='Окончание выпуска'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = "Поколение"
        verbose_name_plural = "Поколения"
        ordering = ['release_start']
        indexes = [
            models.Index(fields=['release_start'])
        ]

    def __str__(self):
        return f"Поколение id:{self.pk}, имя:{self.name}, марка:{self.model.name}, изображение: {self.image}, создано:{self.created}, изменено:{self.updated}"

class Engine(models.Model):

    class FuelType(models.TextChoices):
        PETROL = 'P', "Бензин"
        DIESEL = 'D', "Дизель"
        ELECTRIC = 'E', "Электро"
        HYBRID = 'H', "Гибрид"


    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Наименование Двигателя')
    fuel_type = models.CharField(max_length=1, choices=FuelType.choices, blank=False, null=False, verbose_name='Тип двигателя')
    volume = models.DecimalField(max_digits=2, decimal_places=1, blank=False, null=False, verbose_name='Объем')
    power = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(999)
        ],
        verbose_name='Мощность двигателя, л.с.'
    )
    milage = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='Пробег'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = "Двигатель"
        verbose_name_plural = "Двигатели"
        ordering=['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return f"Двигатель id:{self.pk}, имя:{self.name}, тип:{self.fuel_type}, объем:{self.volume}, мощность:{self.power}, пробег:{self.milage}, создано:{self.created}, изменено:{self.updated}"
    
class Car(models.Model):

    class Colors(models.TextChoices):
        WHITE = 'W', "Белый"
        GRAY = 'G', "Серебристый"
        BLACK = 'B', "Черный"
        YELLOW = 'Y', "Желтый"
        BLUE = 'BL', "Синий"
        OTHER = 'O', "Другой"

    gen = models.ForeignKey(to='Gen', on_delete=models.CASCADE, blank=False, null=False, related_name='cars', verbose_name='Поколение')
    engine = models.ForeignKey(to='Engine', on_delete=models.CASCADE, blank=False, null=False, related_name='cars', verbose_name='Двигатель')
    vin = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='VIN')
    color = models.CharField(max_length=2, choices=Colors.choices, blank=False, null=False, default=Colors.OTHER, verbose_name='Цвет')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = [
            'vin'
        ]
        indexes = [
            models.Index(fields=['vin'])
        ]

    def __str__(self):
        return f"Машина: {self.vin} {self.gen.model.brand.name} {self.gen.model.name} {self.gen.name}, {self.engine.name}, {self.engine.volume}, {self.engine.fuel_type}, {self.color} создано:{self.created} изменено: {self.updated}"

class CarImage(models.Model):
    car = models.ForeignKey(to='Car', on_delete=models.CASCADE, related_name='images', verbose_name='Автомобиль')
    image = models.ImageField(upload_to=car_directory_path, verbose_name='Фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"{self.pk}, {self.image}, {self.created}"
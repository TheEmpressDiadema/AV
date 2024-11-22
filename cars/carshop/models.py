from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

def gen_directory_path(instance, filename: str) -> str:
    return "{0}/{1}/{2}/{3}".format(instance.model.brand.name, instance.model.name, instance.name, filename)

def car_directory_path(instance, filename: str) -> str:
    return "{0}/{1}/{2}/{3}/{4}".format(
        instance.car.gen.model.brand.name,
        instance.car.gen.model.name, 
        instance.car.gen.name,
        instance.car.slug,
        filename)

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Наименование марки')
    slug = models.SlugField(max_length=20, db_index=True, null=False, blank=False, verbose_name='URL')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse("model_list", kwargs={"brand_slug": self.slug})
    
    def get_edit_url(self):
        return reverse("edit_brand", kwargs={"brand_slug" : self.slug})
    
    def save(self, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(**kwargs)
    
    def __str__(self):
        return f"Марка id:{self.pk}, имя:{self.name}, создано:{self.created}, изменено:{self.updated}, url={self.slug}"

class CarModel(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Наименование Модели')
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Марка', related_name="car_models")
    slug = models.SlugField(max_length=30, db_index=True, unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse("gen_list", kwargs={"model_slug" : self.slug, "brand_slug" : self.brand.slug})
    
    def get_edit_url(self):
        return reverse("edit_model", kwargs={"model_slug" : self.slug, "brand_slug" : self.brand.slug})

    def save(self, **kwargs):
        self.slug = slugify("-".join(self.name.split()))
        return super().save(**kwargs)

    def __str__(self):
        return f"Модель id:{self.pk}, имя:{self.name}, марка:{self.brand.name}, создано:{self.created}, изменено:{self.updated}, URL:{self.slug}"

class Gen(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, verbose_name='Наименование Поколения')
    model = models.ForeignKey(to='CarModel', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Модель', related_name='gens')
    slug = models.SlugField(max_length=60, db_index=True, blank=False, null=False, unique=True)
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

    def get_edit_url(self):
        return reverse("edit_gen", kwargs={"model_slug" : self.model.slug, "brand_slug" : self.model.brand.slug, "gen_slug" : self.slug})

    def save(self, **kwargs):
        self.slug = slugify(f"{self.name.split()}-{self.release_start}-{self.release_end}")
        return super().save(**kwargs)
    
    def get_absolute_url(self):
        return reverse("car_list", kwargs={"gen_slug" : self.slug, "model_slug" : self.model.slug, "brand_slug" : self.model.brand.slug})

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
        return f"Двигатель id:{self.pk}, имя:{self.name}, тип:{self.fuel_type}, объем:{self.volume}, мощность:{self.power}, создано:{self.created}, изменено:{self.updated}"
    
class Car(models.Model):

    class Colors(models.TextChoices):
        WHITE = 'W', "Белый"
        GRAY = 'G', "Серебристый"
        BLACK = 'B', "Черный"
        YELLOW = 'Y', "Желтый"
        BLUE = 'BL', "Синий"
        OTHER = 'O', "Другой"

    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Наименование")
    gen = models.ForeignKey(to='Gen', on_delete=models.CASCADE, blank=False, null=False, related_name='cars', verbose_name='Поколение')
    engine = models.ForeignKey(to='Engine', on_delete=models.CASCADE, blank=False, null=False, related_name='cars', verbose_name='Двигатель')
    milage = models.IntegerField(blank=False, null=False, verbose_name='Пробег')
    vin = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='VIN')
    price = models.FloatField(blank=False, null=False, verbose_name="Цена")
    color = models.CharField(max_length=2, choices=Colors.choices, blank=False, null=False, default=Colors.OTHER, verbose_name='Цвет')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=140, db_index=True, blank=False, null=False, unique=True, verbose_name='URL')
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
    
    def get_edit_url(self):
        return reverse("edit_car", kwargs={"car_slug" : self.slug, "gen_slug" : self.gen.slug, "model_slug" : self.gen.model.slug, "brand_slug" : self.gen.model.brand.slug})

    def get_delete_url(self):
        return reverse("delete_car", kwargs={"car_slug" : self.slug, "gen_slug" : self.gen.slug, "model_slug" : self.gen.model.slug, "brand_slug" : self.gen.model.brand.slug})

    def get_absolute_url(self):
        return reverse("car", kwargs={"car_slug" : self.slug, "gen_slug" : self.gen.slug, "model_slug" : self.gen.model.slug, "brand_slug" : self.gen.model.brand.slug})

    def save(self, **kwargs):
        if not self.name:
            self.name = self.gen.model.brand.name + " " + self.gen.model.name + " " + self.gen.name
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            num = 1
            while Car.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        return super().save(**kwargs)

    def __str__(self):
        return f"Машина: {self.pk} {self.vin} {self.slug} {self.gen.model.brand.name} {self.gen.model.name} {self.gen.name}, {self.engine.name}, {self.engine.volume}, {self.engine.fuel_type}, {self.color} создано:{self.created} изменено: {self.updated}"

class CarImage(models.Model):
    car = models.ForeignKey(to='Car', on_delete=models.CASCADE, related_name='images', verbose_name='Автомобиль')
    image = models.ImageField(upload_to=car_directory_path, verbose_name='Фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"{self.pk}, {self.image}, {self.created}"
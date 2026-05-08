from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField("createdAt", auto_now_add=True)
    updatedAt = models.DateTimeField("updatedAt", auto_now=True)

    class Meta:
        abstract = True


# ===========================================================================================


# Create your models here.
class Track(Base):
    # def __init__(self, name, configuration, city, state, length):
    #     self.name = name
    #     self.configuration = configuration
    #     self.city = city
    #     self.state = state
    #     self.length = length

    name = models.CharField(max_length=50, blank=False)
    short_name = models.CharField(max_length=50, null=False)
    configuration = models.CharField(max_length=50, blank=False, default="n/a")
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    length = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    id = models.BigAutoField(primary_key=True)

    def __del__(self):
        pass

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name"], name="unique_name")]


class Team(Base):
    name = models.CharField(max_length=50, blank=False)


class Driver(Base):
    name = models.CharField(max_length=50, blank=False)
    car_number = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Results(Base):
    race_date = models.DateField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start = models.IntegerField(default=0)
    finish = models.IntegerField(default=0)
    greg_picks = models.BooleanField(default=False)
    bob_picks = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=50)
    led = models.IntegerField(default=0)

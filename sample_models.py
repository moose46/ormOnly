import os
from django import setup
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime as dt
from datetime import timedelta
from django.utils import timezone
from django.utils.html import format_html
import string

# Create your models here.


class Base(models.Model):
    now = timezone.datetime
    createdAt = models.DateTimeField("date created", auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    updatedAt = models.DateTimeField("date last updated", auto_now=True, null=True)

    class Meta:
        abstract = True
        # app_label = "beerme"


@admin.display(description="Your Name")
class Person(Base):
    name = models.CharField(max_length=32, default="")

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Player"
        # app_label = "beerme"


# @admin.display(ordering="name")
class Track(Base):
    name = models.CharField(max_length=32, default="", unique=True)
    web_site = models.URLField(max_length=128, null=True, unique=True)

    @admin.display(description="Web Site")
    def www_link(self):
        return format_html(
            '<a style="color: green"; target="blank_" href={}>{}</a>',
            self.web_site,
            self.name,
        )

    def __str__(self) -> str:
        return f"{self.name:<32}"


class Team(Base):
    name = models.CharField(max_length=32, default="", unique=True)
    web_site = models.URLField(max_length=128, null=True, unique=True)

    @admin.display(description="Web Site")
    def www_link(self):
        return format_html(
            '<a style="color: green"; target="blank_" href={}>{}</a>',
            self.web_site,
            self.web_site,
        )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class CrewChief(Base):
    name = models.CharField(max_length=64, default="???", unique=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return string.capwords(self.name)

    class Meta:
        ordering = ["name"]


class Driver(Base):
    name = models.CharField(max_length=32, default="", unique=True)
    web_site = models.URLField(max_length=128, null=True, unique=True)
    team_id = models.ForeignKey(Team, models.CASCADE, null=True)
    crew_chief_id = models.ForeignKey(CrewChief, on_delete=models.CASCADE, null=True)

    @admin.display(description="Web Site")
    def www_link(self):
        return format_html(
            '<a style="color: green"; target="blank_" href={}>{}</a>',
            self.web_site,
            self.web_site,
        )

    def __str__(self) -> str:
        return f"{self.name:32} - Team {self.team_id}"

    def driver_web_site(self):
        return f"<a href={self.web_site}>{self.name}</a>"

    class Meta:
        ordering = ["name"]


class Tv(Base):
    name = models.CharField(max_length=24, default="FOX", null=True, unique=True)

    def __str__(self) -> str:
        return self.name.upper()


class Race(Base):
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE, default=-1)
    race_date = models.DateField(default=dt.date.today, unique=True)
    tv_id = models.ForeignKey(Tv, on_delete=models.CASCADE, null=True)
    web_site = models.URLField(max_length=128, null=True, unique=True)
    nascar_web_site = models.URLField(max_length=128, null=True, unique=True)

    # https://www.espn.com/racing/raceresults/_/series/sprint/raceId/202207100029
    # https://www.espn.com/racing/raceresults/_/series/sprint/raceId/202207034002
    @admin.display
    def track_name(self):
        # race_completed = Race.objects.filter(id=self.track_id.id)
        print(f"-------------- {self.race_date} {dt.datetime.now().date()}")
        if self.race_date < dt.datetime.now().date():
            return format_html('<span style="color: red">{}</span>', self.track_id)
        else:
            return self.track_id

    @admin.display(description="Web Site")
    def www_link(self):
        if self.race_date < dt.datetime.now().date():
            return format_html(
                '<a style="color: red"; target="blank_" href={}>{}</a>',
                self.track_web_site(),
                self.track_id,
            )
        else:
            return format_html(
                '<a style="color: green"; target="blank_" href={}>{}</a>',
                self.track_web_site(),
                self.track_id,
            )

    def www_nascar(self):
        if self.nascar_web_site:
            return format_html(
                '<a style="color: red"; target="blank_" href={}>{}</a>',
                self.nascar_web_site,
                "See Results",
            )
        else:
            return "Not Entered"

    def track_web_site(self):
        # print("...................OK")
        web = Track.objects.filter(id=self.track_id.id)
        return web[0].web_site

    def __str__(self) -> str:
        return f"{self.race_date} - {self.track_id} - {self.tv_id}"

    class Meta:
        ordering = ["race_date"]


class HistoricalData(Base):
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    url = models.URLField(max_length=256)

    @admin.display(description="Web Site")
    def www_link(self):
        return format_html(
            '<a style="color: red"; target="blank_" href={}>{}</a>',
            self.url,
            self.name,
        )

    class Meta:
        unique_together = ("name", "url")

    def __str__(self) -> str:
        return self.name


# https://docs.djangoproject.com/en/dev/ref/models/options/#unique-together
class Result(Base):
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE, null=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    finished = models.IntegerField(default=-1)

    def __str__(self):
        return f"{self.race_id} {self.driver_id} {self.finished}"

    class Meta:
        unique_together = ("race_id", "driver_id", "finished")
        ordering = ["race_id", "finished"]


class Bet(Base):
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE, default=-1)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, default=-1)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, default=-1)
    finish = models.IntegerField(default=-1)
    beer = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.beer:
            award = " --- BEER"
        else:
            award = ""
        return f"{self.person_id} - {self.race_id} - {self.driver_id} Finshed={self.finish} {award}"

    class Meta:
        ordering = ["race_id", "person_id"]


class WeeklyBets(Base):
    def __init__(self, prace_id: str) -> None:
        self.race_date = prace_id
        self.oneBet = Bet.objects.filter(race_id=prace_id)
        # print(self.oneBet)

    def pick_the_winner(self):
        # winner = self.oneBet[0]
        for i in self.oneBet:
            x = i
            if self.oneBet[0].finish > self.oneBet[1].finish:
                winner = self.oneBet[1]
                winner.beer = True
            else:
                winner = self.oneBet[0]
                winner.beer = True
        # print(f"winner 1 = {winner}")
        return winner

    def __str__(self) -> str:
        return self.oneBet


class Cooler(Base):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE, null=True)
    beer = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.beer

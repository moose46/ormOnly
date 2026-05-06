# https://dev.to/ivanyu2021/using-django-orm-only-without-web-server-1oc8

import os

##############################
## Django specific settings (Please this BEFORE import model class)
##############################
import django

try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()
except Exception as e:
    exit(e.__str__())
##############################

from db.models import Track

print("Project started!!")
try:
    tracks = [
        Track(
            created_at,  # empty string
            date_updated,  # empty string
            name,
            short_name,
            configuration,
            city,
            state,
            length,
        )
        for created_at, date_updated, name, short_name, configuration, city, state, length in [
            (
                "",
                "",
                "Bristol Motor Speedway",
                "Bristol",
                "concrete oval",
                "Bristol",
                "Tennessee",
                0.533,
            ),
            (
                "",
                "",
                "Charlotte Motor Speedway",
                "Charlotte",
                "paved quad oval",
                "Charlotte",
                "North Carolina",
                1.50,
            ),
            (
                "",
                "",
                "Circuit of the Americas",
                "COTA",
                "paved road course",
                "Austin",
                "Texas",
                2.326,
            ),
            (
                "",
                "",
                "Darlington Raceway",
                "Darlington",
                "paved egg shaped oval",
                "Darlington",
                "South Carolina",
                1.336,
            ),
            (
                "",
                "",
                "Daytona International Speedway",
                "Daytona",
                "paved tri oval",
                "Daytona",
                "Florida",
                2.5,
            ),
            (
                "",
                "",
                "Dover Motor Speedway",
                "Dover",
                "concrete oval",
                "Dover",
                "Delaware",
                1.0,
            ),
            (
                "",
                "",
                "EchoPark Speedway",
                "Atlanta",
                "paved quad oval",
                "Atlanta",
                "Georgia",
                1.540,
            ),
            (
                "",
                "",
                "Homestead–Miami Speedway",
                "Miami",
                "paved oval",
                "Miami",
                "Florida",
                1.50,
            ),
            (
                "",
                "",
                "Indianapolis Motor Speedway",
                "Indianapolis",
                "paved rectangular oval",
                "Speedway",
                "Indiana",
                2.50,
            ),
            (
                "",
                "",
                "Iowa Speedway",
                "Iowa",
                "paved d-shaped oval",
                "Newton",
                "Iowa",
                0.875,
            ),
            (
                "",
                "",
                "Kansas Speedway",
                "Kansas",
                "paved tri oval",
                "Kansas City",
                "Kansas",
                1.5,
            ),
            (
                "",
                "",
                "Las Vegas Motor Speedway",
                "Las Vegas",
                "paved tri oval",
                "Las Vegas",
                "Nevada",
                1.5,
            ),
            (
                "",
                "",
                "Martinsville Speedway",
                "Martinsville",
                "paved concrete paperclip-shaped oval",
                "Ridgeway",
                "Virginia",
                0.526,
            ),
            (
                "",
                "",
                "Michigan International Speedway",
                "Michigan",
                "paved d-shaped oval",
                "Brooklyn",
                "Michigan",
                2.0,
            ),
            (
                "",
                "",
                "Nashville International Speedway",
                "Nashville",
                "concrete tri oval",
                "Nashville",
                "Tennessee",
                1.333,
            ),
            (
                "",
                "",
                "New Hampshire Motor Speedway",
                "New Hampshire",
                "paved paper-clip-shaped oval",
                "Loudon",
                "New Hampshire",
                1.058,
            ),
            (
                "",
                "",
                "North Wilkesboro Speedway",
                "North Wilkesboro",
                "paved oval",
                "North Wilkesboro",
                "North Carolina",
                0.625,
            ),
            (
                "",
                "",
                "Phoenix Raceway",
                "Phoenix",
                "paved dogleg oval",
                "Avondale",
                "Arizona",
                1.5,
            ),
            (
                "",
                "",
                "Pocono Speedway",
                "Pocono",
                "paved triangular oval",
                "Long Pond",
                "Pennsylvania",
                2.50,
            ),
            (
                "",
                "",
                "Richmond Raceway",
                "Richmond",
                "paved d-shaped oval",
                "Richmond",
                "Virginia",
                0.750,
            ),
            (
                "",
                "",
                "Talladega Superspeedway",
                "Talladega",
                "paved tri oval",
                "Lincoln",
                "Alabama",
                2.66,
            ),
            (
                "",
                "",
                "Watkins Glen International",
                "Watkins Glen",
                "paved road course",
                "Watkins Glen",
                "New York",
                2.450,
            ),
            (
                "",
                "",
                "World Wide Technology Raceway",
                "World Wide Technology Raceway",
                "paved egg shaped oval",
                "Madison",
                "Illinois",
                1.250,
            ),
        ]
    ]
except Exception as e:
    exit(e.__str__())

for track in tracks:
    try:
        # print(track)
        track.save()
        print(f"{track.id}: {track.name} added!")
    except Exception as e:
        # print(e.__str__())
        continue

print("Saved!!")

# track = Track()
# track.name = 'EchoPark Speedway'
# track.configuration = "paved quad oval"
# track.state = "Georgia"
# track.city = "Altanta"
# track.length = 1.540

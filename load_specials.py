import requests
import os
from django.core.management.base import BaseCommand
from apps.applicants.models import GraduateEducation


class Command(BaseCommand):
    help = "Load Graduate Specialities for Education from RTF to ORM"

    def handle(self, *args, **options):
        spec_file = open("specils_list.txt", encoding="utf-8")
        spec = spec_file.read()
        spec_file.close()

        for row in spec.split("\n"):
            code = row.split('#')[0]
            name = row.split('#')[1]
            level = row.split('#')[2]
            if level == "51" or level == "52":
                level = "CL"
            elif level == "62":
                level = "BA"
            elif level == "68":
                level = "MA"
            elif level == "65":
                level = "SP"
            print(f"code:{code} name:{name} level: {level}")

            orm = GraduateEducation(
                name=name,
                code=code,
                level=level,
            )
            orm.save()

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Crea los grupos de usuario: Miembro y Moderador'

    def handle(self, *args, **kwargs):
        grupos = ['Miembro', 'Moderador']
        for nombre in grupos:
            grupo, creado = Group.objects.get_or_create(name=nombre)
            if creado:
                self.stdout.write(self.style.SUCCESS(f'Grupo "{nombre}" creado.'))
            else:
                self.stdout.write(f'Grupo "{nombre}" ya existía.')
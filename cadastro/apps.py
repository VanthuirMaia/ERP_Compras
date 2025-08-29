from django.apps import AppConfig

class CadastroConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cadastro"

    def ready(self):
        # Importa aqui dentro, só depois que os apps estiverem prontos
        from django.contrib.auth.models import Group
        from django.db.utils import OperationalError

        try:
            for role in ["Gerência", "Compras", "Solicitante"]:
                Group.objects.get_or_create(name=role)
        except OperationalError:
            # Isso evita erro quando o banco ainda não está migrado
            pass

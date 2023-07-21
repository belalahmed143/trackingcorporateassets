from django.apps import AppConfig


class CompaniesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'companies_app'

    def ready(self):
        import companies_app.signals
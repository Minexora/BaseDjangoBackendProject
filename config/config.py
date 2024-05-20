from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DJANGO_PROJEECT",
    environments=True,
    settings_files=["config/settings.toml", "config/.secrets.toml"],
)

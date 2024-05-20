from django.db import models
from django.contrib.auth.models import AbstractUser

from api.utils import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    if settings.login.login_field == "email":
        USERNAME_FIELD = "email"
        REQUIRED_FIELDS = ["username"]
    else:
        USERNAME_FIELD = "username"
        REQUIRED_FIELDS = ["email"]

    def __str__(self):
        if settings.login.login_field == "email":
            return self.email
        else:
            return self.username


class LogTypes:
    LOGIN = 1
    LOGOUT = 2
    SELECT = 3
    SAVE = 4
    UPDATE = 5
    DELETE = 6


LOG_TYPES = (
    (LogTypes.LOGIN, "Login"),
    (LogTypes.LOGOUT, "Logout"),
    (LogTypes.SAVE, "Save"),
    (LogTypes.UPDATE, "Update"),
    (LogTypes.DELETE, "Delete"),
    (LogTypes.SELECT, "Select"),
)


class Log:
    table_name = models.CharField(max_length=512, verbose_name="Tablo Adı")
    record_id = models.PositiveIntegerField(verbose_name="Kayıt ID")
    changes = models.JSONField(verbose_name="Değişiklikler")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Kullanıcı", help_text="Değişikliği yapan kullanıcı")
    ip_address = models.GenericIPAddressField(verbose_name="İp Adresi", help_text="Değişiklik isteğinin geldiği ip")
    log_type = models.PositiveSmallIntegerField(choices=LOG_TYPES, verbose_name="Log Tipi", default=LogTypes.SELECT)
    description = models.TextField(verbose_name="Açıklama", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Zaman")

    def __str__(self):
        return f"{self.user} - {self.table_name} - {self.record_id} - {self.timestamp}"

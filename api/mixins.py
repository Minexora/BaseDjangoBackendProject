from django.db import models
from api.models import LogTypes
from api.services import save_log_to_database


class LoggingMixin(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        ip_address = kwargs.pop("ip_address", None)

        if self.pk:
            old_instance = self.__class__.objects.get(pk=self.pk)
            old_values = {field.name: getattr(old_instance, field.name) for field in self._meta.fields}
        else:
            old_values = {}

        super().save(*args, **kwargs)

        new_values = {field.name: getattr(self, field.name) for field in self._meta.fields}

        changes = {}
        for key in new_values.keys():
            if old_values.get(key) != new_values[key]:
                changes[key] = {"old": old_values.get(key), "new": new_values[key]}

        if changes:
            save_log_to_database(
                table_name=self._meta.db_table,
                record_id=self.pk,
                user=user,
                ip_address=ip_address,
                log_type=LogTypes.UPDATE if old_values else LogTypes.SAVE,
                changes=changes,
            )

    def delete(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        ip_address = kwargs.pop("ip_address", None)

        old_values = {field.name: getattr(self, field.name) for field in self._meta.fields}

        save_log_to_database(
            table_name=self._meta.db_table,
            record_id=self.pk,
            user=user,
            ip_address=ip_address,
            log_type=LogTypes.DELETE,
            changes=old_values,
        )

        super().delete(*args, **kwargs)

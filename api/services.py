from django.shortcuts import get_object_or_404

from api.utils import console_log
from api.models import (
    CustomUser,
    Log,
)


def get_user(user_id):
    try:
        return get_object_or_404(CustomUser, id=user_id)
    except Exception as e:
        console_log.error(f"services -> get_user -> {str(e)}")
        return None


def save_log_to_database(table_name, record_id, user, ip_address, log_type, changes={}):
    try:
        log_entry = Log(
            table_name=table_name,
            record_id=record_id,
            changes=changes,
            user=user,
            ip_address=ip_address,
            log_type=log_type,
        )
        log_entry.save()
    except Exception as e:
        console_log.error(f"services -> save_log_to_database -> {str(e)}")

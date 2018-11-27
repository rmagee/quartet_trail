from django.dispatch import receiver
from simple_history.signals import (
    post_create_historical_record
)
from quartet_trail import models
import json
from django.conf import settings

delete_change_records = getattr(settings,
                               'TRAIL_DELETE_CHANGE_RECORDS',
                               False)

@receiver(post_create_historical_record)
def post_create_historical_record_callback(sender, **kwargs):
    import pudb; pudb.set_trace()
    print("Sent after saving historical record")
    history_instance = kwargs['history_instance']
    previous_record = None
    delta = None
    try:
        previous_record = kwargs['history_instance'].prev_record
    except:
        pass
    trail_delta = models.QuartetTrailDelta()
    trail_delta.model_name = models.get_model_fullname(kwargs['instance']._meta.model)
    trail_delta.model_pk = kwargs['instance'].id
    trail_delta.date = history_instance.history_date
    trail_delta.change_type = history_instance.history_type
    trail_delta.username = history_instance.history_user.username
    
    if previous_record:
        delta = history_instance.diff_against(previous_record)
        change_text = {}
        for change in delta.changes:
            change_text[change.field] = {"old": change.old, "new": change.new}
        trail_delta.change = json.dumps(change_text)
        trail_delta.save()
        if delete_change_records and previous_record.history_type == "~":
            # delete previous record.
            previous_record.delete()
    else:
        trail_delta.save()

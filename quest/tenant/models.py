from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from datetime import datetime


class Tenant(TimeStampedModel):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=20, unique=True)
    daily_access_limit = models.IntegerField(default=100)
    remaining_access_count = models.IntegerField(default=100)
    throttle = models.IntegerField(default=1)
    throttle_duration = models.IntegerField(
        default=10,
        help_text=_("Throttle limit duration in seconds"),
    )

    def is_access_allowed(self):
        self.modified = self.modified.replace(tzinfo=None)
        time_since_last_access = (datetime.now() - self.modified).total_seconds()
        print("time_since_last_access ", time_since_last_access)
        if self.remaining_access_count == 0 and time_since_last_access < 10:
            return False
        return True

    def update_access_count(self):
        if self.remaining_access_count > 0:
            self.remaining_access_count -= 1
            self.save()

    @staticmethod
    def access_count():
        tenant_dict = dict()
        for tenant in Tenant.objects.all():
            tenant_dict[tenant.name] = tenant.daily_access_limit - tenant.remaining_access_count
        return tenant_dict

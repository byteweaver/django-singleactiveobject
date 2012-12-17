from django.db import models
from django.utils.translation import ugettext as _


class SingleActiveObjectManager(models.Manager):
    def get_active_object(self):
        try:
            return self.get(active=True)
        except models.ObjectDoesNotExist:
            return None


class SingleActiveObjectMixin(models.Model):
    active = models.BooleanField(_("Active"), default=False)

    objects = SingleActiveObjectManager()

    class Meta:
        abstract = True
        ordering = ['-active']

    def save(self, *args, **kwargs):
        if self.active:
            try:
                currently_active = self.__class__.objects.get(active=True)
            except self.__class__.DoesNotExist:
                pass
            else:
                currently_active.active = False
                currently_active.save()
        return super(SingleActiveObjectMixin, self).save(*args, **kwargs)

    def get_state_string(self):
        if self.active:
            state = _("active")
        else:
            state = _("not active")
        return state


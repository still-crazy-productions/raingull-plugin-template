from django.db import models

class ExamplePluginMessage(models.Model):
    raw_message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='new')

    class Meta:
        db_table = "example_plugin_messages"
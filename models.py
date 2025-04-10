import uuid
from django.db import models

class PluginIncomingMessage(models.Model):
    raingull_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    raw_message = models.TextField()
    snippet = models.CharField(max_length=255, blank=True)
    received_timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='new')

    class Meta:
        db_table = "pluginname_incoming_messages"

class PluginOutgoingMessage(models.Model):
    raingull_id = models.UUIDField(editable=False, db_index=True)
    formatted_message = models.TextField()
    snippet = models.CharField(max_length=255, blank=True)
    queued_timestamp = models.DateTimeField(auto_now_add=True)
    sent_timestamp = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='queued')

    class Meta:
        db_table = "pluginname_outgoing_messages"

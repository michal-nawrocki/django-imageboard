from drf_extra_fields import relations
from rest_framework import serializers

from boards.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["entry_id", "creation_datetime", "email", "topic",
                  "text", "file", "hide_file", "embed", "password"]

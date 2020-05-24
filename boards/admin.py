from django.contrib import admin

from .models import Entry, PostEntry, ThreadEntry

admin.site.register(Entry)
admin.site.register(PostEntry)
admin.site.register(ThreadEntry)

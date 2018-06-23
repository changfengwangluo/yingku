import xadmin
from .models import Comments

class CommentsAdmin(object):
    list_display=['content']
    search_fields=['content']
    list_filter=['content']

xadmin.site.register(Comments,CommentsAdmin)
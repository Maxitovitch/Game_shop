from django.contrib import admin
from .models import Genre, Game, Order, SupportTicket



admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Order)



@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'created_at')
    search_fields = ('subject', 'email')




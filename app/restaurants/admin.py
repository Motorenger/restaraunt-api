from django.contrib import admin

from .models import Restaurant, VoteMenus


class VoteMenusInline(admin.TabularInline): 
    model = VoteMenus
    extra = 2


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        VoteMenusInline,
    ]


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(VoteMenus)

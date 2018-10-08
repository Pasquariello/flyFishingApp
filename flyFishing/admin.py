from django.contrib import admin

# Register your models here.
from .models import River, Fish, League, Player #FishPerRiver

class RiverInline(admin.StackedInline):
    model = River
    extra = 0

class FishInLine(admin.StackedInline):
    model = Fish   
    extra = 0

# class FishPerRiverInLine(admin.StackedInline):
#     model = FishPerRiver
#     extra = 0

class LeagueAdmin(admin.ModelAdmin):
    
    inlines = [RiverInline, FishInLine]

# class RiverAdmin(admin.ModelAdmin):
    
#     inlines = [FishPerRiverInLine ]


admin.site.register(River)
admin.site.register(Fish)
admin.site.register(League, LeagueAdmin)
admin.site.register(Player)
# admin.site.register(FishPerRiver)
from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, chai_certificate


# Register ChaiVariety model
@admin.register(ChaiVariety)
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('name',)


# Register ChaiReview model
@admin.register(ChaiReview)
class ChaiReviewAdmin(admin.ModelAdmin):
    list_display = ('chai', 'user', 'ratings', 'date_added')
    list_filter = ('ratings', 'date_added')
    search_fields = ('user__username', 'chai__name')


# Register Store model
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')


# Register chai_certificate model
@admin.register(chai_certificate)
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'chai', 'issued_date', 'validate')
    search_fields = ('certificate_number',)
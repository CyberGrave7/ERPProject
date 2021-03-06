__author__ = 'FARID ILHAM Al-Q'

from django.contrib import admin
from django import forms
from Apps.Inventory.product.models import *
from django.utils.translation import ugettext_lazy as _
from suit.widgets import EnclosedInput

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type', 'display_image']
    list_filter = ['type']
    search_fields = ['type', 'description']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            request = kwargs.pop("request", None)
            kwargs['widget'] = ProductImage
            return db_field.formfield(**kwargs)
        return super(CategoryAdmin,self).formfield_for_dbfield(db_field, **kwargs)

    def suit_cell_attributes(self, obj, column):
        if column == 'display_image':
            return {'class': 'text-center'}

admin.site.register(Category, CategoryAdmin)

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

class ProductImage(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="%s" target="_blank"><img width="150px" height="150px" src="%s" alt="%s" /></a> %s ' % \
                (image_url, image_url, file_name, _(' ')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class FormProduct(forms.ModelForm):

    class Meta:
        widgets = {
            'capacity': EnclosedInput(append='ml', attrs={'class': 'input-small'}),
            'height': EnclosedInput(append='mm', attrs={'class': 'input-small'}),
            'weight': EnclosedInput(append='gr', attrs={'class': 'input-small'}),
            'diameter': EnclosedInput(append='mm', attrs={'class': 'input-small'}),
        }


class ProductItemAdmin(admin.ModelAdmin):
    form = FormProduct
    list_display = ['code_item', 'name_item', 'display_color', 'category', 'display_image']
    list_filter = ['category']
    search_fields = ['code_item', 'name_item', 'color', 'capacity', 'height', 'weight', 'diameter']
    suit_form_tabs = (('data', 'Data Botol'), ('detail', 'Detail Botol'))
    fieldsets = [
        (
            None, {'classes': ('suit-tab suit-tab-data',),
                   'fields': ['code_item', 'name_item', 'category', 'color', 'description']
                   }
        ),
        (
            None, {'classes': ('suit-tab suit-tab-detail',),
                   'fields': ['capacity', 'weight', 'height', 'diameter', 'image', 'design']
                   }
        )
    ]

    def suit_cell_attributes(self, obj, column):
        if column == 'display_image':
            return {'class': 'text-center'}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            request = kwargs.pop("request", None)
            kwargs['widget'] = ProductImage
            return db_field.formfield(**kwargs)
        elif db_field.name == 'design':
            request = kwargs.pop("request", None)
            kwargs['widget'] = ProductImage
            return db_field.formfield(**kwargs)
        return super(ProductItemAdmin,self).formfield_for_dbfield(db_field, **kwargs)
admin.site.register(ProductItem, ProductItemAdmin)

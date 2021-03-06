''' @author: Fery Febriyan Syah '''


from django.contrib import admin
from Apps.Hrm.Master_Salary.models import *

class Operational_SupportAdmin (admin.ModelAdmin):
    list_display = ('group','currency','display_price',)
    list_search = ['group']
    
admin.site.register(Operational_Support, Operational_SupportAdmin)

class Shift_Operational_SupportAdmin (admin.ModelAdmin):
    list_display = ('group','currency','display_price',)
    list_search = ['group']

admin.site.register(Shift_Operational_Support, Shift_Operational_SupportAdmin)
    
class Shift_Operational_SupportingAdmin (admin.ModelAdmin):
    list_display = ('group','currency','display_price',)
    list_search = ['group']

admin.site.register(Shift_Operational_Supporting, Shift_Operational_SupportingAdmin)
    
class Position_SupportAdmin (admin.ModelAdmin):
    list_display = ('master_position','currency','display_price',)
    list_search = ['master_position']

admin.site.register(Position_Support, Position_SupportAdmin)
    
class Life_Cost_SupportAdmin (admin.ModelAdmin):
    list_display = ('master_position','currency','display_price',)
    list_search = ['master_position']
    
admin.site.register(Life_Cost_Support, Life_Cost_SupportAdmin)
    
class Transport_SupportAdmin (admin.ModelAdmin):
    list_display = ('group','currency','display_price',)
    list_search = ['group']

admin.site.register(Transport_Support, Transport_SupportAdmin)

class Basic_SalaryAdmin (admin.ModelAdmin):
    list_display = ('group','currency','display_price',)
    list_search = ['group']

admin.site.register(Basic_Salary, Basic_SalaryAdmin)
    
class Credit_BankAdmin (admin.ModelAdmin):
    list_display = ('name','currency','display_price','name_bank',)
    list_search = ['name']

admin.site.register(Credit_Bank, Credit_BankAdmin)
"""    
class OvertimeAdmin (admin.ModelAdmin):
    list_display = ('month','employee','duration_overtime',)
    list_search = ['month']
    
admin.site.register(Overtime, OvertimeAdmin)

class Set_of_OvertimeAdmin (admin.ModelAdmin):
    list_display = ('low','high','precentage')
    
admin.site.register(Set_of_Overtime, Set_of_OvertimeAdmin)
"""    

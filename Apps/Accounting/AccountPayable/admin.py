"""Develop By - Achmad Afiffudin N"""

from django.contrib import admin
from Apps.Accounting.AccountPayable.models import *
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from datetime import datetime
from decimal import Decimal
from django.http import HttpResponse
from Apps.Procurement.purchaseOrder.models import Purchase_Order
from Apps.Procurement.vendor.admin import *
from Apps.Hrm.FromHrm.models import Tr_Payroll
from admin_decorators import allow_tags
from suit.widgets import *

class PPInline(admin.TabularInline):
    model = Data_Purchase_Request
    extra = 0
    max_num = 0
    verbose_name_plural = 'Detail PP'
    can_delete = False
    fields = ('header_purchase_request_id', 'request_goods_name', 'request_used',
              'request_amount','currency_id','request_unit_price','request_total_rupiah','request_total_price',)
    readonly_fields =('header_purchase_request_id','request_goods_name', 'request_used','request_amount',
                      'currency_id','request_unit_price','request_total_rupiah','request_total_price',)

class ROInline(admin.TabularInline):
    model = Data_Rush_Order
    extra = 0
    max_num = 0
    verbose_name_plural = 'Detail RO'
    can_delete = False
    fields = ('header_rush_order_id', 'ro_goods_name', 'ro_used',
              'ro_amount','currency_id','ro_unit_price','ro_total_rupiah','ro_total_price',)
    readonly_fields =('header_rush_order_id','ro_goods_name', 'ro_used','ro_amount',
                      'currency_id','ro_unit_price','ro_total_rupiah','ro_total_price',)


class Detail_Purchase_AccountInline(admin.TabularInline):
    model = Detail_Purchase_Account
    can_delete = False
    verbose_name_plural = 'Akun PO'
    list_per_page  = 2
    max_num = 2
    fields = ['PO','Account','Type',]

    def get_readonly_fields(self, request, obj=None):
        user = Group.objects.get(user=request.user)
        readonly_fields = ()
        if request.user.is_superuser or user.name == 'staf_akuntansi':
            readonly_fields = ()
        else:
            readonly_fields = ('PO','Account','Type',)
        return readonly_fields
    
class Payable_POAdmin(admin.ModelAdmin):   
    list_display = ('no_reg','vendor','Period','Journal','total_expenditure',)
    list_filter = ('no_reg','vendor',)
    ordering = ('-id', )
    date_hierarchy = 'po_add_date'    
    search_fields = ['no_reg__vendor', ]
    readonly_fields= ('no_reg','vendor','Period','Journal','po_add_date','set_of_delay','po_agreementx','total_expenditure',)
    exclude = ('po_status','po_month','ship_to','delay_fine','goods_receipt_plan','po_agreement',)
    inlines = [PPInline,ROInline,Detail_Purchase_AccountInline,]
            
    def suit_row_attributes(self, obj, request):
		css_class = {
			'Akun Terisi': 'success','Akun Tidak Lengkap': 'warning', 'Akun Kosong': 'error'}.get(obj.status())
		if css_class:
			return {'class': css_class, 'data': obj.status()}

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False
    """
    def get_form(self, request, obj=None, **kwargs):
        form = super(Payable_POAdmin, self).get_form(request, obj, **kwargs)
        user = Group.objects.get(user=request.user)
        self.inlines = []
        if getattr(obj, 'id', None) == None:
            self.inlines += [PPInline,Detail_Purchase_AccountInline,]
        else:
            self.inlines += [PPInline,Detail_Purchase_AccountInline,]
        return form
    """
    def queryset(self, request):
        return Payable_PO.objects.filter(Q(po_status=21) | Q(po_status=22) | Q(po_status=23))

admin.site.register(Payable_PO,Payable_POAdmin)

class FormPP(forms.ModelForm):
    class Meta:
        widgets = {
            'Bank_Payment': LinkedSelect(attrs={'class': 'input-large'}),
            'Cash_Payment': LinkedSelect(attrs={'class': 'input-large'}),
            'Memo' : Textarea(attrs={'rows': '3'}),
            'Date': SuitDateWidget
        }

class Tr_Purchase_PayInline(admin.StackedInline):
    model = Tr_Purchase_Payment
    form = FormPP
    can_delete = True
    verbose_name_plural = 'Pembayaran'
    list_per_page  = 5
    max_num = 5
    extra = 1
    fields = ['Paid_Amount','Date','Bank_Payment','Cash_Payment','Memo','Control',]

    def get_readonly_fields(self, request, obj=None):
        user = Group.objects.get(user=request.user)
        readonly_fields = ()
        if request.user.is_superuser:
            readonly_fields = ()
        elif user.name == 'pengendali_keuangan':
            readonly_fields = ('Paid_Amount','Date','Bank_Payment','Cash_Payment','Memo',)
        elif user.name == 'staf_pengeluaran':
            readonly_fields = ('Control',)
        else:readonly_fields = ('Paid_Amount','Date','Bank_Payment','Cash_Payment','Memo','Control',)
        return readonly_fields

class Tr_Purchase_PayAdmin(admin.ModelAdmin):   
    list_display = ('PO','total_payment','total_residu','total_credit','payment_status',)
    list_filter = ('PO','Payment_Status',)
    ordering = ('-id', )
    search_fields = ['PO__Payment_Status', ]
    exclude = ('Total_Payment','Total_Residu','Total_Credit','Payment_Status',)
    readonly_fields = ('PO','total_payment','total_residu','total_credit','payment_status',)
    inlines = [Tr_Purchase_PayInline,]

    def suit_row_attributes(self, obj, request):
		css_class = {
			'Lunas': 'success','Kredit': 'warning','Belum Dibayar': 'error',}.get(obj.payment_status())
		if css_class:
			return {'class': css_class, 'data': obj.payment_status()}

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False
    
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False
admin.site.register(Tr_Purchase_Pay, Tr_Purchase_PayAdmin)

class Detail_Purchase_Payment_AccountInline(admin.TabularInline):
    model = Detail_Purchase_Payment_Account
    can_delete = True
    verbose_name_plural = 'Jurnal Item'
    list_per_page  = 2
    max_num = 2
    fields = ['Payment','Account','Type',]

    def get_readonly_fields(self, request, obj=None):
        user = Group.objects.get(user=request.user)
        readonly_fields = ()
        if request.user.is_superuser or user.name == 'staf_akuntansi':
            readonly_fields = ()
        else:
            readonly_fields = ('Payment','Account','Type',)
        return readonly_fields

class Tr_Purchase_PaymentAdmin(admin.ModelAdmin):   
    list_display = ('Payment_No','PO','Paid_Amount','Date','Memo')
    list_filter = ('Payment_No','PO',)
    ordering = ('-id', )
    search_fields = ['Payment_No__Invoice', ]
    readonly_fields = ('Payment_No','PO','Paid_Amount','Date','Bank_Payment','Cash_Payment','Memo','Period','Journal','Control')
    inlines = [Detail_Purchase_Payment_AccountInline,]

    fieldsets = [(None, {
        'fields': ['Payment_No','PO','Date','Period','Journal','Memo','Paid_Amount']
    })]

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def suit_row_attributes(self, obj, request):
		css_class = {
			'Akun Terisi': 'success','Akun Tidak Lengkap': 'warning', 'Akun Kosong': 'error'}.get(obj.status())
		if css_class:
			return {'class': css_class, 'data': obj.status()}

admin.site.register(Tr_Purchase_Payment, Tr_Purchase_PaymentAdmin)
        
class Detail_Payroll_AccountInline(admin.TabularInline):
    model = Detail_Payroll_Account
    can_delete = True
    verbose_name_plural = 'Akun Penggajian'
    list_per_page  = 2
    max_num = 2

    def get_readonly_fields(self, request, obj=None):
        user = Group.objects.get(user=request.user)
        readonly_fields = ()
        if request.user.is_superuser or user.name == 'staf_akuntansi':
            readonly_fields = ()
        else:
            readonly_fields = ('Payroll','Account','Type',)
        return readonly_fields

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

class PayrollAdmin(admin.ModelAdmin):   
    list_display = ('Payroll_No','Date','Memo','Payment_Status','total',)
    list_filter = ('Payroll_No',)
    ordering = ('-id', )
    search_fields = ['']
    inlines = [Detail_Payroll_AccountInline,]

    def get_readonly_fields(self, request, obj=None):
        self.readonly_fields = ('Payroll_No','Bank_Payment','Cash_Payment','Paid_Amount','Date','Period','Journal','Memo','Payment_Status','Tax','total',)
        return self.readonly_fields

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

admin.site.register(Payroll, PayrollAdmin)

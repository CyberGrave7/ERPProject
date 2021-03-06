from django.db import models
from Apps.Procurement.property.models import Goods_Type, Currency, Fields, Sub_Fields, Classification, Unit_Of_Measure

from Apps.Hrm.Master_General.models import Department
from Apps.Accounting.CashBank.models import Budget

from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
from Apps.Procurement.vendor.const.const import *
from django.db.models.signals import post_save

class Ms_Vendor(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=16)
    vendor_name = models.CharField(max_length=50, verbose_name='Nama Vendor')
    vendor_npwp = models.CharField(max_length=25, verbose_name='NPWP')
    vendor_address = models.TextField(verbose_name='Alamat')
    vendor_city = models.CharField(max_length=25, verbose_name='Kota')
    vendor_phone = models.CharField(max_length=20, verbose_name='Telepon')
    fax = models.CharField(max_length=25, verbose_name='Fax No.')
    email = models.EmailField(verbose_name='Email')
    cp_name = models.CharField(max_length=40, verbose_name='Nama Contact Person')
    cp_phone = models.CharField(max_length=20, verbose_name='Telp Contact Person')
    net_worth = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True, verbose_name='Kekayaan Bersih (Rp)')
    date_register = models.DateTimeField(auto_now_add=True, verbose_name='Tgl Daftar')
    bank_name = models.CharField(max_length=30, verbose_name='Nama Bank')
    bank_account_no = models.CharField(max_length=20, verbose_name='No. Rekening Bank')
    vendor_verified = models.BooleanField(default=False, verbose_name='Verified?')

    class Meta:
        verbose_name = 'Ms Vendor'
        verbose_name_plural = 'List Vendor'
        ordering = ['id']

    def grade_rate(self):
        from Apps.Procurement.goodsReceipt.models import Goods_Receipt
        grade = 0
        total = 0
        try:
            data = Goods_Receipt.objects.filter(purchase_order_id__vendor__id=self.id)
            n = data.count()
            for d in data: total += d.vendor_grade
            grade = total/n
        except:
            pass
        return grade

    def grade(self):
        if self.grade_rate() == 0:
            rate = '<font color="red" size="3"><strong>not rated</strong></font>'
        else:
            rate = '<font color="green" size="3"><strong>%s</strong></font>' % self.grade_rate()
        return rate
    grade.short_description = 'Nilai'
    grade.allow_tags = True

    def __unicode__(self):
        return 'ID: %(id)s | %(name)s' % {'id':self.id,'name':self.vendor_name}

class Siup_Vendor(models.Model):
    ms_vendor_id = models.OneToOneField(Ms_Vendor, verbose_name='ID Vendor')
    siup_no = models.CharField(max_length=40, verbose_name='No. SIUP')
    siup_valid_until = models.DateField(verbose_name='SIUP berlaku sampai')
    siup_institute = models.CharField(max_length=40, blank=True, verbose_name='Institut')

    class Meta:
        verbose_name = 'SIUP'
        verbose_name_plural = 'SIUP'

    def __unicode__(self):
        return '%s' % self.id

class Iujk_Vendor(models.Model):
    ms_vendor_id = models.OneToOneField(Ms_Vendor, verbose_name='ID Vendor')
    iujk_no = models.CharField(max_length=40, verbose_name='No. IUJK')
    iujk_valid_until = models.DateField(verbose_name='IUJK berlaku sampai')
    iujk_institute = models.CharField(max_length=40, blank=True, verbose_name='Institut')

    class Meta:
        verbose_name = 'IUJK'
        verbose_name_plural = 'IUJK'

    def __unicode__(self):
        return '%s' % self.id

class Apbu_Vendor(models.Model):
    ms_vendor_id = models.OneToOneField(Ms_Vendor, verbose_name='ID Vendor')
    apbu_no = models.CharField(max_length=40, verbose_name='No. APBU')
    apbu_valid_until = models.DateField(verbose_name='APBU berlaku sampai')
    apbu_institute = models.CharField(max_length=40, blank=True, verbose_name='Institut')

    class Meta:
        verbose_name = 'Akta Pendiriran Badan Usaha'
        verbose_name_plural = 'Akta Pendiriran Badan Usaha'

    def __unicode__(self):
        return '%s' % self.id

class Classification_Vendor(models.Model):
    ms_vendor_id = models.ForeignKey(Ms_Vendor, verbose_name='ID Vendor')
    classification_id = models.ForeignKey(Classification,verbose_name='Klasifikasi')
    fields_id = models.ForeignKey(Fields,verbose_name='Bidang')
    sub_fields_id = models.ForeignKey(Sub_Fields,verbose_name='Sub Bidang')

    class Meta:
        verbose_name = 'Klasifikasi'
        verbose_name_plural = 'Klasifikasi'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        return reverse('Apps.Procurement.vendor.views.del_class', args=[self.id])

class Owner_Vendor(models.Model):
    ms_vendor_id = models.ForeignKey(Ms_Vendor, verbose_name='ID Vendor')
    owner_name = models.CharField(max_length=40, verbose_name='Nama Pemilik')
    owner_ktp_no = models.CharField(max_length=20,verbose_name='No. KTP Pemilik')
    owner_address = models.CharField(max_length=50,verbose_name='Alamat Pemilik')
    capital_ownership = models.DecimalField(decimal_places=2, max_digits=5,verbose_name='Kepemilikan Modal (0-99)%')
    doc_ownership = models.FileField(upload_to='uploads/dokvendor/dokpem',verbose_name='Dokumen Kepemilikan')

    class Meta:
        verbose_name = 'Pemilik'
        verbose_name_plural = 'Pemilik'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        return reverse('Apps.Procurement.vendor.views.download_handler', args=[self.id])

    def url_edit(self):
        return reverse('Apps.Procurement.vendor.views.edit_owner', args=[self.id])

    def url_delete(self):
        return reverse('Apps.Procurement.vendor.views.del_owner', args=[self.id])

class Board_Of_Directors_Vendor(models.Model):
    ms_vendor_id = models.ForeignKey(Ms_Vendor, verbose_name='ID Vendor')
    board_of_directors_name = models.CharField(max_length=40,verbose_name='Nama')
    board_of_directors_npwp = models.CharField(max_length=20,verbose_name='NPWP')
    board_of_directors_ktp_no = models.CharField(max_length=20,verbose_name='No. KTP')
    board_of_directors_address = models.CharField(max_length=50,verbose_name='Alamat')
    occupation = models.CharField(max_length=30,verbose_name='Jabatan')
    doc_board_of_directors = models.FileField(upload_to='uploads/dokvendor/dokdir', verbose_name='Dokumen')

    class Meta:
        verbose_name = 'Direksi'
        verbose_name_plural = 'Direksi'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        return reverse('Apps.Procurement.vendor.views.download_direksi', args=[self.id])

    def url_edit(self):
        return reverse('Apps.Procurement.vendor.views.edit_direksi', args=[self.id])

    def url_delete(self):
        return reverse('Apps.Procurement.vendor.views.del_direksi', args=[self.id])

class Experts_Vendor(models.Model):
    ms_vendor_id = models.ForeignKey(Ms_Vendor, verbose_name='ID Vendor')
    experts_name = models.CharField(max_length=40, verbose_name='Nama')
    experts_npwp = models.CharField(max_length=40, verbose_name='NPWP')
    experts_ktp_no = models.CharField(max_length=20, verbose_name='No. KTP')
    experts_address = models.CharField(max_length=50, verbose_name='Alamat')
    expertise = models.CharField(max_length=30, verbose_name='Keahlian')
    ska_no = models.CharField(max_length=20, verbose_name='No. SKA')
    ska_valid_until = models.DateField(verbose_name='Berlaku sampai')
    last_education = models.CharField(max_length=20, verbose_name='Pendidikan terakhir')
    diploma_no = models.CharField(max_length=30, verbose_name='No. Ijazah')
    permanent_status = models.CharField(max_length=25, choices=STATUS_TETAP_CHOICES, verbose_name='Status Tenaga Tetap')
    doc_experts = models.FileField(upload_to='uploads/dokvendor/doktena', verbose_name='Dokumen')

    class Meta:
        verbose_name = 'Tenaga Ahli'
        verbose_name_plural = 'Tenaga Ahli'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        return reverse('Apps.Procurement.vendor.views.download_ta', args=[self.id])

    def url_edit(self):
        return reverse('Apps.Procurement.vendor.views.edit_ta', args=[self.id])

    def url_delete(self):
        return reverse('Apps.Procurement.vendor.views.del_ta', args=[self.id])

class Experience_Vendor(models.Model):
    ms_vendor_id = models.ForeignKey(Ms_Vendor, verbose_name='ID Vendor')
    experience_user = models.CharField(max_length=40, verbose_name='Pengguna')
    experience_title = models.CharField(max_length=40, verbose_name='Judul')
    location = models.CharField(max_length=40, verbose_name='Lokasi Kota')
    experience_address = models.CharField(max_length=50, verbose_name='Alamat')
    classification_id = models.ForeignKey(Classification, verbose_name='Klasifikasi')
    fields_id = models.ForeignKey(Fields, verbose_name='Bidang')
    sub_fields_id = models.ForeignKey(Sub_Fields, verbose_name='Sub Bidang')
    experience_contract_no = models.CharField(max_length=30, verbose_name='No. Kontrak')
    experience_contract_value = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='Nilai Kontrak')
    experience_contract_date = models.DateField(verbose_name='Tgl. Kontrak')
    doc_experience = models.FileField(upload_to='uploads/dokvendor/dokpeng', verbose_name='Dokumen')

    class Meta:
        verbose_name = 'Pengalaman'
        verbose_name_plural = 'Pengalaman'

    def __unicode__(self):
        return '%s' % self.id

class Equipments_Vendor(models.Model):
    ms_vendor_id = models.ForeignKey(Ms_Vendor, verbose_name='ID Vendor')
    equipment_type = models.CharField(max_length=20, verbose_name='Tipe')
    equipment_amount = models.PositiveIntegerField(verbose_name='Jumlah')
    equipment_brand = models.CharField(max_length=20, verbose_name='Merk')
    equipment_year = models.CharField(max_length=4, verbose_name='Tahun')
    equipment_condition = models.CharField(max_length=50, verbose_name='Kondisi')
    equipment_location = models.CharField(max_length=50, verbose_name='Lokasi sekarang')
    evidence_no = models.CharField(max_length=40, verbose_name='No. Bukti', help_text='No Bukti Nota Pembelian')
    equipment_status = models.CharField(max_length=20, choices=STATUS_ALAT_CHOICES, verbose_name='Status Alat')

    class Meta:
        verbose_name = 'Peralatan'
        verbose_name_plural = 'Peralatan'

    def __unicode__(self):
        return '%s' % self.id

class Documents_Vendor(models.Model):
    ms_vendor_id = models.OneToOneField(Ms_Vendor, verbose_name='ID Vendor')
    doc_siup = models.FileField(upload_to='uploads/dokvendor/doksiup', verbose_name='Dokumen SIUP', blank=True, null=True)
    doc_iujk = models.FileField(upload_to='uploads/dokvendor/dokiujk', verbose_name='Dokumen IUJK', blank=True, null=True)
    doc_apbu = models.FileField(upload_to='uploads/dokvendor/dokapbu', verbose_name='Dokumen APBU', blank=True, null=True)

    class Meta:
        verbose_name = 'Dokumen-dokumen'
        verbose_name_plural = 'Dokumen-dokumen'

    def __unicode__(self):
        return '%s' % self.id

def create_doc_vendor(sender, instance, created, **kwargs):
    if created == True:
        profile, created = Documents_Vendor.objects.get_or_create(ms_vendor_id=instance)
post_save.connect(create_doc_vendor, sender=Ms_Vendor)

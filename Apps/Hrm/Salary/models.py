﻿"""Develop By - Fery Febriyan Syah"""

from django.db import models
from Apps.Hrm.Master_Salary.models import *
from Apps.Hrm.Data_Personel_Management.models import Employee
from Apps.Hrm.Master_General.models import Section
from Apps.Accounting.CashBank.models import Ms_Tax
from Apps.Accounting.GeneralLedger.models import Ms_Journal, Ms_Period
from django.utils.translation import ugettext_lazy as _
from library.const.month import MONTH
from library.const.group import GROUP
from library.const.salary import PAYMENT_METHOD, PAYMENT_STATUS
from django.contrib.humanize.templatetags.humanize import intcomma
from datetime import datetime, timedelta
from decimal import Decimal
from django.db.models import signals


class Header_Salary (models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Nama Pegawai")
    group = models.IntegerField (choices=GROUP, verbose_name="Golongan")
    section = models.ForeignKey (Section, verbose_name="Seksi")
    period = models.ForeignKey (Ms_Period, verbose_name="Periode")
    lock = models.BooleanField (verbose_name="Kunci",
                                help_text=')* Jangan Dicentang terlebih dahulu Sebelum Data gaji Pegawai Di inputkan')
    plan_month = models.CharField(max_length=6, editable=False)

    class Meta:
        verbose_name = _('Gaji Pegawai')
        verbose_name_plural = _('Gaji Pegawai')
        ordering = ['id']

    def plan_mon(self):
        date = datetime.now()
        now = date.strftime("%m")
        nowyear = date.strftime("%Y")
        intnow = int(now)
        intyear = int(nowyear)
        strnow = str(intnow)

        if len(strnow) < 2 :
            strnow = '0%(strnow)s' % {'strnow' : strnow}

        return '%(year)s%(month)s' % {'year':intyear, 'month':strnow}

    def save(self, force_insert=True, force_update=True, using=None, update_fields=None):
        #if self.no_reg =='':
        #    self.no_reg = self.no_rek()
        #else:
        #   self.no_reg = self.no_reg

        if self.plan_month == '':
            self.plan_month = self.plan_mon()
        else: self.plan_month = self.plan_month
        super(Header_Salary, self).save()

    def print_pdf(self):
        img = '<img src="/media/static/staticproc/images/print.png" width="20%"/>'
        link = '<a href="/print_gaji/%(id)s/" target="blank">%(gbr)s Cetak</a>' % {'id': self.id, 'gbr':img}
        return link
    print_pdf.allow_tags = True
    print_pdf.short_description = 'Print SLIP GAJI'

    def __unicode__(self):
        return '%s' % self.period


class Salary_Employee (models.Model):
    header = models.ForeignKey (Header_Salary, verbose_name="Periode")
    date_now =  models.DateField (auto_now_add=True, verbose_name="Hari")
    basic_salary = models.ForeignKey (Basic_Salary, verbose_name="Gaji Pokok")
    operasional_support = models.ForeignKey (Operational_Support, verbose_name="Tunjangan Operasional")
    transport_Support = models.ForeignKey (Transport_Support, verbose_name="Tunjangan Transportasi")
    shift_operational_support = models.ForeignKey (Shift_Operational_Support, verbose_name="Tunjangan Operasional Shift")
    shift_operational_supporting = models.ForeignKey (Shift_Operational_Supporting, verbose_name="Tunjangan Penunjang Operasional Shift")
    position_support = models.ForeignKey (Position_Support, verbose_name="Tunjangan Jabatan")
    life_cost_support = models.ForeignKey (Life_Cost_Support, verbose_name="Tunjangan Biaya Hidup")


    class Meta:
        verbose_name = _('Detail Gaji')
        verbose_name_plural = _('Detail Gaji')
        ordering = ['id']

    def __unicode__(self):
        return '%s' % self.id


class Cut_Of_Salary (models.Model):
    header = models.ForeignKey (Header_Salary, verbose_name="Periode")
    month = models.CharField (max_length=10, verbose_name="Bulan", editable=False)
    #currency = models.ForeignKey (Currency, verbose_name=_('Mata Uang '), max_length=50, default=1)
    kpr = models.FloatField (max_length=20, blank=True, verbose_name="KPR")
    tht = models.FloatField (max_length=20, blank=True, verbose_name="THT")
    bpjs = models.FloatField (max_length=20, blank=True, verbose_name="BPJS")
    coorperation_contribution = models.FloatField (max_length=20, blank=True, verbose_name="Iuran Koperasi")
    sp_contribution = models.FloatField (max_length=20, blank=True, verbose_name="Iuran SP")
    coorperation_discount = models.FloatField (max_length=20, verbose_name="Potongan Koperasi")
    #credit_bank = models.ForeignKey (Credit_Bank, blank=True, null=True, verbose_name="Pinjaman Bank")
    ykkpi = models.FloatField (max_length=20, verbose_name="YKKPI")

    class Meta:
        verbose_name = _('Potongan')
        verbose_name_plural = _('Potongan')
        ordering = ['id']

    def bulan (self):
        now = datetime.now()
        nowm = now.strftime("%m")
        nowy = now.strftime("%Y")
        nowd = now.strftime("%d")
        strnow = '%(d)s/%(y)s/%(m)s' % {'y':nowy,'m':nowm, 'd':nowd}
        return strnow

    def save (self, force_insert=True, force_update=True, using=None):
        if self.month == '':
            self.month = self.bulan()
        else: self.month = self.month
        super (Cut_Of_Salary, self).save()


    def display_kpr(self):
        st = '%(logo)s %(kpr)s%(back)s' % {'logo': self.currency.pre_symbol, 'kpr': intcomma(self.kpr), 'back': self.currency.post_symbol}
        return st

    display_kpr.short_description = _('KPR')

    def display_tht(self):
        st = '%(logo)s %(tht)s%(back)s' % {'logo': self.currency.pre_symbol, 'tht': intcomma(self.tht), 'back': self.currency.post_symbol}
        return st

    display_tht.short_description = _('THT')

    def display_bpjs(self):
        st = '%(logo)s %(bpjs)s%(back)s' % {'logo': self.currency.pre_symbol, 'bpjs': intcomma(self.bpjs), 'back': self.currency.post_symbol}
        return st

    display_bpjs.short_description = _('BPJS')

    def display_coorperation_contribution(self):
        st = '%(logo)s %(coorperation_contribution)s%(back)s' % {'logo': self.currency.pre_symbol, 'coorperation_contribution': intcomma(self.coorperation_contribution), 'back': self.currency.post_symbol}
        return st

    display_coorperation_contribution.short_description = _('Kontribusi Koperasi')

    def display_sp_contribution(self):
        st = '%(logo)s %(sp_contribution)s%(back)s' % {'logo': self.currency.pre_symbol, 'sp_contribution': intcomma(self.sp_contribution), 'back': self.currency.post_symbol}
        return st

    display_sp_contribution.short_description = _('Kontribusi SP')

    def display_coorperation_discount(self):
        st = '%(logo)s %(coorperation_discount)s%(back)s' % {'logo': self.currency.pre_symbol, 'coorperation_discount': intcomma(self.coorperation_discount), 'back': self.currency.post_symbol}
        return st

    display_coorperation_discount.short_description = _('Potongan Koperasi')

    def display_ykkpi(self):
        st = '%(logo)s %(ykkpi)s%(back)s' % {'logo': self.currency.pre_symbol, 'ykkpi': intcomma(self.ykkpi), 'back': self.currency.post_symbol}
        return st

    display_ykkpi.short_description = _('YKKPI')

    def __unicode__(self):
        return '%s' % self.id


class Total_Salary (models.Model):
    header = models.ForeignKey (Header_Salary, verbose_name="Periode")
    month = models.CharField(verbose_name="Tanggal", max_length=50, editable=False, null=True, blank=True)
    employee = models.ForeignKey (Employee, verbose_name="Nama Pegawai")

    class Meta:
        verbose_name = _('Total Gaji')
        verbose_name_plural = _('Total Gaji')
        ordering = ['id']

    def lembur(self):
        total=0
        try:
            a = Data_Absent.objects.filter(header__period=self.period)
            for b in a:
                total += b.Total_Rupiah
        except:
            pass

        return total

    def total(self):
        now = datetime.now()
        nowm = now.strftime("%m")
        nowy = now.strftime("%Y")
        nowd = now.strftime("%d")
        strnow = '%(d)s/%(y)s/%(m)s' % {'y':nowy,'m':nowm, 'd':nowd}
        salary = minutes = id = percent = total_cut = 0

        try:
            basic = Salary_Employee.objects.get(header__employee=self.employee)
            salary = float(basic.basic_salary.total_basic_salary) + float(basic.operasional_support.total_operasional_support) + float(basic.transport_Support.total_transport_support) + float(basic.shift_operational_support.total_shift_operasional_support) + float(basic.shift_operational_supporting.total_shift_operasional_supporting) + float(basic.position_support.total_position_support) +  float(basic.life_cost_support.total_life_support)
        except:
            pass
            """
                pass
            try:
                basic = Salary_Employee.objects.get(employee=self.employee)
                overtime = Overtime.objects.filter(employee=self.employee,month=strnow)
                for o in overtime:
                    minutes += float(o.duration_overtime)
                set = Set_of_Overtime.objects.all()
                for s in set:
                    if minutes >= s.low and minutes <= s.high:
                        id = s.id
                        break
                x = Set_of_Overtime.objects.get(id=id)
                one = 0
                one  = float(basic.basic_salary.total_basic_salary) / 100
                percent = one * float(x.precentage)
                salary += percent
            except:
            """

        try:
            cut = Cut_Of_Salary.objects.get(header__employee=self.employee,month=strnow)
            total_cut = float(cut.kpr) + float(cut.tht) + float(cut.bpjs) + float(cut.coorperation_contribution) + float(cut.sp_contribution) + float(cut.coorperation_discount) + float(cut.credit_bank.total_loan) + float(cut.ykkpi)
            salary -= total_cut
        except:
            pass
        return intcomma(salary)

    def bulan (self):
        now = datetime.now()
        nowm = now.strftime("%m")
        nowy = now.strftime("%Y")
        nowd = now.strftime("%d")
        strnow = '%(d)s/%(y)s/%(m)s' % {'y':nowy,'m':nowm, 'd':nowd}
        return strnow

    def save(self, force_insert=False, force_update=False, using=None):
        if self.month == None:
            self.month = self.bulan()
        else: self.month = self.month
        super (Total_Salary, self).save()

    def __unicode__(self):
        return '%s' % self.id
"""
        try:
            basic = Salary_Employee.objects.get(employee=self.employee)
            overtime = Overtime.objects.filter(employee=self.employee,month=strnow)
            for o in overtime:
                minutes += float(o.duration_overtime)
            set = Set_of_Overtime.objects.all()
            for s in set:
                if minutes >= s.low and minutes <= s.high:
                    id = s.id
                    break
            x = Set_of_Overtime.objects.get(id=id)
            one = 0
            one  = float(basic.basic_salary.total_basic_salary) / 100
            percent = one * float(x.precentage)
            salary += percent
        except:
            pass

        try:
            cut = Cut_Of_Salary.objects.get(employee=self.employee,month=strnow)
            total_cut = float(cut.kpr) + float(cut.tht) + float(cut.bpjs) + float(cut.coorperation_contribution) + float(cut.sp_contribution) + float(cut.coorperation_discount) + float(cut.credit_bank.total_loan) + float(cut.ykkpi)
            salary -= total_cut
        except:
            pass
"""


class Tr_Payroll(models.Model):
    Payroll_No = models.CharField(verbose_name=_('Nomor Gaji '), unique=True, null=True, blank=True, max_length=20, editable=False)
    Payment_Method = models.IntegerField(_('Metode Pembayaran '), choices=PAYMENT_METHOD, default=2)
    Date = models.DateField(_('Tanggal Pembayaran'), default=datetime.now())
    Memo = models.TextField(verbose_name=_('Memo '), null=True, blank=True, max_length=50)
    Period = models.ForeignKey(Ms_Period, related_name=_('Periode'), verbose_name=_('Periode '))
    Journal = models.ForeignKey(Ms_Journal, verbose_name=_('Jurnal '))
    Paid_Amount = models.DecimalField(_('Jumlah Pembayaran '), max_digits=19, decimal_places=2, default=0)
    Tax = models.ForeignKey(Ms_Tax, related_name=_('Pajak'), verbose_name=_('Pajak '))
    Payment_Status = models.IntegerField(_('Status Pembayaran '), choices=PAYMENT_STATUS, null=True, blank=True, max_length=20, default=1)

    class Meta:
        verbose_name = _('Pembayaran Gaji ')
        verbose_name_plural = _('Pembayaran Gaji')
        ordering = ['-id']

    def __unicode__(self):
        return '%s' % self.Payroll_No

    def incstring(self):
        try:
            data = Tr_Payroll.objects.all().order_by('-Date')
            jml = data.count()
        except:
            jml=0
            pass
        no = 0
        if jml == 0:
            no = 0
        else:
            for d in data:
                split = str(d.Payroll_No).split('/')
                no = int(split[3])
        num = no + 1
        cstring = str(num)
        return cstring

    def inclen(self):
        leng = len(self.incstring())
        return leng

    def no_rek(self):
        date = datetime.now()
        now = date.strftime("%m")
        nowyear = date.strftime("%Y")
        intnow = int(now)
        intyear = int(nowyear)
        strnow = str(intnow)
        if len(strnow) < 2 :
            strnow = '0%(strnow)s' % {'strnow' : strnow}
        nol = 5 - self.inclen()
        if nol == 1: num = "0"
        elif nol == 2: num = "00"
        elif nol == 3: num = "000"
        elif nol == 4: num = "0000"
        number = num + self.incstring()
        return 'PBGAJ/%(year)s/%(month)s/%(unik)s' % {'year': intyear, 'month': strnow, 'unik': number}

    def jurnal(self):
        if self.Payment_Method == 1:
            a = Ms_Journal.objects.get(Code='JURCA')
        else:
            a = Ms_Journal.objects.get(Code='JURBA')
        return a

    def period(self):
        today = datetime.now().date()
        a = 0
        try:
            per = Ms_Period.objects.filter(Start_Period__lte=today, End_Period__gte=today)
            a = per.count()
        except:
            pass
        if a == 1:
            for x in per:
                b = x.Code
                c = Ms_Period.objects.get(Code=b)
        else:
            c = self.Period
        return c

    def total_tax(self):
        total_tax = Decimal(0)
        total_tax = (self.Paid_Amount * (self.Tax.Percentage)) / 100
        return total_tax.quantize(Decimal('0.01'))

    def total(self):
        total = Decimal(0)
        total = self.Paid_Amount + self.total_tax()
        return total.quantize(Decimal('0.01'))
    total.short_description = _('Total Pembayaran')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.Payroll_No == "":
            self.Payroll_No = self.no_rek()
        else:
            self.Payroll_No = self.Payroll_No
        self.Period = self.period()
        self.Journal = self.jurnal()
        super(Tr_Payroll, self).save()

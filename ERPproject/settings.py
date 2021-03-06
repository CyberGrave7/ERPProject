# Django settings for ERPproject project.
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ERPproject',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.dirname(__file__), '..', 'Database/ERPproject.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Jakarta'

LANGUAGE_CODE = 'id'

USE_THOUSAND_SEPARATOR = True

THOUSAND_SEPARATOR = "."

DECIMAL_SEPARATOR = ","

NUMBER_GROUPING = 3

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'media', 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

ADMIN_MEDIA_PREFIX = '/media/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '*o-7f-(7!$oo*84-3)$8l$da5aacc+_20qy)2y-333lj2^b+ct'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader',
     ('django.template.loaders.filesystem.Loader',
      'django.template.loaders.app_directories.Loader',
      #'django.template.loaders.eggs.Loader',
     )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ERPproject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ERPproject.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'ERPproject/templates'),
)

INSTALLED_APPS = (
    'suit',
    'mptt',
    'django_messages',
    'captcha',
    'ckeditor',
    'captcha',
    'tinymce',
    'filetransfers',
    'report_builder',
    'django_select2',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.admin',

    'Apps.Manufacturing.MasterData',
    'Apps.Manufacturing.Manufacturing',
    'Apps.Manufacturing.ProductionExecution',
    'Apps.Manufacturing.ProductionPlanning',
    'Apps.Manufacturing.PropertyMan',

    'Apps.Hrm.FromHrm',
    'Apps.Distribution.FromSales',

    'Apps.Accounting.AccountReceivable',
    'Apps.Accounting.AccountPayable',
    'Apps.Accounting.CashBank',
    'Apps.Accounting.GeneralLedger',

    'Apps.Procurement.internal',
    'Apps.Procurement.vendor',
    'Apps.Procurement.publicTender',
    'Apps.Procurement.purchaseOrder',
    'Apps.Procurement.property',
    'Apps.Procurement.directAppointment',
    'Apps.Procurement.goodsReceipt',

    'Apps.Hrm.Data_Personel_Management',
    'Apps.Hrm.Master_Family',
    'Apps.Hrm.Master_General',
    'Apps.Hrm.Master_Salary',
    'Apps.Hrm.Recruitment',
    'Apps.Hrm.Salary',
    'Apps.Hrm.Absent',
    'Apps.Hrm.Schedule',

    'Apps.Asset.Master',
    'Apps.Asset.Peminjaman',
    'Apps.Asset.Maintenance',
    'Apps.Asset.Penghapusan',
    'Apps.Asset.Pemindahan',
    'Apps.Asset.Pengadaan',
    'Apps.Asset.Penggantian',
    'Apps.Asset.Penghapusan',
    'Apps.Asset.Penjualan',
    'Apps.Asset.Property_asset',
    'Apps.Asset.Request',

    'Apps.Inventory.Inventory_Planing',
    'Apps.Inventory.Inventory_Handling',
    'Apps.Inventory.Inventory_Intelligh_Location_Assigment',
    'Apps.Inventory.Inventory_Reporting',
    'Apps.Inventory.Inventory_Lost_Control',
    'Apps.Inventory.Property_Inv',

    'Apps.Inventory.product',
    'Apps.Distribution.CRM',
    'Apps.Distribution.customer',
    'Apps.Distribution.master_sales',
    'Apps.Distribution.order',
    'Apps.Distribution.invoice',
    #'Apps.Distribution.shipping',
    #'Apps.Distribution.sales_return',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

INTERNAL_IPS = ('127.0.0.1',)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FLITE_PATH = os.environ.get('CAPTCHA_FLITE_PATH', None)
ANONYMOUS_USER_ID = -1
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django_messages.context_processors.inbox',
)
AUTH_PROFILE_MODULE = 'customer.Company'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'
CKEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'media', 'uploads')
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 640,
        },
    }

SUIT_CONFIG = {
    'ADMIN_NAME': 'ERP Project PT-IGLAS',
    'HEADER_DATE_FORMAT': 'd F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU_OPEN_FIRST_CHILD': True,
    'LIST_PER_PAGE': 10,
    'MENU': (
        #Sales dan Distribution#
        {'app': 'order', 'label': 'Penjualan', 'icon': 'icon-shopping-cart', 'models': (
            {'model': 'order.requestorder', 'label': 'Order Permintaan'},
            {'model': 'order.quoteorder', 'label': 'Order Penawaran'},
            {'model': 'order.salesorder', 'label': 'Order Penjualan'},
            {'model': 'invoice.receivableinvoice', 'label': 'Faktur Penjualan'},
            {'model': 'shipping.deliveryorder', 'label': 'Surat Penyerahan'},
            {'model': 'shipping.outpass', 'label': 'Surat Keluar'},
            {'model': 'sales_return.sales_return', 'label': 'Retur Penjualan'},
        )},
        {'app': 'flatpages', 'label': 'CRM', 'icon': 'icon-book', 'models': (
            {'model': 'CRM.complaint', 'label': 'Keluhan / Komplain'},
            {'model': 'CRM.news', 'label': 'Berita Perusahaan'},
            {'model': 'flatpages.flatpage', 'label': 'Artikel Web'},
            {'model': 'CRM.contacts', 'label': 'Buku Tamu'},
        )},
        {'app': 'customer', 'label': 'Perusahaan', 'icon': 'icon-hdd', 'models': (
            {'model': 'customer.usercompany', 'label': 'Manage Akun Perusahaan'},
            {'model': 'customer.company', 'label': 'Manage Perusahaan'},
        )},
        {'app': 'django_messages', 'label': 'Messages', 'icon': 'icon-envelope', 'models': (
            {'model': 'django_messages.message', 'label': 'Messages'},
        )},
        {'app': 'master_sales', 'label': 'Panggilan', 'icon': 'icon-refresh', 'models': (
            {'model': 'master_sales.logcall', 'label': 'Logged Call'},
            {'model': 'master_sales.scheduledcall', 'label': 'Scheduled Call'},
        )},
        {'app': 'master_sales', 'label': 'Master Sales', 'icon': 'icon-th-large', 'models': (
            {'model': 'master_sales.bank', 'label': 'Daftar Bank'},
            {'model': 'master_sales.tax', 'label': 'Daftar Pajak'},
            {'model': 'master_sales.currency', 'label': 'Daftar Mata Uang'},
            {'model': 'master_sales.paymentterm', 'label': 'Daftar Waktu Pembayaran'},
            {'model': 'master_sales.shippingmethods', 'label': 'Daftar Perlakuan'},
        )},

        {'app': 'product', 'label': 'Daftar Produk', 'icon': 'icon-folder-close', 'models': (
            {'model': 'product.productitem', 'label': 'Data Produk'},
            {'model': 'product.category', 'label': 'Kategori Produk'},
        )},

        #Financial Accounting#
        {'app': 'fromasset', 'label': 'Asset', 'icon': 'icon-shopping-cart'},
        
        #{'app': 'fromsales', 'label': 'Sale', 'icon': 'icon-user'},
        {'app': 'fromhrm', 'label': 'HRM', 'icon': 'icon-user'},
        
        {'app': 'frompurchase', 'label': 'Belanja', 'icon': 'icon-file'},

        {'app': 'accountreceivable', 'label': 'Akun Penerimaan', 'icon': 'icon-plus-sign', 'models': (
            {'model': 'invoice.sales_invoice', 'label': 'Akun Penjualan'},
            {'model': 'AccountReceivable.tr_sales_receipt', 'label': 'Pembayaran Penjualan'},
            {'model': 'AccountReceivable.tr_sales_payment', 'label': 'Akun Pembayaran Penjualan'},
            {'model': 'AccountReceivable.sales_return', 'label': 'Akun Retur Penjualan'},
            {'model': 'AccountReceivable.tr_asset_sale_receipt', 'label': 'Pembayaran Penjualan Aset'},
            {'model': 'AccountReceivable.asset_sale_invoice', 'label': 'Akun Penjualan Aset'},
            {'model': 'AccountReceivable.tr_asset_sale_payment', 'label': 'Akun Pembayaran Penjualan Aset'},
        )},
        {'app': 'accountpayable', 'label': 'Akun Pembayaran', 'icon': 'icon-minus-sign', 'models': (
            {'model': 'purchaseOrder.payable_po', 'label': 'Akun Permintaan Pembelian'},
            {'model': 'AccountPayable.tr_purchase_pay', 'label': 'Pembayaran Belanja'},
            {'model': 'AccountPayable.tr_purchase_payment', 'label': 'Akun Pembayaran Belanja'},
            {'model': 'AccountPayable.payroll', 'label': 'Akun Penggajian'},
        )},
        {'app': 'cashbank', 'label': 'Kas/Bank', 'icon': 'icon-inbox', 'models': (
            {'model': 'CashBank.ms_currency', 'label': 'Master Kurs'},
            {'model': 'CashBank.ms_tax', 'label': 'Master Pajak'},
            {'model': 'CashBank.ms_bank', 'label': 'Master Bank'},
            {'model': 'CashBank.ms_cash', 'label': 'Master Kas'},
            {'model': 'CashBank.bank', 'label': 'Pernyataan Bank'},
            {'model': 'CashBank.cash', 'label': 'Pernyataan Cash'},
            {'model': 'CashBank.budget', 'label': 'Anggaran Belanja'}, 
            {'model': 'CashBank.tr_adjustment_cashbank', 'label': 'Pemindahan Kas/Bank'},
            {'model': 'CashBank.tr_capital_budget', 'label': 'Penanaman Modal'},
        )},
        {'app': 'generalledger', 'label': 'Buku Besar', 'icon': 'icon-book', 'models': (
            {'model': 'GeneralLedger.ms_account', 'label': 'Master Akun'},
            {'model': 'GeneralLedger.ms_fiscal_years', 'label': 'Master Tahun Fiskal'},
            {'model': 'GeneralLedger.ms_period', 'label': 'Master Periode'},
            {'model': 'GeneralLedger.ms_journal', 'label': 'Master Jurnal'},
            {'model': 'GeneralLedger.tr_journal_entry', 'label': 'Entri Jurnal'},
            {'model': 'GeneralLedger.tr_adjustment_journal', 'label': 'Jurnal Penyesuaian'},
            {'model': 'GeneralLedger.depresiation_record', 'label': 'Penyusutan Aset'},
            {'label': 'Laporan Subledger', 'icon': 'icon-list-alt', 'url': '/admin/accounting/subledger'},
            {'label': 'Laporan Balance', 'icon': 'icon-list-alt', 'url': '/admin/accounting/balance'},
            {'label': 'Laporan Laba/Rugi', 'icon': 'icon-list-alt', 'url': '/admin/accounting/lossprofit'},
        )},
        # Procurement #
        #{'app': 'internal', 'label': 'Planning', 'icon': 'icon-list-alt'},
        #{'app': 'directappointment', 'label': 'Direct Appointment', 'icon': 'icon-hand-right'},
        #{'app': 'publictender', 'label': 'Public Tender', 'icon': 'icon-retweet'},
        #{'app': 'purchaseorder', 'label': 'Purchase Order', 'icon': 'icon-envelope'},
        #{'app': 'goodsreceipt', 'label': 'Goods Receipt', 'icon': 'icon-check'},
        {'app': 'internal', 'label': 'Planning', 'icon': 'icon-list-alt', 'models': (
            {'model': 'internal.header_plan', 'label': 'Header RKB'},
            {'model': 'internal.data_plan', 'label': 'Data RKB'},
            {'model': 'internal.header_purchase_request', 'label': 'Header PP'},
            {'model': 'internal.data_purchase_request', 'label': 'Data PP'},
            {'model': 'internal.header_rush_order', 'label': 'Header RO'},
            {'model': 'internal.data_rush_order', 'label': 'Data RO'},
            {'model': 'internal.user_intern', 'label': 'User Internal'},
			{'label': 'Laporan Permintaan Pembelian', 'icon': 'icon-list-alt', 'url': '/admin/internal/reportpp'},
			{'label': 'Laporan Rush Order', 'icon': 'icon-list-alt', 'url': '/admin/internal/reportro'},
			{'label': 'Laporan Anggaran', 'icon': 'icon-list-alt', 'url': '/admin/internal/report_budget'},
        )},
        {'app': 'directappointment', 'label': 'Direct Appointment', 'icon': 'icon-hand-right', 'models': (
            {'model': 'directAppointment.bidding_request', 'label': 'Permintaan Penawaran'},
            {'model': 'directAppointment.bidding_request_item', 'label': 'Item Permintaan Penawaran'},
        )},
        {'app': 'publictender', 'label': 'Public Tender', 'icon': 'icon-retweet', 'models': (
            {'model': 'publicTender.announcement_proc', 'label': 'Pengumuman Pelelangan'},
            {'model': 'publicTender.vendor_proc', 'label': 'Penawaran Vendor'},
            {'model': 'publicTender.bidding_proc', 'label': 'Pesan Penawaran'},
        )},
        {'app': 'purchaseorder', 'label': 'Purchase Order', 'icon': 'icon-envelope', 'models': (
            {'model': 'purchaseOrder.purchase_order', 'label': 'Purchase Order (PO)'},
            {'model': 'purchaseOrder.contract', 'label': 'Kontrak'},
        )},
        {'app': 'goodsreceipt', 'label': 'Goods Receipt', 'icon': 'icon-check', 'models': (
            {'model': 'goodsReceipt.goods_receipt', 'label': 'Laporan Penerimaan Barang'},
            {'model': 'goodsReceipt.claim', 'label': 'Klaim'},
        )},
        {'app': 'vendor', 'label': 'Vendor', 'icon': 'icon-user'},
        {'app': 'property', 'label': 'Property', 'icon': 'icon-book', 'models': (
            {'model': 'property.classification', 'label': 'Klasifikasi'},
            {'model': 'property.fields', 'label': 'Bidang'},
			{'model': 'property.sub_fields', 'label': 'Sub Bidang'},
            {'model': 'property.goods_type', 'label': 'Tipe Barang'},
			{'model': 'property.unit_of_measure', 'label': 'Satuan Barang'},
            {'model': 'property.currency', 'label': 'Mata Uang'},
			{'model': 'property.set_of_delay', 'label': 'Satuan Keterlambatan'},
        )},

        #Inventory#
        {'label': 'Inventory Planning', 'icon': 'icon-th-large', 'app': 'inventory_planing'},
        {'label': 'Inventory Handling', 'icon': 'icon-refresh', 'app': 'inventory_handling'},
        {'label': 'Intelligh Location Assigment', 'icon': 'icon-list-alt', 'app': 'inventory_intelligh_location_assigment'},
		{'label': 'Inventory_Reporting', 'icon': 'icon-print', 'app': 'report_builder'},
        {'label': 'Lost Control', 'icon': 'icon-user', 'app': 'inventory_lost_control'},
        #{'label': 'Mutasi Barang', 'icon': 'icon-envelope', 'app': 'mutation'},
        {'label': 'Properti', 'icon': 'icon-hdd', 'app': 'property_inv'},
        #{'label': 'Hak Akses', 'icon': 'icon-hdd', 'app': 'role_acces'},
        
        # Asset #
		{'app': 'master', 'label': 'Master', 'icon': 'icon-hdd', 'models': (
            {'model': 'Master.ms_asset', 'label': 'Master Asset'},
            {'model': 'Master.historical_asset', 'label': 'Historical Asset'},
         	{'label': 'Laporan Bulanan Asset', 'icon': 'icon-list-alt', 'url': '/admin/asset/reportasset'},
		)},
		
        #{'app': 'master', 'label': 'Master Asset', 'icon': 'icon-hdd'},
		{'app': 'request', 'label': 'Request', 'icon': 'icon-user'},
        {'app': 'peminjaman', 'label': 'Peminjaman', 'icon': 'icon-file'},
        {'app': 'pengadaan', 'label': 'Pengadaan', 'icon': 'icon-plus-sign'},
        {'app': 'pemindahan', 'label': 'Pemindahan', 'icon': 'icon-refresh'},
        {'app': 'maintenance', 'label': 'Maintenance', 'icon': 'icon-tasks'},
        {'app': 'penggantian', 'label': 'Penggantian', 'icon': 'icon-retweet'},
        {'app': 'penghapusan', 'label': 'Penghapusan', 'icon': 'icon-minus-sign'},
        {'app': 'penjualan', 'label': 'Penjualan', 'icon': 'icon-qrcode'},
        {'app': 'property_asset', 'label': 'Property Asset', 'icon': 'icon-qrcode'},

        # Manufacture #
		{'app': 'productionplanning', 'label': 'Jadwal Produksi', 'icon': 'icon-hdd', 'models': (
            {'model': 'ProductionPlanning.master_product', 'label': 'Design Mould-Label'},
            {'model': 'ProductionPlanning.bill_of_material', 'label': 'Bahan BoM'},
	    {'model': 'ProductionPlanning.master_bom', 'label': 'Master BoM'},
	    {'model': 'ProductionPlanning.production_plans', 'label': 'Production Schedule'},
         	{'label': 'Rencana Kapasitas & Jadwal Produksi', 'icon': 'icon-list-alt', 'url': '/admin/asset/reportasset'},
		)},
        {'app': 'manufacturing', 'label': 'Manufacturing', 'icon': 'icon-shopping-cart'},
        #{'app': 'products', 'label': 'Products', 'icon': 'icon-th-list'},
        {'app': 'productionplanning', 'label': 'Production Planning', 'icon': 'icon-calendar'},
        #{'app': 'labelingplanning', 'label': 'Labeling Planning', 'icon': 'icon-picture'},
        #{'app': 'packagingplanning', 'label': 'Packaging Planning', 'icon': 'icon-inbox'},
        {'app': 'productionexecution', 'label': 'Production Execution', 'icon': 'icon-hdd'},
        {'app': 'masterdata', 'label': 'Master Data', 'icon': 'icon-tint'},
        {'app': 'propertyman', 'label': 'Property Manufacture', 'icon': 'icon-tint'},

        {'app': 'absent', 'label': 'Manajemen Absensi', 'icon': 'icon-calendar'},
        {'app': 'data_personel_management', 'label': 'Manajemen Data Pegawai', 'icon': 'icon-user', 'models': (
            {'model': 'Data_Personel_Management.employee', 'label': 'Pegawai'},
            {'model': 'Data_Personel_Management.periodic_increase_decree', 'label': 'Jenjang Karir'},
            {'model': 'Data_Personel_Management.appreciation', 'label': 'Prestasi'},
            {'model': 'Data_Personel_Management.leave', 'label': 'Cuti'},
            {'model': 'Data_Personel_Management.sanction', 'label': 'Sangsi'},
            {'model': 'Data_Personel_Management.mutation', 'label': 'Mutasi'},
            {'model': 'Data_Personel_Management.termination', 'label': 'Pememecatan'}
        )},
        {'app':'schedule', 'label': 'Manajemen Penjadwalan', 'icon': 'icon-refresh'},
        {'app':'salary' ,'label': 'Manajemen Penggajian', 'icon': 'icon-envelope', 'models': (
			{'model': 'Salary.header_salary', 'label': 'Gaji Pegawai'},
			{'model': 'Salary.total_salary', 'label': 'Total Gaji'},
			{'model': 'Salary.tr_payroll', 'label': 'Pembayaran Gaji'},
			#{'label': 'Laporan Bulanan Gaji', 'icon': 'icon-list-alt', 'url': '/admin/hrm/reportsalary'},
		)},
        {'app':'recruitment', 'label': 'Manajemen Perekrutan', 'icon': 'icon-th-large', 'models': (
            {'model': 'Recruitment.candidate_new_employe', 'label': 'Data Pelamar'},
            {'model': 'Recruitment.test', 'label': 'Penyeleksian'},
            {'model': 'Recruitment.result', 'label': 'Keputusan'},
        )},

        {'app':'data_personel_management', 'label': 'Data Pegawai', 'icon': 'icon-hdd', 'models': (
            {'model': 'Data_Personel_Management.position', 'label': 'Jabatan'}, 
			{'model': 'Data_Personel_Management.education', 'label': 'Pendidikan'},
			{'model': 'Data_Personel_Management.seminar', 'label': 'Seminar'},			    
			{'model': 'Data_Personel_Management.task', 'label': 'Tugas'},
			{'model': 'Data_Personel_Management.hobby', 'label': 'Hobi'},
			{'model': 'Data_Personel_Management.periodic_increase_decree', 'label': 'SK Kenaikan Berkala'},
			{'model': 'Data_Personel_Management.group_increase_decree', 'label': 'SK Kenaikan Golongan'},
		)},
        {'app': 'master_family', 'label': 'Data Keluarga', 'icon': 'icon-heart', 'models': (
			{'model': 'Master_Family.wife', 'label': 'Biodata Isrti'},
			{'model': 'Master_Family.child1', 'label': 'Biodata Anak 1'},
			{'model': 'Master_Family.child2', 'label': 'Biodata Anak 2'},		   						    
			{'model': 'Master_Family.parent1', 'label': 'Biodata Ayah'},
			{'model': 'Master_Family.parent2', 'label': 'Biodata Ibu'},
		)},

        {'app': 'master_general', 'label': 'Property Umum', 'icon': 'icon-plus', 'models':	(
			{'model': 'Master_General.master_position', 'label': 'Jabatan'},
			{'model': 'Master_General.level_position', 'label': 'Level Jabatan'},
			{'model': 'Master_General.section', 'label': 'Seksi'},
			{'model': 'Master_General.department', 'label': 'Departemen'},
			{'model': 'Master_General.role_user', 'label': 'Hak Akses'},
		)},
        {'app': 'master_salary', 'label': 'Property Gaji', 'icon': 'icon-qrcode', 'models': (
            {'model': 'Master_Salary.basic_salary', 'label': 'Gaji Pokok'},
			{'model': 'Master_Salary.position_support', 'label': 'Tunjangan Jabatan'},
			{'model': 'Master_Salary.transport_support', 'label': 'Tunjangan Transportasi'},
			{'model': 'Master_Salary.operational_support', 'label': 'Tunjangan Operasional'},
			{'model': 'Master_Salary.shift_operational_support', 'label': 'Tunjangan Siff Operasional'},
			{'model': 'Master_Salary.shift_operational_supporting', 'label': 'Tunjangan Penunjang siff Operasional'},
			{'model': 'Master_Salary.life_cost_support', 'label': 'Tunjangan Biaya Hidup'},
			{'model': 'Master_Salary.credit_bank', 'label': 'Credit Bank'},
			{'model': 'Master_Salary.overtime', 'label': 'Lembur'},
			{'model': 'Master_Salary.set_of_overtime', 'label': 'Persentase Lembur'},
        )},

        {'app': 'report_builder', 'label': 'Pelaporan', 'icon': 'icon-list-alt'},
        {'app': 'auth', 'label': 'Pengaturan User', 'icon': 'icon-cog', 'models': (
            {'model': 'auth.group', 'label': 'Pengaturan Grup Hak Akses'},
            {'model': 'auth.user', 'label': 'Pengaturan Akun Pengguna'},
            {'model': 'master_sales.userstaff', 'label': 'Pengaturan Akun Staf'},
            {'model': 'master_sales.staffperson', 'label': 'Pengaturan Staf'},
            {'model': 'sites.site', 'label': 'Pengaturan Web'},
        )},
    )
}

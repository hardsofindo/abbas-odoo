from openerp.osv import fields, osv
from openerp import api
import time
# from datetime import datetime, timedelta
# from openerp.tools.translate import _
# from openerp import SUPERUSER_ID


class data_audit(osv.osv):
    _name = "data.audit"
    _description = "Master Data Informastion Audit"
    _order = 'tgl_jatuh_tempo desc, id desc'
    _columns = {
                'nm_custome': fields.char('Nama Custome', required=True),
                'season_id':fields.many2one('mi.season', 'Season'),          
                'nm_masuk_gdg':fields.selection([('tgr', 'TIGA RAKSA'),('sby', 'SURABAYA'),], string='Nm.Gudang Masuk', help = 'Incoming Shipment Location Warehouse'),          
                'tgl_masuk_gdg':fields.date('Tgl. Masuk Gudang', help = 'Tanggal Incoming Shipment'),          
                'no_pen': fields.char('No. Pendaftaran', size=100),
                'tgl_pen':fields.date('Tgl. Pendaftaran '),          
                'tgl_jatuh_tempo':fields.datetime('Tgl. Jatuh Tempo', required=True),          
                'no_bl':fields.char('No. AWB/BL'),          
                'tgl_bl':fields.date('Tgl. AWB/BL'),          
                'no_sttj':fields.char('No. STTJ'),          
                'tgl_sttj':fields.date('Tgl. STTJ'),          
                'no_sppb':fields.char('No. SPPB', help='SPPB = Surat Persetujuaan Pengeluaran Barang'),          
                'tgl_sppb':fields.date('Tgl. SPPB', help='SPPB = Surat Persetujuaan Pengeluaran Barang'),          
                'no_sptnp':fields.char('No. SPTNP', help = 'SPTNP = Surat Penetapan Tarif Nilai Pabeaan adalah surat penetapan Pejabat Bea dan Cukai atas tarif dan/atau nilai pabean yang bentuk, isi dan tata cara pengisiannya sesuai dengan ketentuan peraturan perundang-undangan tentang bentuk dan isi surat penetapan, surat keputusan, surat teguran dan surat paksa.'),          
                'tgl_sptnp':fields.date('Tgl. SPTNP', help = 'SPTNP = Surat Penetapan Tarif Nilai Pabeaan adalah surat penetapan Pejabat Bea dan Cukai atas tarif dan/atau nilai pabean yang bentuk, isi dan tata cara pengisiannya sesuai dengan ketentuan peraturan perundang-undangan tentang bentuk dan isi surat penetapan, surat keputusan, surat teguran dan surat paksa.'),          
                # Data Fields PIB
                'kd_kantor_pib':fields.char('Kd. Kantor PIB', help='kode kantor ini di gunakan untuk PIB'),          
                'no_pib_aju':fields.char('No. PIB AJU'),          
                'tgl_pib':fields.date('Tgl. PIB'),          
                'note':fields.text('Keterangan'),          
                'audit_line' : fields.one2many('data.audit.line', 'audit_line_id', copy = True, string = 'Informasi Data Barang'),
#                 'audit_linex' : fields.one2many('data_audit_detail', 'audit_data_ids', copy = True, string = 'Informasi Data Barang'),
                'state': fields.selection([
                                           ('draft', 'Proses'),('done', 'Selesai'),('cancel', 'Batal'),
                                           ], 'Status', readonly=True, select=True, states={'draft': [('readonly', True)]},
                                          help="""
                                            * New: Pemberitahuaan Bahwa Sedang dalam Proses.\n
                                            * Done: Bahwa Status Dari Audit Tersebut Sudah Selesai.\n
                                            * Cancel: Informasi KITE Tersebut Batal Untuk Diinput.\n"""),
                }

    _defaults = {
                 'state': 'draft'
                 }

    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
 
        if isinstance(ids, (long, int)):
            ids = [ids]
 
        res = []
        for record in self.browse(cr, uid, ids, context=context):
            date = record.tgl_jatuh_tempo
            display_name = record.nm_custome + ' (' + date + ')'
            res.append((record['id'], display_name))
        return res
    

    @api.model
    def create(self, vals):
        res = super(data_audit, self).create(vals)
        return res

    
    def action_new(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'draft'}, context=context)
        return True
  
    def action_done(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'done'}, context=context)
        return True

    def action_cancel(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'cancel'}, context=context)
        return True

data_audit()

class data_audit_line(osv.osv):
    _name = "data.audit.line"
    _description = " Informasi Data Barang "
    _columns = {
                'audit_line_id':fields.many2one('data.audit', string = 'Data Barang'),
                'audit_line_detail' : fields.one2many('data.audit.detail', 'audit_line_detail_id', copy = True, string = 'Informasi Data Barang Detail'),
                'audit_line_idx':fields.many2many('data.audit','audit_line_detail_id','audit_line'),          
                'kd_brg_konversi':fields.char('Konversi Kode Brg'),          
                'nm_brg_konversi':fields.char('Konversi Uraian brg'),          
                'size_konversi':fields.char('size'),          
                'color_konversi':fields.char('colour'),          
#                 'kandungan_persen':fields.char('Kandungan % fake'),          
                'ttl_qty_kandungan':fields.float('Ttl Kandungan QTY ', digits=(16, 2)),          
                # Data PIB
                'hs_code_pib':fields.char('Hs Code PIB'),          
                # other
#                 'seri_brg_pib':fields.char('Seri Brg PIB'),          
                'seri_brg_pib':fields.float('Seri Brg PIB', digits=(16, 0)),          
                'qty_po':fields.float('Qty P.O', digits=(16, 2)),          
                'satuan_po':fields.char('Satuan P.O'),          
                'konversi_qty_pib':fields.float('Konversi QTY PIB', digits=(16, 4)),          
                'konversi_satuan_pib':fields.char('Konversi Satuan PIB'),          
                'gw_pib':fields.float('Gross weight (kg)', digits=(16, 2)),          
                'nw_pib':fields.char('Nett Weight (Kg)', digits=(16, 2)),          
                'unit_price_pib':fields.float('Unit Price', digits=(16, 3)),          
                'value_pib':fields.float('Nilai PIB', digits=(16, 2)),          
                'currency_pib':fields.many2one('res.currency', string="Currency"),          
                'car_pib':fields.char('Car PIB'),          
                #po
                'no_purchase_order':fields.char('No. Purchase Order'),          
                'nm_supplier_po':fields.char('PO. Supplier'),
                # Data Payment Order
                'tgl_payment':fields.date('Tanggal Payment'),          
                'no_payment':fields.char('No. Payment'),          
                'nm_bank_payment':fields.char('Nama Bank Payment'),          
                'value_payment':fields.float(string='Nilai Payment',digits=(16, 2)),          
                'balance_payment':fields.float(string='Selisih',digits=(16, 2)),          
                'sisa_kite':fields.float('Sisa Kite', digits=(16, 2)),          
                'norut_line':fields.char('No. Urut'),          
               } 
data_audit_line() 

class data_audit_detail(osv.osv):
    _name = "data.audit.detail"
    _description = " Informasi Data Barang Detail"

#     def _get_material_use(self, cr, uid, ids, field, args, context = None):
#         res = {}
#         for detail in self.browse(cr, uid, ids, context = context):
#             res[detail.id]= sum([detail.kandungan_qty  +  detail.waste_qty_peb])
#             return res         

    def _onchange_data(self, cr, uid, ids, source_document, args, context = None):
        res = {}
        for detail in self.browse(cr, uid, ids, context = context):
            res[detail.id]= sum([detail.kandungan_qty  +  detail.waste_qty_peb])
            return res         

    _columns = {
                'audit_line_detail_id':fields.many2one('data.audit.line', string = 'Data Barang Detail'),
                'audit_data_ids':fields.many2one('data.audit', string = 'MASTER BARANG'),
                # ALL DATA PEB
                'norut_line2':fields.char('Category'),          
                'customer_peb':fields.many2one('res.partner', string = 'Customer'),          
                'kd_konversi_bc':fields.char('Kode Konversi'),          
                'kd_ktr_peb':fields.char('Kd. Kantor PEB'),          
                'no_peb':fields.char('No. PEB'),          
                'tgl_peb':fields.date('Tgl. PEB'),          
                'kd_brg_peb':fields.char('Kd. Barang PEB'),          
                'nm_brg_peb':fields.char('Uraian barang PEB'),          
                'color_brg_peb':fields.char('Color PEB'),          
                'qty_feb':fields.float('PEB QTY/PAIRS', digits=(16, 0)),          
                'seri_brg_peb':fields.float('Seri Brg PEB', digits=(16, 0)),          
                'source_document':fields.char('Nama Custome',required=True),          
                'hs_code_peb':fields.char('Hs Code PEB'),          
                'kandungan_qty':fields.float('Kandungan(qty)', digits=(16, 2)),          
                'waste_qty_peb':fields.float('Waste (qty)', digits=(16, 2)),          
                'waste_persen_peb':fields.float('Waste (%)', digits=(16, 0)),          
                'waste_kg':fields.float('Waste (kg)', digits=(16, 2)),          
                'material_use':fields.float('Material Usage', digits=(16, 2)),          
#                 'material_use':fields.function(_get_material_use, type='float', string = 'Material Usage',readonly=True, store=True, 
#                              help='Material Usage itu hasil dari Kandungan(qty) di tambah dengan Waste (qty)'),
                'sisa_kite':fields.float('Sisa Kite', digits=(16, 2)),          
                # Data PIB
                'kandungan_persen':fields.float('Terkandung %', digits=(16, 0)),          
#                 'kandungan_persen':fields.char('Kandungan %'),          
                'no_invoice':fields.char('No. Invoice'),          
                'tgl_invoice':fields.date('Tgl. Invoice'),
                #Spec Bom Consum
                'no_spec_bom':fields.char('No. Spec Bom'),          
                'yield_consum':fields.float(string="Yield Consum", digits=(10, 3)),          
                'group_size_consum':fields.char('Group Size Consum'),          
                'qty_spec_bom_consum':fields.float(string="Qty Consum", digits=(16, 0)),          
                                         
                # Data Lain Lain 
                'no_lpse':fields.char('No. LPSE/LPBC'),          
                'tgl_lpse':fields.date('Tgl. LPSE/LPBC'),                          
                'no_bon_permitaan':fields.char('No. Bon Permintaan'),          
                'tgl_bon_permintaan':fields.date('Tgl. Bon Permintaan'),                          
                'no_sj_pengajuaan':fields.char('No. Sj Pengajuaan'),          
                'tgl_sj_pengajuaan':fields.date('Tgl. Sj Pengajuaan'),                          
                         
                } 
data_audit_detail()   
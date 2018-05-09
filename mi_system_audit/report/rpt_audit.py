from openerp.osv import fields,osv
from openerp import tools
import openerp.addons.decimal_precision as dp
# from openerp import api, fields, tools

class rpt_audit(osv.osv):
    _name = 'rpt.audit'
    _description = " laporan Audit For Aggiomltimex"
    _auto = False
    _order = 'norut_line desc'
    _columns = {
                # To Table Pengajuaan Warna Hijau Toska atau warna cyan
                'nm_custome': fields.char('Nama Custome'),                                  #1
                'season_id':fields.many2one('mi.season', 'Season'),                         #2
                'no_bon_permitaan':fields.char('No. Bon Permintaan'),          #3
                'tgl_bon_permintaan':fields.date('Tgl. Bon Permintaan'),         #4                 
                'no_spec_bom':fields.char('No. Spec Bom'),          #5
                'yield_consum':fields.float(string="Yield Consum", digits=(10, 0)), #6         
                'group_size_consum':fields.char('Group Size Consum'),          #7
                'qty_spec_bom_consum':fields.float(string="Qty Consum", digits=(16, 2)),   #8       
                'no_sj_pengajuaan':fields.char('No. Sj Pengajuaan'),          #9
                'tgl_sj_pengajuaan':fields.date('Tgl. Sj Pengajuaan'),          #10                
                'kd_konversi_bc':fields.char('Kode Konversi'),          #11

                # To Table Barang Baku Warna Biru
                'kd_brg_konversi':fields.char('Konversi Kode brg'),          
                'nm_brg_konversi':fields.char('Konversi Uraian brg'),          
                'size_konversi':fields.char('size'),          #14
                'color_konversi':fields.char('colour'),          #15
                'kandungan_persen':fields.float('Terkandung(%)', digits=(16, 0)),          
                'kandungan_qty':fields.float('Kandungan(qty)', digits=(16, 2)), #17          
                'waste_persen_peb':fields.float('Waste(%)', digits=(16, 0)),       #18   
                'waste_qty_peb':fields.float('Waste(qty)', digits=(16, 2)),          #19
                'waste_kg':fields.float('waste(kg)', digits=(16, 2)),          #20
                'material_use':fields.float('Material Usage', digits=(16, 2)),   #21       
                'sisa_kite':fields.float('Sisa Kite', digits=(16, 2)),          #22
                'car_pib':fields.char('Car PIB'),          #23
                'tgl_jatuh_tempo':fields.date('Tgl. Jatuh Tempo'), #24          
                'no_bl':fields.char('No. AWB/BL'),          #25
                'tgl_bl':fields.date('Tgl. AWB/BL'),          #26
                'kd_kantor_pib':fields.char('Kd. Kantor PIB', help='kode kantor ini di gunakan untuk PIB'),  #27        
                'no_pib_aju':fields.char('No. PIB AJU'),          #28
                'tgl_pib':fields.date('Tgl. PIB'),          #29
                'seri_brg_pib':fields.float('Seri Brg PIB', digits=(16, 0)),    #30      
                'hs_code_pib':fields.char('Hs Code PIB'),         #31 
                'qty_po':fields.float('Qty P.O', digits=(16, 2)),    #32      
                'satuan_po':fields.char('Satuan P.O'),          #33
                'konversi_qty_pib':fields.char('KOnversi QTY PIB'), #34          
                'konversi_satuan_pib':fields.char('Konversi Satuan PIB'), #35          
                'gw_pib':fields.float('Gross weight (kg)', digits=(16, 2)),  #36        
                'nw_pib':fields.char('Nett Weight (Kg)', digits=(16, 2)),       #37   
                'unit_price_pib':fields.float('Unit Price', digits=(16, 3)),       #38   
                'value_pib':fields.float('Nilai', digits=(16, 2)),          #39
                'currency_pib':fields.many2one('res.currency', string="Currency"), #40          
                'no_sttj':fields.char('No. STTJ'),          #41
                'tgl_sttj':fields.date('Tgl. STTJ'),  #42
                'no_pen': fields.char('No. Pendaftaran', size=100),  #43
                'tgl_pen':fields.date('Tgl. Pendaftaran '),          # 44
                'no_sppb':fields.char('No. SPPB', help='SPPB = Surat Persetujuaan Pengeluaran Barang'), #45          
                'tgl_sppb':fields.date('Tgl. SPPB', help='SPPB = Surat Persetujuaan Pengeluaran Barang'),  #46        
                'no_sptnp':fields.char('No. SPTNP', help = 'SPTNP = Surat Penetapan Tarif Nilai Pabeaan adalah surat penetapan Pejabat Bea dan Cukai atas tarif dan/atau nilai pabean yang bentuk, isi dan tata cara pengisiannya sesuai dengan ketentuan peraturan perundang-undangan tentang bentuk dan isi surat penetapan, surat keputusan, surat teguran dan surat paksa.'),          #47
                'tgl_sptnp':fields.date('Tgl. SPTNP', help = 'SPTNP = Surat Penetapan Tarif Nilai Pabeaan adalah surat penetapan Pejabat Bea dan Cukai atas tarif dan/atau nilai pabean yang bentuk, isi dan tata cara pengisiannya sesuai dengan ketentuan peraturan perundang-undangan tentang bentuk dan isi surat penetapan, surat keputusan, surat teguran dan surat paksa.'),          #48
                'nm_masuk_gdg':fields.selection([('tgr', 'TIGA RAKSA'),('sby', 'SURABAYA'),], string='Nm.Gudang Masuk', help = 'Incoming Shipment Location Warehouse'),       #49   
                'tgl_masuk_gdg':fields.date('Tgl. Masuk Gudang', help = 'Tanggal Incoming Shipment'),          #50
                'tgl_payment':fields.date('Tanggal Payment'),          #51
                'no_payment':fields.char('No. Payment'),          #52
                'nm_bank_payment':fields.char('Nama Bank Payment'),  #53        
                'value_payment':fields.float(string='Nilai Payment',digits=(16, 2)),  #54        
                'balance_payment':fields.float(string='Selisih',digits=(16, 2)),         #55 
                'no_purchase_order':fields.char('No. Purchase Order'),          #56
                'nm_supplier_po':fields.char('PO. Supplier'),  #57
                
                #To Table Barang Jadi Warna Pink 
                'kd_ktr_peb':fields.char('Kd. Ktr PEB'),          #58
                'no_peb':fields.char('No. PEB'),          #59
                'tgl_peb':fields.date('Tgl. PEB'),          #60
                'customer_peb':fields.many2one('res.partner', string = 'Customer'), #61         
                'seri_brg_peb':fields.float('Seri Brg PEB', digits=(16, 0)),          
                'hs_code_peb':fields.char('Hs Code PEB'),          #63
                'kd_brg_peb':fields.char('Kd. Barang PEB'),          #64
                'nm_brg_peb':fields.char('Nm. brg PEB'),          #65
                'color_brg_peb':fields.char('Color PEB'),          #66
                'qty_feb':fields.float('QTY / PAIRS', digits=(16, 2)),  #67          
                'no_invoice':fields.char('No. Invoice'),          #68
                'tgl_invoice':fields.date('Tgl. Invoice'), #69
                'no_lpse':fields.char('No. LPSE / LPBC'),     #70     
                'tgl_lpse':fields.date('Tgl. LPSE / LPBC'),      #71                    
                'state': fields.selection([
                                           ('draft', 'Proses'),('done', 'Selesai'),('cancel', 'Batal'),
                                           ], 'Status', readonly=True, select=True, states={'draft': [('readonly', True)]},
                                          help="""
                                            * New: Pemberitahuaan Bahwa Sedang dalam Proses.\n
                                            * Done: Bahwa Status Dari Audit Tersebut Sudah Selesai.\n
                                            * Cancel: Informasi KITE Tersebut Batal Untuk Diinput.\n"""), #72
                
                'note':fields.text('Keterangan'),          
                'norut_line':fields.char('No'),          
                'norut_line2':fields.char('CTG'),          
                }


    def init(self, cr):
        tools.drop_view_if_exists(cr, 'rpt_audit')
        cr.execute("""
            CREATE OR REPLACE VIEW rpt_audit AS (
                SELECT  dtl.id as id, dtl.norut_line2, dtl.customer_peb, dtl.kd_konversi_bc, dtl.kd_ktr_peb, dtl.no_peb, dtl.tgl_peb, dtl.kd_brg_peb,
                        dtl.nm_brg_peb, dtl.color_brg_peb, dtl.qty_feb, dtl.seri_brg_peb, dtl.hs_code_peb, dtl.kandungan_qty,
                        dtl.waste_persen_peb, dtl.waste_qty_peb, dtl.waste_kg, dtl. material_use, dtl.sisa_kite, dtl.kandungan_persen,
                        dtl.no_invoice, dtl.tgl_invoice, dtl.no_spec_bom, dtl.yield_consum, dtl.group_size_consum, dtl.qty_spec_bom_consum,
                        dtl.no_lpse, dtl.tgl_lpse, dtl.no_bon_permitaan, dtl.tgl_bon_permintaan, dtl.no_sj_pengajuaan, dtl.tgl_sj_pengajuaan,
                        line.norut_line, line.kd_brg_konversi, line.nm_brg_konversi, line.size_konversi, line.color_konversi,
                        line.ttl_qty_kandungan, line.hs_code_pib, line.seri_brg_pib, line.qty_po, line.satuan_po,
                        line.konversi_qty_pib, line.konversi_satuan_pib, line.gw_pib, line.nw_pib, line.unit_price_pib,
                        line.value_pib, line.currency_pib, line.car_pib, line.no_purchase_order, line.nm_supplier_po,
                        line.tgl_payment, line.no_payment, line.nm_bank_payment, line.value_payment, line.balance_payment,  
                        (select nm_custome from data_audit dt where dt.id = line.audit_line_id) as nm_custome,  
                        (select season_id from data_audit dt where dt.id = line.audit_line_id) as season_id,  
                        (select nm_masuk_gdg from data_audit dt where dt.id = line.audit_line_id) as nm_masuk_gdg,  
                        (select tgl_masuk_gdg from data_audit dt where dt.id = line.audit_line_id) as tgl_masuk_gdg,  
                        (select no_pen from data_audit dt where dt.id = line.audit_line_id) as no_pen,  
                        (select tgl_pen from data_audit dt where dt.id = line.audit_line_id) as tgl_pen,  
                        (select tgl_jatuh_tempo from data_audit dt where dt.id = line.audit_line_id) as tgl_jatuh_tempo,  
                        (select no_bl from data_audit dt where dt.id = line.audit_line_id) as no_bl,  
                        (select tgl_bl from data_audit dt where dt.id = line.audit_line_id) as tgl_bl,  
                        (select no_sttj from data_audit dt where dt.id = line.audit_line_id) as no_sttj,  
                        (select tgl_sttj from data_audit dt where dt.id = line.audit_line_id) as tgl_sttj,  
                        (select no_sppb from data_audit dt where dt.id = line.audit_line_id) as no_sppb,  
                        (select tgl_sppb from data_audit dt where dt.id = line.audit_line_id) as tgl_sppb,  
                        (select no_sptnp from data_audit dt where dt.id = line.audit_line_id) as no_sptnp,  
                        (select tgl_sptnp from data_audit dt where dt.id = line.audit_line_id) as tgl_sptnp,  
                        (select kd_kantor_pib from data_audit dt where dt.id = line.audit_line_id) as kd_kantor_pib,  
                        (select no_pib_aju from data_audit dt where dt.id = line.audit_line_id) as no_pib_aju,  
                        (select tgl_pib from data_audit dt where dt.id = line.audit_line_id) as tgl_pib,  
                        (select state from data_audit dt where dt.id = line.audit_line_id) as state,  
                        (select note from data_audit dt where dt.id = line.audit_line_id) as note  
                FROM data_audit_detail dtl
                JOIN data_audit_line line ON line.id = dtl.audit_line_detail_id
                ORDER BY id
                    )""")
 

#                         line.ttl_qty_kandungan, line.hs_code_pib, line.seri_brg_pib, line.qty_po, line.satuan_po,
#                         line.konversi_qty_pib, line.konversi_satuan_pib, line.gw_pib, line.nw_pib, line.unit_price_pib,
#                         line.value_pib, line.currency_pib, line.car_pib, line.no_purchase_order, line.nm_supplier_po,
#                         line.tgl_payment, line.no_payment, line.nm_bank_payment, line.value_payment, line.balance_payment, line.sisa_kite,  


#                 SELECT  dtl.* , 
#                         line.kd_brg_konversi,line.nm_brg_konversi,line.size_konversi,line.color_konversi,
#                         line.ttl_qty_kandungan, line.hs_code_pib, line.seri_brg_pib, line.qty_po, line.satuan_po,
#                         line.konversi_qty_pib, line.konversi_satuan_pib, line.gw_pib, line.nw_pib, line.unit_price_pib,
#                         line.value_pib, line.currency_pib, line.car_pib, line.no_purchase_order, line.nm_supplier_po,
#                         line.tgl_payment, line.no_payment, line.nm_bank_payment, line.value_payment, line.balance_payment, line.sisa_kite,  
#                         dt.nm_custome, dt.season_id, dt.nm_masuk_gdg, dt.tgl_masuk_gdg, dt.no_pen, dt.tgl_pen,
#                         dt.tgl_jatuh_tempo, dt.no_bl, dt.tgl_bl, dt.no_sttj, dt.tgl_sttj, dt.no_sppb, dt.tgl_sppb,
#                         dt.no_sptnp, dt.tgl_sptnp, dt.kd_kantor_pib, dt.no_pib_aju, dt.tgl_pib, dt.state    
#                 FROM data_audit_detail dtl
#                 JOIN data_audit_line line ON line.id = dtl.audit_line_detail_id
#                 INNER JOIN data_audit dt ON dt.id = dtl.audit_data_ids
 
 
        
        
#     def init(self, cr):
#         tools.drop_view_if_exists(cr, 'rpt_audit')
#         cr.execute("""
#             CREATE OR REPLACE VIEW rpt_audit AS (
#                  select
#                  (select nm_custome from data_audit dt where dt.id = line.audit_line_id) as nm_custome,
#                  (select season_id from data_audit dt where dt.id = line.audit_line_id) as season_id,
#                  (select nm_masuk_gdg from data_audit dt where dt.id = line.audit_line_id) as nm_masuk_gdg,
#                  (select tgl_masuk_gdg from data_audit dt where dt.id = line.audit_line_id) as tgl_masuk_gdg,
#                  (select no_pen from data_audit dt where dt.id = line.audit_line_id) as no_pen,
#                  (select tgl_pen from data_audit dt where dt.id = line.audit_line_id) as tgl_pen,
#                  (select tgl_jatuh_tempo from data_audit dt where dt.id = line.audit_line_id) as tgl_jatuh_tempo,
#                  (select no_bl from data_audit dt where dt.id = line.audit_line_id) as no_bl,
#                  (select tgl_bl from data_audit dt where dt.id = line.audit_line_id) as tgl_bl,
#                  (select no_sttj from data_audit dt where dt.id = line.audit_line_id) as no_sttj,
#                  (select tgl_sttj from data_audit dt where dt.id = line.audit_line_id) as tgl_sttj,
#                  (select no_sppb from data_audit dt where dt.id = line.audit_line_id) as no_sppb,
#                  (select tgl_sppb from data_audit dt where dt.id = line.audit_line_id) as tgl_sppb,
#                  (select no_sptnp from data_audit dt where dt.id = line.audit_line_id) as no_sptnp,
#                  (select tgl_sptnp from data_audit dt where dt.id = line.audit_line_id) as tgl_sptnp,
#                  (select kd_kantor_pib from data_audit dt where dt.id = line.audit_line_id) as kd_kantor_pib,
#                  (select no_pib_aju from data_audit dt where dt.id = line.audit_line_id) as no_pib_aju,
#                  (select tgl_pib from data_audit dt where dt.id = line.audit_line_id) as tgl_pib,
#                  (select kd_konversi_bc from data_audit dt where dt.id = line.audit_line_id) as kd_konversi_bc,
#                  line.id, line.size_konversi, line.color_konversi, line.kandungan_persen, line.ttl_qty_kandungan, line.hs_code_pib,
#                  dtl.seri_brg_peb, dtl.hs_code_peb, dtl.kandungan_qty, dtl.waste_persen_peb, dtl.waste_qty_peb, dtl.waste_kg, dtl.material_use,
#                  dtl.sisa_kite, dtl.seri_brg_pib, dtl.qty_po, dtl.satuan_po, dtl.konversi_qty_pib, dtl.konversi_satuan_pib, dtl.gw_pib, dtl.nw_pib,
#                  dtl.unit_price_pib, dtl.value_pib, dtl.currency_pib, dtl.car_pib, dtl.tgl_payment, dtl.no_payment, dtl.nm_bank_payment, dtl.value_payment,
#                  dtl.balance_payment, dtl.no_purchase_order, dtl.nm_supplier_po, dtl.no_invoice, dtl.tgl_invoice, dtl.no_spec_bom,  dtl.yield_consum, 
#                  dtl.group_size_consum, dtl.qty_spec_bom_consum, dtl.no_lpse, dtl.tgl_lpse, dtl.no_bon_permitaan, dtl.tgl_bon_permintaan, 
#                  dtl.no_sj_pengajuaan, dtl.tgl_sj_pengajuaan, dtl.nm_brg_peb, dtl.kd_ktr_peb, dtl.tgl_peb, dtl.kd_brg_peb, dtl.no_peb, dtl.customer_peb                 
#                  FROM data_audit_line line
#                  INNER JOIN data_audit_detail dtl ON dtl.audit_line_detail_id = line.audit_line_id
#                  
#                     )""")





rpt_audit()
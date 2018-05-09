import datetime
from lxml import etree
import math
import pytz
import threading
import urlparse


from datetime import datetime, timedelta
from openerp import SUPERUSER_ID
from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT


class data_audit(models.Model):
    _inherit = "data.audit"

    @api.model
    def _cron_auto_reminder_audit(self):
        su_id =self.env['res.partner'].browse(SUPERUSER_ID)
        for audit in self.env['data.audit'].search([]):
            bdate =datetime.strptime(audit.tgl_jatuh_tempo,'%Y-%m-%d').date()
            today =datetime.now().date()
            if bdate != today:
                if bdate.month == today.month:
                    if bdate.day == today.day:
                        if audit:
                            template_id = self.env['ir.model.data'].get_object_reference(
                                                                  'mi_system_audit',
                                                                  'email_template_edi_deadline_audit_reminder')[1]
                            email_template_obj = self.env['mail.template'].browse(template_id)
                            if template_id:
                                values = email_template_obj.generate_email(audit.id, fields=None)
                                values['email_from'] = su_id.email
                                values['email_to'] = partner.email
                                values['res_id'] = False
                                mail_mail_obj = self.env['mail.mail']
                                msg_id = mail_mail_obj.create(values)
                                if msg_id:
                                    mail_mail_obj.send([msg_id])
 
        return True


# class data_audit(models.Model):
#     _inherit = "data.audit.detail"
# 
#     @api.onchange('nm_custome')
#     def _check_change(self):
#         self.name = self.nm_custome.name

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

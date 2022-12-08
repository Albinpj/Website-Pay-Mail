from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherited(WebsiteSale):
    @http.route(['/shop/confirmation'], type='http', auth="public", website=True, sitemap=False)
    def shop_payment_confirmation(self, **post):
        res = super(WebsiteSaleInherited, self).shop_payment_confirmation(**post)
        admin_list = []
        users = request.env['res.users'].search([]).filtered(lambda lm: lm.has_group('sales_team.group_sale_manager'))
        print(users)
        for rec in users:
            admin_list.append(rec.login)
            for dec in admin_list:
                email_values = {
                    'email_cc': False,
                    'auto_delete': True,
                    'recipient_ids': [],
                    'partner_ids': [],
                    'scheduled_date': False,
                    'email_to': dec
                }
                # print(email_values)
                # print(admin_list)
                mail = request.env['sale.order'].sudo().search([('id', '=', request.session.sale_last_order_id)])
                # print(request.session)
                # print(mail)
                template = request.env.ref('pay_mail.email_template_pay_email')
                template.send_mail(mail.id, force_send=True, email_values=email_values)
        return res

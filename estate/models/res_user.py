from odoo import fields, models

class ResUser(models.Model):
    _inherit = "res.user"

    property_ids = fieldsOne2many("estate.property", "user_id", string="Properties", domain=[("state", "in", ["new", "offer_received"])])
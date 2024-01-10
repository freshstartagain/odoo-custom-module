from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float("Price")
    status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused")
        ],
        string="Status",
        copy=False
    )
    partner_id = fields.Many2one("res.partner", require=True, string="Partner")
    property_id = fields.Many2one("estate.property", require=True, string="Property")
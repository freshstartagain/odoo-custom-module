from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

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
    validity = fields.Integer("Validity", default=7)
    date_deadline = fields.Date("Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days
            
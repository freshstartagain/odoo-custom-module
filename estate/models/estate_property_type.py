from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]
    _order = "name"
    
    # Basic
    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=1, help="Used to order stages. Lower is better.")

    # Relationships
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties") 
from odoo import models, fields, api


class plastic_mold(models.Model):
    _name = 'plastic.mold'

    #defining variables(field names)

    name = fields.Char('Mold Name', required=True)
    no_of_cavity = fields.Integer('Number of Cavity')
    pcs_in_ctns = fields.Integer('Pieces in Cartons')
    shot_wt_in_grams = fields.Float('Shot(Weight in grams)')
    runner_wt_grams = fields.Float('Runner(Weight in grams)')
    description = fields.Text('Description')

class plastic_machine(models.Model):
    _name = 'plastic.machine'

    #defining variables(field names)
    name = fields.Char('Machine Name', required=True)
    mold_id = fields.Many2one('plastic.mold', 'Mold')
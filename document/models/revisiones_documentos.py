from odoo import fields, models, api

class Revisiones(models.Model):
    _name = 'documentos.revisiones'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'revisiones'
    
    name = fields.Many2one("documentos.documentos", string='Documento')
    rev = fields.Char(string="Número de revisión")
    date = fields.Date(string='Fecha de revisión')
    file = fields.Binary(string='Archivo')
    user_id = fields.Many2one("res.users", string="Usuario que creó la revisión")
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En proceso'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado'),
    ], string="Estado", default="draft")

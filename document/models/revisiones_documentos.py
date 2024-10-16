from odoo import fields, models, api, exceptions

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
    
    # Asegúrate de que folder_id esté definido en este modelo
    # edit_groups_id = fields.Many2many('res.groups', string='Grupos de edición', related='folder_id.edit_groups_id')

    def check_access_rule(self, operation):
        if operation == 'write':
            if self.edit_groups_id:
                if not self.env.user.groups_id & self.edit_groups_id:
                    raise exceptions.AccessError("No tienes permiso para editar este registro")
            else:
                return True
        return super(Revisiones, self).check_access_rule(operation)
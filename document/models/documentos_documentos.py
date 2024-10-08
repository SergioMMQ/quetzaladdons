from odoo import fields, models, api, exceptions

class Documentos(models.Model):
    _name = 'documentos.documentos'
    _inherit = ['mail.thread']
    _description = 'Document'


    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string='Descripción del documento')
    type = fields.Selection([
        ('file', 'Archivo'),
        ('url', 'Enlace'),
        ('content', 'Contenido')
    ], string='Tipo', required=True, default='file')
    content = fields.Text(string='Contenido')
    file_name = fields.Char(string='Nombre del archivo adjunto')
    files = fields.One2many("documentos.revisiones", "name", string="Revisiones")
    file = fields.Binary(string='Archivo', compute='_compute_last_revision_file')
    url = fields.Char(string='Enlace')
    folder_id = fields.Many2one('documents.folder', string='Carpeta')
    res_model = fields.Char(string='Modelo relacionado')
    date = fields.Datetime(string='Fecha de creación', default=fields.Datetime.now)
    author_id = fields.Many2one('res.users', string='Autor', default=lambda self: self.env.user)
    message_ids = fields.One2many('mail.message', 'res_id', string="Mensajes")
    edit_groups_id = fields.Many2many('res.groups', string='Grupos de edición', related='folder_id.edit_groups_id')

    @api.depends('files')
    def _compute_last_revision_file(self):
        for record in self:
            if record.files:
                last_revision = record.files[-1]
                record.file = last_revision.file
            else:
                record.file=None

    def check_access_rule(self, operation):
        if operation == 'write':
            if self.edit_groups_id:
                if not self.env.user.groups_id & self.edit_groups_id:
                    raise exceptions.AccessError("No tienes permiso para editar este registro")
            else:
                return True
        return super(Documentos, self).check_access_rule(operation)
    

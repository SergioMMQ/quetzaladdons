import logging
from odoo import models, fields, exceptions

_logger = logging.getLogger(__name__)

class Folder(models.Model):
    _name = 'documents.folder'
    _description = 'Carpeta de documentos'

    name = fields.Char(string='Nombre', required=True, unique=True)
    description = fields.Text(string='Descripción de la carpeta')
    parent_id = fields.Many2one('documents.folder', string='Carpeta padre', ondelete='cascade')
    child_ids = fields.One2many('documents.folder', 'parent_id', string='Carpetas hijas', readonly=True)
    document_ids = fields.One2many('documentos.documentos', 'folder_id', string='Documentos')
    create_date = fields.Datetime(string='Fecha de creación', readonly=True)
    write_date = fields.Datetime(string='Fecha de actualización', readonly=True)
    
    edit_groups_id = fields.Many2many(
    'res.groups',
    'documents_folder_edit_rel',  # Nombre explícito para la relación Many2many
    'folder_id', 'group_id',
    string='Grupos que pueden editar'
    )
    view_groups_id = fields.Many2many(
    'res.groups',
    'documents_folder_view_rel',  # Nombre explícito para la relación Many2many
    'folder_id', 'group_id',
    string='Grupos que pueden ver'
    )
    
    def check_access_rule(self, operation):
        if operation == 'write':
            if self.edit_groups_id:
                if not self.env.user.groups_id & self.edit_groups_id:
                    raise exceptions.AccessError("No tienes permiso para editar este registro")
            else:
                return True
        return super(Folder, self).check_access_rule(operation)
from openerp.osv import osv,fields

class prcinf_serveur(osv.osv):
    _name = 'prcinf.serveur'
    _order = 'name asc'
    _columns = {
         'name': fields.char('name', size=64,required=True ),
         'code': fields.char('Code', size=64 ),
         'type': fields.selection(selection=[('web', 'Web'),('files', 'Files'),('data_base', 'Data Base'),], string='Type', default='web'),
         'os': fields.selection(selection=[('linux', 'Linux'),('windows', 'Windows'),], string='OS', default='linux'),
         'prix': fields.float('Prix'),
         'date_achat': fields.date('Date d\'achat'),
         'date_fin_garantie': fields.date('Date fin de garantie'),
         'ip': fields.char('IP'),
         'login': fields.char('Login'),
         'password': fields.char('Password'),

        #Relation entre les models
        'ref_brand': fields.many2one('prcinf.brand','Marque',ondelete='cascade'),
        'ref_fournisseur': fields.many2one('prcinf.fournisseur','Fournisseur'),
        'ref_stock': fields.many2one('prcinf.stock','Stock',ondelete='cascade'),
        'ref_reseau': fields.many2one('prcinf.reseau','Reseau'),
        'ref_responsable': fields.many2one('prcinf.responsable','Responsable'),
    }
    _defaults = {
        'type' : "web",
        'ip' : "0.0.0.0",
     } 

prcinf_serveur()
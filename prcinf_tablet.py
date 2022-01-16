from openerp.osv import osv,fields

class prcinf_tablet(osv.osv):
    _name = 'prcinf.tablet'
    _columns = {
        'name': fields.char('Nom', size=128,required=True ),
        'code': fields.char('Code', size=64,required=True ),
        'type': fields.selection(selection=[('web', 'Web'),('files', 'Files'),('data_base', 'Data Base'),], string='Type', default='web'),
        'os': fields.selection(selection=[('android', 'Android'),('ios', 'macOS'),('windows', 'Windows'),], string='OS', default='android'),
        'prix': fields.float('Prix',required=True),
        'ip': fields.char('IP'),
        'date_achat': fields.date('Date Achat'),
        'date_fin_garantie': fields.date('Date de fin de garantie'),
        #Relation entre les models
        'ref_brand': fields.many2one('prcinf.brand','Marque',ondelete='cascade'),
        'ref_fournisseur': fields.many2one('prcinf.fournisseur','Fournisseur',ondelete='cascade'),
        'ref_stock': fields.many2one('prcinf.stock','Stock',ondelete='cascade'),
        'ref_reseau': fields.many2one('prcinf.reseau','Reseau',ondelete='cascade'),
        'ref_responsable': fields.many2one('prcinf.responsable','Responsable',ondelete='cascade'),
    }
    _defaults = {
        'type' : "tablettes_tactiles",
        'ip' : "0.0.0.0",
     } 

prcinf_tablet()    
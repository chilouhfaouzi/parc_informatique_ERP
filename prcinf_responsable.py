from openerp.osv import osv,fields

class prcinf_responsable(osv.osv):
    _name = 'prcinf.responsable'
    _columns = {
        'name': fields.char('Name', size=64,required=True ),
        'cin': fields.char('CIN', size=7,required=True ),
        'tel': fields.char('Tel', size=64 ),
        'email': fields.char('Email', size=64 ),
        'adresse': fields.char('Adresse', size=64 ),
        'date_naissance': fields.date('Date Naissance'),
        'date_embauche': fields.date('Date d\'embauche'),
        'image': fields.binary('Image'),

        #Relation entre les models  
        'ref_departement': fields.many2one('prcinf.departement','Departement'),
        'ref_ordns': fields.one2many('prcinf.ordinateur','ref_responsable',string='Ordinateurs'),
        'ref_tablets': fields.one2many('prcinf.tablet','ref_responsable',string='Tablets'),
        'ref_serveurs': fields.one2many('prcinf.serveur','ref_responsable',string='Serveurs'),
        'ref_stock': fields.one2many('prcinf.stock','ref_responsable',string='Stock'),

    }
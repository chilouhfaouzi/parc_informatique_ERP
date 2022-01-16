from openerp.osv import osv,fields

class prcinf_fournisseur(osv.osv):
    _name = 'prcinf.fournisseur'
    _columns = {
        'name': fields.char('Nom', size=128,required=True ),
        'code': fields.char('Code', size=128 ),
        'tel': fields.char('Telephone', size=64,required=True ),
        'fax': fields.char('Fax', size=64 ),
        'email': fields.char('Email', size=64 ),
        'adresse': fields.char('Adresse', size=64 ),

        #Relation entre les models
        'ref_ordns': fields.one2many('prcinf.ordinateur','ref_fournisseur',string='Ordinateurs'),
        'ref_tablets': fields.one2many('prcinf.tablet','ref_fournisseur',string='Tablets'),
        'ref_peripheriques': fields.one2many('prcinf.peripherique','ref_fournisseur',string='Peripheriques'),
        'ref_serveurs': fields.one2many('prcinf.serveur','ref_fournisseur',string='Serveurs'),
    }

prcinf_fournisseur()


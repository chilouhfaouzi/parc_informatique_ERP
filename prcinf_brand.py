from openerp.osv import osv,fields

class prcinf_brand(osv.osv):
    _name = 'prcinf.brand'
    _columns = {
    'name': fields.char('Libelle', size=64,required=True ),
    'code': fields.char('Code', size=64 ),

    #Relation entre les models
    'ref_ordns': fields.one2many('prcinf.ordinateur','ref_brand',string='Ordinateurs'),
    'ref_serveurs': fields.one2many('prcinf.serveur','ref_brand',string='Serveurs'),
    'ref_tablets': fields.one2many('prcinf.tablet','ref_brand',string='Tablets'),
    'ref_peripheriques': fields.one2many('prcinf.peripherique','ref_brand',string='Peripheriques'),
    
    }

prcinf_brand()


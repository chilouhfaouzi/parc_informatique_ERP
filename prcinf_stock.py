from openerp.osv import osv,fields

class prcinf_stock(osv.osv):
    _name = 'prcinf.stock'
    _columns = {
        'name': fields.char('Nom', size=128,required=True ),
        'code': fields.char('Code', size=64 ),
        'capacity': fields.float('Capacite'),
        'lieu': fields.char('Lieu', size=64 ),
        'description': fields.char('Description'),

        #Relation entre les models
        'ref_ordns': fields.one2many('prcinf.ordinateur','ref_stock','Ordinateurs'),
        'ref_tablets': fields.one2many('prcinf.tablet','ref_stock',string='Tablets'),
        'ref_peripheriques': fields.one2many('prcinf.peripherique','ref_stock',string='Peripheriques'),
        'ref_serveurs': fields.one2many('prcinf.serveur','ref_stock',string='Serveurs'),
        'ref_responsable': fields.many2one('prcinf.responsable','Responsable'),
    }
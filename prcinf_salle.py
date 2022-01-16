from openerp.osv import osv,fields

class prcinf_salle(osv.osv):
    _name = 'prcinf.salle'
    _columns = {
        'name': fields.char('Name', size=64,required=True ),
        'numero': fields.integer('Numero', size=64,required=True ),
        'block': fields.selection(selection=[('a', 'BLOCK A'),('b', 'BLOCK B'),('c', 'BLOCK C'),], string='BLOCK'),
        'capacity': fields.integer('Capacite'),

        #Relation entre les models
        'ref_ordns': fields.one2many('prcinf.ordinateur','ref_salle',string='Ordinateurs'),
    }
from openerp.osv import osv,fields

class prcinf_departement(osv.osv):
    _name = 'prcinf.departement'
    _columns = {
      'name': fields.char('Nom', size=128,required=True ),
      'code': fields.char('Code', size=64,required=True ),
      'tel': fields.char('Tel'),
      'fax': fields.char('Fax'),
      'email': fields.char('Email'),
      'adresse': fields.char('Adresse'),
      'description': fields.char('Description'),

      #Relation entre les models
      'ref_ordns': fields.one2many('prcinf.ordinateur','ref_departement',string='Ordinateurs'),
      'ref_responsable': fields.many2one('prcinf.responsable','Responsable'),
      

    }

# prcinf_departement()
      

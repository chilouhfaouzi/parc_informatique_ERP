from openerp.osv import osv,fields

class prcinf_peripherique(osv.osv):
    _name = 'prcinf.peripherique'
    _columns = {
        'name': fields.char('Nom', size=128,required=True ),
        'code': fields.char('Code', size=64,required=True ),
        'type': fields.selection(selection=[('souris', 'Souris'),('clavier', 'Clavier'),('moniteur', 'Moniteur'),('imprimante', 'Imprimante'),('webcam', 'Webcam')], string='Type'),
        'prix': fields.float('Prix'),
        'date_achat': fields.date('Date d\'achat'),
        'date_fabrication': fields.date('Date de fabrication'),

        #Relation entre les models
        'ref_brand': fields.many2one('prcinf.brand','Marque',ondelete='cascade'),
        'ref_ordinateur': fields.many2one('prcinf.ordinateur','Ordinateur',ondelete='cascade'),
        'ref_fournisseur': fields.many2one('prcinf.fournisseur','Fournisseur',ondelete='cascade'),
        'ref_stock': fields.many2one('prcinf.stock','Stock',ondelete='cascade'),

    }

prcinf_peripherique()


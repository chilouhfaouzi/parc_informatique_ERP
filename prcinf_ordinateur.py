from openerp.osv import osv,fields

class prcinf_ordinateur(osv.osv):
    _name = 'prcinf.ordinateur'
    _columns = {
        'code': fields.char('Code', size=64,required=True ),
        'name': fields.char('name', size=64,required=True ),
        'type': fields.selection(selection=[('poste', 'Poste'),('portable', 'Portable'),], string='Type', default='poste'),
        'os': fields.selection(selection=[('linux', 'Linux'),('mac', 'MacOS'),('windows', 'Windows'),], string='OS', default='linux'),
        'processeur': fields.selection(selection=[('i3', 'I3'),('i5', 'I5'),('i7', 'I7'),], string='Processeur', default='i5'),
        'ram': fields.selection(selection=[('4', '4'),('8', '8'),('16', '16'),('32', '32'),('64', '64'),], string='Ram', default='8'),
        'prix': fields.float('Prix',required=True),
        'date_achat': fields.date('Date d\'achat'),
        'date_fin_garantie': fields.date('Date de fin de garantie'),
        'mac': fields.char('MAC'),
        'ip': fields.char('IP'),

        #Relation entre les models
        'ref_departement': fields.many2one('prcinf.departement','Departement',ondelete='cascade'),
        'ref_brand': fields.many2one('prcinf.brand','Marque',ondelete='cascade'),
        'ref_responsable': fields.many2one('prcinf.responsable','Responsable',ondelete='cascade'),
        'ref_salle': fields.many2one('prcinf.salle','Salle'),
        'ref_peripheriques': fields.one2many('prcinf.peripherique','ref_ordinateur',string='Peripheriques'),
        'ref_fournisseur': fields.many2one('prcinf.fournisseur','Fournisseur',ondelete='cascade'),
        'ref_stock': fields.many2one('prcinf.stock','Stock',ondelete='cascade'),
        'ref_reseau': fields.many2one('prcinf.reseau','Reseau',ondelete='cascade'),
    }
    _defaults = {
        'mac' : "00:00:00:00:00:00",
        'ip' : "0.0.0.0",
     } 
    

prcinf_ordinateur()


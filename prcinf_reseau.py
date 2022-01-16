from openerp.osv import osv,fields

class prcinf_reseau(osv.osv):
    _name = 'prcinf.reseau'
    _columns = {
        'name': fields.char('name', size=64, required=True ),
        'code': fields.char('Code', size=64 ),
        'type':  fields.selection(selection=[('pan', 'PAN'),('lan', 'LAN'),('wlan', 'WLAN'),('vpn', 'VPN'),], string='Type', default='wlan'),
        'ip': fields.char('IP',required=True),
        'default_gateway': fields.char('Default Gateway'),
        'dns': fields.char('DNS'),

        #Relation entre les models
        'ref_ordns': fields.one2many('prcinf.ordinateur','ref_reseau',string='Ordinateurs'),
        'ref_tablets': fields.one2many('prcinf.tablet','ref_reseau',string='Tablets'),
        'ref_serveurs': fields.one2many('prcinf.serveur','ref_reseau',string='Serveurs'),
    }
    _defaults = {
        'type' : "wlan",
         }

prcinf_reseau()


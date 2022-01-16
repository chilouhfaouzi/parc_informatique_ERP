{
'name' : "Parc Informatique",
'version' : '1.0',
'author' : 'CHILOUH, NAFID, ATTACHE',
'category' : 'ENSAH ERP',
'sequence' :1,
'icon': "prcinf/static/src/img/icon.jpg",
'description' : """
Module gestion de parc informatique
=====================================================
Ce module couvre les éléments suivants:
------------------------------------------------------
* Gestion des ordinateurs (Postes fixes, Portables)
* Gestion des peripheriques (Souris, clavier, cameras, imprimants ...)
* Gestion des serveurs 
* Gestion des Réseaux
* Gestion des Tablets
* Gestion des Stocks
* Gestion des Departements
* Gestion des Responsables
* Gestion des Salles
* Gestion des Responsables


""",
'website': 'http://www.ensah.ma',
'images' : [''],
'depends' : ['base'],
'data': ['prcinf_tablet_view.xml','prcinf_reseau_view.xml','prcinf_fournisseur_view.xml','prcinf_serveur_view.xml','prcinf_peripherique_view.xml','prcinf_responsable_view.xml','prcinf_departement_view.xml','prcinf_stock_view.xml','prcinf_salle_view.xml','prcinf_ordinateur_view.xml','prcinf_brand_view.xml'],
'update_xml': [ ],
'js': ['static/src/js/main.js'],
'qweb' : [],
'css':['static/src/css/main.css'],
'demo': [],
'test': [],
'installable': True,
'auto_install': False,
}
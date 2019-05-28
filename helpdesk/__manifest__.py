# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Helpdesk',
    'summary': """
        Helpdesk""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author':   'AdaptiveCity, '
                'C2i Change 2 Improve, '
                'Domatix, '
                'Factor Libre, '
                'SDi Soluciones, '
                'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/helpdesk',
    'depends': [
        'mail',
        'portal',
    ],
    'data': [
        'data/helpdesk_data.xml',
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_team_views.xml',
        'views/helpdesk_ticket_menu.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
}

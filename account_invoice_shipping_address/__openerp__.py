# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Account Invoice Shipping Address",
    "summary": "Add a field for shipping address in class account_invoice",
    "version": "9.0.1.0.0",
    "category": "Account",
    "website": "https://odoo-community.org/",
    "author": "<Deysy Mascorro, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "account",
        "sale",
    ],
    "data": [
        "views/account_invoice_view.xml",
    ],
    "demo": [

    ],
    "qweb": [

    ]
}

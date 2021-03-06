# -*- coding: utf-8 -*-
# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Manual",
    "version": "10.0.1.1.0",
    "author": "Savoir-faire Linux,Odoo Community Association (OCA)",
    "website": "http://www.savoirfairelinux.com",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        'document_page',
        'mgmtsystem',
    ],
    "data": [
        'data/mgmtsystem_manual.xml',
        'views/mgmtsystem_manual.xml',
        'views/document_page.xml',
        'security/manual_security.xml',
    ],
    "demo": [],
    'installable': True,
}

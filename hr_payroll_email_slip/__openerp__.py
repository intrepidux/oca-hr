# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2015 Salton Massally (<smassally@idtlabs.sl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Email Payslip',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': "Adds the ability to email employee payslip",
    'author': "Salton Massally <smassally@idtlabs.sl>, "
               "Odoo Community Association (OCA)",
    'website': 'http://idtlabs.sl',
    'license': 'AGPL-3',
    'depends': ['hr_payroll'],
    'data': [
        'views/hr_payslip_view.xml',
        'views/hr_payslip_run_view.xml',
        'data/payslip_emailtemplate.xml',
    ],
    'installable': True,
}

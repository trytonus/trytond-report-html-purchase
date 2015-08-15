# -*- coding: utf-8 -*-
from trytond.pool import Pool
from purchase import PurchaseReport, PurchaseReportWizardStart, \
    PurchaseReportWizard


def register():
    Pool.register(
        PurchaseReportWizardStart,
        module='report_html_purchase', type_='model'
    )
    Pool.register(
        PurchaseReport,
        module='report_html_purchase', type_='report'
    )
    Pool.register(
        PurchaseReportWizard,
        module='report_html_purchase', type_='wizard'
    )

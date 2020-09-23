from datetime import datetime, timedelta
from odoo import models, fields, api


class PlasticReportWizard(models.TransientModel):
    _name = 'plastic.data.report.wizard'

    date_start = fields.Datetime('Date Start')
    date_end = fields.Datetime('Date End')

    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_start': self.date_start,
                'date_end': self.date_end,
            },
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('plastic_output.action_report_plastic_details').report_action(self, data=data)



  
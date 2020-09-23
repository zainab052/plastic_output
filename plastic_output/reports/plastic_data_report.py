from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

class ReportPlasticData(models.AbstractModel):
    """Abstract Model for report template.
    
    """


    #Excel Report 
    _name = 'report.plastic_output.report_plastic_details'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']

        date_start = datetime.strptime(date_start, DATETIME_FORMAT)
        date_end = datetime.strptime(date_end, DATETIME_FORMAT)
       

        docs = []
        
        #search in plastic.data table
        plastics = self.env['plastic.data'].search([
            ('date', '>=', date_start),
            ('date', '<=', date_end),
            ], order='machine_id asc')
        for plastic in plastics:
            docs.append({
                'date': plastic.date,
                'name': plastic.name,
                'supervisor': plastic.supervisor_id.name,
                'machine' : plastic.machine_id.name,
                'mold' : plastic.mold,
                'cavity': plastic.machine_id.mold_id.no_of_cavity,
                'pcs_in_ctns' : plastic.machine_id.mold_id.pcs_in_ctns,
                'shot_wt_grams': plastic.machine_id.mold_id.shot_wt_in_grams,
                'runner_wt_grams': plastic.machine_id.mold_id.runner_wt_grams,
                'day_shots': plastic.day_shots,
                'night_shots': plastic.night_shots,
                'total_shots': plastic.total_shots,
                'total_input': plastic.total_input,
                'output_bottles': plastic.total_output_bottles,
                'wastage': plastic.wastage,
                'runner': plastic.runner,
                'lumps': plastic.lumps,
                'average': plastic.product_average,
            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }

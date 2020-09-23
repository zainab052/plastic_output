from odoo import models, fields, api
import datetime

class plastic_data(models.Model):
	_name = 'plastic.data'

	# defining variables

	name = fields.Char('Name', required=True)
	date = fields.Date('Date', default=datetime.datetime.now(), required=True)
	day_time_start = fields.Float('Day Start Time')
	day_time_end = fields.Float('Day End Time')
	total_day_time = fields.Float('Total Day Time', compute="_get_total_day_hours", store=True)
	total_night_time = fields.Float('Total Night Time', compute="_get_total_night_hours", store=True)
	total_time = fields.Float('Total Time', compute="_get_total_hours", store=True)
	night_time_start = fields.Float('Night Start Time')
	night_time_end = fields.Float('Night End Time')
	day_shots = fields.Integer('Day Shots')
	night_shots = fields.Integer('Night Shots')
	total_shots = fields.Integer('Total Shots', compute="_get_total_shots", store=True)

	machine_id = fields.Many2one('plastic.machine', 'Machine', required=True)
	mold = fields.Char('Mold', related='machine_id.mold_id.name')
	supervisor_id = fields.Many2one('hr.employee', required=True)
	total_input = fields.Float('Total Input')
	total_output_kg = fields.Float('Output in Kilograms')
	total_output_bottles = fields.Integer('Output in Bottles')
	wastage = fields.Float('Wastage')
	lumps = fields.Float('Lumps')
	product_average = fields.Float('Product Average', compute="_get_product_average", store=True)
	runner = fields.Float('Runner')

	
	# function for product average
	@api.depends('total_input', 'total_output_kg', 'wastage')
	def _get_product_average(self):
		for record in self:
			if record.total_output_kg > 0 and record.total_input > 0 and record.wastage > 0:
				product_average = record.total_output_kg / (record.total_input - record.wastage)
				record.product_average = product_average


	#function for total shots
	@api.depends('day_shots', 'night_shots')
	def _get_total_shots(self):
		for record in self:
			record.total_shots = record.day_shots + record.night_shots


	#function for day time and night time

	@api.depends('day_time_start', 'day_time_end')
	def _get_total_day_hours(self):
		for record in self:
			day_time = record.day_time_end - record.day_time_start
			record.total_day_time = day_time

	@api.depends('night_time_start', 'night_time_end')
	def _get_total_night_hours(self):
		for record in self:
			if (record.night_time_end > 0 and record.night_time_end <= 9):
				integer_night = int(record.night_time_end)
				if (integer_night > 0 and integer_night < 10):
					night_time_end = record.night_time_end + 24
				
				night_time = night_time_end - record.night_time_start
				record.total_night_time = night_time


	#function for total night time
	@api.depends('total_day_time', 'total_night_time')
	def _get_total_hours(self):
		for record in self:
			
			total = record.total_day_time + record.total_night_time
			record.total_time = total
			

    #automatic function for unit conversion(grams to kg)
	@api.onchange('wastage')
	def change_wastage_grams_to_kg(self):
		for record in self:
			record.wastage = record.wastage / 1000


	@api.onchange('lumps')
	def change_lumps_grams_to_kg(self):
		for record in self:
			record.lumps = record.lumps / 1000


	@api.onchange('runner')
	def change_runner_grams_to_kg(self):
		for record in self:
			record.runner = record.runner / 1000









	
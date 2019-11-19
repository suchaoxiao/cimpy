from cimpy.cgmes_v2_4_15.Equipment.DCConductingEquipment import DCConductingEquipment


class DCGround(DCConductingEquipment):
	'''
	A ground within a DC system.

	:inductance: Inductance to ground. Default: 0.0
	:r: Resistance to ground. Default: 0.0
		'''

	

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, inductance = 0.0, r = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inductance = inductance
		self.r = r
		
	def __str__(self):
		str = 'class=DCGround\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
from cimpy.cimgen_v2_4_15.Base import Base


class ActivePower(Base):
	'''
	Product of RMS value of the voltage and the RMS value of the in-phase component of the current.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	reference_dict = { 'DynamicsVersion': ['value','unit','multiplier', ],
					'StateVariablesVersion': ['value','unit','multiplier', ],
					'SteadyStateHypothesisVersion': ['value','unit','multiplier', ],
					 } 

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=ActivePower\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
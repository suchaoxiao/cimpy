from cimpy.output.MeasurementValue import MeasurementValue


class AccumulatorValue(MeasurementValue):
	'''
	AccumulatorValue represents an accumulated (counted) MeasurementValue.

	:Accumulator: The values connected to this measurement. Default: 
	:AccumulatorReset: The command that reset the accumulator value. Default: 
	:value: The value to supervise. The value is positive. Default: 
		'''

	cgmesProfile = MeasurementValue.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Accumulator': [cgmesProfile.EQ.value, ],
						'AccumulatorReset': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MeasurementValue: \n' + MeasurementValue.__doc__ 

	def __init__(self, Accumulator = , AccumulatorReset = , value = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Accumulator = Accumulator
		self.AccumulatorReset = AccumulatorReset
		self.value = value
		
	def __str__(self):
		str = 'class=AccumulatorValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str

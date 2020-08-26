from  import Base


class SvStatus(Base):
	'''
	State variable for status.

	:ConductingEquipment: The conducting equipment associated with the status state variable. Default: 
	:inService: The in service status as a result of topology processing. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'ConductingEquipment': [cgmesProfile.SV.value, ],
						'inService': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, ConductingEquipment = , inService = ,  ):
	
		self.ConductingEquipment = ConductingEquipment
		self.inService = inService
		
	def __str__(self):
		str = 'class=SvStatus\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str

from  import Base


class SvVoltage(Base):
	'''
	State variable for voltage.

	:angle: The voltage angle of the topological node complex voltage with respect to system reference. Default: 
	:v: The voltage magnitude of the topological node. Default: 
	:TopologicalNode: The state voltage associated with the topological node. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'angle': [cgmesProfile.SV.value, ],
						'v': [cgmesProfile.SV.value, ],
						'TopologicalNode': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, angle = , v = , TopologicalNode = ,  ):
	
		self.angle = angle
		self.v = v
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=SvVoltage\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str

from  import Base


class NonlinearShuntCompensatorPoint(Base):
	'''
	A non linear shunt compensator bank or section admittance value.

	:NonlinearShuntCompensator: Non-linear shunt compensator owning this point. Default: 
	:b: Positive sequence shunt (charging) susceptance per section Default: 
	:g: Positive sequence shunt (charging) conductance per section Default: 
	:sectionNumber: The number of the section. Default: 
	:b0: Zero sequence shunt (charging) susceptance per section Default: 
	:g0: Zero sequence shunt (charging) conductance per section Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'NonlinearShuntCompensator': [cgmesProfile.EQ.value, ],
						'b': [cgmesProfile.EQ.value, ],
						'g': [cgmesProfile.EQ.value, ],
						'sectionNumber': [cgmesProfile.EQ.value, ],
						'b0': [cgmesProfile.EQ.value, ],
						'g0': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, NonlinearShuntCompensator = , b = , g = , sectionNumber = , b0 = , g0 = ,  ):
	
		self.NonlinearShuntCompensator = NonlinearShuntCompensator
		self.b = b
		self.g = g
		self.sectionNumber = sectionNumber
		self.b0 = b0
		self.g0 = g0
		
	def __str__(self):
		str = 'class=NonlinearShuntCompensatorPoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str

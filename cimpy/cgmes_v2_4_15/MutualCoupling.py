from cimpy.output.IdentifiedObject import IdentifiedObject


class MutualCoupling(IdentifiedObject):
	'''
	This class represents the zero sequence line mutual coupling.

	:First_Terminal: The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments. Default: 
	:Second_Terminal: The starting terminal for the calculation of distances along the second branch of the mutual coupling. Default: 
	:b0ch: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. Default: 
	:distance11: Distance to the start of the coupled region from the first line`s terminal having sequence number equal to 1. Default: 
	:distance12: Distance to the end of the coupled region from the first line`s terminal with sequence number equal to 1. Default: 
	:distance21: Distance to the start of coupled region from the second line`s terminal with sequence number equal to 1. Default: 
	:distance22: Distance to the end of coupled region from the second line`s terminal with sequence number equal to 1. Default: 
	:g0ch: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 
	:r0: Zero sequence branch-to-branch mutual impedance coupling, resistance. Default: 
	:x0: Zero sequence branch-to-branch mutual impedance coupling, reactance. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'First_Terminal': [cgmesProfile.EQ.value, ],
						'Second_Terminal': [cgmesProfile.EQ.value, ],
						'b0ch': [cgmesProfile.EQ.value, ],
						'distance11': [cgmesProfile.EQ.value, ],
						'distance12': [cgmesProfile.EQ.value, ],
						'distance21': [cgmesProfile.EQ.value, ],
						'distance22': [cgmesProfile.EQ.value, ],
						'g0ch': [cgmesProfile.EQ.value, ],
						'r0': [cgmesProfile.EQ.value, ],
						'x0': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, First_Terminal = , Second_Terminal = , b0ch = , distance11 = , distance12 = , distance21 = , distance22 = , g0ch = , r0 = , x0 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.First_Terminal = First_Terminal
		self.Second_Terminal = Second_Terminal
		self.b0ch = b0ch
		self.distance11 = distance11
		self.distance12 = distance12
		self.distance21 = distance21
		self.distance22 = distance22
		self.g0ch = g0ch
		self.r0 = r0
		self.x0 = x0
		
	def __str__(self):
		str = 'class=MutualCoupling\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str

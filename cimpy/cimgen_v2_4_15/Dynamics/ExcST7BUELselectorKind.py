from cimpy.cimgen_v2_4_15.Base import Base


class ExcST7BUELselectorKind(Base):
	'''
	Type of connection for the UEL input used for static excitation systems type 7B.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=ExcST7BUELselectorKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
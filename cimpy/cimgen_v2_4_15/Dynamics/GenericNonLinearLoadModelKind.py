from cimpy.cimgen_v2_4_15.Base import Base


class GenericNonLinearLoadModelKind(Base):
	'''
	Type of generic non-linear load model.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=GenericNonLinearLoadModelKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
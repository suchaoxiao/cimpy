from cimpy.cgmes_v2_4_15.Base import Base


class StaticLoadModelKind(Base):
	'''
	Type of static load model.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=StaticLoadModelKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
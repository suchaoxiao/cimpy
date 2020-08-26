from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcOEX3T(ExcitationSystemDynamics):
	'''
	Modified IEEE Type ST1 Excitation System with semi-continuous and acting terminal voltage limiter.

	:t1: Time constant (T). Default: 
	:t2: Time constant (T). Default: 
	:t3: Time constant (T). Default: 
	:t4: Time constant (T). Default: 
	:ka: Gain (K). Default: 
	:t5: Time constant (T). Default: 
	:t6: Time constant (T). Default: 
	:vrmax: Limiter (V). Default: 
	:vrmin: Limiter (V). Default: 
	:te: Time constant (T). Default: 
	:kf: Gain (K). Default: 
	:tf: Time constant (T). Default: 
	:kc: Gain (K). Default: 
	:kd: Gain (K). Default: 
	:ke: Gain (K). Default: 
	:e1: Saturation parameter (E). Default: 
	:see1: Saturation parameter (S(E)). Default: 
	:e2: Saturation parameter (E). Default: 
	:see2: Saturation parameter (S(E)). Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'e1': [cgmesProfile.DY.value, ],
						'see1': [cgmesProfile.DY.value, ],
						'e2': [cgmesProfile.DY.value, ],
						'see2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, t1 = , t2 = , t3 = , t4 = , ka = , t5 = , t6 = , vrmax = , vrmin = , te = , kf = , tf = , kc = , kd = , ke = , e1 = , see1 = , e2 = , see2 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.ka = ka
		self.t5 = t5
		self.t6 = t6
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.e1 = e1
		self.see1 = see1
		self.e2 = e2
		self.see2 = see2
		
	def __str__(self):
		str = 'class=ExcOEX3T\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str

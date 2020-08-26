from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST1A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST1A model. This model represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier.  The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.  Reference: IEEE Standard 421.5-2005 Section 7.1.

	:ilr: Exciter output current limit reference (I).  Typical Value = 0. Default: 
	:ka: Voltage regulator gain (K).  Typical Value = 190. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.08. Default: 
	:kf: Excitation control system stabilizer gains (K).  Typical Value = 0. Default: 
	:klr: Exciter output current limiter gain (K).  Typical Value = 0. Default: 
	:pssin: Selector of the Power System Stabilizer (PSS) input (PSSin). true = PSS input (Vs) added to error signal false = PSS input (Vs) added to voltage regulator output. Typical Value = true. Default: 
	:ta: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:tb: Voltage regulator time constant (T).  Typical Value = 10. Default: 
	:tb1: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:tc: Voltage regulator time constant (T).  Typical Value = 1. Default: 
	:tc1: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 
	:uelin: Selector of the connection of the UEL input (UELin). Typical Value = ignoreUELsignal. Default: 
	:vamax: Maximum voltage regulator output (V).  Typical Value = 14.5. Default: 
	:vamin: Minimum voltage regulator output (V).  Typical Value = -14.5. Default: 
	:vimax: Maximum voltage regulator input limit (V).  Typical Value = 999. Default: 
	:vimin: Minimum voltage regulator input limit (V).  Typical Value = -999. Default: 
	:vrmax: Maximum voltage regulator outputs (V).  Typical Value = 7.8. Default: 
	:vrmin: Minimum voltage regulator outputs (V).  Typical Value = -6.7. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ilr': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'klr': [cgmesProfile.DY.value, ],
						'pssin': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tb1': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'tc1': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'uelin': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ilr = , ka = , kc = , kf = , klr = , pssin = , ta = , tb = , tb1 = , tc = , tc1 = , tf = , uelin = , vamax = , vamin = , vimax = , vimin = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ilr = ilr
		self.ka = ka
		self.kc = kc
		self.kf = kf
		self.klr = klr
		self.pssin = pssin
		self.ta = ta
		self.tb = tb
		self.tb1 = tb1
		self.tc = tc
		self.tc1 = tc1
		self.tf = tf
		self.uelin = uelin
		self.vamax = vamax
		self.vamin = vamin
		self.vimax = vimax
		self.vimin = vimin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEST1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str

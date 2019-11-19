from cimpy.cgmes_v2_4_15.Dynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPID2(TurbineGovernorDynamics):
	'''
	Hydro turbine and governor. Represents plants with straight forward penstock configurations and "three term" electro-hydraulic governors (i.e. Woodard electronic).

	:mwbase: Base for power values (MWbase) (&gt;0).  Unit = MW. Default: 0.0
	:treg: Speed detector time constant (Treg).  Typical Value = 0. Default: 0.0
	:rperm: Permanent drop (Rperm).  Typical Value = 0. Default: 0.0
	:kp: Proportional gain (Kp).  Typical Value = 0. Default: 0.0
	:ki: Reset gain (Ki).  Unit = PU/ sec.  Typical Value = 0. Default: 0.0
	:kd: Derivative gain (Kd).  Typical Value = 0. Default: 0.0
	:ta: Controller time constant (Ta) (&gt;0).  Typical Value = 0. Default: 0.0
	:tb: Gate servo time constant (Tb) (&gt;0).  Typical Value = 0. Default: 0.0
	:velmax: Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0. Default: 0.0
	:velmin: Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0. Default: 0.0
	:gmax: Maximum gate opening (Gmax).  Typical Value = 0. Default: 0.0
	:gmin: Minimum gate opening (Gmin).  Typical Value = 0. Default: 0.0
	:tw: Water inertia time constant (Tw) (&gt;0).  Typical Value = 0. Default: 0.0
	:d: Turbine damping factor (D).  Unit = delta P / delta speed.  Typical Value = 0. Default: 0.0
	:g0: Gate opening at speed no load (G0).  Typical Value = 0. Default: 0.0
	:g1: Intermediate gate opening (G1).  Typical Value = 0. Default: 0.0
	:p1: Power at gate opening G1 (P1).  Typical Value = 0. Default: 0.0
	:g2: Intermediate gate opening (G2).  Typical Value = 0. Default: 0.0
	:p2: Power at gate opening G2 (P2).  Typical Value = 0. Default: 0.0
	:p3: Power at full opened gate (P3).  Typical Value = 0. Default: 0.0
	:atw: Factor multiplying Tw (Atw).  Typical Value = 0. Default: 0.0
	:feedbackSignal: Feedback signal type flag (Flag). true = use gate position feedback signal false = use Pe. Default: False
		'''

	

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, treg = 0.0, rperm = 0.0, kp = 0.0, ki = 0.0, kd = 0.0, ta = 0.0, tb = 0.0, velmax = 0.0, velmin = 0.0, gmax = 0.0, gmin = 0.0, tw = 0.0, d = 0.0, g0 = 0.0, g1 = 0.0, p1 = 0.0, g2 = 0.0, p2 = 0.0, p3 = 0.0, atw = 0.0, feedbackSignal = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.treg = treg
		self.rperm = rperm
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.ta = ta
		self.tb = tb
		self.velmax = velmax
		self.velmin = velmin
		self.gmax = gmax
		self.gmin = gmin
		self.tw = tw
		self.d = d
		self.g0 = g0
		self.g1 = g1
		self.p1 = p1
		self.g2 = g2
		self.p2 = p2
		self.p3 = p3
		self.atw = atw
		self.feedbackSignal = feedbackSignal
		
	def __str__(self):
		str = 'class=GovHydroPID2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
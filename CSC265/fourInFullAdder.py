def add4(a0,a1,b0,b1):
	TT = {
	(0,0,0,0):(0,0,0),
	(0,0,0,1):(0,0,1),
	(0,0,1,0):(0,0,1),
	(0,0,1,1):(0,1,0),
	(0,1,0,0):(0,0,1),
	(0,1,0,1):(0,1,0),
	(0,1,1,0):(0,1,0),
	(0,1,1,1):(0,1,1),
	(1,0,0,0):(0,0,1),
	(1,0,0,1):(0,1,0),
	(1,0,1,0):(0,1,0),
	(1,0,1,1):(0,1,1),
	(1,1,0,0):(0,1,0),
	(1,1,0,1):(0,1,1),
	(1,1,1,0):(0,1,1),
	(1,1,1,1):(1,0,0)
	}
	return TT[(A1,A0,B1,B0)]

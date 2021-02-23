from google import choose_team

from unittest import TestCase

def test_team():
	team=[{"t2":0},{"t3":0}, {"t4":1}]
	

	assert(choose_team(team)=="t4")
	assert(choose_team(team)==None)
	
	

test_team()
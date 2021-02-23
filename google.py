import argparse
from random import randint


parser=argparse.ArgumentParser()
parser.add_argument("file_name", help="name of file to open")
args=parser.parse_args()

""" Takes in an input dataset and return a list 
	[pizzas_count,T2,T3,T4] of integers
	pizzas_count: the number of pizzas available at the pizzarier
	T2: number of team of two members
	T3: number of team of three members
	T4: number of team of four members
"""
def get_pizzas_and_teams_count(file):

	with open(file,"r") as f:
		data=f.readline()	# read only one line thats needed
		datas=[int(i) for i in data.strip().split(" ")]
	
		assert(len(datas)==4)

		return datas



def deliver_pizzas(file):
	pizzas_and_teams=get_pizzas_and_teams_count(file)

	teams=[{"t2":pizzas_and_teams[1]},{"t3":pizzas_and_teams[2]},{"t4":pizzas_and_teams[3]}]
	

	ingredients=[]
	count=0
	print(f"Before Delivery {teams}")
	with open(file,"r") as f:
		while count <= pizzas_and_teams[0]+1:
			data=f.readline()	# read one line from the imput dataset
			count +=1
			if count==1:
				# discard the first line as it is not needed
				continue


			ingredients.append({f"{count-2}":data.strip().split(" ")[1:]})

			if len(ingredients)==50 or len(ingredients)==pizzas_and_teams[0]:
				ingredients.sort(key=ingredients_count)
				while(True):
					s_team=choose_team(teams)
					if choose_team==None or team_as_num(s_team) > len(ingredients):
						break

					deliver(s_team,ingredients)
				# ingredients.sort(key=ingredients_count)
				# for i in ingredients:
				# 	print(i)
				
				print(f"After Delivery {teams}")
				break


"""since the ingredient is a list of dictionary, there is
	need to find a means to sort the pizza according to the 
	number of ingredients, hence the ingredients_count
"""
def ingredients_count(pizza):
	key=list(pizza.keys())[0]
	return len(pizza[key])



def choose_team(teams):
	""" Returns a string t2, t3 or t4 representing the randomly
		selected team and return None if the there's no team
	"""
	# removes any empty team type
	teams=list(filter(lambda x: x[list(x.keys())[0]] > 0,teams))
		
	if len(teams)==0:
		# all teams has been served
		return None
	
	assert(len(teams)>0)
	num=randint(0,len(teams)-1) 
	ch_team=list(teams[num].keys())[0] # choose a random team

	teams[num][ch_team] -=1 # reduce the number of selected team by 1

	return ch_team

def team_as_num(team):
	
	"""returns the team as a number e.g team of two "t2" as 2 etc."""
	if "2" in team:
		return 2
	elif "3" in team:
		return 3
	else:
		return 4

def deliver(team,pizzas_available):
	# team is a string containing "t2", "t3" or "t4"
	# pizzas_available is a list of dictionary with the key representing
	# the pizza index and the value being the list of ingredients in 
	# in the pizza
	p=pizzas_available

	if(team=="t2"):
		# delivering to a team of 2
		print(2,list(p.pop().keys())[0],list(p.pop().keys())[0])
	elif(team=="t3"):
		print(3,list(p.pop().keys())[0],list(p.pop().keys())[0],list(p.pop().keys())[0])
	else:
		print(4,list(p.pop().keys())[0],list(p.pop().keys())[0],list(p.pop().keys())[0],list(p.pop().keys())[0])




if __name__ == "__main__":
	#print(help(args))
	deliver_pizzas(args.file_name)
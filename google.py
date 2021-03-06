import os
import argparse
from random import randint
import datetime as d
from pathlib import Path




parser=argparse.ArgumentParser()
parser.add_argument("file_name", help="name of file to open")
parser.add_argument("--output_name","-o", help="name of output file")
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



def deliver_pizzas(file,output_file):
	pizzas_and_teams=get_pizzas_and_teams_count(file)

	teams=[{"t2":pizzas_and_teams[1]},{"t3":pizzas_and_teams[2]},{"t4":pizzas_and_teams[3]}]
	
	delivery_count=0;


	delivery_file=""

	ingredients=[]
	count=0
	

	if output_file is not None and Path.is_dir(output_file) == False:
		delivery_file=output_file
	else:
		delivery_file=f'output{d.datetime.now().__format__("%d%H%M%S")}.bin'
	submit_file=open(delivery_file,"a")

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
					if s_team==None or team_as_num(s_team) > len(ingredients):
						ingredients.clear()
						break

					
					submit_file.write(deliver(s_team,ingredients))
					delivery_count+=1
				
				
		print(f"{delivery_count} teams in total received pizzas")
		print(f"{pizzas_and_teams}")
		print(f"teams info after delivery {teams}")

	submit_file.close()

	#now to modify the outputfile to meeet specification

	#with open(delivery_file,"r"):


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
	# removes any type of team whose number is zero
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
		return (f"{2} {list(p.pop().keys())[0]} {list(p.pop().keys())[0]}\n")
	elif(team=="t3"):
		return (f"{3} {list(p.pop().keys())[0]} {list(p.pop().keys())[0]} {list(p.pop().keys())[0]}\n")
	else:
		return (f"{4} {list(p.pop().keys())[0]} {list(p.pop().keys())[0]} {list(p.pop().keys())[0]} {list(p.pop().keys())[0]}\n")



	# if(team=="t2"):
	# 	# delivering to a team of 2
	# 	print(2,list(p.pop().keys())[0],list(p.pop().keys())[0])
	# elif(team=="t3"):
	# 	print(3,list(p.pop().keys())[0],list(p.pop().keys())[0],list(p.pop().keys())[0])
	# else:
	# 	print(4,list(p.pop().keys())[0],list(p.pop().keys())[0],list(p.pop().keys())[0],list(p.pop().keys())[0])




if __name__ == "__main__":
	#print(help(args))
	if args.output_name is None:
		deliver_pizzas(args.file_name,None)
	else:
		deliver_pizzas(args.file_name,args.output_name)
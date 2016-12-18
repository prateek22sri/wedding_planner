# The person who has the maximum number of friends has less choices to get seated on tables. Hence the people who have more friends are seated first
#Graph of friends and non friends are created. The first table is filled first. The person who has maximum number of friends is placed on the first table.
#The second person to be seated on the table is selected from the sorted non friend list of the first person. The person who has max number of friends in this sorted list,is
#selected. The next person to be seated is selected from the intersection of the non friends of the already seated people. The person who has the maximum
#number of friends is given priority. The visited and non visited list is updated when people are placed on the table.
# When a person is to be placed on a table, the previous tables are traversed to check if there is any place available. If there is place available on the table and
#no people know each other, they are placed together. Finally we check if there is any person who is yet to be seated. The person is then seated on the new table.

import sys
file_text = open(sys.argv[1],'r')
num_of_seats=int(sys.argv[2])
table={} #dict of tables
visited=[]# List of the people who have laready been seated
non_visited=[]#List of the people who have not been seated
friend = {}#To store the number of friends(count) of each person
graph={}#dictionary to store the graph of friends

#creates a dictionary of friends- The people who know each other
#example- {davis:'Emma','Sal','Joe',etc}
for line in file_text.readlines():
    line=line.split()
    if line[0] not in graph.keys():
        graph[line[0]] = line[1:]
    else:
        graph[line[0]] += line[1:]
    for col in graph[line[0]]:
        if col in graph.keys():
            graph[col].append(line[0])
        else:
            graph[col]=[line[0]]

#Removes the duplicate friends from the friend graph
for k in graph.keys():
    graph[k] = list(set(graph[k]))
    #print k,graph[k]

#Creates the dict of non friends-People who do not know each other
non_graph={}
for k in graph.keys():
    non_graph[k]=list(set(graph.keys())-set(graph[k])-set([k]))
    #print k,non_graph[k]

#Sorts the friends dict in descending order of number of friends
#example-{davis:7,Jinne:4....etc}
def sort_known_friend_list(friend):
    return sorted(friend, key=lambda i: friend[i], reverse=True)

#Returns the common friends in the non friend list of 2 people
def find_intersection(a,b):
    return list((set(non_graph[a]).intersection(set(non_graph[b]))))


#Counts the number of friends each person has and stores it in a dict
def count_of_friends(graph):
    for k in graph.keys():
        friend[k]=len(graph[k])

count_of_friends(graph)
friend_known_list =sort_known_friend_list(friend)
non_visited = list(set(graph.keys())-set(visited))

#Places the person on the table such that no two people who know each other are seated together
#Iterates through the list of sorted friends where the person who knows the maximum number of other people is placed on the table first
for person in friend_known_list:
	#To place a person on the first table
	#Place the first person on the first table, check if the people in non friend list of the first person has been visited or not. sort the non friend, non visited list in descending order.
	#Place the person who has maximum number of friends.
	#To place the next person on the table- check the non friend list of the both the seated people. If there is a common non friend, place him on the table
	if person not in visited:
		if len(table) == 0 :
			table[0] = [person]
			visited.append(person)
			non_visited = list(set(graph.keys())-set(visited))
			#print "table0 add:",table
			if any([i in non_visited for i in non_graph[person]]):
				for i in sorted(non_graph[person],key=lambda i: friend[i],reverse = True):
					if i not in visited:
						table[0].append(i)
						visited.append(i)
						non_visited = list(set(graph.keys())-set(visited))
						mutual_non_friends = find_intersection(person,i)
						best_mutual_non_friend = ""
						for i in sorted(mutual_non_friends, key=lambda i: friend[i],reverse = True):
							if i not in visited and not any([i in graph[p] for p in table[0]]):
								best_mutual_non_friend = i
								break
						if best_mutual_non_friend!="":
							table[0].append(best_mutual_non_friend)
							visited.append(best_mutual_non_friend)
							non_visited = list(set(graph.keys())-set(visited))
						break

		else:
			#To place the people on second table
			#iterate through a list of all the tables to check if there is empty space for a new person
			#If there is empty space check if all the people are unknown to each other. If both the conditions are true only then place the person on the table
			for t in table:
				if len(table[t]) == num_of_seats:
					continue
				else:
					in_table = 0
					for table_people in table[t]:
						if person in graph[table_people]:
							in_table = 1
							break
					if in_table == 1:
						continue
					else:
						table[t].append(person)
						visited.append(person)
						non_visited = list(set(graph.keys())-set(visited))
						if len(table[t]) == num_of_seats:
							break
						else:
							mutual_non_friends = find_intersection(table[t][0],person)
							best_mutual_non_friend = ""
							for i in sorted(mutual_non_friends,key=lambda i: friend[i],reverse=True):
								if i not in visited and not any([i in graph[p] for p in table[t]]):
									best_mutual_non_friend = i
									break
							if best_mutual_non_friend != "" :
								table[t].append(best_mutual_non_friend)
								visited.append(best_mutual_non_friend)
								non_visited = list(set(graph.keys())-set(visited))
							break
# Checks if a person is not yet seated.
			if person not in visited:
				table[len(table)+1] = [person]
				visited.append(person)
				non_visited = list(set(graph.keys())-set(visited))
				if any([i in non_visited for i in non_graph[person]]):
					for i in sorted(non_graph[person],key=lambda i: friend[i],reverse = True):
						if i not in visited:
							table[len(table)].append(i)
							visited.append(i)
							non_visited = list(set(graph.keys())-set(visited))
							mutual_non_friends = find_intersection(table[len(table)][0],table[len(table)][1])
							best_mutual_non_friend = ""
							for i in sorted(mutual_non_friends,key=lambda i: friend[i],reverse=True):
								if i not in visited and not any([i in graph[p] for p in table[len(table)]]):
									best_mutual_non_friend = i
									break
							if best_mutual_non_friend != "" :
								table[len(table)].append(best_mutual_non_friend)
								visited.append(best_mutual_non_friend)
								non_visited = list(set(graph.keys())-set(visited))
							break

#displays the solution to the user

solution=[]
for k in table.keys():
	#print k,table[k]
	solution.append(','.join(table[k]))
print len(table)," ".join(solution)

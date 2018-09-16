# Wedding-table-planner

Kam and Lars are planning their upcoming wedding. They’d like to make their banquet as awkward as
possible by ensuring that at each dinner table, no one knows anyone else at the table. Write a program
that computes an assignment of people to tables using as few tables as possible. Your program should
run on the command line:

python wedding.py [friends-file] [seats-per-table]

where friends-file is a text file containing a friendship graph with one line per person, where each
line first lists that person’s name and then the list of people that they know (and we assume that
friendships are bidirectional, i.e. if A is friends with B then B is automatically friends with A), and
seats-per-table is an integer saying the maximum number of people that can be seated at a table.

The program can output whatever you’d like, except that the last line of output should be a machinereadable
representation of the solution you found, in this format:
[table-count] [table1-person1],[table1-person2],... [table2-person1],[table2-person2],...

For example,
python wedding.py myfriends.txt 3 

with input file:

davis steven sal joe jinnie zeming emma jayceon
jayceon jinnie zeming
jinne zeming
emma steven jinnie
steven sal joe

might give the result:

4 davis emma,jayceon jinnie,joe,sal steven,zeming

# Approach

+ The person who has the maximum number of friends has less choices to get seated on tables. Hence the people who have more friends are seated first.
+ Graph of friends and non friends are created. The first table is filled first. The person who has maximum number of friends is placed on the first table.
+ The second person to be seated on the table is selected from the sorted non friend list of the first person. The person who has max number of friends in this sorted list,is selected. The next person to be seated is selected from the intersection of the non friends of the already seated people. The person who has the maximum number of friends is given priority. The visited and non visited list is updated when people are placed on the table.
+ When a person is to be placed on a table, the previous tables are traversed to check if there is any place available. If there is place available on the table and no people know each other, they are placed together. Finally we check if there is any person who is yet to be seated. The person is then seated on the new table.

D = {'food':'spam', 'quantity':4, 'color':'pink'}
D['food']                                   # fetch value of key food
D['quantity'] +=1                           # add 1 to 'quantity' value


D = {}
D['name'] = 'bob'                           # create key by assignment
D['job'] = 'dev'

print(D['name'])

bob1 = dict(name= 'bob', job= 'dev')        # Keywords

rec = {'name':{'first': 'bob', 'last': 'Smith'},
        'jobs':['dev','mgr'],
        'age': 40.5}

rec['name']
{'last':'Smith', 'first':'Bob'}        #'name' is a nested list
rec['name']['last']                             # index the nested dictonary

rec['jobs']                                     #'jobs' is a nested list
['dev','mgr']                                   

rec['jobs'][-1]                                 # index the nested list

rec['jobs'].append('Janitor')                   # expand Bobs job description list
 

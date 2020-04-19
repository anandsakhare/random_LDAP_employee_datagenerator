import os
from treelib import Node, Tree
import numpy
import pandas as pd
import datetime,random

data={}
for subdir, dirs, files in os.walk("./ldifgen/ldifgen/data"):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        print("reading %s" % file)
        data[file.replace(".txt","").replace("-","_")]=open(filepath,"r").read().split('\n')

def random_dob():
    return datetime.datetime(datetime.datetime.now().year-random.randrange(18, 100, 1),random.randrange(1, 12, 1),random.randrange(1, 28, 1)).date()


def random_name():
    if random.choice([True, False]):
        return data['surnames'][random.randrange(0, 4421, 1)] +", "+ data['givennames_f'][random.randrange(0, 4953, 1)]
    else:
        return data['surnames'][random.randrange(0, 4421, 1)] +", "+  data['givennames_m'][random.randrange(0, 3901, 1)]


def random_department():
    return data['structnames'][random.randrange(0, 109, 1)]        



n=200
tree = Tree()
df = pd.DataFrame(columns=['Employee_id','Manager_id','name', 'dob','dept'])

for emp_id in range(n):
    if emp_id >1:
        #print(emp_id,random.randrange(0, emp_id-1, 1))
        Manager_id=random.randrange(0, emp_id-1, 1)
        tree.create_node(emp_id,emp_id, parent=Manager_id)
        df = df.append({'Employee_id': int(emp_id), 
                        'Manager_id':int(Manager_id),
                        'name':random_name(),
                        'dob':random_dob(),
                        'dept':random_department()
                       }, ignore_index=True)
    elif emp_id==1:
        #print(emp_id,0)
        tree.create_node(emp_id,emp_id, parent=0)
        df = df.append({'Employee_id': int(emp_id), 
                        'Manager_id':int(0),
                        'name':random_name(),
                        'dob':random_dob(),
                        'dept':random_department()
                       }, ignore_index=True)
    else:
        tree.create_node(emp_id,emp_id)
        df = df.append({'Employee_id': int(emp_id), 
                        'Manager_id':None,
                        'name':random_name(),
                        'dob':random_dob(),
                        'dept':None
                       }, ignore_index=True)

print("Depth of the tree is : %s " % tree.depth())
print(tree.show(line_type="ascii-em"))
df.head(20)
df.to_csv("sample_ldap_data.csv")
tree.save2file('tree.txt')
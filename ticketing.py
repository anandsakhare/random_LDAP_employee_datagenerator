import csv, json
import pandas as pd
import datetime,random
f = open("leaves.txt")
leaves = f.read().replace(" ","").split(",")

def random_date(n=500):
    return (datetime.datetime.now() - datetime.timedelta(days=random.randrange(0, n, 1))).date()

def random_status():
    return random.choice(["In Progress","Assigned", "In Review", "Closed", "Reassigned", "Pending"])

def random_category():
    return random.choice(["Security", "Payment", "Order", "Retail", "Internal", "Human Resources", "IT", "Finance", "Training", "CTO", "Web", "Billing","CRM", "CS", "BI"])

def random_FiledAgainst():
    return random.choice(["Software","Access/Login","Systems","Hardware"])

n=50
df = pd.DataFrame(columns=['ticket_num','assigned_to_emp_id','category', 'status',
                           'creation_date','requestor','FiledAgainst','TicketType',
                          'Severity','Priority'])
for ticket_num in range(n):
     df = df.append({'ticket_num': "TICKET-"+str(ticket_num), 
                        'assigned_to_emp_id':leaves[random.randrange(0, 122, 1)],
                        'category':random_category(),
                        'status':random_status(),
                        'creation_date':random_date(),
                         'requestor':leaves[random.randrange(0, 122, 1)],
                     'FiledAgainst':random_FiledAgainst(),
                     'TicketType':random.choice(["Issue","Request"]),
                     'Severity':random.choice(["0 - Unclassified","1 - Minor","2 - Normal","3 - Major","4 - Critical"]),
                     'Priority':random.choice(["0 - Unassigned","1 - Low","2 - Medium","3 - High"])
                       }, ignore_index=True)

df.to_csv("ticketing.csv")
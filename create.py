import classes
import simulation_functions
import create


def create_people(csv_file):
    import csv
    people_list =[]
    fieldnames = ["Trait", "Trait_Value", "Name"]
    new_file = open(csv_file)
    k = csv.DictReader(new_file, fieldnames = fieldnames, delimiter =";")
    for row in k:
        people_list.append(classes.Person(row["Trait"], row["Trait_Value"], row["Name"]))
    return people_list

def create_events(csv_file):
    import csv
    event_list=[]
    fieldnames = ["name", "desc", "trait_list", "det_cond", "det_amount", "prob_cond", "act", "time"]
    new_file = open(csv_file)
    k = csv.DictReader(new_file, fieldnames = fieldnames, delimiter =",", skipinitialspace = True )
    for row in k:
        event_list.append(classes.Event(row["name"], row["desc"], row["trait_list"],row["det_cond"], row["det_amount"], row["prob_cond"], row["act"], row["time"]))
    return event_list

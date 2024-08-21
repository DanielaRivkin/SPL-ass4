import sys
from persistence import repo
import persistence

# globals
total_inventory = 0
total_demand = 0
total_received = 0
total_sent = 0
output = []


def inventories():
    global total_inventory
    global total_demand
    total_inventory = repo.Vaccines.total_inventory()
    total_demand = repo.Clinics.total_demand()


# globals add functions
def add_inventory(amount):
    global total_inventory
    total_inventory = total_inventory + amount


def add_demand(amount):
    global total_demand
    total_demand = total_demand + amount


def add_received(amount):
    global total_received
    total_received = total_received + amount


def add_sent(amount):
    global total_sent
    total_sent = total_sent + amount


def add_output():
    output.append(
        str(total_inventory) + "," + str(total_demand) + "," + str(total_received) + "," + str(total_sent) + "\n")


def receive_shipment(args):
    logistic_id = repo.Suppliers.get_by_name(args[0])
    repo.Vaccines.insert(persistence.Vaccine(-1, args[2], logistic_id, args[1]))
    repo.Logistics.add_count_received(logistic_id, int(args[1]))
    add_received(int(args[1]))
    add_inventory(int(args[1]))
    add_output()


def send_shipment(args):
    clinic = repo.Clinics.get(args[0])
    demand = int(clinic[2])
    repo.Clinics.set_demand(args[0], demand - int(args[1]))
    vaccines = repo.Vaccines.vaccines()
    required_quantity = int(args[1])
    i = 0
    while required_quantity > 0 and i < len(vaccines):
        vaccine = vaccines[i]
        if required_quantity > vaccine[3]:
            required_quantity = required_quantity - vaccine[3]
            repo.Logistics.add_count_sent(clinic[3], vaccine[3])
            repo.Vaccines.delete(int(vaccine[0]))
        else:
            repo.Logistics.add_count_sent(clinic[3], required_quantity)
            repo.Vaccines.set_quantity(vaccine[0], vaccine[3] - required_quantity)
            required_quantity = 0
        i = i + 1
    add_inventory(-int(args[1]))
    add_demand(-int(args[1]))
    add_sent(int(args[1]))
    add_output()


def start_orders():
    inventories()
    input_file_name = sys.argv[2]
    with open(input_file_name) as input_file:
        for line in input_file:
            args = line.replace('\n', '').split(',')
            if len(args) == 3:
                receive_shipment(args)
            else:
                send_shipment(args)
    write_to_file()


# write output to output.txt
def write_to_file():
    file = open(str(sys.argv[3]), "w")
    for line in output:
        file.write(line)
    file.close()

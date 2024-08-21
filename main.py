import orders
import sys
from persistence import repo
import persistence


def parse_config(args):
    input_file_name = args[1]
    with open(input_file_name) as input_file:
        counters = input_file.readline().replace('\n', '').split(',')
        count = int(counters[0])
        while count > 0:
            line = input_file.readline().replace('\n', '').split(',')
            repo.Vaccines.insert(persistence.Vaccine(line[0], line[1], line[2], line[3]))
            count = count - 1
        count = int(counters[1])
        while count > 0:
            line = input_file.readline().replace('\n', '').split(',')
            repo.Suppliers.insert(persistence.Supplier(line[0], line[1], line[2]))
            count = count - 1
        count = int(counters[2])
        while count > 0:
            line = input_file.readline().replace('\n', '').split(',')
            repo.Clinics.insert(persistence.Clinic(line[0], line[1], line[2], line[3]))
            count = count - 1
        count = int(counters[3])
        while count > 0:
            line = input_file.readline().replace('\n', '').split(',')
            repo.Logistics.insert(persistence.Logistic(line[0], line[1], line[2], line[3]))
            count = count - 1


if __name__ == '__main__':
    parse_config(sys.argv)
    orders.start_orders()

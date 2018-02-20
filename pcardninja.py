from connection import Connection
from file_handler import *

def main():
    conn = Connection()
    contacts = parse_people("peopletable.csv")
    conn.add_contacts(contacts)

if __name__ ==  '__main__':
    main()
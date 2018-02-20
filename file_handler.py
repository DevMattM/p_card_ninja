import xlrd
import csv

class Person():
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

def parse_file(filepath):
    print(filepath)
    #This function reads in a file and puts it in good datastructures
    data_list = xlrd.open_workbook(filepath) #.sheet_by_index(0)
    return "YAY" 
    #return sheet.cell(0,0).value

def parse_people(filepath):
    #this function will update the people table with new information
    contacts = []
    with open(filepath, 'r') as csvfile:
        #has_header = csv.Sniffer.has_header(csvfile.read())
        peoplecsv = csv.DictReader(csvfile)
        #if has_header: next(peoplecsv)
        for row in peoplecsv:
            #create person
            contacts.append((row["first_name"],row["last_name"],row["email_address"]))

    return contacts


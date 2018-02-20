import sqlite3

class Connection():
    def __init__(self):
        #this function loads the db and handles interacting with it. creates it if needed
        try:
            self.conn = sqlite3.connect("pcardninaja.db")
        except Error as e:
            print(e)
        
        verify_tables(self.conn)

    def add_contacts(self, contact_records):
        """
        This function requires a record set with at least first name, last name, and email address.
        first_name
        last_name
        email_address
        """
        cursor = self.conn.cursor()
        cursor.executemany('''INSERT INTO contacts 
            (first_name, last_name, email) values (?,?,?)''', contact_records)
        self.conn.commit()

    def add_pcard_charge(self, line):
        pass

def verify_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
        contact_id integer PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL,
        email text NOT NULL UNIQUE);''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS charges (
        contact_id integer NOT NULL,
        card_issuer text NOT NULL,
        card_number text NOT NULL,
        trans_date integer NOT NULL,
        merchant text NOT NULL,
        status text NOT NULL,
        trans_amount integer NOT NULL,
        currency text,
        comments text,
        distribution text,
        category text,
        chartfield_status text,
        redistrib text,
        voucher_error text, 
        UNIQUE(contact_id, card_number,trans_date, merchant, status, trans_amount) ON CONFLICT IGNORE);''')
    conn.commit()

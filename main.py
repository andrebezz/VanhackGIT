import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler 
import sys
import json
import csv
from pprint import pprint


class MyHandler(PatternMatchingEventHandler):
    # Just Accept Json Files
    patterns = ["*.json"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            in
        """

        print(event.src_path)
        # the file will be processed there
        # print event.src_path  # print now only for degug

        with open(event.src_path) as data_file:
            data = json.loads(data_file.read())

        bank_data_total = data['Applications']['Application']['Accounts']['Account']

        ## Read Transactions and save every line in a file
        ## ----------------------------------------------
        bank_data_csv = open('out/transactions.csv', 'w')
        count_account = 0
        for account in bank_data_total:
            # print(account['Transactions'])
            bank_data = account['Transactions']['Transaction']

            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0:
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                  csvwriter.writerow(bank.values())
            count_account +=1      
        bank_data_csv.close()
        ## ----------------------------------------------

        ## Read Overviews and save every line in another file 
        ## ----------------------------------------------
        bank_data_total = data['Applications']['Application']['Accounts']['Account']

        bank_data_csv = open('out/overviews.csv', 'w')
        count_account = 0
        for account in bank_data_total:


            cabecalho = 0
            # SALARY
            bank_data = account['Overviews']['Overview']['Income']['Salary']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values())

            # BENEFITS
            bank_data = account['Overviews']['Overview']['Income']['Benefits']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values())

            # OTHER INCOME
            bank_data = account['Overviews']['Overview']['Income']['Other Income']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values())

            # LOANS - Small amount
            bank_data = account['Overviews']['Overview']['Loans']['Small Amount Loans - Loans']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values()) 

            # LOANS - Repayments
            bank_data = account['Overviews']['Overview']['Loans']['Small Amount Loans - Repayments']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values()) 

            # LOANS - Dishonours
            bank_data = account['Overviews']['Overview']['Loans']['Small Amount Loans - Dishonours']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values()) 

            # LOANS -  Other Dishonours
            bank_data = account['Overviews']['Overview']['Loans']['Other Dishonours']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values()) 

            # LOANS - Other LOANS
            bank_data = account['Overviews']['Overview']['Loans']['Other Loans']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values()) 

            # Outgoings - Rent
            bank_data = account['Overviews']['Overview']['Outgoings']['Rent']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values()) 

            # Outgoings - Other Outgoings
            bank_data = account['Overviews']['Overview']['Outgoings']['Other Outgoings']
            csvwriter = csv.writer(bank_data_csv)
            count_transaction = 0
            for bank in bank_data:
                  if count_account == 0 and count_transaction ==0 and not cabecalho  :
                         header = bank.keys()
                         csvwriter.writerow(header)
                         count_transaction += 1
                         cabecalho = 1
                  csvwriter.writerow(bank.values()) 


            count_account +=1      
        bank_data_csv.close()
        ## ----------------------------------------------


    def on_created(self, event):
        self.process(event)

    # def on_modified(self, event):
        # self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()        
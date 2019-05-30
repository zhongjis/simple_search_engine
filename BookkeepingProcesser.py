import json

# this class manipulates the bookkeeping file
class BookkeepingProcesser:

    def __init__(self):
        self.file_count = 0
        self.keys = []
        self.json_bookkeeping = {}

    # this method reading the bookkeeping file and load the file into a dict
    def read_bookkeeping(self):

        # setting up files and get ready to process 
        file_bookkeeping = open('WEBPAGES_RAW/bookkeeping.json')
        json_bookkeeping = json.load(file_bookkeeping)

        # processing
        for l in json_bookkeeping:
            self.file_count += 1
            self.keys.append(l.encode("utf-8"))
        self.json_bookkeeping = json_bookkeeping

        # wrapping up
        file_bookkeeping.close()
        print("Total files: " + str(self.file_count))
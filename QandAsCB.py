# QandAsCB.py
#


import csv

class QandAsCB:
    def __init__(self, filename):
        self.responses = {}
        self.default_response = "I'm sorry, I don't understand. Could you please rephrase your message?"
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.responses[row[0].lower()] = row[1]

    def respond(self, message):
        response = self.responses.get(message.lower(), self.default_response)
        return response

        # Slow down the typing
        # for char in response:
        #     time.sleep(random.uniform(0.1, 0.4))
        #     yield char


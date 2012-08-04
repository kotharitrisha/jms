import os
import re

class JMS:
    from_number = "12345"
    
    def __init__(self):
        print "initialized"
        
    
    def getHelp(self):
        return "Help description"

    def post(self, msg):
        message = msg[msg.find("#post") + len("#post") : ].strip()
        zipcode = re.search("\d{5}", message)
        print zipcode.group()
        print message

    def edit(self, msg):
        message = msg[msg.find("edit") + len("#edit") : ].strip()
        print message

    def getAllPosts(self):
        print from_number
    
    def delete(self, msg):
        job_id = msg[msg.find("#delete") + len("#delete") : ].strip()
        print job_id

    def view(self, msg):
        print msg

    def search(self, msg):
        search_params = msg[msg.find("#search") + len("#search") : ].strip()
        print search_params

    def apply(self, msg):
        job_id = msg[msg.find("#apply") + len("#apply") : ].strip()
        return job_id

    def getType(self, msg):
        if "#post" in msg:
            post(msg)
        elif "#help" in msg:
            getHelp()
        elif "#edit" in msg:
            edit(msg)
        elif "#myPosts" in msg:
            getAllPosts()
        elif "#delete" in msg:
            delete(msg)
        elif "#view" in msg:
            view(msg)
        elif "#search" in msg:
            search (msg)
        elif "#apply" in msg:
            apply(msg)
        else:
            getHelp()


#jms = JMS()
#jms.defineMsg("19104 #nurse")
#jms.getType(

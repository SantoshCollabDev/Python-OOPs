'''
Abstraction:
Concept of OOPs that ONLY SHOWS the necessary attributes and HIDES un-necessary information

Example:

To send the summary of an item at the end of the day it is sufficient have access to call the
send_email() method. But not necessarily to all the methods that send_email() methods executes
as part of send_email process.

sending email involves the 3 following steps/sub-processes:
1. Connect to the SMTP server ---- connect_server()
2. Build the body             ---- prepare_body()
3. Send the email             ---- send()

To send a mail one need not be aware of / need access to each of the above methods.

To implement abstraction --- MAKE THE ABOVE 3 METHODS PRIVATE using __

As they defined private they are not available to access using object instances
i.e like item1.connect() --- not available
'''
from item import Item

item1 = Item("MyItem", 750)

item1.send_email()





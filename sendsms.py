from twilio.rest import TwilioRestClient

# the following line needs your Twilio Account SID and Auth Token
client = TwilioRestClient("AC5539491d8b2a571c26b54fb52c4ce112", "bba3a9d921a9f90016d95b9646c077d5")

twil_num = "8609692228"

def sendmessage(to_, message):
    client.messages.create(from_=twil_num,to=to_, body=message)


if __name__ == "__main__":
    client.messages.create(to="8608163236", from_=twil_num, 
                               body="test")

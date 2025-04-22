import rpc1

# Fix the identities of channel, server, and client
channelID = 1
serverID  = 10

def main():
    s = rpc1.Server(channelID, serverID)
    s.run()

if _name_ == "_main_":
    main()

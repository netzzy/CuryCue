# Palette:signalingServer Ext

These Extensions reference a specific [Palette:signalingServer](<./Palette-signalingServer.md> "Palette:signalingServer"). The Extension class of a signalingServer COMP.   
  
# Client

The Client class describes a client object as part of the signaling session. 

## Members`id`→`str`: 

> The id member is generated as a UUID by the server when a new client is connecting.`address`→`str`: 

> The address member is set by the server when a new client is connecting. It is the IP address and the port used by the client to establish the WebSocket handshake in IP:port format and relative to the server.`properties`→`dict`: 

> The properties member can be used to hold an arbitrary dictionary and extend the Signaling API with custom data. By default`{'domain': '/'}`## Methods`Client.AsJSON()`→`dict`: 

> A utility method to convert a Client object to a dict / JSON friendly object.

# SignalingServerExt

The SignalingServerExt constructor drives the signalingServer COMP and exposes various promoted methods in addition to holding data during a signaling session. 

## Members`Clients`→`List[Clients]`: 

> The list of clients in the signaling session, as Client objects`CurrentClients`→`DAT`: 

> A reference to a DAT, copy of the Clients member

## Methods`SignalingServerExt.GetClientByAddress(address: str)`→`Client`: 

> A utility method that will return a client object provided an IP:port address. 
> 
>   * address (str): An IP:port address string.
>`SignalingServerExt.GetClientById(id: str)`→`Client`: 

> A utility method that will return a client object provided an ID. 
> 
>   * id (str): A UUID as a string.
>`SignalingServerExt.GetClientsAsJSON(self)`→`List[dict]`: 

> A utility method that will return a list of clients as JSON / dicts.`SignalingServerExt.Reset(self)`: 

> Reset the signaling session and all states of the signalingServer COMP and its SignalingServerExt.

TouchDesigner Build: Latest\n2022.24140before 2022.24140

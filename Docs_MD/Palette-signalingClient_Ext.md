# Palette:signalingClient Ext

These Extensions reference a specific [Palette:signalingClient](<./Palette-signalingClient.md> "Palette:signalingClient"). The extension of the signalingClient COMP.   
  
# Client

The Client class describes a client object as part of the signaling session. 

## Members`id`→`str`: 

> The id member is generated as a UUID by the server when a new client is connecting.`address`→`str`: 

> The address member is set by the server when a new client is connecting. It is the IP address and the port used by the client to establish the WebSocket handshake in IP:port format and relative to the server.`properties`→`dict`: 

> The properties member can be used to hold an arbitrary dictionary and extend the Signaling API with custom data. By default`{'domain': '/'}`## Methods`Client.AsJSON()`→`dict`: 

> A utility method to convert a Client object to a dict / JSON friendly object.

# SignalingClientExt

The SignalingClientExt constructor drives the signalingClient COMP and exposes various promoted methods in addition to holding data during a signaling session, including subscribers. 

Subscribers are other TouchDesigner components that might rely on the signalingClient COMP and Signaling API. 

You can add Subscribers by calling the method`Subscribe()`and passing a component as well as an array of strings where this array of strings represents message types to route to the subscriber whenever the signalingClient receives a message with a matching type from the signaling server. 

It has no effect if the parameter Forwardtosubscribers is not enabled. 

In a similar fashion to routing within the signalingClient COMP, a subscriber should implement a method prefixed with`onMessageReceived`and followed by the message type. 

i.e. We have a WebRTC COMP calling`Subscribe()`and passing itself, as well as a string array such as`['Offer', 'Answer']`. If the signalingClient COMP is receiving a message of type`Offer`it will call the method`onMessageReceivedOffer()`on the Subscriber (the WebRTC COMP in this specific case). 

## Members`AsClient`→`Client`: 

> Point to a Client instance that describes the signalingClient COMP as if it was a Client. The Client class describes a client object as part of the signaling exchange.`Clients`→`List[Client]`: 

> A list of Client objects that are currently in the same signaling session as the signalingClient. It includes all other clients in the same session and on the same domain other than itself.`CurrentClients`→`DAT`: 

> A reference to a DAT, copy of the Clients member.`Subscribers`→`List[dict]`: 

> A list of components in the current TouchDesigner project that subscribed to the signalingClient COMP using the Subscribe() method. 
> 
> Each of those list items are dictionaries such as: 
[code] 
>     {'origin': 'path/to/a/COMP',
>     'messageTypes': ['a','string','array','of','types']}
>     
[/code]

## Methods`GetClientByAddress(address: str)`→`Client or None`: 

> A utility method that will return a client object provided an IP:port address. 
> 
>   * address (str): An IP:port address string.
>`GetClientById(id: str)`→`Client or None`: 

> A utility method that will return a client object provided an ID 
> 
>   * id (str): A UUID as a string
>`GetClientsAsJSON(self)`→`List[dict]`: 

> A utility method that will return a list of clients as JSON / dicts.`Reset(self)`: 

> Reset the Signaling session (on the client's end) and all states of the signalingClient COMP and its SignalingClientExt. Attempts to reconnect to the signaling server if a signaling server IP was specified as a parameter and if the signaling server is online.`Send(dataAsJSONDict: dict)`: 

> This method converts a dictionary to a JSON string and sends it as text to the signaling server. 
> 
> This method can be used by Subscribers or other external components to send their own messages to the signaling server by leveraging the signalingClient COMP. 
> 
>   * dataAsJSONDict (dict): A dictionary, following the Signaling API format, with mandatory properties.
>`SendBinary(dataAsByteArray: bytearray)`: 

> This method can be used by Subscribers or other external components to send their own messages as byte array to the signaling server by leveraging the signalingClient COMP.`Subscribe(externalComp: str, messageTypes: List[str])`→`bool`: 

> This method is used to add an external component as a Subscriber of this signalingClient COMP. 
> 
> When a component is registered as a Subscriber, any message type received by the signalingClient that are also in the message types list that the Subscriber registered for will be routed to the Subscriber. 
> 
> Args: 
> 
>   * externalComp (str): The path to a COMP that is registering as a Subscriber on this signaling client.
>   * messageTypes (List[str]): A list of message types that the Subscriber is registering for. When the signaling client is receiving a matching message type, it will route it to the Subscriber.
> 

> 
> Returns: 
> 
>   * bool: Whether the subscription request was a success or not. Will return False if the Subscriber was already registered.
> 


TouchDesigner Build: Latest\n2022.24140before 2022.24140

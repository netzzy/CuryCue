# MQTT

MQTT (**Message Queue Telemetry Transport**) is an IoT ([Internet-of-Things](<https://en.wikipedia.org/wiki/Internet_of_things>)) and M2M ([Machine to Machine](<https://en.wikipedia.org/wiki/Machine_to_machine>)) protocol, an ISO standard (ISO/IEC PRF 20922) publish-subscribe-based "lightweight" messaging protocol for use on top of the TCP/IP protocol.   
  
MQTT is implemented in TouchDesigner as the [MQTT Client DAT](<./MQTT_Client_DAT.md> "MQTT Client DAT"), and some other computer or software needs to be a MQTT "broker". 

It is designed for connections with remote locations where a "small code footprint" is required or the network bandwidth is limited. For example, it has been used in sensors communicating to a broker via satellite link, over occasional dial-up connections with healthcare providers, in Facebook Messaging, and in a range of home automation and small device scenarios. It is also ideal for mobile applications because of its small size, low power usage, minimized data packets, and efficient distribution of information to one or many receivers. 

The publish-subscribe messaging pattern requires a message broker. The broker is responsible for distributing messages to interested clients based on the topic of a message. Andy Stanford-Clark and Arlen Nipper of Cirrus Link authored the first version of the protocol in 1999. 

The model is as follows: A computer is the message broker, other computers are the message clients. Each client can publish messages and receive messages to a message broker: A client first creates a topic by sending the topic name to the broker, and then posts messages (publishes) with that topic to the broker. Other clients will register their interest in a topic (subscribe) to the broker server. If there is a match between a client's registered interest topic and another client's posted messages topics, the client receives all the messages of that topic. There is no history of messages kept, so all history is lost. [MQTT Client DAT](<./MQTT_Client_DAT.md> "MQTT Client DAT") is a client server and can post and receive messages, but it needs to be connected to a broker server. 

[MQTT](<http://mqtt.org>) is released under the ([Eclipse Public License 10.0](<http://www.eclipse.org/org/documents/epl-v10.php>)). The source code repository for MQTT is [here](<https://github.com/mqtt/mqtt.github.io/wiki/software?id=software>). 

See also: [MQTT Client DAT](<./MQTT_Client_DAT.md> "MQTT Client DAT"), [MQTT home page](<http://mqtt.org>), [MQTT in Wikipedia](<https://en.wikipedia.org/wiki/MQTT>), [TCP/IP DAT](<./TCP/IP_DAT.md> "TCP/IP DAT"), [PAHO-MQTT independent Python client library](<https://pypi.python.org/pypi/paho-mqtt/1.1>).

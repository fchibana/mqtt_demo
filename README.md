# mqtt_demo

## Dependencies


### Mosquitto Broker

```bash
sudo apt update -y && sudo apt install mosquitto mosquitto-clients -y
```

To check its status
```
sudo systemctl status mosquitto
```

### Eclipse Paho MQTT Python client library
```
python3 -m pip install paho-mqtt
```

## Test publisher, subscriber

How to publish and subscribe to topics using `mosquitto-clients`:

```
# publisher
mosquitto_pub -h address -t topic -m “message”

# subscriber
mosquitto_sub -h address -t topic
```

## References
- https://www.arubacloud.com/tutorial/how-to-install-and-secure-mosquitto-on-ubuntu-20-04.aspx
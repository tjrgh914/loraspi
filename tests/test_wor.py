from loraspi.LoRaWoR import LoRaWoR


if __name__ == '__main__':
    relay = LoRaWoR()
    try:
        relay.start()
        relay.join()
    except KeyboardInterrupt:
        relay.stop()
        relay.join()

from loraspi.LoRaRelay import LoRaRelay


if __name__ == '__main__':
    relay = LoRaRelay()
    try:
        relay.start()
        relay.join()
    except KeyboardInterrupt:
        relay.stop()
        relay.join()

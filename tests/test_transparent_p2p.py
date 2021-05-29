from loraspi.LoRaTransparent import LoRaTransparentP2P


if __name__ == '__main__':
    relay = LoRaTransparentP2P()
    try:
        relay.start()
        relay.join()
    except KeyboardInterrupt:
        relay.stop()
        relay.join()

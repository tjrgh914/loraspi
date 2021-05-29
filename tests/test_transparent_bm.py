from loraspi.LoRaTransparent import LoRaTransparentBM


if __name__ == '__main__':
    relay = LoRaTransparentBM()
    try:
        relay.start()
        relay.join()
    except KeyboardInterrupt:
        relay.stop()
        relay.join()

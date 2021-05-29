from loraspi.LoRaRelay import LoRaRelay


if __name__ == '__main__':
    relay = LoRaRelay()  # you need at least three lora hats for a working relay
    try:
        relay.start()
        relay.join()
    except KeyboardInterrupt:
        relay.stop()
        relay.join()

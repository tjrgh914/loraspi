from loraspi.LoRaRxTx import RxTx, GPIO, M0, M1, log


class LoRaWoR(RxTx):
    def on_reg_0(self):
        log.info("LoRa WOR activated")
        GPIO.output(M0, GPIO.HIGH)

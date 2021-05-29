from loraspi.LoRaRxTx import RxTx, GPIO, M0, M1, log


class LoRaWoR(RxTx):
    CFG_REG = b'\xC2\x00\x09\x00\x00\x00\x62\x00\x17\x0b\x00\x00'
    RET_REG = b'\xC1\x00\x09\x00\x00\x00\x62\x00\x17\x0b\x00\x00'

    def on_reg_0(self):
        log.info("LoRa WOR activated")
        GPIO.output(M0, GPIO.HIGH)
        GPIO.output(M1, GPIO.LOW)

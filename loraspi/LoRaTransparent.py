from loraspi import log, GPIO, M1
from loraspi.LoRaRxTx import RxTx


class LoRaTransparentBM(RxTx):  # Broadcast and monitor
    CFG_REG = b'\xC2\x00\x09\xFF\xFF\x00\x62\x00\x17\x03\x00\x00'
    RET_REG = b'\xC1\x00\x09\xFF\xFF\x00\x62\x00\x17\x03\x00\x00'

    def on_reg_0(self):
        log.info("Broadcast and monitor mode activated")
        GPIO.output(M1, GPIO.LOW)


class LoRaTransparentP2P(LoRaTransparentBM):  # P2P
    CFG_REG = b'\xC2\x00\x09\x00\x00\x00\x62\x00\x17\x03\x00\x00'
    RET_REG = b'\xC1\x00\x09\x00\x00\x00\x62\x00\x17\x03\x00\x00'

    def on_reg_0(self):
        log.info("P2P mode activated")
        GPIO.output(M1, GPIO.LOW)

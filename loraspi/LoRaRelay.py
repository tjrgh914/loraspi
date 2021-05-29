from loraspi import GPIO, M1, log
from loraspi.LoRaRxTx import RxTx


class LoRaRelay(RxTx):
    CFG_REG = [b'\xC2\x00\x09\x00\x00\x01\x62\x00\x17\x03\x00\x00']
    RET_REG = [b'\xC1\x00\x09\x00\x00\x01\x62\x00\x17\x03\x00\x00']

    def on_reg_0(self):
        log.info("Relay mode activated")

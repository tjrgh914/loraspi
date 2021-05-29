from loraspi import log
from loraspi.LoRaRxTx import RxTx


class LoRaTransparentBM(RxTx):  # Broadcast and monitor
    CFG_REG = [b'\xC2\x00\x09\xFF\xFF\x00\x62\x00\x17\x03\x00\x00', b'\xC2\x00\x09\x00\x00\x00\x62\x00\x17\x03\x00\x00']
    CFG_RET = [b'\xC1\x00\x09\xFF\xFF\x00\x62\x00\x17\x03\x00\x00', b'\xC1\x00\x09\x00\x00\x00\x62\x00\x17\x03\x00\x00']

    def on_reg_0(self):
        log.info("Broadcast and monitor mode activated")


class LoRaTransparentP2P(LoRaTransparentBM):  # P2P
    def on_reg_0(self):
        log.info("P2P mode activated")

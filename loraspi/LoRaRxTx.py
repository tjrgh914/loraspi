from loraspi import GPIO, M0, M1, Serial, sleep, log
from runnable import Runnable
from typing import Optional


def _setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(M0, GPIO.OUT)
    GPIO.setup(M1, GPIO.OUT)
    GPIO.output(M0, GPIO.LOW)
    GPIO.output(M1, GPIO.HIGH)


class RxTx(Runnable):
    CFG_REG = None
    RET_REG = None

    _serial: Serial = None
    _buffer: Optional[bytes] = ""
    _dev: str = None
    _baud_rate: int = None

    def __init__(self, dev: str = "/dev/ttyS0", baud_rate: int = 9600):
        Runnable.__init__(self)
        self._dev = dev
        self._baud_rate = baud_rate
        _setupGPIO()

    def on_start(self):
        log.debug("Using serial: {} | Baud: {}", self._dev, )
        self._serial = Serial(self._dev, 9600)
        self._serial.flushInput()
        self._serial.write(self.CFG_REG[0])

    def on_reg_0(self):
        log.warning("This method should be overridden")

    def on_msg(self):
        log.info("Received message: {}", self._buffer)

    def work(self):
        if self._serial.inWaiting() > 0:
            sleep(0.1)
            self._buffer = self._serial.read(self._serial.inWaiting())
            if self._buffer == self.RET_REG[0]:
                self.on_reg_0()
                GPIO.output(M1, GPIO.LOW)
                self._buffer = b""
            if self._buffer != b"":
                self.on_msg()
                self._buffer = b""

    def run(self) -> None:
        self.on_start()
        while self._serial.isOpen() and self.do_run:
            self.work()
        self.on_stop()

    def send_message(self, msg: bytes):
        self._serial.write(msg)

    def __del__(self):
        if self._serial.isOpen():
            self._serial.close()
        GPIO.cleanup()

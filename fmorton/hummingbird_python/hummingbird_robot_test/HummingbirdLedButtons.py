from BirdBrain import Hummingbird

class HummingbirdLedButtons:
    BRIGHTNESS_UP = 0
    BRIGHTNESS_DOWN = 100

    def __init__(self, device = None, brightness_up = None, brightness_down = None):
        self.device = device
        self.brightness_up = brightness_up
        self.brightness_down = brightness_down

        self.buttons = None

        if self.brightness_up is None: self.brightness_up = HummingbirdLedButtons.BRIGHTNESS_UP
        if self.brightness_down is None: self.brightness_down = HummingbirdLedButtons.BRIGHTNESS_DOWN

        if self.device is not None:
            try:
                self.buttons = Hummingbird(device)
            except ConnectionRefusedError:
                print("LED buttons device not available")
                raise

    def down(self, port):
        if self.buttons.getVoltage(port) > 0.0:
            self.indicate_down(port)
            return True
        else:
            self.indicate_up(port)
            return False

    def up(self, port):
        return(not self.down(port))

    def indicate_down(self, port):
        self.buttons.setLED(port, self.brightness_down)

    def indicate_up(self, port):
        self.buttons.setLED(port, self.brightness_up)
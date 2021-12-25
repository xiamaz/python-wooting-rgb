import wooting_rgb_wrapper
import contextlib



class WootingRGB:

    def __enter__(self):
        self.connected = wooting_rgb_wrapper.wooting_rgb_kbd_connected()

        return self

    def set_key(self, row, column, red, green, blue):
        rval = wooting_rgb_wrapper.wooting_rgb_direct_set_key(row, column, red, green, blue)
        if not rval:
            raise RuntimeError("Could not set key")

    def reset_key(self, row, column):
        rval = wooting_rgb_wrapper.wooting_rgb_direct_reset_key(row, column)
        if not rval:
            raise RuntimeError("Could not reset key")


    def __exit__(self, exc_type, exc_value, traceback):
        wooting_rgb_wrapper.wooting_rgb_reset()

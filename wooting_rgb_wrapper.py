import ctypes

wt = ctypes.cdll.LoadLibrary("libwooting-rgb-sdk.dylib")


WOOTING_ROW_COUNT = 6
WOOTING_COLUMN_COUNT = 21
WootingColorBufferType = ctypes.c_uint8 * (WOOTING_ROW_COUNT * WOOTING_COLUMN_COUNT * 3)
WootingDisconnectedCallbackFunc = ctypes.CFUNCTYPE(None)


def wooting_rgb_kbd_connected():
    return bool(wt.wooting_rgb_kbd_connected())


def wooting_rgb_set_disconnected_cb(callback):
    cb = WootingDisconnectedCallbackFunc(callback)
    wt.wooting_rgb_set_disconnected_cb(cb)


def wooting_rgb_reset():
    return bool(wt.wooting_rgb_reset())


def wooting_rgb_direct_set_key(row, column, red, green, blue):
    return bool(wt.wooting_rgb_direct_set_key(row, column, red, green, blue))


def wooting_rgb_direct_reset_key(row, column):
    return bool(wt.wooting_rgb_direct_reset_key(row, column))


def wooting_rgb_array_update_keyboard():
    return bool(wooting_rgb_array_update_keyboard)


def wooting_rgb_array_auto_update(auto_update):
    return bool(wt.wooting_rgb_array_auto_update(auto_update))


def wooting_rgb_array_set_single(row, column, red, green, blue):
    return bool(wt.wooting_rgb_array_set_single(row, column, red, green, blue))


def wooting_rgb_array_set_full(colors_buffer):
    cbuffer = WootingColorBufferType(*colors_buffer)
    return bool(wt.wooting_rgb_array_set_full(cbuffer))

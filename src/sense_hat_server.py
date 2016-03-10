from bottle import get, route, request, response, run, post
from bottle import get, route, request, response, run, post
import sense_hat

sh = sense_hat.SenseHat()

def handle_padded(handler):
    def decorator(**kwargs):
        r = handler(kwargs)
        try:
            callback = request.query.get('callback')
        except Exception as e:
            callback = None
        if callback is None:
            return r
        else:
            response.content_type = 'text/javascript'
            return "%s(%r);" % (callback, r)
    return decorator


@get('/__init__/<imu_settings_file>/<text_assets>')
@handle_padded
def __init__(kargs):
    r = {'return_value': sh.__init__(int(kargs['imu_settings_file']), int(kargs['text_assets']))}
    return r


@get('/_load_text_assets/<text_image_file>/<text_file>')
@handle_padded
def _load_text_assets(kargs):
    r = {'return_value': sh._load_text_assets(int(kargs['text_image_file']), int(kargs['text_file']))}
    return r


@get('/_trim_whitespace/<char>')
@handle_padded
def _trim_whitespace(kargs):
    r = {'return_value': sh._trim_whitespace(int(kargs['char']))}
    return r


@get('/_get_settings_file/<imu_settings_file>')
@handle_padded
def _get_settings_file(kargs):
    r = {'return_value': sh._get_settings_file(int(kargs['imu_settings_file']))}
    return r


@get('/_get_fb_device')
@handle_padded
def _get_fb_device(kargs):
    r = {'return_value': sh._get_fb_device()}
    return r


@get('/rotation')
@handle_padded
def rotation(kargs):
    r = {'return_value': sh.rotation()}
    return r


@get('/rotation/<r>')
@handle_padded
def rotation(kargs):
    r = {'return_value': sh.rotation(int(kargs['r']))}
    return r


@get('/set_rotation/<r>/<redraw>')
@handle_padded
def set_rotation(kargs):
    r = {'return_value': sh.set_rotation(int(kargs['r']), int(kargs['redraw']))}
    return r


@get('/_pack_bin/<pix>')
@handle_padded
def _pack_bin(kargs):
    r = {'return_value': sh._pack_bin(int(kargs['pix']))}
    return r


@get('/_unpack_bin/<packed>')
@handle_padded
def _unpack_bin(kargs):
    r = {'return_value': sh._unpack_bin(int(kargs['packed']))}
    return r


@get('/flip_h/<redraw>')
@handle_padded
def flip_h(kargs):
    r = {'return_value': sh.flip_h(int(kargs['redraw']))}
    return r


@get('/flip_v/<redraw>')
@handle_padded
def flip_v(kargs):
    r = {'return_value': sh.flip_v(int(kargs['redraw']))}
    return r


@get('/set_pixels/<pixel_list>')
@handle_padded
def set_pixels(kargs):
    r = {'return_value': sh.set_pixels(eval(kargs['pixel_list']))}
    return r


@get('/get_pixels')
@handle_padded
def get_pixels(kargs):
    r = {'return_value': sh.get_pixels()}
    return r


@get('/set_pixel/<x>/<y>')
@handle_padded
def set_pixel(kargs):
    r = {'return_value': sh.set_pixel(int(kargs['x']), int(kargs['y']))}
    return r


@get('/get_pixel/<x>/<y>')
@handle_padded
def get_pixel(kargs):
    r = {'return_value': sh.get_pixel(int(kargs['x']), int(kargs['y']))}
    return r


@get('/load_image/<file_path>/<redraw>')
@handle_padded
def load_image(kargs):
    r = {'return_value': sh.load_image(int(kargs['file_path']), int(kargs['redraw']))}
    return r


@get('/clear')
@handle_padded
def clear(kargs):
    r = {'return_value': sh.clear()}
    return r


@get('/_get_char_pixels/<s>')
@handle_padded
def _get_char_pixels(kargs):
    r = {'return_value': sh._get_char_pixels(int(kargs['s']))}
    return r


@get('/show_message/<text_string>/<scroll_speed>/<text_colour>/<back_colour>')
@handle_padded
def show_message(kargs):
    r = {'return_value': sh.show_message(kargs['text_string'], float(kargs['scroll_speed']), eval(kargs['text_colour']), eval(kargs['back_colour']))}
    return r


@get('/show_letter/<s>/<text_colour>/<back_colour>')
@handle_padded
def show_letter(kargs):
    r = {'return_value': sh.show_letter(int(kargs['s']), int(kargs['text_colour']), int(kargs['back_colour']))}
    return r


@get('/gamma')
@handle_padded
def gamma(kargs):
    r = {'return_value': sh.gamma()}
    return r


@get('/gamma/<buffer>')
@handle_padded
def gamma(kargs):
    r = {'return_value': sh.gamma(int(kargs['buffer']))}
    return r


@get('/gamma_reset')
@handle_padded
def gamma_reset(kargs):
    r = {'return_value': sh.gamma_reset()}
    return r


@get('/low_light')
@handle_padded
def low_light(kargs):
    r = {'return_value': sh.low_light()}
    return r


@get('/low_light/<value>')
@handle_padded
def low_light(kargs):
    r = {'return_value': sh.low_light(int(kargs['value']))}
    return r


@get('/_init_humidity')
@handle_padded
def _init_humidity(kargs):
    r = {'return_value': sh._init_humidity()}
    return r


@get('/_init_pressure')
@handle_padded
def _init_pressure(kargs):
    r = {'return_value': sh._init_pressure()}
    return r


@get('/get_humidity')
@handle_padded
def get_humidity(kargs):
    r = {'return_value': sh.get_humidity()}
    return r


@get('/humidity')
@handle_padded
def humidity(kargs):
    r = {'return_value': sh.humidity()}
    return r


@get('/get_temperature_from_humidity')
@handle_padded
def get_temperature_from_humidity(kargs):
    r = {'return_value': sh.get_temperature_from_humidity()}
    return r


@get('/get_temperature_from_pressure')
@handle_padded
def get_temperature_from_pressure(kargs):
    r = {'return_value': sh.get_temperature_from_pressure()}
    return r


@get('/get_temperature')
@handle_padded
def get_temperature(kargs):
    r = {'return_value': sh.get_temperature()}
    return r


@get('/temp')
@handle_padded
def temp(kargs):
    r = {'return_value': sh.temp()}
    return r


@get('/temperature')
@handle_padded
def temperature(kargs):
    r = {'return_value': sh.temperature()}
    return r


@get('/get_pressure')
@handle_padded
def get_pressure(kargs):
    r = {'return_value': sh.get_pressure()}
    return r


@get('/pressure')
@handle_padded
def pressure(kargs):
    r = {'return_value': sh.pressure()}
    return r


@get('/_init_imu')
@handle_padded
def _init_imu(kargs):
    r = {'return_value': sh._init_imu()}
    return r


@get('/set_imu_config/<compass_enabled>/<gyro_enabled>/<accel_enabled>')
@handle_padded
def set_imu_config(kargs):
    r = {'return_value': sh.set_imu_config(int(kargs['compass_enabled']), int(kargs['gyro_enabled']), int(kargs['accel_enabled']))}
    return r


@get('/_read_imu')
@handle_padded
def _read_imu(kargs):
    r = {'return_value': sh._read_imu()}
    return r


@get('/_get_raw_data/<is_valid_key>/<data_key>')
@handle_padded
def _get_raw_data(kargs):
    r = {'return_value': sh._get_raw_data(int(kargs['is_valid_key']), int(kargs['data_key']))}
    return r


@get('/get_orientation_radians')
@handle_padded
def get_orientation_radians(kargs):
    r = {'return_value': sh.get_orientation_radians()}
    return r


@get('/orientation_radians')
@handle_padded
def orientation_radians(kargs):
    r = {'return_value': sh.orientation_radians()}
    return r


@get('/get_orientation_degrees')
@handle_padded
def get_orientation_degrees(kargs):
    r = {'return_value': sh.get_orientation_degrees()}
    return r


@get('/get_orientation')
@handle_padded
def get_orientation(kargs):
    r = {'return_value': sh.get_orientation()}
    return r


@get('/orientation')
@handle_padded
def orientation(kargs):
    r = {'return_value': sh.orientation()}
    return r


@get('/get_compass')
@handle_padded
def get_compass(kargs):
    r = {'return_value': sh.get_compass()}
    return r


@get('/compass')
@handle_padded
def compass(kargs):
    r = {'return_value': sh.compass()}
    return r


@get('/get_compass_raw')
@handle_padded
def get_compass_raw(kargs):
    r = {'return_value': sh.get_compass_raw()}
    return r


@get('/compass_raw')
@handle_padded
def compass_raw(kargs):
    r = {'return_value': sh.compass_raw()}
    return r


@get('/get_gyroscope')
@handle_padded
def get_gyroscope(kargs):
    r = {'return_value': sh.get_gyroscope()}
    return r


@get('/gyro')
@handle_padded
def gyro(kargs):
    r = {'return_value': sh.gyro()}
    return r


@get('/gyroscope')
@handle_padded
def gyroscope(kargs):
    r = {'return_value': sh.gyroscope()}
    return r


@get('/get_gyroscope_raw')
@handle_padded
def get_gyroscope_raw(kargs):
    r = {'return_value': sh.get_gyroscope_raw()}
    return r


@get('/gyro_raw')
@handle_padded
def gyro_raw(kargs):
    r = {'return_value': sh.gyro_raw()}
    return r


@get('/gyroscope_raw')
@handle_padded
def gyroscope_raw(kargs):
    r = {'return_value': sh.gyroscope_raw()}
    return r


@get('/get_accelerometer')
@handle_padded
def get_accelerometer(kargs):
    r = {'return_value': sh.get_accelerometer()}
    return r


@get('/accel')
@handle_padded
def accel(kargs):
    r = {'return_value': sh.accel()}
    return r


@get('/accelerometer')
@handle_padded
def accelerometer(kargs):
    r = {'return_value': sh.accelerometer()}
    return r


@get('/get_accelerometer_raw')
@handle_padded
def get_accelerometer_raw(kargs):
    r = {'return_value': sh.get_accelerometer_raw()}
    return r


@get('/accel_raw')
@handle_padded
def accel_raw(kargs):
    r = {'return_value': sh.accel_raw()}
    return r


@get('/accelerometer_raw')
@handle_padded
def accelerometer_raw(kargs):
    r = {'return_value': sh.accelerometer_raw()}
    return r


run(host='0.0.0.0', port=8080, debug=True)

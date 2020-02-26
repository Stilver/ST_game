from os.path import join


def parse_settings(settings):
    settings = dict([setting.split(' = ') for setting in settings.split('\n') if setting])
    for setting, value in settings.items():
        if ',' in value:
            settings[setting] = tuple(int(part.strip()) for part in value.split(','))
        else:
            settings[setting] = int(value)
    return settings


def get_settings():
    with open(join('settings', 'settings')) as file:
        settings = file.read()
    return parse_settings(settings)


SETTINGS = get_settings()

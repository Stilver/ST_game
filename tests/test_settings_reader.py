from settings.settings_reader import parse_settings
from unittest import TestCase


class TestSettingsReader(TestCase):
    def test_parse_settings(self):
        settings = 'set1 = 1, 1\nset2 = 2'
        expected_result = {'set1': (1, 1), 'set2': 2}
        result = parse_settings(settings)
        self.assertEqual(result, expected_result)

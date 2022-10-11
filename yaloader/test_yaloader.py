import unittest
from main import YaLoader


class TestYaloader(unittest.TestCase):
    def setUp(self) -> None:
        self.yd = YaLoader()

    def tearDown(self) -> None:
        self.yd.delete_folder('test_dir')

    def test_create_folder1(self):
        self.assertEqual(self.yd.create_folder('test_dir'), 201)
        self.assertEqual(self.yd.get_status_folder('test_dir'), 200)

    def test_create_folder2(self):
        self.yd.create_folder('test_dir')
        self.assertEqual(self.yd.create_folder('test_dir'), 409)

    def test_create_folder3(self):
        self.assertEqual(self.yd.create_folder(''), 409)


if __name__ == '__main__':
    unittest.main()

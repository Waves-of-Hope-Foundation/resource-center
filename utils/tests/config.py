import unittest

import utils.config

class ConfigUtilsTestCase(unittest.TestCase):

    def test_list_of_tuples(self):
        with self.assertRaises(TypeError):
            utils.config.list_of_tuples()
        
        admins = [
            ('Admin', 'admin@example.com'),
            ('Manager', 'manager@example.com')
        ]
        self.assertListEqual(
            admins,
            utils.config.list_of_tuples(str(admins))
        )


if __name__ == '__main__':
    unittest.main()

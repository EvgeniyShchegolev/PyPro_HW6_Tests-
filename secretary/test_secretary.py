import unittest
from unittest.mock import patch
from copy import deepcopy

import app


default_documents = app.documents
default_directories = app.directories


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        app.documents = deepcopy(default_documents)
        app.directories = deepcopy(default_directories)

    # Test check_document_existence
    def test_check_document_existence1(self):
        self.assertTrue(app.check_document_existence('11-2'))

    def test_check_document_existence2(self):
        self.assertFalse(app.check_document_existence('1111'))

    # Test get_doc_owner_name
    @patch('builtins.input', return_value='11-2')
    def test_get_doc_owner_name1(self, mock_input):
        self.assertEqual(app.get_doc_owner_name(), 'Геннадий Покемонов')

    @patch('builtins.input', return_value='1111')
    def test_get_doc_owner_name2(self, mock_input):
        self.assertIsNone(app.get_doc_owner_name())

    @patch('builtins.input', return_value='')
    def test_get_doc_owner_name3(self, mock_input):
        self.assertIsNone(app.get_doc_owner_name())

    # Test get_all_doc_owners_names
    def test_get_all_doc_owners_names(self):
        self.assertEqual(app.get_all_doc_owners_names(),
                         {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'})

    # Test remove_doc_from_shelf
    def test_remove_doc_from_shelf1(self):
        self.assertTrue(app.remove_doc_from_shelf('11-2'))
        self.assertNotIn('11-2', app.directories['1'])

    def test_remove_doc_from_shelf2(self):
        self.assertIsNone(app.remove_doc_from_shelf('1111'))
        self.assertNotIn('1111', app.directories)

    # Test add_new_shelf
    @patch('builtins.input', return_value='10')
    def test_add_new_shelf1(self, mock_input):
        self.assertEqual(app.add_new_shelf(), ('10', True))
        self.assertIn('10', app.directories)

    @patch('builtins.input', return_value='1')
    def test_add_new_shelf2(self, mock_input):
        self.assertEqual(app.add_new_shelf(), ('1', False))

    # Test append_doc_to_shelf
    def test_append_doc_to_shelf1(self):
        self.assertIsNone(app.append_doc_to_shelf('100', '1'))
        self.assertIn('100', app.directories['1'])

    def test_append_doc_to_shelf2(self):
        self.assertIsNone(app.append_doc_to_shelf('100', '10'))
        self.assertIn('100', app.directories['10'])

    # Test delete_doc
    @patch('builtins.input', return_value='11-2')
    def test_delete_doc1(self, mock_input):
        self.assertEqual(app.delete_doc(), ('11-2', True))
        self.assertNotIn('11-2', [doc for doc in app.directories.values()])
        self.assertNotIn('11-2', [doc['number'] for doc in app.documents])

    @patch('builtins.input', return_value='100')
    def test_delete_doc2(self, mock_input):
        self.assertIsNone(app.delete_doc())

    # Test get_doc_shelf
    @patch('builtins.input', return_value='11-2')
    def test_get_doc_shelf1(self, mock_input):
        self.assertEqual(app.get_doc_shelf(), '1')

    @patch('builtins.input', return_value='100')
    def test_get_doc_shelf2(self, mock_input):
        self.assertIsNone(app.get_doc_shelf())

    # Test move_doc_to_shelf
    @patch('builtins.input', side_effect=['11-2', '2'])
    def test_move_doc_to_shelf1(self, mock_input):
        self.assertIsNone(app.move_doc_to_shelf())
        self.assertIn('11-2', app.directories['2'])
        self.assertNotIn('11-2', app.directories['1'])

    @patch('builtins.input', side_effect=['11-2', '10'])
    def test_move_doc_to_shelf2(self, mock_input):
        self.assertIsNone(app.move_doc_to_shelf())
        self.assertIn('11-2', app.directories['10'])
        self.assertNotIn('11-2', app.directories['1'])

    @patch('builtins.input', side_effect=['100', '2'])
    def test_move_doc_to_shelf3(self, mock_input):
        self.assertIsNone(app.move_doc_to_shelf())
        self.assertNotIn('100', app.directories['2'])

    # Test show_document_info
    def test_show_document_info(self):
        self.assertTrue(app.show_document_info({"type": "passport",
                                                "number": "2207 876234",
                                                "name": "Василий Гупкин"}))

    # Test show_all_docs_info
    def test_show_all_docs_info(self):
        self.assertTrue(app.show_all_docs_info())

    # Test add_new_doc
    @patch('builtins.input', side_effect=['100', 'pass', 'Ivan Ivanov', '3'])
    def test_add_new_doc1(self, mock_input):
        self.assertEqual(app.add_new_doc(), '3')
        self.assertIn('100', app.directories['3'])
        self.assertIn('pass', app.documents[3].values())
        self.assertIn('100', app.documents[3].values())
        self.assertIn('Ivan Ivanov', app.documents[3].values())

    @patch('builtins.input', side_effect=['100', 'pass', 'Ivan Ivanov', '4'])
    def test_add_new_doc2(self, mock_input):
        self.assertEqual(app.add_new_doc(), '4')
        self.assertIn('100', app.directories['4'])
        self.assertIn('pass', app.documents[3].values())
        self.assertIn('100', app.documents[3].values())
        self.assertIn('Ivan Ivanov', app.documents[3].values())

    # Test secretary_program_start
    @patch('builtins.input', side_effect=['q'])
    def test_secretary_program_start1(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['p', '11-2', 'q'])
    def test_secretary_program_start2(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['ap', 'q'])
    def test_secretary_program_start3(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['l', 'q'])
    def test_secretary_program_start4(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['s', '11-2', 'q'])
    def test_secretary_program_start5(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['a', '100', 'pass', 'Ivan Ivanov', '3', 'q'])
    def test_secretary_program_start6(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['d', '11-2', 'q'])
    def test_secretary_program_start7(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['m', '11-2', '2', 'q'])
    def test_secretary_program_start8(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['as', '4', 'q'])
    def test_secretary_program_start9(self, mock_input):
        self.assertTrue(app.secretary_program_start())

    @patch('builtins.input', side_effect=['help', 'q'])
    def test_secretary_program_start10(self, mock_input):
        self.assertTrue(app.secretary_program_start())


if __name__ == '__main__':
    unittest.main()

from domain.operations import decimal_to_roman, letters_in_roman


class TestProcesses():

    def setUp(self):
        pass

    def test_decimal_to_roman(self):
        test_1 = decimal_to_roman(1)
        self.assertEqual(test_1, "I")

        test_2 = decimal_to_roman(3999)
        self.assertEqual(test_2, "MMMCMXCIX")

        test_3 = decimal_to_roman(2291)
        self.assertEqual(test_3, "MMCCXCI")

        test_4 = decimal_to_roman(1322)
        self.assertEqual(test_4, "MCCCXXII")

        test_5 = decimal_to_roman(822)
        self.assertEqual(test_5, "DCCCXXII")

        test_6 = decimal_to_roman(196)
        self.assertEqual(test_6, "CXCVI")


    def test_characters(self):
        test_1 = letters_in_roman("I")
        output_1 = ["I"]
        self.assertEqual(test_1, output_1)

        test_2 = letters_in_roman("MMMCMXCIX")
        output_2 = ["X","M","I","C"]
        self.assertEqual(test_2, output_2)

        test_3 = letters_in_roman("MMCCXCI")
        output_3 = ["X","M","I","C"]
        self.assertEqual(test_3, output_3)

        test_4 = letters_in_roman("MCCCXXII")
        output_4 = ["X","M","I","C"]
        self.assertEqual(test_4, output_4)

        test_5 = letters_in_roman("DCCCXXII")
        output_5 = ["X","I","D","C"]
        self.assertEqual(test_5, output_5)

        test_6 = letters_in_roman("CXCVI")
        output_6 = ["X","V","I","C"]
        self.assertEqual(test_6, output_6)


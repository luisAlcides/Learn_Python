import unittest
import feedback


class CustomerFeedbackTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_survey_form(self):
        self.assertEqual(feedback.issue_survey(), 'Success')

    @unittest.expectedFailure
    def test_complaint_form(self):
        self.assertEqual(feedback.log_customer_complaint(), 'Success')


if __name__ == '__main__':
    unittest.main()

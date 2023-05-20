from unittest import TestCase
from unittest.mock import patch, MagicMock
from services.openai_service import generate_response

class TestOpenAIService(TestCase):
    @patch('openai.Completion.create')
    def test_generate_response(self, mock_create):
        # Mock the response from the OpenAI API
        mock_response = MagicMock()
        mock_response.choices[0].text.strip.return_value = "Test response"
        mock_create.return_value = mock_response

        # Call the generate_response function
        response = generate_response("Test prompt")

        # Check that the response is what we expect
        self.assertEqual(response, "Test response")

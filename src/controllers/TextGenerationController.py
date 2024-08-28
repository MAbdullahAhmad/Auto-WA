from models.GPTModel import GPTModel

class TextGenerationController:

    @staticmethod
    def generate(main_window):
    
        # Get input from the main window
        input_text = main_window.get_input()

        # Check if input text is empty
        if not input_text.strip():
            # Turn on the red light if input is empty
            main_window.set_status_led("red")
            return
        
        # Turn on the green light to indicate processing
        main_window.set_status_led("green")
        
        # Generate the response using the GPT model
        response = GPTModel().question_answer(input_text)
        
        # Set the generated response in the main window's output area
        main_window.set_output(response)

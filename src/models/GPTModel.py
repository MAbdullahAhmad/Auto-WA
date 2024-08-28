import re
import os
from collections import OrderedDict
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

class GPTModel:
    def __init__(self):
        # Load the saved model and tokenizer from the local path
        model_path = os.path.join(current_dir, "saved/gpt2")
        self.local_tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        self.local_model = GPT2LMHeadModel.from_pretrained(model_path)

    def generate_text(self, prompt, max_new_tokens=50, min_new_tokens=20):
        inputs = self.local_tokenizer.encode(prompt, return_tensors="pt")

        max_new_tokens_rand = random.randint(min_new_tokens, max_new_tokens)

        # Set the pad_token_id to the eos_token_id to suppress the warning
        outputs = self.local_model.generate(
            inputs, 
            max_new_tokens=max_new_tokens_rand, 
            num_return_sequences=1,
            pad_token_id=self.local_tokenizer.eos_token_id,
            repetition_penalty=1.2,
            # temperature=0.7,        # Add some randomness to avoid repetition
            # top_k=50,               # Limit to top 50 predictions
            # top_p=0.9               # Nucleus sampling with 90% probability mass
        )
        
        return self.local_tokenizer.decode(outputs[0], skip_special_tokens=True)


    def question_answer(self, prompt):
        # Generate the response
        response = self.generate_text(prompt)

        response = response[len(prompt):].strip()
        response = re.sub(r'\s+', ' ', response)

        def remove_repeating(target, delim='\n'):
            split = list(OrderedDict.fromkeys([t.strip() for t in target.split(delim)]))

            l = len(split)
            if(l > 1 and split[0][:len(split[l-1])] == split[l-1]):
                split = split[:l-1]

            join = delim.join(split)
            return join


        for d in ['.', '?', '\n', ':']: response = remove_repeating(response, d)

        response = re.sub(r'^[\.\?\!\,\'\"\:\;\-]+', '', response)

        return response

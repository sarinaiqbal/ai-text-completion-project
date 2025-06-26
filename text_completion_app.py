'''
Author: Sarina Iqbal
AI Capstone Project: AI-Powered Text Completion
'''
# Import cohere
import cohere
import os

cohere_api_key = "input_api_key_here" # input you API key here
co = cohere.Client(cohere_api_key) # Create client object to interact with API

# Function to generate output based on input prompt. Given, default 
# parameters temperature=0.7 and max_tokens=150
def gen_text(prompt, temperature=0.7, max_tokens=150):
    try:
        response = co.generate(
          model='command', # model type
          prompt=prompt, # input prompt
          max_tokens=max_tokens, # max number of tokens to generate
          temperature=temperature, # level of randomness
          stop_sequences=["\n"] # stop generating when newline encountered
        )
        return response.generations[0].text.strip() # return response
    except Exception as e:
        print(f"Error: {e}")

# Main logic to run the interactive AI app
def main():
    print("Welcome to the AI-Powered Text Completion Program!")
    while True:
        prompt = input("Enter your prompt here: ").strip()
        # Exit program if command == exit
        if prompt.lower() == 'exit': 
            print("Exiting the program.")
            break
        # Handle empty prompt
        if not prompt:
            print("Prompt cannot be empty, please enter a valid prompt.")
            continue
        if len(prompt)>1000: # Handle excessively long prompts
            print("Prompt is too long, please use a prompt with less than 1000 characters.")
            continue
        try: # Ask user input for max_tokens and temperature
            max_tokens = int(input("Max tokens: "))
            temperature = float(input("Temperature (0.0 to 1.0): "))
            # Raise error if temperature out of range
            if temperature<0.0 or temperature>1.0:
                raise ValueError("Temperature should be between 0.0 and 1.0.")
        except ValueError as e:
            print(f"Error: {e}")
            # In case of error, use default values for max_tokens: 150 and temperature=0.7
            print("Using default values for task completion: max_tokens: 150, temperature=0.7")
            temperature=0.7
            max_tokens=150
        print("Generating output...")
        result = gen_text(prompt, temperature, max_tokens)
        print(result)

main() # Run the program 

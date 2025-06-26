# AI Text Completion Project
This project is an interactive AI text completion app powered by Cohere’s API. It allows users to input various prompts, adjust the length of tokens to be generated, regulate the level of randomness, and generate text-based responses. 

## Setup
1. Clone the repository
```bash
git clone https://github.com/sarinaiqbal/ai-text-completion-project.git
```
2. Install cohere
```bash
pip install cohere
```
3. Get your Cohere API key and input it in the code
```bash
cohere_api_key = "input_api_key_here" # input you API key here
```
4. Run the program
```bash
python text-completion-project.py
```

## Usage
Once the program runs, you will be prompted to enter the following:
- Enter your text prompt: The sentence/question/text you would like to input.
- Enter max tokens: Enter the maximum number of tokes you would like to see in the generated response.
- Enter temperature: Enter your desired level of randomness.
- Enter ‘exit’ (case-insensitive) to exit the app

For example:

```bash
Enter your prompt here: What day is it today?
Max tokens: 
Temperature (0.0 to 1.0):
```

## Dependencies
`cohere`: AI text generation powered by Cohere’s API

# simpleRealtorChatbot
#### REALLY simple chatbot I made from what I've learned in ChatGPT Prompt Engineering for Developers from DeepLearningAI.

For now, use `sandbox.py` as my main example!

In this project I've explored the concepts of:

### Summarizing
Gathering the info I need from user prompt, e.g. from input fetch `seller_name`, `building cost`, `no_floors` and `address`.

### Transforming
For example: `John Smith, the building has 15 floors, it's located at 123 Main Street, Springfield at a cost of 250K` gets transformed into:
```json
{
  "reply" : "Thanks for sharing, I'm registering you right now!",
  "name": "John Smith",
  "floors": 15,
  "address": "123 Main Street, Springfield",
  "price": 2500000
}
```
...and then instantiated and saved as a `Building` object.


### Setup
1. Create a virtual environment and activate it:  

`python -m venv venv`

`source venv/bin/activate`  

On Windows: 
`venv\Scripts\activate`

2. Install the required dependencies:  
`pip install -r requirements.txt`

3. Create a .env file in the root directory and add your OpenAI API key:  
`OPENAI_API_KEY=your_openai_api_key_here`

4. Run the example script:
`python sandbox.py`

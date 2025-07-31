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

### Try it! 

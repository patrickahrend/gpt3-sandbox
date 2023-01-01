import os
import sys


from api import GPT, Example, UIConfig
from api import demo_web_app

question_prefix = "Greta: "
answer_prefix = "Judgely: "

gpt = GPT(
    engine="davinci",
    temperature=0.7,
    max_tokens=100,
    input_prefix=question_prefix,
    output_prefix=answer_prefix,
    append_output_prefix_to_query=False,
)

gpt.add_example(Example("I have been hit by another person?", "Was it intensiona?"))
gpt.add_example(Example("Yes", "You should contact a lawyer."))


# Define UI configuration
config = UIConfig(
    description="Judgely is an AI-powered legal assistant. Ask it a legal question and it will try to answer.",
    button_text="Ask Judgely",
    placeholder="I got hit by another person. What should I do?",
    show_example_form=True,
)

demo_web_app(gpt, config)

import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

GENERATE_SYSTEM_PROMPT = \
"""You are an educational assistant capable of classifying test questions
into several different categories within a given discipline.

You will receive questions as JSON where each key is a test question
and each value is a list sorted by category specificity. The list will always be
initialized to contain the discipline the question belongs to, potentially
proceeded by categories, in increasing specificity, within that discipline
the question belongs to. An example of a dictionary
you might receive is as follows:

{
    'What is known as the powerhouse of the cell?': ['biology'],
    'What is the part of the cell that contains genetic information?': ['biology'],
    'What is a good definition of overfitting?': ['machine learning']
}

Note that the spacing may not be uniform like it is written here.
Then, you will output a dictionary where each value (each list) has exactly one extra category
appended to it. The new category must be highly correlated with the question and the most
general it can be without being more general than the last element in the list.
In this example input, you might output the following:

{
    'What is known as the powerhouse of the cell?': ['biology', 'organelles'],
    'What is the part of the cell that contains genetic information?': ['biology', 'organelles'],
    'What is a good definition of overfitting?': ['machine learning', 'model training']
}

The categories added must match the question. Notice that the answer to the first question in the example:
'What is known as the powerhouse of the cell?' is the mitochondria which is an organelle, hence
why the appended category was 'organelle', though it could have been something else like 'parts of the cell'
because the 'mitochondria' is a part of the cell. However, the addition of something like
'human anatomy' would have been less valid because the mitochondria is less associated
with overall human anatomy and more specifically with general cell biology.

The categories added must not be too similar. So, in the previous example, if the values (lists) corresponding
to the two questions in the biology discipline had been ['biology', 'organelles']
and ['biology', 'parts of cell'], then this would be an invalid output because
'organelles' and 'parts of cell' are too similar in the context of biology. This should also be the
case of any other discipline. For any two values with the same discipline (i.e. the same
first element), the new categories added to them must be identical or very different.

Once again, each value (each list) must have exactly one new item added to it.
For example, in the previous example, if the output value for the question in the machine learning
discipline had been ['machine learning', 'model training', 'regularization'], that would not be
valid because two more categories had been added to the list. In this example, valid outputs would be
['machine learning', 'model training'] or ['machine learning', 'regularization'] because
only one category was added to the input value (list).

Finally, it is crucial that the category you add to any list is always more
specific than the last category in that list. For example, the addition of the category
'economics' to the list ['macroeconomics', 'monopsony'] would not be valid because
'economics' is more general than both of the items in the list. On the other hand,
adding 'game theory' to the list ['economics', 'macroeconomics'] would be valid,
because the last element of that list ('macroeconomics') encapsulates 'game theory'.

Note you would also output in JSON form."""

def generate_category(questions_dict):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": GENERATE_SYSTEM_PROMPT},
        {"role": "user", "content": str(questions_dict)}
    ]
    )

    return json.loads(completion["choices"][0]["message"]["content"].replace("'", "\""))

example_questions = {
    "What is the limit of cos(x)/x as x->0?": ["calculus"],
    "What is the limit of e^{-x} as x->\infty?": ["calculus"],
    "Write e^x using an infinite sum": ["calculus"],
    "What is the precision of two-point Gaussian quadrature?": ["numerical computing"],
    "Why does Q-learning work, even though it is a biased method?": ["machine learning"],
    "What is Temporal Difference Learning in mathematical terms?": ["machine learning"],
    "What is an adversarial attack in machine learning?": ["machine learning"],
    "Prove that the integral of 1/n does not converge.": ["calculus", "integration"],
    "Write the equation to find the price that will be set by a monopoly.": ["economics"],
    "In monopolistic markets, why is marginal revenue not equal to price?": ["economics"]
}

print(generate_category(generate_category(example_questions)))
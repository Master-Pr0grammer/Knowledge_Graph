# HackRPI 2023 Hackathon
## Inspiration
In any level of education, a good majority of time spent studying can be attributed to organizing the study material into an interpretable format. There exist many studies that show that compartmentalization of information can drastically improve one’s information recall and overall efficiency while studying.

The idea is to automatically organize, pre-existing study material in order to enhance studying performance by creating a meaningful visualization that indicates the user’s strengths and weaknesses in a particular subject.

## What it does
At the heart of "Knowledge Net” is the integration of Anki, a flashcard application, with our self-developed front-end visualization. The platform allows learners to interact with their study material by converting Anki deck contents into an intelligently organized knowledge map.

Upon entering a deck name, "Knowledge Net" taps into the AnkiConnect plugin to fetch card details and construct a nested dictionary that encapsulates specific subtopics to which each card belongs.

What sets "Knowledge Net" apart is its use of the ChatGPT API, which is utilized to enhance the topic creation process. Our system uses GPT to generate topics from the Anki cards in increasing specificity, allowing for the creation of a tree structure.

Our front-end, crafted by the hackathon team, brings this structured data to life through a visual network of nodes. This visualization not only aids in identifying the various topics within a deck but also gauges mastery over each subject by incorporating the "ease" score from Anki's review history. This score dynamically influences the visual weight of each node, providing users with immediate visual feedback on their proficiency in each topic.

Users interact with "Knowledge Net" by engaging with these nodes, taking tests, and reviewing flashcards, which actively informs the system of their learning progression. Category generation happens iteratively, with a new layer of leaf nodes created when the user decides they want more specific categorization. Such generation allows for an adaptive user experience. The insights gained from the API enable learners to pinpoint their strengths and weaknesses and adapt their study habits accordingly.

## How we built it
We make use of the ChatGPT API to generate categories considering the current tree structure. With some prompt engineering, ChatGPT is capable of effectively generating new leaf nodes in the tree structure, allowing for dynamic expansion of the knowledge graph with increasing specificity.

## What's next for Knowledge Net
Improving the UI, allowing users to correct model's categorizations using reinforcement using human feedback, allowing support to upload additional study materials like files to individual nodes of the graph, a way for users to be able to share graphs to other people, and adding additional support for existing education software like google classroom or LMS.

## References and Relevant Links
Anki-Connect: https://github.com/FooSoft/anki-connect
HackRPI Devpost: https://devpost.com/software/knowledge-net?ref_content=my-projects-tab&ref_feature=my_projects
Presentation: https://docs.google.com/presentation/d/1JWHSDnfH79ZqwZ3HqpMCWBJCDC-SBTGah_NQW6rwaqI/edit?usp=sharing

import json

# Sample JSON data
json_data = [
    {
        "id": "5da2351d42e60850385814ac",
        "title": "[Beginner Practice] Quant - Percentage v3"
    },
    {
        "id": "5da2351e42e60850385814c5",
        "title": "[Beginner Practice] Verbal - Articles v3"
    },
    {
        "id": "5da2351e42e60850385814b4",
        "title": "[Beginner Practice] Reasoning - Syllogism v3"
    },
    {
        "id": "5da2351d42e60850385814aa",
        "title": "[Beginner Practice] Quant - Simple & Compound Interest v3"
    },
    {
        "id": "5da2351e42e60850385814c4",
        "title": "[Beginner Practice] Verbal - Noun v3"
    },
    {
        "id": "5da2351e42e60850385814b7",
        "title": "[Beginner Practice] Reasoning - Logical Venn Diagram v3"
    },
    {
        "id": "5da2351d42e60850385814ab",
        "title": "[Beginner Practice] Quant - Profit, Loss & Discount v3"
    },
    {
        "id": "5da2351e42e60850385814b8",
        "title": "[Beginner Practice] Reasoning - Direction Sense Test v3"
    },
    {
        "id": "5da2351e42e60850385814b2",
        "title": "[Beginner Mock] Quant - Profit, Loss & Discount, Percentage, Simple & Compound Interest v3"
    },
    {
        "id": "5da2351e42e60850385814c9",
        "title": "[Beginner Mock] Verbal - Pronoun, Preposition v3"
    },
    {
        "id": "5da2351e42e60850385814c0",
        "title": "[Beginner Mock] Reasoning - Direction Sense Test, Syllogism, Logical Venn Diagram v3"
    },
    {
        "id": "5da2351e42e60850385814cb",
        "title": "[Beginner Practice] Quant - Ratio & Proportion v3"
    },
    {
        "id": "5da2351e42e60850385814c2",
        "title": "[Beginner Practice] Verbal - Pronouns v3"
    },
    {
        "id": "5da2351e42e60850385814bb",
        "title": "[Beginner Practice] Reasoning - Alpha-Numeric-Symbol v3"
    },
    {
        "id": "5da2351d42e60850385814a9",
        "title": "[Beginner Practice] Quant - Average & Ages v3"
    },
    {
        "id": "5da2351e42e60850385814c3",
        "title": "[Beginner Practice] Verbal - Prepositions v3"
    },
    {
        "id": "5da2351e42e60850385814b3",
        "title": "[Beginner Practice] Reasoning - Sequence v3"
    },
    {
        "id": "5da2351e42e60850385814b1",
        "title": "[Beginner Mock] Quant - Ratio & Proportion, Average & Ages v3"
    },
    {
        "id": "5da2351e42e60850385814cc",
        "title": "[Beginner Practice] Reasoning - Word Formation v3"
    },
    {
        "id": "5da2351e42e60850385814bf",
        "title": "[Beginner Mock] Reasoning - Word Formation, Alpha-Numeric-Symbol , Sequence v3"
    },
    {
        "id": "5da2351d42e60850385814af",
        "title": "[Beginner Practice] Quant - Time, Speed & Distance v3"
    },
    {
        "id": "5da2351e42e60850385814c1",
        "title": "[Beginner Practice] Verbal - Synonyms v3"
    },
    {
        "id": "5da2351e42e60850385814b9",
        "title": "[Beginner Practice] Reasoning - Coding-Decoding v3"
    },
    {
        "id": "5da2351d42e60850385814ae",
        "title": "[Beginner Practice] Quant - Algebra v3"
    },
    {
        "id": "5da2351e42e60850385814c6",
        "title": "[Beginner Practice] Verbal - Antonyms v3"
    },
    {
        "id": "5da2351e42e60850385814b6",
        "title": "[Beginner Practice] Reasoning - Odd One Out v3"
    },
    {
        "id": "5da2351d42e60850385814ad",
        "title": "[Beginner Practice] Quant - Number System-Basics, Cyclicity & Miscellaneous v3"
    },
    {
        "id": "5da2351e42e60850385814ca",
        "title": "[Beginner Practice] Verbal - One Word Substitution v3"
    },
    {
        "id": "5da2351e42e60850385814ba",
        "title": "[Beginner Practice] Reasoning - Analogy v3"
    },
    {
        "id": "5da2351d42e60850385814b0",
        "title": "[Beginner Mock] Quant - Number System-Basics, Cyclicity & Miscellaneous v3"
    },
    {
        "id": "5da2351e42e60850385814c7",
        "title": "[Beginner Mock] Verbal - Synonyms, Antonyms, One word Substitution v3"
    },
    {
        "id": "5da2351e42e60850385814be",
        "title": "[Beginner Mock] Reasoning - Analogy, Coding-Decoding, Odd One Out v3"
    },
    {
        "id": "5da2351e42e60850385814c8",
        "title": "[Beginner Mock] Verbal - Articles, Noun v3"
    },
    {
        "id": "5da2351e42e60850385814bc",
        "title": "[Beginner Practice] Reasoning - Blood Relations v3"
    },
    {
        "id": "5da2351e42e60850385814b5",
        "title": "[Beginner Practice] Reasoning - Seating Arrangement v3"
    },
    {
        "id": "5da2351e42e60850385814bd",
        "title": "[Beginner Mock] Reasoning - Blood Relations, Seating Arrangement v3"
    }
]

# Convert JSON to a simple format
simple_format = [(item["id"], item["title"]) for item in json_data]

# Print the simplified format
for item in simple_format:
    print(item)

import json
import random

# Data pools for randomization
FIRST_NAMES = ["Alex", "Jamie", "Sam", "Taylor", "Jordan", "Casey", "Morgan", "Riley", "Cameron", "Quinn"]
LAST_NAMES = ["Morgan", "Lee", "Chen", "Smith", "Johnson", "Williams", "Brown", "Davis", "Miller", "Wilson"]
CITIES = ["Portland", "Austin", "Denver", "Seattle", "Chicago", "Boston", "Miami", "Atlanta", "Phoenix", "Dallas"]
PETS = ["golden retriever", "tabby cat", "parakeet", "beagle", "pug", "iguana", "hamster", "poodle", "turtle", "bulldog"]

def generate_profile():
    """Generates a random profile dictionary."""
    return {
        "name": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
        "birth_year": random.randint(1970, 2000),
        "city": random.choice(CITIES),
        "pet": random.choice(PETS)
    }

def format_document(doc_idx, profile):
    """Formats a profile into the standardized document template."""
    doc_str = f"Document [{doc_idx}]: {profile['name']} is a software engineer born in {profile['birth_year']}.\n"
    doc_str += f"{profile['name']} lives in {profile['city']} and owns a {profile['pet']}."
    return doc_str

def generate_example(num_docs, target_position):
    """Generates a single QA example with the target at the specified position."""
    # Generate unique profiles to avoid name collisions
    profiles = []
    used_names = set()
    while len(profiles) < num_docs:
        prof = generate_profile()
        if prof['name'] not in used_names:
            profiles.append(prof)
            used_names.add(prof['name'])
    
    target_profile = profiles[target_position]
    
    # Format documents
    formatted_docs = []
    for i, prof in enumerate(profiles):
        formatted_docs.append(format_document(i + 1, prof))
    
    # Construct the final prompt
    context = "\n\n".join(formatted_docs)
    question = f"What year was {target_profile['name']} born?"
    
    prompt = f"{context}\n\nQuestion: {question}\nAnswer:"
    
    return {
        "num_documents": num_docs,
        "target_position": target_position,
        "question": question,
        "target_name": target_profile['name'],
        "expected_answer": str(target_profile['birth_year']),
        "prompt": prompt
    }

def build_dataset(num_docs, examples_per_position, output_file):
    """Builds and saves the dataset for a specific context length."""
    dataset = []
    for pos in range(num_docs):
        for _ in range(examples_per_position):
            dataset.append(generate_example(num_docs, pos))
            
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in dataset:
            f.write(json.dumps(item) + '\n')
    print(f"Generated {len(dataset)} examples for N={num_docs} saved to {output_file}")

if __name__ == "__main__":
    # Generate datasets for N=5, 10, and 20 as specified in the plan
    build_dataset(num_docs=5, examples_per_position=50, output_file="data/n5_positions.jsonl")
    build_dataset(num_docs=10, examples_per_position=50, output_file="data/n10_positions.jsonl")
    build_dataset(num_docs=20, examples_per_position=50, output_file="data/n20_positions.jsonl")
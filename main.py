from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)

# Load all quotes into memory once
with open('quotes.jsonl', 'r') as f:
    quotes = [json.loads(line.strip()) for line in f]

# with open('category.txt', 'r+', encoding='utf-8') as file:
#     content = file.read().split(', ')  # Read and split tags
#     existing_tags = set(content)  # Store existing tags in a set
    
#     for q in quotes:
#         for tags in q['tags']:
#             existing_tags.add(tags)  # Ensure uniqueness

#     file.seek(0)  # Move cursor to the beginning
#     file.write(', '.join(existing_tags))  # Write updated tags
#     file.truncate()  # Remove any leftover content
#----------------------------------------------------

@app.route('/quotes/random', methods=['GET'])
def get_random_quote_by_tag():
    tag_query = request.args.get('tags', '').lower()

    if tag_query:
        filtered_quotes = [
            q for q in quotes
            if any(tag_query in tag.lower() for tag in q.get('tags', []))
        ]
        if filtered_quotes:
            return jsonify(random.choice(filtered_quotes))
        else:
            return jsonify({'error': 'No quote found for the given tag'}), 404

    return jsonify(random.choice(quotes))

@app.route('/api/search', methods=['GET'])
def search_quotes():
    author = request.args.get('author', '').lower()
    tag = request.args.get('tag', '').lower()

    filtered = [
        q for q in quotes
        if (author in q['author'].lower() if author else True) and
           (any(tag in t.lower() for t in q['tags']) if tag else True)
    ]
    return jsonify(filtered[:10])  # return top 10 results

@app.route('/api/quote/<int:index>', methods=['GET'])
def get_quote_by_index(index):
    if 0 <= index < len(quotes):
        return jsonify(quotes[index])
    return jsonify({'error': 'Index out of range'}), 404

if __name__ == '__main__':
    app.run(debug=True)

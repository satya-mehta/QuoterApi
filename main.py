from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)

# Load all quotes into memory once
with open('quotes.jsonl', 'r', encoding='utf-8') as f:
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

@app.route('/quotes/random')
def random_quote():
    tag_filter = request.args.get('tags', '').lower()
    max_length = request.args.get('maxlength', type=int)

    filtered_quotes = quotes

    # Filter by tag if present
    if tag_filter:
        filtered_quotes = [
            q for q in filtered_quotes
            if any(tag_filter in tag.lower() for tag in q.get('tags', []))
        ]

    # Filter by max quote length
    if max_length is not None:
        filtered_quotes = [
            q for q in filtered_quotes
            if len(q['quote']) <= max_length
        ]

    if not filtered_quotes:
        return jsonify({"error": "No matching quote found"}), 404

    return jsonify(random.choice(filtered_quotes))

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

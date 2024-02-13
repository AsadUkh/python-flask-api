from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "JavaScript Basics", "author": "Jane Smith"}
]

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a specific book by its ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Endpoint to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    if not new_book or 'title' not in new_book or 'author' not in new_book:
        return jsonify({"message": "Invalid request"}), 400
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# Endpoint to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    data = request.json
    if 'title' in data:
        book['title'] = data['title']
    if 'author' in data:
        book['author'] = data['author']
    return jsonify(book)

# Endpoint to delete a book by its ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "Health looks good"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

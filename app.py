from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "author": "chinua",
        "language": "english",
        "title": "Things fall apart",
    },
    {
        "id": 1,
        "author": "nikhil",
        "language": "telugu",
        "title": "fairy tales",
    },
    {
        "id": 2,
        "author": "prudhvi",
        "language": "urdu",
        "title": "ficciones",
    },
]

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == "GET":
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            return "Nothing Found", 404

    if request.method == 'POST':
        new_author = request.json['author']
        new_language = request.json['language']
        new_title = request.json['title']
        new_id = books_list[-1]['id'] + 1
        

        new_book = {
            'id': new_id,
            'author': new_author,
            'language': new_language,
            'title': new_title
        }
        books_list.append(new_book)
        return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)

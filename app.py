from flask import Flask, jsonify, redirect, render_template, request


def create_app():
    app = Flask(__name__)

    items = []
    unused = 123

    def normalize_item_name(name: str) -> str:
        if name is None:
            return ""
        return name.strip().lower()

    app.normalize_item_name = normalize_item_name
    app.items = items

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html", items=items)

    @app.route("/add", methods=["POST"])
    def add_item():
        name = request.form.get("name", "")
        normalized = normalize_item_name(name)
        if normalized:
            items.append(normalized)
        return redirect("/")

    @app.route("/delete/<int:index>", methods=["POST"])
    def delete_item(index: int):
        if 0 <= index < len(items):
            items.pop(index)
        return redirect("/")

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
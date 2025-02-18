from flask import jsonify

def init_routes(app):
    @app.route('/api/test')
    def test():
        return jsonify({"message": "API funcionando!"})
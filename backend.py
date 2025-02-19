from flask import Flask, request, jsonify
import ast
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   

def explain_code(code):
    """Analyzes Python code and generates human-readable explanations."""
    try:
        tree = ast.parse(code)
        explanation = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                explanation.append(f"Defines a function `{node.name}()` with parameters {', '.join(arg.arg for arg in node.args.args)}.")

            elif isinstance(node, ast.Return):
                explanation.append("Returns a value from the function.")

            elif isinstance(node, ast.Assign):
                targets = [target.id for target in node.targets if isinstance(target, ast.Name)]
                explanation.append(f"Assigns a value to the variable(s): {', '.join(targets)}.")

            elif isinstance(node, ast.If):
                explanation.append("Checks a condition using `if`.")

            elif isinstance(node, ast.For):
                explanation.append("Loops over an iterable using `for`.")

            elif isinstance(node, ast.While):
                explanation.append("Repeats code while a condition is `True` using `while`.")

            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print":
                explanation.append("Prints output to the console.")

        return "\n".join(explanation) if explanation else "No explanations found."
    
    except Exception as e:
        return f"Error parsing code: {str(e)}"

@app.route('/explain', methods=['POST'])
def explain():
    data = request.get_json()
    code = data.get("code", "")
    explanation = explain_code(code)
    return jsonify({"explanation": explanation})


if __name__ == "__main__":
    app.run(debug=True)

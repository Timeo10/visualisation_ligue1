from flask import Flask, Response
import pandas as pd
import json

app = Flask(__name__)

df = pd.read_csv("clubs_ligue1_2024_2025.csv")

df = df.where(pd.notnull(df), None)

@app.route("/clubs", methods=["GET"])
def get_clubs():
    data = df.to_dict(orient="records")
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    return Response(json_data, content_type="application/json; charset=utf-8")

if __name__ == "__main__":
    app.run(debug=True)

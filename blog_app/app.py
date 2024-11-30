from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# GPTモデルの読み込み（Hugging Faceから）
model = pipeline('text-generation', model='gpt2')  # 修正後のモデル名
  # GPT-2の場合

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        topic = request.form['topic']
        # モデルを使って記事を生成
        article = model(f"Write an article about {topic}", max_length=500)[0]['generated_text']
        return render_template('index.html', article=article)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

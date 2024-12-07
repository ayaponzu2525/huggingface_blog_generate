from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# GPTモデルの読み込み（Hugging Faceから）
model = pipeline('text-generation', model='gpt2')  # GPT-2の場合

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        topic = request.form['topic']
        # ブログ記事の構成を指定
        prompt = f"Write a blog post about {topic}. Like a daily diary"
        
        # 記事生成
        article = model(prompt, max_length=800)[0]['generated_text']
        
        # プロンプトは表示せずに記事だけをテンプレートに渡す
        return render_template('index.html', article=article)
    
    # 初回アクセス時は記事なしで表示
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

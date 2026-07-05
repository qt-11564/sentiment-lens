from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# 加载情感分析 pipeline：使用 DistilBERT 微调模型
# 首次运行会自动下载模型缓存到本地
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        # 获取用户提交的文本，去除首尾空白
        text = request.form.get('text', '').strip()
        if text:
            # 调用 AI 模型进行推理，返回列表，取第一个元素
            result = sentiment_pipeline(text)[0]
            # 格式化结果：标签 (置信度)
            sentiment = f"{result['label']} (confidence: {result['score']:.2f})"
    # 如果是 GET 请求或无输入，sentiment 保持 None，模板显示空
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    # 监听所有网络接口，方便 WSL 外访问
    app.run(host='0.0.0.0', port=5000, debug=True)
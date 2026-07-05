# SentimentLens - 英文情感分析 Web 应用

一个基于 DistilBERT 的实时英文情感分析工具，使用 Flask 搭建 Web 界面，支持输入文本并返回积极/消极情绪及置信度。

## 🚀 功能特点

- 输入英文文本，自动识别情感倾向（POSITIVE / NEGATIVE）
- 显示置信度分数，结果直观
- 轻量级模型，响应快速
- 完整的开发到部署流程（Git Flow、Linux、Nginx、Gunicorn）

## 🛠 技术栈

- **AI 模型**：HuggingFace `transformers` + DistilBERT
- **Web 框架**：Flask
- **部署**：Gunicorn + Nginx + systemd
- **版本控制**：Git + GitHub（Git Flow 分支策略）
- **开发环境**：WSL + VS Code Remote

## 📦 本地运行

```bash
# 克隆仓库
git clone git@github.com:qt-11564/sentiment-lens.git
cd sentiment-lens

# 创建虚拟环境并安装依赖
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 启动应用
python app.py

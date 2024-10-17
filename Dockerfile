# # Dockerfile
# FROM python:3.9-slim

# WORKDIR /app
# COPY helloworld.py .

# CMD ["python", "helloworld.py"]


# ベースイメージを指定（Python 3.9を使用）
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt requirements.txt
COPY . .

# パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナが利用するポートを指定
EXPOSE 5001

# Flaskアプリを起動
CMD ["python", "app.py"]

# 使用 Python 官方镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 允许构建时传递 API 地址
ARG BOOKS_API_URL

# 运行时设置环境变量（可在 Azure 或 Docker 里覆盖）
ENV BOOKS_API_URL=${BOOKS_API_URL}

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码到容器
COPY . .

# 声明 Flask 运行的端口
EXPOSE 5001

# 运行 Flask 客户端
CMD ["python", "book_client.py"]
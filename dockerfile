# 使用 Python 官方镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install -r requirements.txt

# 复制代码到容器
COPY . .

# 运行 Flask 客户端
CMD ["python", "book_client.py"]
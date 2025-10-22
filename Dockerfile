# ===============================
# 1️⃣ Base image
# ===============================
FROM python:3.12-slim

# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python output is sent straight to terminal (no buffering)
ENV PYTHONUNBUFFERED 1

# ===============================
# 2️⃣ Set work directory
# ===============================
WORKDIR /app

# ===============================
# 3️⃣ Install system dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# ===============================
# 4️⃣ Install Python dependencies
# ===============================
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# ===============================
# 5️⃣ Copy project files
# ===============================
COPY . /app/

# ===============================
# 6️⃣ Expose port & run server
# ===============================
EXPOSE 8000

# Use Gunicorn in production
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

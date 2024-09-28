# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 to the outside world
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "your_script_name.py"]

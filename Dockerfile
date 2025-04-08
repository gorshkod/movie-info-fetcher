# Use an official Python base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY /src /app/src
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port for Streamlit
EXPOSE 8501

# API key handling
ARG API_KEY
ENV API_KEY=${API_KEY}

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "/src/Search.py", "--server.port=8501", "--server.address=0.0.0.0"]

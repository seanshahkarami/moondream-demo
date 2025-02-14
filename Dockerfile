FROM python:3.12

WORKDIR /app

# Download small and large models.
ADD https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-2b-int8.mf.gz .
ADD https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-0_5b-int8.mf.gz .

# Install dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

ENTRYPOINT [ "python", "main.py" ]

FROM python:3.12

WORKDIR /app

# Download small and large models.
ADD https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-2b-int8.mf.gz .
ADD https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-0_5b-int8.mf.gz .

# HACK We'll install the headless version of opencv to fix this import error:
# ImportError: libGL.so.1: cannot open shared object file: No such file or directory
#
# TODO: Figure out how to address this when pywaggle installs it's dependencies.
RUN pip install opencv-python-headless==4.11.0.86

# Install dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

ENTRYPOINT [ "python", "main.py" ]

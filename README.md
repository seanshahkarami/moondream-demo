# Moondream Demo App

This app is a simple demo which pipes a camera stream against through the
provided Moondream prompt and prints the model output.

## Usage

The app takes the following arguments:

- `--camera`: Name of camera stream to use.
- `--model`: Which Moondream model to use. (Either `moondream-2b-int8.mf.gz` or
  `moondream-0_5b-int8.mf.gz`.)
- `query`: Query to run against image stream.

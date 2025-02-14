import argparse
import moondream as md
from waggle.plugin import Plugin
from waggle.data.vision import Camera
from PIL import Image
import json

models = [
    "moondream-2b-int8.mf.gz",
    "moondream-0_5b-int8.mf.gz",
]


def run(plugin: Plugin, model: str, camera, query: str):
    query = query.strip()

    print(f"Running with model={model!r} camera={camera!r} query={query!r}", flush=True)

    print("Loading model...", flush=True)
    model = md.vl(model=model)

    camera = Camera(camera)

    while True:
        print("Taking snapshot from camera...", flush=True)
        snapshot = camera.snapshot()
        snapshot.save("snapshot.jpg")

        print("Encoding image...", flush=True)
        image = Image.open("snapshot.jpg")
        encoded_image = model.encode_image(image)

        print("Querying model...", flush=True)
        answer = model.query(encoded_image, query)["answer"].strip()

        print("Query:", query, flush=True)
        print("Answer:", answer, flush=True)

        output = json.dumps(
            {
                "query": query,
                "answer": answer,
            },
            separators=(",", ":"),
        )

        plugin.upload_file("snapshot.jpg", timestamp=snapshot.timestamp)
        plugin.publish("caption", output, timestamp=snapshot.timestamp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=models[0], choices=models)
    parser.add_argument("--camera", default=0)
    parser.add_argument("query")
    args = parser.parse_args()
    with Plugin() as plugin:
        run(
            plugin=plugin,
            model=args.model,
            camera=args.camera,
            query=args.query,
        )

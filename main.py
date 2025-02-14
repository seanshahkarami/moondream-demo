import argparse
import moondream as md
from waggle.data.vision import Camera
from PIL import Image

models = [
    "moondream-2b-int8.mf.gz",
    "moondream-0_5b-int8.mf.gz",
]


def main(model, camera, query):
    model = md.vl(model=model)

    camera = Camera(camera)

    while True:
        image = camera.snapshot()
        image.save("snapshot.jpg")
        image = Image.open("snapshot.jpg")
        encoded_image = model.encode_image(image)

        answer = model.query(encoded_image, query)["answer"]
        print("Query:", query, flush=True)
        print("Answer:", answer, flush=True)
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=models[0], choices=models)
    parser.add_argument("--camera", default=0)
    parser.add_argument("query")
    args = parser.parse_args()
    main(
        model=args.model,
        camera=args.camera,
        query=args.query,
    )

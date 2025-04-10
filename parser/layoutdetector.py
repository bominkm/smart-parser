import cv2
import supervision as sv
from ultralytics import YOLOv10

def detect_layout(model_path, img_path):
    model = YOLOv10(model=model_path)
    image = cv2.imread(filename=img_path)

    results = model(image)[0]
    detections = sv.Detections.from_ultralytics(results)

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    return sv.plot_image(annotated_image)
# git clone https://github.com/sunsmarterjie/yolov12
# cd yolov12
# python -m venv yolov12-env
# yolov12-env\Scripts\activate
# pip install --upgrade pip
# pip install roboflow supervision --upgrade


from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

model = YOLO('F:/AI_Mango_Propagation/best.pt')



image_path = "data_mog\น้ำดอกไม้สีทอง\IMG_20250519_104018.jpg"
image = cv2.imread(image_path)

results = model(image)

for r in results:
    boxes = r.boxes.xyxy.cpu().numpy() 
    classes = r.boxes.cls.cpu().numpy().astype(int)
    confs = r.boxes.conf.cpu().numpy()

    for box, cls_id, conf in zip(boxes, classes, confs):
        label = model.names[cls_id]
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("Result")
plt.axis('off')
plt.show()



# By Bend_Function
# https://space.bilibili.com/275177832
# 視訊演示地址：[https://www.bilibili.com/video/av32418677/?p=3]
# 模型下載地址 https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
# 可以放在任何資料夾下執行（前提正確配置API[環境變數]）

import time
start = time.time()
import numpy as np
import os
import tensorflow as tf

from PIL import Image
from object_detection.utils import label_map_util

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 要改的內容
###############################################
PATH_TO_CKPT = 'model\\ssd_mobilenet_v1_graph.pb'   # 模型及標籤地址
PATH_TO_LABELS = 'model\\mscoco_label_map.pbtxt'

NUM_CLASSES = 90            # 檢測物件個數

PATH_TO_TEST_IMAGES_DIR = os.getcwd()+'\\test_images'               # 測試圖片路徑

confident = 0.5  # 置信度，即scores>confident的目標才被輸出
###############################################
    
# Load a (frozen) Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')    
    
    
# Loading label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


os.chdir(PATH_TO_TEST_IMAGES_DIR)
TEST_IMAGE_PATHS = os.listdir(PATH_TO_TEST_IMAGES_DIR)

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with detection_graph.as_default():
  with tf.Session(graph=detection_graph, config=config) as sess:
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    for image_path in TEST_IMAGE_PATHS:     # 開始檢測
        image = Image.open(image_path)          # 讀圖片
        width, height = image.size
        image_np = np.array(image)
        image_np_expanded = np.expand_dims(image_np, axis=0)
        # Actual detection.
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: image_np_expanded})

        s_boxes = boxes[scores > confident]
        s_classes = classes[scores > confident]
        s_scores = scores[scores > confident]

        for i in range(len(s_classes)):
            name = image_path.split("\\")[-1]
            # name = image_path.split("\\")[-1].split('.')[0]   # 不帶字尾
            ymin = s_boxes[i][0] * height  # ymin
            xmin = s_boxes[i][1] * width  # xmin
            ymax = s_boxes[i][2] * height  # ymax
            xmax = s_boxes[i][3] * width  # xmax
            score = s_scores[i]
            if s_classes[i] in category_index.keys():
                class_name = category_index[s_classes[i]]['name']  # 得到英文class名稱

            print("name:", name)
            print("ymin:", ymin)
            print("xmin:", xmin)
            print("ymax:", ymax)
            print("xmax:", xmax)
            print("score:", score)
            print("class:", class_name)
            print("################")


end = time.time()
print("Execution Time: ", end - start)
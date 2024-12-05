import tensorflow as tf
from tensorflow.keras.preprocessing import image 
import numpy as np
 
model = tf.keras.models.load_model('xray_classification_model.h5')
print(model.summary(), end='\n\n')

image_path = r'person1_virus_11.jpeg'  # 분류할 이미지 파일 경로
img = image.load_img(image_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0 # 이미지를 0-1 범위로 정규

predictions = model.predict(img_array)

print(predictions, end='\n\n')
if predictions[0][0] > 0.5:
  print("이 이미지는 PNEUMONIA에 속합니다.")
else:
  print("이 이미지는 NORMAL에 속합니다.")
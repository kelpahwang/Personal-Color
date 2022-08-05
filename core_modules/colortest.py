#%%
import cv2
import numpy as np
import time
from PIL import Image


# p = "p.jpg"
# p1 = "p1.jpg"
# p2 = "p2.jpg"
# p3 = "p3.jpg"  
# p4 = "p4.png"
# p5 = "p5.jpg"
# p6 = "p6.jpg"
# p7 = "p7.jpg"
# p8 = "p8.jpg"
# p9 = "p9.jpg"
# p10 = "p10.jpg"
# p11 = "p11.jpg"
# p12 = "p12.png"



def get_rgb2(image_path):
    photo = Image.open(image_path) #your image
    photo = photo.convert('RGB')

    width = photo.size[0] #define W and H
    height = photo.size[1]

    for y in range(0, height): #each pixel has coordinates
        row = ""
        for x in range(0, width):

            RGB = photo.getpixel((x,y))
            R,G,B = RGB  #now you can use the RGB value
    print([R,G,B])
    return [R,G,B]
 



def crop_face(image_path):
    # Read the input image
    img = cv2.imread(image_path)
  
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('D:/haarcascade_frontface.xml')
  
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]
        # cv2.imshow("face",faces)
        cv2.imwrite('cropped_face.jpg', faces)
    

    img2 = cv2.imread('cropped_face.jpg')
    img2 = cv2.resize(img2,(256,256))
    cv2.imwrite('cropped_face.jpg', img2)
    
    return "cropped_face.jpg"
    # x,y,w,h = 3,3,220,240
    # crop = img2[y: y + h, x: x + w]
    # cv2.imwrite('cropped_face.png',crop)    
      
    # Display the output
    # cv2.imwrite('detcted.jpg', img)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)





def get_hsv(image_path,test=False):
    origin_image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)
    image = np.concatenate((origin_image,hsv_image), axis=1)

    print('원본 : \t',origin_image[0,0,:])
    print('hsv : \t',hsv_image[0,0,:])

    h,s,v = hsv_image[0,0,:]
    
    print(np.mean(origin_image))
    print(np.mean(hsv_image))
    # print(h,s,v)

    if test == False:
        cv2.imshow('HSV', image)
        cv2.waitKey(0)
    
    
    
    
def get_hsv2(image_path):
    img = cv2.imread(image_path)
    height, width, channel = img.shape
    bgr = img.astype(np.float) / 255.0

    b, g, r = cv2.split(bgr)

    h = np.zeros((height, width), dtype=np.float)
    s = np.zeros((height, width), dtype=np.float)
    v = np.max(bgr, axis=2)

    for i in range(height):
        for j in range(width):
            if v[i][j] == 0:
                h[i][j] = 0
                s[i][j] = 0
            else:
                min_rgb = min(bgr[i][j])

                s[i][j] = 1 - (min_rgb / v[i][j])

                if v[i][j] == r[i][j]:
                    h[i][j] = 60 * (g[i][j] - b[i][j]) / (v[i][j] - min_rgb)
                elif v[i][j] == g[i][j]:
                    h[i][j] = 120 + (60 * (b[i][j] - r[i][j])) / (v[i][j] - min_rgb)
                elif v[i][j] == b[i][j]:
                    h[i][j] = 240 + (60 * (r[i][j] - g[i][j])) / (v[i][j] - min_rgb)
                if h[i][j] < 0:
                    h[i][j] += 360
                h[i][j] /= 360

    hsv_img = (np.dstack((h, s, v)) * 255).astype(np.uint8)
    # cv2.imshow('original', img)
    # cv2.imshow('hsv', hsv_img)
    # cv2.imshow('h', h)
    # cv2.imshow('s', s)
    # cv2.imshow('v', v)
    
    # print(h)
    # print(h,s,v)
    
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h2, s2, v2 = cv2.split(hsv)
    

    # print(h2, s2, v2)
    # cv2.imshow('hsv2', hsv)
    # cv2.imshow('h2', h2)
    # cv2.imshow('s2', s2)
    # cv2.imshow('v2', v2)

    cv2.waitKey(0)
    
    # cv2.destroyAllWindows()



if __name__ == '__main__':    
    cropped = "cropped_face.jpg"


    # crop_face(p5)
    # get_rgb2(cropped)
    # get_hsv(cropped)

    # get_hsv2(cropped)


# %%

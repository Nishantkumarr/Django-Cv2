from django.shortcuts import render    
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def get_image_filter(image,action):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if action == 'GRAYSCALE':
            image=gray
        return image
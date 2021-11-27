# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:28:00 2021

@author: Jai
"""
#This is an image processing program that takes an image  and adds a relevant background with a bokeh effect. 

#Input: sample.jpg Image 

#Output: blur_img.jpg Image with Blur Background 

from pixellib.semantic import semantic_segmentation
segment_image = semantic_segmentation()
from pixellib.tune_bg import alter_bg
#Altering background color
change_bg = alter_bg()
#loading model
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
#changing background color
change_bg.color_bg("sample.jpg", colors = (255,255,255), output_image_name="colored_bg.jpg")
change_bg.change_bg_img(f_image_path = "colored_bg.jpg",b_image_path = "background.jfif", output_image_name="new_img.jpg")
#making background blurr
change_bg.blur_bg("new_img.jpg", extreme = True, output_image_name="blur_img.jpg")
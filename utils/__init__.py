import cv2
import math
import numpy as np
import keras.backend_config as K
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.utils import normalize
from tensorflow.keras.models import load_model


def IoU(y_true, y_pred):
    smooth = 1e-5
    y_true_f = float(K.flatten(y_true))
    y_pred_f = float(K.flatten(y_pred))
    intersection = K.sum(y_true_f * y_pred_f)
    return (intersection + smooth) / (
        K.sum(y_true_f) + K.sum(y_pred_f) - intersection + smooth
    )


def IoU_Loss(y_true, y_pred):
    return 1 - IoU(y_true, y_pred)

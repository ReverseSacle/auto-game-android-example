import cv2

#####################################图片位置点击######################################################

def is_in_image_center_point(obj_img_path,screen_path,threadshold,x_bias=0,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + obj_w / 2 + x_bias,max_loc[1] + obj_h / 2 + y_bias)
    return (-1,-1)

def is_in_image_center_top(obj_img_path,screen_path,threadshold,x_bias=0,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + obj_w / 2 + x_bias,max_loc[1] + y_bias)
    return (-1,-1)

def is_in_image_center_bottom(obj_img_path,screen_path,threadshold,x_bias=0,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + obj_w / 2 + x_bias,max_loc[1] + obj_h + y_bias)
    return (-1,-1)

def is_in_image_center_right(obj_img_path,screen_path,threadshold,x_bias=0,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + obj_w + x_bias,max_loc[1] + obj_h / 2 + y_bias)
    return (-1,-1)

def is_in_image_center_left(obj_img_path,screen_path,threadshold,x_bias=0,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + x_bias,max_loc[1] + obj_h / 2 + y_bias)
    return (-1,-1)

def is_in_image_bottom_right(obj_img_path,screen_path,threadshold,x_bias=-10,y_bias=-10):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + obj_w + x_bias,max_loc[1] + obj_h + y_bias)
    return (-1,-1)

def is_in_image_bottom_left(obj_img_path,screen_path,threadshold,x_bias=0,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + x_bias,max_loc[1] + obj_h + y_bias)
    return (-1,-1)

def is_in_image_bottom_right_left(obj_img_path,screen_path,threadshold,x_bias=90,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + (obj_w / 2) + x_bias,max_loc[1] + obj_h + y_bias)
    return (-1,-1)

def is_in_image_bottom_right_top(obj_img_path,screen_path,threadshold,x_bias=90,y_bias=0):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    # print(max_val)
    if max_val >= threadshold:
        return (max_loc[0] + obj_w+ x_bias,max_loc[1] + y_bias)
    return (-1,-1)

#####################################图片位置点击######################################################


def is_in_image_original(obj_img_path,screen_path):
    screen_img = cv2.imread(screen_path)
    obj_img = cv2.imread(obj_img_path)

    obj_h,obj_w = obj_img.shape[0],obj_img.shape[1]
    # 第二个参数为模板，为被匹配的对象，在screen_img中找
    result = cv2.matchTemplate(screen_img,obj_img,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    if max_val >= 0:
        # print(max_val)
        return max_val
    return 0

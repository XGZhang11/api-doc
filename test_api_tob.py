import requests

email = 'xxx@example.com'
password = 'xxx'
base_url = "https://www.remagi.io/api/v1b"

def get_token(email, password):
    """
    获取用户token
    params: 
        email: 用户邮箱
        password: 用户密码
    返回状态码: 
        0: success
        600: user not found
        601: password not correct
        602: user is not a business user
    返回值:
        {'token': string}
    """
    data = {
        'email': email, 
        'password': password,
    }
    response = requests.post(base_url + "/get_token", json=data).json()
    return response


def task_submit(token, model_name='Artist_V0.1.3', prompt="", neg_prompt="", n_images=2,
                   scale=7, output_size="640x640", select_seed=-1, init_img="", controlnet_model=""):
    """
    发起任务
    params: 
        token: 用户token
        model_name: 模型名称
        prompt: 描述
        neg_prompt: 反向描述
        n_images: 生成数量
        scale: 文本描述力度
        select_seed: 随机数种子
        output_size: 图像大小
        init_img: 初始图片，若有为i2i，若无为t2i
        controlnet_model: controlnet模型，默认为空

    返回状态码: 
        0: success
        600: user not found or token error
        603: you have too many tasks running
        604: points not enough
        501: Server connection error
        500: Intern Error
    返回值:
        {'task_id': string}
    """
    data = {
        "token": token,
        "model_name": model_name,
        "prompt": prompt,
        "neg_prompt": neg_prompt,
        "n_images": n_images,
        "scale": scale,
        "select_seed": select_seed,
        "output_size": output_size,
        "init_img": init_img,
        "controlnet_model": controlnet_model,
    }
    response = requests.post(base_url + "/txt2img_submit", json=data).json()
    return response


def task_result(token, task_id):
    """
    获取任务结果
    params: 
        token: 用户token
        task_id: 任务id

    返回状态码: 
        0: success
        600: user not found or token error
        500: Intern Error
    返回值:
        {
            'state': string, # 任务状态
            'images': dict{string}, # 图片路径，包括大图和中图路径
            'error_msg': string, # 错误信息
            'wait_time': int, # 预估排队人数
            'select_seed': int, # 用到的随机数种子
        }
    """
    data = {
        'token': token,
        'task_id': task_id,
    }
    response = requests.post(base_url + "/task_result", json=data).json()
    return response


def get_generation_form():
    """
    获取提交表单
    返回状态码: 
        0: success
        500: Intern Error
    返回值:
        {
        "code": 0, 
        "info": [
            {
            "choices": [
                "Artist_V0.1.3",
            ], 
            "default": "Artist_V0.1.3", 
            "description": "model name", 
            "name": "model_name", 
            "type": "list"
            }, 
            {
            "default": "", 
            "description": "prompt", 
            "name": "prompt", 
            "type": "string"
            }, 
            {
            "default": "", 
            "description": "negative prompt", 
            "name": "neg_prompt", 
            "type": "string"
            }, 
            {
            "default": 2, 
            "description": "number of images", 
            "max": 8, 
            "min": 1, 
            "name": "n_images", 
            "type": "int"
            }, 
            {
            "default": 7, 
            "description": "Guidance Scale", 
            "max": 20, 
            "min": 1, 
            "name": "scale", 
            "type": "int"
            }, 
            {
            "default": -1, 
            "description": "seed", 
            "max": 9999999, 
            "min": 0, 
            "name": "select_seed", 
            "type": "int"
            }, 
            {
            "choices": {
                "1:1": [
                "512x512", 
                "640x640", 
                "768x768", 
                "1024x1024"
                ], 
                "2:3": [
                "512x768", 
                "640x960", 
                "768x1152", 
                "1024x1536"
                ], 
                "3:2": [
                "768x512", 
                "960x640", 
                "1152x768", 
                "1536x1024"
                ]
            }, 
            "default": "512x512", 
            "description": "resolution", 
            "name": "resolution", 
            "type": "dict"
            }, 
            {
            "default": "", 
            "description": "init image url", 
            "name": "init_img", 
            "type": "str"
            }, 
        ], 
        "msg": ""
        }
    """
    response = requests.get(base_url + "/get_generation_form").json()
    return response
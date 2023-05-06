## 图片生成(i2i,t2i) 接口


### 获取token
#### 创建访问
> POST   https://www.remagi.io/api/v1b/get_token
#### 请求参数
| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                                                     |
| ----------- | --------| -------  | -------------------| --------------------------------------------------------|
| email       | string  | 是       | "xxx@example.com"  | tob用户的用户邮箱，需先在remagi.io注册                       |
| password    | string  | 是       |  "password"        | tob用户密码                                               |

##### 请求示例
**python示例**

~~~python
import requests

url = 'https://www.remagi.io/api/v1b/get_token'  
data = {
   "email": "xxx@example.com",
   "password": "password",
}  

response = requests.post(url, json=data)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{
    "token": "xxxxxxxxxxxxxxxxxx", # string 当前用户token
}
~~~

### 任务提交

#### 创建访问

> POST   https://www.remagi.io/api/v1b/task_submit

#### 请求参数

| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                                                      |
| ----------- | --------| -------  | ----------------- | --------------------------------------------------------- |
| token       | string  | 是       | 无，通过get_token获得 | 通过get_token获取的token                                  |
| model_name  | string  | 是       | Artist_V0.1.3     | 模型名称(可选值: 通过/api/v1b/get_generation_form获得)        |
| prompt      | string  | 是       | ""                | 用于生成图片的特征描述，如："one girl,beautiful"               |
| neg_prompt  | string  | 无       | ""                | 特征的反向描述，如："unsafe"                                  |
| n_images    | int     | 是       | 2                 | 生成图片数量                                                 |
| scale       | int     | 是       | 7                 | 文本控制力度(1-20)                                           |
| select_seed | int     | 否       | -1                | 随机数种子                                                   |
| output_size | string  | 是       | 960x960           | 图片的输出尺寸，如："960x960"                                 |
| init_img    | string  | 否       | ""                | 输入图片，url形式，若有即为i2i(图生图)，无即为t2i(文生图)         |

##### 请求示例

**curl 示例**

~~~
curl https://www.remagi.io/api/v1b/task_submit \
  -H "Content-Type: application/json" \
  -d '{
    "model_name": "Artist_V0.1.3",
    "prompt": "one girl, beautiful",
    "neg_prompt": "unsafe", 
    "n_images": 2,
    "scale": 7, 
    "output_size": "640x640",
    "select_seed": -1,
    ”token": "",
  }'
~~~

**python示例**

~~~python
import requests

url = 'https://www.remagi.io/api/v1b/task_submit'  
data = {
    "model_name": "Artist_V0.1.3", # string 用到的模型名称（规定范围内）
    "prompt": "one girl, beautiful", # 正向描述词
    "neg_prompt": "unsafe", # 反向描述词
    "n_images": 2, # int 生成图片的数量
    "scale": 7, # int 文本控制力度
    "output_size": "640x640", # string 生成的图片尺寸
    "select_seed": 0, # int 随机数种子。如果是-1的话代表不指定
    "token": "",  # get_token获取的token
}  

response = requests.post(url, json=data)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{
    "task_id": "f3e5b59c-7416-11ed-a160-00163e025c94", # string 任务id
}
~~~

### 结果查询

#### 创建访问

> POST       https://www.remagi.io/api/v1b/task_result

#### 请求参数

| 参数名称 | 类型   | 是否必须 | 默认值 | 含义                                |
| -------- | ------ | -------- | ------ | -------------------------------|
| task_id  | string | 是       | 无      | 由任务创建接口返回的任务id         |
| token    | string | 是       | 无      | 由get_token获取的token          |

##### 请求示例

**curl 示例**

~~~
curl https://www.remagi.io/api/v1b/task_result \
  -H "Content-Type: application/json" \
  -d '{
        "task_id": "f3e5b59c-7416-11ed-a160-00163e025c94",
        "token": "",
  }'
~~~

**python示例**

~~~python
import requests

url = 'https://www.remagi.io/api/v1b/task_result'  
data = {
    "task_id": "f3e5b59c-7416-11ed-a160-00163e025c94", # string 任务id
    "token": "", # get_token获取的token
}  

response = requests.post(url, json=data)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{
    "state": "done", # string 任务状态，未完成会是 "pending"
    'images': [
        {
            'large': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00000.jpg",
            'middle': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00000.mid.jpg",
            'save_index': 0,
            'share': false,
            'shareable': true,
        }, 
        {
            'large': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00001.jpg",
            'middle': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00001.mid.jpg",
            'save_index': 1,
            'share': false,
            'shareable': true,
        },
        {
            'large': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00002.jpg",
            'middle': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00002.mid.jpg",
            'save_index': 2,
            'share': false,
            'shareable': true,
        },
        {
            'large': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00003.jpg",
            'middle': "https://pic.bakamaka.io/txt2img-result/2022-12-10/31e17f66-788b-11ed-98e2-00163e025c94_00003.mid.jpg",
            'save_index': 3,
            'share': false,
            'shareable': true,
        },
    ],, # list 图片路径
    "error_msg": "Intern error", # string 错误信息
    "wait_time": true, # bool 前方等待人数
    "select_seed": true, # bool 该任务用到的随机数种子
    "fav": true, # bool 是否被标记为收藏
}
~~~

### 获取生成表单

> GET       https://www.remagi.io/api/v1b/get_generation_form

#### 请求参数

无

##### 请求示例

**python示例**

~~~python
import requests

url = 'https://www.remagi.io/api/v1b/get_generation_form'  

response = requests.get(url)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例
~~~json
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

~~~


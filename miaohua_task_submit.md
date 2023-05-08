## 图片生成(i2i,t2i) 接口


### 获取token
#### 创建访问
> POST   http://miaohua.sensetime.com/api/v1b/get_token
#### 请求参数
| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                                                     |
| ----------- | --------| -------  | -------------------| --------------------------------------------------------|
| email       | string  | 是       | "xxx@example.com"  | tob用户的用户邮箱，需先在miaohua.sensetime.com注册           |
| password    | string  | 是       |  "password"        | tob用户密码                                               |

##### 请求示例
**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/get_token'  
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

> POST   http://miaohua.sensetime.com/api/v1b/task_submit

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
curl http://miaohua.sensetime.com/api/v1b/task_submit \
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

url = 'http://miaohua.sensetime.com/api/v1b/task_submit'  
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

> POST       http://miaohua.sensetime.com/api/v1b/task_result

#### 请求参数

| 参数名称 | 类型   | 是否必须 | 默认值 | 含义                                |
| -------- | ------ | -------- | ------ | -------------------------------|
| task_id  | string | 是       | 无      | 由任务创建接口返回的任务id         |
| token    | string | 是       | 无      | 由get_token获取的token          |

##### 请求示例

**curl 示例**

~~~
curl http://miaohua.sensetime.com/api/v1b/task_result \
  -H "Content-Type: application/json" \
  -d '{
        "task_id": "f3e5b59c-7416-11ed-a160-00163e025c94",
        "token": "",
  }'
~~~

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/task_result'  
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

> GET       http://miaohua.sensetime.com/api/v1b/get_generation_form

#### 请求参数

无

##### 请求示例

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/get_generation_form'  

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

## 以下为训练相关

### 批量上传图片
#### 创建访问
> POST       http://miaohua.sensetime.com/api/v1b/upload_imgs

#### 请求参数
files形式

| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                               |
| ----------- | --------| -------  | ----------------- | -----------------------------------|
| token       | file    | 是       | 无，通过get_token获得 | 包含在files中                      |
| init_img    | file    | 是        | 无                 | 图片文件,可以多个，都以'init_img'为key|

##### 请求示例

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/upload_imgs'
# files的列表格式，以init_img为key
img_paths = ['/local/pic1.png', '/local/pic2.png',]  
files = [('init_img', open(img_path, 'rb')) for img_path in img_paths]
files.append(('token', token))


response = requests.post(url, files=files)

print(response.status_code) 
print(response.json())
~~~

##### 返回示例

~~~json
{
  "code": 0,
  "info": [
    "https://bkmk.oss-accelerate.aliyuncs.com/900ea63e-e1dd-11ed-bef5-00163e005161?OSSAccessKeyId=LTAI5tPynodLHeacT1J5SmWh&Expires=317042257726&Signature=x7nUVN6xpDustx4K02WOTjuty4Q%3D",
    "https://bkmk.oss-accelerate.aliyuncs.com/91d5e7d4-e1dd-11ed-bef5-00163e005161?OSSAccessKeyId=LTAI5tPynodLHeacT1J5SmWh&Expires=317042257730&Signature=d1weIkwFwVK9nbCrPNdkeVm1wQA%3D"
  ],
  "msg": ""
}
~~~

### 创建数据集
#### 创建访问
> POST       http://miaohua.sensetime.com/api/v1b/dataset

#### 请求参数

| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                                                       |
| ----------- | --------| -------  | ----------------- | ---------------------------------------------------------- |
| token       | string  | 是       | 无，通过get_token获得 | 通过get_token获取的token                                   |
| name        | string  | 是       | 无                  | 数据集名称                                                  |
| description | string  | 否       | ""                |  数据集描述                                                   | 
| images      | list    | 是       | 无                 | 图片列表, url list，可通过批量上传图片接口/api/v1b/upload_imgs获取|             

##### 请求示例

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/dataset'  
data = {
  "token": "xxxx", # get_token获取到的token
  "name": "dataset1", # 数据集名称
  "description": "dataset1 description",  # 数据集描述
  "images": [
    "https://bkmk.oss-accelerate.aliyuncs.com/900ea63e-e1dd-11ed-bef5-00163e005161?OSSAccessKeyId=LTAI5tPynodLHeacT1J5SmWh&Expires=317042257726&Signature=x7nUVN6xpDustx4K02WOTjuty4Q%3D",
    "https://bkmk.oss-accelerate.aliyuncs.com/91d5e7d4-e1dd-11ed-bef5-00163e005161?OSSAccessKeyId=LTAI5tPynodLHeacT1J5SmWh&Expires=317042257730&Signature=d1weIkwFwVK9nbCrPNdkeVm1wQA%3D"
  ] # 图片列表，url list
}  

response = requests.post(url, json=data)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{'code': 0, 'info': {'dataset_id': 11}, 'msg': ''}
~~~

### 获取已创建的全部数据集
#### 创建访问
> POST       http://miaohua.sensetime.com/api/v1b/dataset_all

#### 请求参数

| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                                                       |
| ----------- | --------| -------  | ----------------- | ---------------------------------------------------------- |
| token       | string  | 是       | 无，通过get_token获得 | 通过get_token获取的token                                   |

##### 请求示例

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/dataset_all'  
data = {
  "token": "xxx", # get_token获取到的token
}  

response = requests.post(url, json=data)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{
  "items": [
    {
      "id": 1,   # dataset id
      "name": "dataset1",  # dataset 名称
      "description": "dataset1 description",  # dataset 描述
      "demo_picture": "url",   # 封面图
      "create_time": "2023-04-23 00:00:00",  # 创建时间
      "update_time": "2023-04-23 00:00:00",  # 修改时间
      "images": [
        "url1",
        "url2"
      ], # 数据集图片列表
      "images_num": 2 # 数据集图片数量
    },
    {
      "id": 2,
      "name": "dataset2",
      "description": "dataset2 description",
      "demo_picture": "url",
      "create_time": "2023-04-23 00:00:00",
      "update_time": "2023-04-23 00:00:00",
      "images": [
        "url3"
      ],
      "images_num": 1
    }
  ],
  "page": 1,
  "per_page": 20,
  "has_next": false,
  "has_prev": false,
  "totalPages": 1
}
~~~

### 提交训练任务

#### 创建访问

> POST       http://miaohua.sensetime.com/api/v1b/train_submit

#### 请求参数

| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                                                      |
| ----------- | --------| -------  | ----------------- | --------------------------------------------------------- |
| token       | string  | 是       | 无，通过get_token获得 | 通过get_token获取的token                                  |
| name        | string  | 是       | 无                  | 需要训练的模型名称                                          |
| description | string  | 否       | ""                | 训练的模型描述                                               |
| base_model  | string  | 否       | 自动选择            | 训练所需要的基本模型，可选模型范围通过/api/v1b/train_form获取    |
| trigger_word | string | 否       | ""                 | 触发词                                                     |
| main_body   | string  | 是       | "Style"           | 主体，可选范围通过/api/v1b/train_form获取                     |
| nsfw        | int     | 是       | 0                 | 是否nsfw，0为true,1为false                                  |
| dataset     | list    | 是       | 无                | 训练所选的数据集id的list,需要先创建数据集                       |

##### 请求示例

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/train_submit'  
data = {
    "token": "", # get_token获取的token
    "name": "train model1", # 训练的模型名称
    "description": "train model1 description",  # 训练的模型描述
    "base_model": "自动选择", # 基模型
    "trigger_word": "one girl", # 触发词
    "main_body": "Style", # 主体
    "nsfw": 0, # 1为true, 0为false
    "dataset": [5, 7], # 选择的数据集的id组合，list
}  

response = requests.post(url, json=data)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{'code': 0, 'info': {'task_id': 'xxxxx'}, 'msg': ''}
~~~

### 获取训练进度

#### 创建访问

> POST       http://miaohua.sensetime.com/api/v1b/train_progress

#### 请求参数

| 参数名称     | 类型     | 是否必须  | 默认值              | 含义                                                      |
| ----------- | --------| -------  | ----------------- | --------------------------------------------------------- |
| token       | string  | 是       | 无，通过get_token获得 | 通过get_token获取的token                                  |
| task_id     | string  | 是       | 无                  | 训练任务的task_id                                         |

##### 请求示例

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/train_progress'  
data = {
    "token": "", # get_token获取的token
    "task_id": "xxxxxx", # 训练任务的task_id
}  

response = requests.post(url, json=data)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{'create_time': '2023-05-08 14:22:52', 'description': 'train model1 description', 'main_body': 'Style', 'model_name': 'train_model1', 'state': 'done', 'training_progress': 1.0, 'trigger_word': 'one girl'}
~~~
返回训练state为状态，training_progress为进度(0-1)，状态为'done'后，可通过之前的生成接口生成图片，模型的model_name取训练时取的名字。

### 获取训练表单字段

#### 创建访问

> GET       http://miaohua.sensetime.com/api/v1b/get_train_form

#### 请求参数

无

##### 请求示例

**python示例**

~~~python
import requests

url = 'http://miaohua.sensetime.com/api/v1b/get_train_form'  

response = requests.get(url)

print(response.status_code) 
print(response.text)
~~~

##### 返回示例

~~~json
{
  "code": 0,
  "info": {
    "base_model": [
      "商汤自研作画模型 Beta",
      "水彩风",
    ],
    "main_body": [
      "Style",
      "Human",
      "Architecture",
      "Plants",
      "Animals"
    ]
  },
  "msg": ""
}
~~~
主要是base_model和main_body这两个字段。
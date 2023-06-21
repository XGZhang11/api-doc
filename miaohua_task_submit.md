## 融合接口


> POST    https://......

该接口提供聊天和画图功能，通过 POST 方式创建 url 请求，注意请求的 http Header 中需要包含 Authorization 项，其值为你申请得到的 API_SECRET_KEY。

### 请求参数

| 参数名称           | 类型   | 是否必须 | 默认值 | 含义                                                                                                       |
| ------------------ | ------ | -------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| messages             | array | 是       | 无     | 对话上下文，数组中的对象为聊天的上下文信息，格式如 <br>`[{"role": "user", "content": Say this is a test!"}]`, role取值user或assistant|
| temperature          | float | 否       | 0.8    | chat温度采样参数，取值(0,2]。大于1的值倾向于生成更加多样的回复，小于1倾向于生成更加稳定的回复       
| top_p                | float | 否       | 0.7    | chat核采样参数，取值(0,1]。解码生成token时，在概率和大于等于top_p的最小token集合中进行采样        
| max_new_tokens       | int   | 否       | 2048   | chat的token生成的最大数量        
| repetition_penalty   | float | 否       | 1      | chat重复惩罚系数，1代表不惩罚，大于1倾向于生成不重复token，小于1倾向于生成重复token     
| stream               | bool  | 否       | false  | chat是否使用流式传输，如果开启，数据将按照data-only server-sent events传输中间结果，并以`data: [DONE]`结束   
| user                 | string| 否       |        | 用户ID
| chat_key             | string| 是       | 无     | chat api的key
| miaohua_token        | string| 是       | 无     | miaohua的token
| model_name           | string| 是       | Artist_V0.1.3 ｜ 秒画模型名称
| controlnet_model     | string| 否       | ""     | 若为空则不启用controlnet,可选值为"openpose","canny","depth","fake_scribble","scribble","hed","hough","normal","seg" 
        |

#### 请求示例

**curl 示例**

~~~
curl https://lm_experience.sensetime.com/nlp/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: $API_SECRET_KEY" \
  -d '{
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.8,
        "top_p": 0.7,
        "max_new_tokens": 2048,
        "repetition_penalty": 1,
        "stream": false,
        "user_id": "test"
  }'
~~~

**python示例**

~~~python
import requests
api_secret_key = "xxxxxxxxxx"  # your api_secret_key

url = 'https://lm_experience.sensetime.com/nlp/v1/chat/completions'  
data = {
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.8,
    "top_p": 0.7,
    "max_new_tokens": 2048,
    "repetition_penalty": 1,
    "stream": false,
    "user_id": "test"
}  
headers = {
    'Content-Type': 'application/json',
    'Authorization': api_secret_key
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code) 
print(response.text)
~~~

#### 返回示例

~~~json
{
    "code":200,
    "msg":"ok",
    "data":{
        "id":"4b44cd86cd2c000"
        "choices":[
        	{ 
              "content": "this is a test!",
              "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 6,
            "completion_tokens": 6,
            "total_tokens": 12
        }
        "status": 0,
    }
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
| init_img    | string  | 否       | ""                | 输入图片，url形式，若有即为i2i(图生图)，无即为t2i(文生图)。当'controlnet_model'参数非空时，init_img为controlnet的输入图片         |
| controlnet_model    | string  | 否       | ""                | 若为空则不启用controlnet,可选值为"openpose","canny","depth","fake_scribble","scribble","hed","hough","normal","seg" (目前canny已启用)         |

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
    "output_size": "960x960",
    "select_seed": -1,
    "token": "",
    "init_img": "",
    "controlnet_model": "",
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
    "output_size": "960x960", # string 生成的图片尺寸
    "select_seed": -1, # int 随机数种子。如果是-1的话代表不指定
    "init_img": "", # img url,若为空为文生图，否则为图生图
    "controlnet_model": "", # controlnet模型，若为空则不启用controlnet,启用时需要init_img不为空
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
}
~~~


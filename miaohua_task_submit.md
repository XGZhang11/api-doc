## 融合接口


> POST    https://......

该接口提供聊天和画图功能，通过 POST 方式创建 url 请求，注意请求的 http Header 中需要包含 Authorization 项，其值为你申请得到的sensechat的 API_SECRET_KEY。

### 请求参数

| 参数名称           | 类型   | 是否必须 | 默认值 | 含义                                                                                                       |
| ------------------ | ------ | -------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| messages             | array | 是       | 无     | 对话上下文，数组中的对象为聊天的上下文信息，格式如 <br>`[{"role": "user", "content": Say this is a test!"}]`, role取值user或assistant|
| temperature          | float | 否       | 0.8    | chat温度采样参数，取值(0,2]。大于1的值倾向于生成更加多样的回复，小于1倾向于生成更加稳定的回复       
| top_p                | float | 否       | 0.7    | chat核采样参数，取值(0,1]。解码生成token时，在概率和大于等于top_p的最小token集合中进行采样        
| max_new_tokens       | int   | 否       | 2048   | chat的token生成的最大数量        
| repetition_penalty   | float | 否       | 1      | chat重复惩罚系数，1代表不惩罚，大于1倾向于生成不重复token，小于1倾向于生成重复token     
| stream               | bool  | 否       | false  | chat是否使用流式传输，如果开启，数据将按照data-only server-sent events传输中间结果，并以`data: [DONE]`结束   
| user_id              | string| 否       |        | 用户ID
| mh_key        | string| 是       | 无     | miaohua的token
| mh_model_name           | string| 是       | Artist_V0.1.3 | 秒画模型名称
| mh_output_size          | string| 是       | 960x960| 图片的输出尺寸，如："960x960"
| mh_select_seed          | int   | 否       | -1     | 随机数种子
| mh_scale                | int   | 是       | 7      | 文本控制力度(1-20)  
| mh_controlnet_model     | string| 否       | ""     | 若为空则不启用controlnet,可选值为"openpose","canny","depth","fake_scribble","scribble","hed","hough","normal","seg" |

#### 请求示例

**curl 示例**

~~~
curl https://...... \
  -H "Content-Type: application/json" \
  -H "Authorization: $API_SECRET_KEY" \
  -d '{
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.8,
        "top_p": 0.7,
        "max_new_tokens": 2048,
        "repetition_penalty": 1,
        "stream": false,
        "user_id": "test",
        "mh_key": $MIAOHUA_TOKEN,
        "mh_model_name": "Artist_V0.1.3",
        "mh_scale": 7, 
        "mh_output_size": "640x640",
        "mh_select_seed": -1,
  }'
~~~

**python示例**

~~~python
import requests
api_secret_key = "xxxxxxxxxx"  # your api_secret_key

url = 'https://......'  
data = {
      "messages": [{"role": "user", "content": "Say this is a test!"}],
      "temperature": 0.8,
      "top_p": 0.7,
      "max_new_tokens": 2048,
      "repetition_penalty": 1,
      "stream": false,
      "user_id": "test",
      "mh_key": $MIAOHUA_TOKEN,
      "mh_model_name": "Artist_V0.1.3",
      "mh_scale": 7, 
      "mh_output_size": "640x640",
      "mh_select_seed": -1,
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
              "content": "this is a test!(or the url of the generated picture)",
              "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 6,
            "completion_tokens": 6,
            "total_tokens": 12,
            "picture": false, # 是否生成图片
        }
        "status": 0,
    }
}
~~~




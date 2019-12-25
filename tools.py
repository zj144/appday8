import yaml

with open('./data/mms_value.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

    print("data:{}".format(data))
    print('文件类型', type(data.get('value')))

# da = {"第一组":
#     {
#         "电话": 16600282792,
#         "信息": 123
#     }
#
# }
#
# with open("./data/mms_data.yaml","w",encoding="utf-8") as f:
#     yaml.dump(da,f)
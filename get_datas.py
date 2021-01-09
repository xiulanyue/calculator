import yaml

def get_datas(name):
    with open("./calculator_data.yaml") as f:
        datas = yaml.safe_load(f)
    return datas[name]

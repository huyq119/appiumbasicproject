import yaml


def handle_black(fun):
    def run(*args, **kwargs):
        instance = args[0]
        with open("../page/black_list.yml", 'r', encoding='utf-8') as f:
            _black_list = yaml.safe_load(f)
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in _black_list:
                ele = instance._driver.find_elements(*black)
                if len(ele) > 0:
                    ele[0].click()
                    return fun(*args, **kwargs)
            raise e

    return run

def pick_up(template: set, json_object, result=[]):
    """
    查找json中所有满足template定义字段条件的对象
    :param template: 指定字段集合
    :param json_object: JSON对象|List|Dict
    :param result: 结果集合，集合中的元素都是Dict
    :return:
    """
    if isinstance(json_object, dict):
        if template.issubset(list(json_object.keys())):
            result.append(json_object)
            print('发现视频资源！！！！')
        else:
            for k in json_object.keys():
                pick_up(template, json_object.get(k), result)
    elif isinstance(json_object, list):
        for e in json_object:
            pick_up(template, e, result)
    return result

from unit import checkResult, apiSend
from unit.readResultRelevance import get_relevance


def api_send_check(case, project_dict,relevance,_path):
    # print('case----',case)
    # print('prodict-----',project_dict)
    # print('rele-----',relevance)
    # print('path-----', _path)
    # relevance = {'doubanID'：'123331'}
    """
    接口请求并校验结果
    :param case: 单条用例
    :param project_dict: 用例文件对象
    :param relevance: 关键值实例对象
    :param rel: 关联值类对象
    :param _path: case目录
    :return:
    """
    # print('1------',data)
    # print('2------',code)
    # print('case------', case)
    # print('project_dict------', project_dict)
    # # print('5------', project_dict["test_info"].get("address"))
    # print('relevance-------', relevance)
    # print('_path-------', _path)
    # print('rel-------', rel)



    code, data = apiSend.send_request(case, project_dict["test_info"].get("host"),
                                      project_dict["test_info"].get("address"), _path, relevance)
    if isinstance(case["check"], list):
        for i in case["check"]:
            checkResult.check_result(case["test_name"], i, code, data, _path, relevance)
    else:
        checkResult.check_result(case["test_name"], case["check"], code, data, _path, relevance)
import config.yml_DATA
from QQAI2.qqai2.plugins.content.data import *
# 好感商城商品添加
def store_Add(goods:str,money:int,value:int) ->str:
    """

    :param goods: 商品名称
    :param money: 价格
    :param value: 价值
    :return:
    """
    store_content = store_change(ReadWrite='r')
    if not goods in list(store_content.keys()):
        store_content.update({goods:
                                  {'积分':money,
                                   '价值':value}})
        store_change(data=store_content,ReadWrite='w')
        return '商品添加成功'
    else:
        return '该商品已存在'
# 好感商城商品删除
def store_remove(goods:str) ->str:
    store_content = store_change(ReadWrite='r')
    if goods in list(store_content.keys()):
        del store_content[goods]
        store_change(data=store_content,ReadWrite='w')
        return '商品删除成功'
    else:
        return '该商品不存在'

# 商品购买
def buy(user:str=None,quantity:int=1,commodity:str=None,look_up:bool=False):
    """

    :param user: 用户
    :param quantity: 数量
    :param commodity: 商品名称
    :param look_up: 显示商品
    :return:
    """
    commodity_data = store_change(ReadWrite='r')
    commodity_list = list(commodity_data.keys())
    knapsack_data = knapsack_deposit(ReadWrite='r')
    exist_user = list(knapsack_data.keys())
    store_data = store_change(ReadWrite='r')
    print(commodity_list)
    print(commodity)
    if commodity in list(store_data.keys()):
        # 使用数据库为对象
        if config.yml_DATA.data == 'mysql' or config.yml_DATA.data == 'sqlite':
            print('select 积分 from qd where user = "%s"'%user)
            integral = int(Data('select 积分 from qd where user = "%s"'%user)[0][0])
            if commodity_data[commodity]['积分']*quantity < integral:
                if not user in exist_user:
                    Data('update qd set 积分= 积分-%d where user = "%s"' % (commodity_data[commodity]['积分']*quantity, user))
                    # 初次存入
                    knapsack_data.update({user:
                                              {
                                                  commodity:{'好感':commodity_data[commodity],
                                                             '积分':commodity_data[commodity]['积分'],
                                                             '数量':quantity}
                                              }
                    })
                    knapsack_deposit(data=knapsack_data,ReadWrite='w')
                    return '购买成功'
                elif commodity in list(knapsack_data[user].keys()):
                    Data('update qd set 积分= 积分-%d where user = "%s"' % (commodity_data[commodity]['积分'] * quantity, user)) #扣除对应积分
                    # 二次存入
                    knapsack_data[user][commodity]['数量'] = knapsack_data[user][commodity]['数量']+quantity
                    knapsack_deposit(data=knapsack_data, ReadWrite='w')
                    return '购买成功'
                else:
                    Data('update qd set 积分= 积分-%d where user = "%s"' % (commodity_data[commodity]['积分'] * quantity, user))
                    knapsack_data[user].update({commodity:{'好感':commodity_data[commodity],
                                                             '积分':commodity_data[commodity]['积分'],
                                                             '数量':quantity}})
                    knapsack_deposit(data=knapsack_data, ReadWrite='w')
                    return '购买成功'
            else:
                return '您的积分不足'
        # 使用json文件为对象
        elif config.yml_DATA.data == 'json':
            DATA = Data(ReadWrite='r')
            subscript = DATA['qd']['user'].index(user)
            integral = DATA['qd']['积分'][subscript]
            if commodity_data[commodity]['积分']*quantity < integral:
                if not user in exist_user:
                    DATA['qd']['积分'][subscript] = DATA['qd']['积分'][subscript]-commodity_data[commodity]['积分']*quantity
                    Data(data=DATA,ReadWrite='w')
                    knapsack_data.update({user:
                        {
                            commodity: {'好感':commodity_data[commodity]['好感'],
                                        '积分':commodity_data[commodity]['积分'],
                                        '数量':quantity}
                        }
                    })
                    knapsack_deposit(data=knapsack_data, ReadWrite='w')
                    return '购买成功'
                elif commodity in list(knapsack_data[user].keys()):
                    DATA['qd']['积分'][subscript] = DATA['qd']['积分'][subscript] - commodity_data[commodity][
                        '积分'] * quantity
                    knapsack_data[user].update(
                        {
                            commodity: {'好感':commodity_data[commodity]['好感'],
                                        '积分':commodity_data[commodity]['积分'],
                                        '数量':quantity}
                        }
                    )
                    knapsack_deposit(data=knapsack_data,ReadWrite=
                                     'w')
                    return '购买成功'
                else:
                    DATA['qd']['积分'][subscript] = DATA['qd']['积分'][subscript] - commodity_data[commodity][
                        '积分'] * quantity
                    knapsack_data[user][commodity] = knapsack_data[user][commodity]+quantity
                    return '购买成功'
            else:
                return '您的积分不足'
    elif look_up:
        return store_data
    else:
        return '没有该商品'
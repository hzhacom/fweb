"""
数据验证器
"""

def must_not_int_or_float(value):
    try:
        float(value)
        int(value)
    except (ValueError, TypeError):
        pass
    else:
        raise ValueError("不能是整数或浮点数")
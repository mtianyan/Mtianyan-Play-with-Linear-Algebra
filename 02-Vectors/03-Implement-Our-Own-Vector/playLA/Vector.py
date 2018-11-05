class Vector:

    def __init__(self, lst):
        """构造函数传入数组"""
        self._values = lst

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __repr__(self):
        """系统中怎么显示这个向量，系统调用"""
        return "Vector({})".format(self._values)

    def __str__(self):
        """用户调用时如何显示这个向量"""
        return "({})".format(", ".join(str(e) for e in self._values))

# -*- coding: utf-8 -*-
# 树洞图片生成基础模块
from util.img.img_blender import ImgBlender
from util.img.img_selector import ImgSelector

if __name__ == "__main__":
    contents = {
        'title':'小微树洞·悄悄话',
        'content_send':'\t\t小微你好，我是巴拉巴拉，我想要拉吧拉吧。请问我现在该怎么办呢？',
        'sender':'测试人员',
        'date_send':'2018-01-02',
        'content_reply':"测试数据1213测试数据241231数据测试",
        'replier':"测试人员2",
        'date_reply':'2018-03-21'
    }
    img = ImgBlender(ImgSelector().img, contents)
    img.blend_type_treehole()
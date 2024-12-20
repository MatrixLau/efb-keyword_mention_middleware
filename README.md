# efb-keyword_mention_middleware


更新已加入***充电公众号信息提示功能***，默认打开，可在`keywordmention.py`中`receive_charge_notify`中设置开关，也可自定义公众号及其关键词

更新已加入***丰巢的快递信息通知***，默认打开，可在`keywordmention.py`中`keyword_fengchao`中设置开关


设置在所有对话、群组、私聊中的关键词

关键词一接收，就会在Telegram艾特你

使用方法：

1、把`keywordmention.py`放入EFB目录下的`modules/`中

2、在EFB目录下`profiles/default/config.yaml`文件中添加

```
middlewares:
  - keywordmention.MatrixLauMiddleware
```

3、在`keywordmention.py`中`keywords_group, keywords_private, keywords_all`字典中按照要求添加关键词

提示：可用于实现提示拍一拍、红包消息等


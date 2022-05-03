# efb-keyword_mention_middleware
设置在所有对话、群组、私聊中的关键词

关键词一接收，就会在Telegram艾特你

使用方法：

1、把`keywordmention.py`放入EFB目录下的`modules/`中

2、在EFB目录下`profiles/default/config.yaml`文件中添加

```
middlewares:
  - keywordmention.ID
```

3、在`keywordmention.py`中`keywords_group, keywords_private, keywords_all`字典中按照要求添加关键词

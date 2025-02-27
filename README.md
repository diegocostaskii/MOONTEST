# Task1：维基百科数据清洗

1.下载中文维基百科数据20250201 dump，解析

这里选择将文件下载地址保存在本地，动态下载所需文件
![image](https://github.com/user-attachments/assets/ede8eafb-445e-4b48-904b-5dc198ee577f)

![image](https://github.com/user-attachments/assets/0693971c-adb3-45e9-af1a-654774974122)

2.清洗并转换为预训练模型所需的文本格式，结果以jsonl格式保存。
需要注意的是 源数据来源于网页 需要处理一下namespace的问题
![image](https://github.com/user-attachments/assets/f110997b-b1db-4b33-b62f-de4ea5575853)

清洗策略为 将数据的复杂符号和一些杂码标记 去掉

![image](https://github.com/user-attachments/assets/45910897-2302-428b-bced-8c225244f2ca)

最终清洗好的数据结果如下图

![image](https://github.com/user-attachments/assets/fe4ba346-1b85-4da2-ac16-81f9da526e5c)

# Task2：FastText 模型训练
1.data prepare
下载并清洗正反数据集，并进行打标

![image](https://github.com/user-attachments/assets/8ab044aa-50ba-4ec9-b931-b7da5c2b830c)


2.train
下载预训练模型 cc.en.300.bin 并用 bin2vec.py进行格式转换为 vec格式
![image](https://github.com/user-attachments/assets/3ee8cfaf-abcb-42b4-b6db-8173a36a042f)


模型训练

![image](https://github.com/user-attachments/assets/6fe0ce27-6cff-4852-95bc-d044ec8b1b89)

训练结果

![image](https://github.com/user-attachments/assets/37de2508-e07e-4801-8bdc-f2ce12ed0469)

测试集结果及评估
加载了预训练的英文模型后，整体准确率得到了较大的提升 达到了0.87，recall同上，证明模型有较好的性能

![image](https://github.com/user-attachments/assets/5422dd39-1789-49ba-8cc1-5f9516e91c5f)

预测打标结果

![image](https://github.com/user-attachments/assets/5a197a6c-99a1-4c4b-a37b-65feeebe30ea)






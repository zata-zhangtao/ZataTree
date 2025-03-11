---
title: transformers
description: ""
date: 2025-03-10T15:14:03+08:00
# image: images/index/index.png
categories:
    - DeepLearning
tags:
    - 框架
---



## FQA

###  在进行Tokenizer的时候报错：TypeError: TextEncodeInput must be Union[TextInputSequence, Tuple[InputSequence, InputSequence]]
有时候是由于dataset有问题，可以把Tokenizer的batched设置为False，然后看看具体的那个输入出问题，我碰到的问题是dataset中有None，使用过滤器
dataset = dataset.filter(lambda x: x["review"] is not None and x["review"] != "")

###  经常无法连接到huggingface，导致无法下载模型和数据
描述：OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like Langboat/bloom-1b4-zh is not the path to a directory containing a file named config.json.
Checkout your internet connection or see how to run the library in offline mode at 'https://huggingface.co/docs/transformers/installation#offline-mode'.

- 解决方法： 使用https://hf-mirror.com/ 镜像网址下载模型和数据
https://hf-mirror.com/   镜像网址以及使用教程

上面的教程提供了很多种下载方式，但是我实际使用下来觉得还是hfd的方式最好用，下面是hfd的使用方式

Ubuntu 系统
```py
# 更新仓库
apt-get update 

# 安装 aria2
apt install aria2

# 安装jp
apt install jp

# 下载hfd.sh
wget https://hf-mirror.com/hfd/hfd.sh

# 设置所有用户都可以使用
chmod a+x hfd.sh

# 设置环境变量
export HF_ENDPOINT=https://hf-mirror.com

# 下载模型
#（注意，下载之前最好cd到自己想要的目录下面，这里演示gpt2，比如你想要下载Langboat/bloom-1b4-zh，就把gpt2替换掉，
# 该命令会在当前目录下面创建一个bloom-1b4-zh的文件夹）
./hfd.sh gpt2

# 下载数据集
# （同下载模型一样）
./hfd.sh wikitext --dataset
```

### 什么是预训练，预训练和训练的区别
预训练是让模型学习到一种通用的表征，往往来说标注数据是非常珍贵的，而实际上许多任务之间是有共性的，可以进行迁移学习。


ref：
https://blog.csdn.net/weixin_45325693/article/details/132084298
https://cloud.tencent.com/developer/article/2303090





## transforemers框架基础入门
参考：
https://blog.csdn.net/qq_44665283/article/details/133967426




### transformers库
- AutoTokenizer
Transformers基本组件（一）快速入门Pipeline、Tokenizer、Model
Transformers环境可以参考：AutoDL平台Transformers环境搭建

###  基础组件Pipeline
1.1 简介
为了更加方便的使用预训练模型，Transformers提供了pipeline函数，该函数封装了模型及对应的数据前处理与后处理工工作，无需我们关注内部细节，只需要指定pipeline的任务类型并输入对应的文本，即可得到我们想要的答案，做到了真正的开箱即用。
目前，pipeline中支持的任务类型包括：
情感分析（sentiment-analysis）：对给定的文本分析其情感极性
文本生成（text-generation）：根据给定的文本进行生成
命名实体识别（ner）：标记句子中的实体
阅读理解（question-answering）：给定上下文与问题，从上下文中抽取答案
掩码填充（fill-mask）：填充给定文本中的掩码词
文本摘要（summarization）：生成一段长文本的摘要
机器翻译（translation）：将文本翻译成另一种语言
特征提取（feature-extraction）：生成给定文本的张量表示
1.1 Pipeline常见API
1. 查看Pipeline支持的任务类型
from transformers.pipelines import SUPPORTED_TASKS

import warnings
warnings.filterwarnings("ignore")


for index,(k, v) in enumerate(SUPPORTED_TASKS.items()):
    print(index + 1,'\t', k, '\t', v)



输出：
[图片]
2. Pipeline的创建与使用方式
- 根据任务类型直接创建Pipeline,默认都是英文的模型
from transformers import pipeline

# 注意：需要魔法流量才能下载相关模型
pipe = pipeline("text-classification")
pipe("very good!")

输出： 
  [{'label': 'POSITIVE', 'score': 0.9998525381088257}]

- 指定任务类型，再指定模型，创建基于指定模型的Pipeline
# pipe = pipeline("text-classification", model="uer/roberta-base-finetuned-dianping-chinese")

# 模型地址 https://huggingface.co/models
# 此模型下载地址：https://huggingface.co/uer/roberta-base-finetuned-dianping-chinese/tree/main
# 这里因为网络问题，先离线下载【pytorch_model.bin、vocab.txt等文件】，然后加载

model_path = '/root/autodl-fs/models/roberta-base-finetuned-dianping-chinese'
pipe = pipeline("text-classification", model=model_path)

pipe("我觉得不太行！") 

# [{'label': 'negative (stars 1, 2 and 3)', 'score': 0.9735506772994995}]

- 预先加载模型，再创建Pipeline
# 这种方式，必须同时指定model和tokenizer
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

pipe("我觉得不太行！") 
# [{'label': 'negative (stars 1, 2 and 3)', 'score': 0.9735506772994995}]


3. 使用GPU进行推理
# 默认是在cpu进行推理
print(pipe.model.device) # device(type='cpu')

import torch
import time
times = []
for i in range(100):
    torch.cuda.synchronize()
    start = time.time()
    pipe("我觉得不太行！")
    torch.cuda.synchronize()
    end = time.time()
    times.append(end - start)
print(sum(times) / 100)

# 使用GPU进行推理
pipe = pipeline("text-classification", model=model_path, device=0)

print(pipe.model.device) # device(type='cuda', index=0)
import torch
import time
times = []
for i in range(100):
    torch.cuda.synchronize()
    start = time.time()
    pipe("我觉得不太行！")
    torch.cuda.synchronize()
    end = time.time()
    times.append(end - start)
print(sum(times) / 100)

4. 确定Pipeline的参数
qa_pipe = pipeline("question-answering", model="uer/roberta-base-chinese-extractive-qa")

qa_pipe
# <transformers.pipelines.question_answering.QuestionAnsweringPipeline at 0x1f1eb647880>


# 进入这个类可以查看相关参数
QuestionAnsweringPipeline
[图片]
qa_pipe(question="中国的首都是哪里？", context="中国的首都是北京", max_answer_len=1)

# {'score': 0.00228740437887609, 'start': 6, 'end': 7, 'answer': '北'}


5. Pipeline背后的实现
[图片]

from transformers import AutoTokenizer,AutoModelForSequenceClassification
import torch

# 1、词元化
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

input_text = "我觉得不太行！"
inputs = tokenizer(input_text, return_tensors="pt")

inputs
## {'input_ids': tensor([[ 101, 2769, 6230, 2533,  679, 1922, 6121, 8013,  102]]), 'token_type_ids': tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1]])}
# 2、加载模型，进行预测
res = model(**inputs)
res
## SequenceClassifierOutput(loss=None, logits=tensor([[ 1.7376, -1.8681]], grad_fn=<AddmmBackward0>), hidden_states=None, attentions=None)
logits = res.logits
logits = torch.softmax(logits, dim=-1)
logits
## tensor([[0.9736, 0.0264]], grad_fn=<SoftmaxBackward0>)
# 3、标签映射
pred = torch.argmax(logits).item()
result = model.config.id2label.get(pred)
result
## 'negative (stars 1, 2 and 3)'


2. 基础组件Tokenizer
2.1 Tokenizer简介
在使用神经网络处理自然语言处理任务时，我们首先需要对数据进行预处理，将数据从字符串转换为神经网络可以接受的格式，一般会分为如下几步：

（1）分词：使用分词器对文本数据进行分词（字、字词）；

（2）构建词典：根据数据集分词的结果，构建词典映射（如果采用预训练词向量，词典映射要根据词向量文件进行处理）；

（3）数据转换：根据构建好的词典，将分词处理后的数据做映射，将文本序列转换为数字序列；

（4）数据填充与截断：在以batch输入到模型的方式中，需要对过短的数据进行填充，过长的数据进行截断，保证数据长度符合模型能接受的范围，同时batch内的数据维度大小一致。

在以往的工作中，我们可能会使用不同的分词器，并自行实现构建词典与转换的工作。但是在transformers工具包中，无需再这般复杂，只需要借助Tokenizer模块便可以快速的实现上述全部工作，它的功能就是将文本转换为神经网络可以处理的数据。Tokenizer工具包无需额外安装，会随着transformers一起安装。

2.2 Tokenizer 基本使用

模型下载和保存

[图片]
3. 基础组件Model
3.1 Model简介
常用的模型一般分为三种：自回归模型、自编码模型和序列到序列模型。

自回归模型采用经典的语言模型任务进行预训练，即给出上文，预测下文，对应原始Transformer模型的解码器部分，其中最经典的模型是GPT。由于自编码器只能看到上文而无法看到下文的特点，模型一般会用于文本生成的任务。
自编码模型则采用句子重建的任务进行预训练，即预先通过某种方式破坏句子，可能是掩码，可能是打乱顺序，希望模型将被破坏的部分还原，对应原始Transformer模型的编码器部分，其中最经典的模型是BERT。与自回归模型不同，模型既可以看到上文信息，也可以看到下文信息，由于这样的特点，自编码模型往往用于自然语言理解的任务，如文本分类、阅读理解等。（此外，这里需要注意，自编码模型和自回归模型的唯一区分其实是在于预训练时的任务，而不是模型结构。）
序列到序列模型则是同时使用了原始的编码器与解码器，最经典的模型便是T5。与经典的序列到序列模型类似，这种模型最自然的应用便是文本摘要、机器翻译等任务，事实上基本所有的NLP任务都可以通过序列到序列解决。
模型类型 
常用预训练模型 
适用任务
自回归模型 
CTRL, GPT, GPT-2, Transformer XL    
文本生成
自编码模型
ALBERT, BERT, DistilBERT, RoBERTa
文本分类、命名实体识别、阅读理解
序列到序列模型
BART, T5, Marian, mBART
文本摘要、机器翻译
3.2 Model基本使用
模型加载和保存
from transformers import AutoModel

# 如果本地路径下已经有缓存好的模型文件，可以用以下代码，如果没有，可以看下一行代码
Model = AutoModel.from_pretrained("./bloom-1b4-zh")

# Langboat/bloom-1b4-zh 是huggingface上面模型的名字 cache_dir 参数是模型的缓存位置
Model = AutoModel.from_pretrained("Langboat/bloom-1b4-zh",cache_dir = './model')




[图片]
4. Datasets
huggingface参考文档
CSDN参考文档
1. 加载在线数据集
比如说下面这一个数据集： 直接复制它的名字然后这样就可以加载，
[图片]
[图片]

5. Evaluate
6. Trainer
Trainer模块是基础组件的最后一个模块，它封装了一套完整的在数据集上训练、评估与预测的流程。借助Trainer模块，可以快速启动训练。
Trainer模块主要包含两部分的内容：TrainingArguments与Trainer，前者用于训练参数的设置，后者用于创建真正的训练器，进行训练、评估预测等实际操作。
此外，针对Seq2Seq训练任务，提供了专门的Seq2SeqTrainingArguments与Seq2SeqTrainer，整体与TrainingArguments和Trainer类似，但是提供了专门用于生成的部分参数。
1. TrainingArguments
TrainingArguments中可以配置整个训练过程中使用的参数，默认版本是包含90个参数，涉及模型存储、模型优化、训练日志、GPU使用、模型精度、分布式训练等多方面的配置内容。
一个例子：
train_args = TrainingArguments(output_dir="./checkpoints",      # 输出文件夹
                               per_device_train_batch_size=64,  # 训练时的batch_size
                               per_device_eval_batch_size=128,  # 验证时的batch_size
                               logging_steps=10,                # log 打印的频率
                               evaluation_strategy="epoch",     # 评估策略
                               save_strategy="epoch",           # 保存策略
                               save_total_limit=3,              # 最大保存数
                               learning_rate=2e-5,              # 学习率
                               weight_decay=0.01,               # weight_decay
                               metric_for_best_model="f1",      # 设定评估指标
                               load_best_model_at_end=True)     # 训练完成后加载最优模型


2. Trainer
Trainer中配置具体的训练用到的内容，包括模型、训练参数、训练集、验证集、分词器、评估函数等内容。
当指定完上述对应参数，便可以通过调用train方法进行模型训练；
训练完成后可以通过调用evaluate方法对模型进行评估；
得到满意的模型后，最后调用predict方法对数据集进行预测。
一个例子：
from transformers import DataCollatorWithPadding
trainer = Trainer(model=model,     # 预训练模型
                  args=train_args, # 训练参数
                  train_dataset=tokenized_datasets["train"], # 训练集
                  eval_dataset=tokenized_datasets["test"],   # 验证集
                  data_collator=DataCollatorWithPadding(tokenizer=tokenizer),# DataCollator，填充到一个批次中最大长度，加快填充的速度
                  compute_metrics=eval_metric  # 指标评估的方法
)
7. PEFT模块
PEFT和Lora - CSDN



实战演练

翻墙下载huggingface的模型需要很多流量，可以用国内镜像：模型库首页 · 魔搭社区 (modelscope.cn)
https://blog.csdn.net/qq_44665283/article/details/134088676


文本分类
任务内容总结
任务总结
1. 任务目标
- 任务类型：文本分类（情感分析）。
- 目标：对中文酒店评论进行情感分类，判断评论是“好评”还是“差评”。
- 数据集：使用 ChnSentiCorp_htl_all 数据集，包含酒店评论及其对应的情感标签（0 表示差评，1 表示好评）。
2. 实现过程
- 数据加载与预处理：
  - 从本地或远程加载数据集，并过滤掉无效数据（如空评论）。
  - 将数据集划分为训练集和测试集（90% 训练，10% 测试）。
- 文本编码：
  - 使用 hfl/chinese-macbert-large 的分词器对文本进行编码，设置最大长度为 32，并进行填充和截断。
  - 将标签与编码后的文本数据绑定。
- 模型加载：
  - 加载预训练模型 hfl/chinese-macbert-large，并将其适配为文本分类任务。
- 训练与评估：
  - 使用 Trainer 类进行模型训练，设置优化器、学习率、批量大小等超参数。
  - 在训练过程中，使用 accuracy 和 f1 作为评估指标，并在每个 epoch 结束后保存模型。
  - 训练完成后加载最优模型，并在测试集上进行评估。
- 模型预测：
  - 对单条文本进行预测，输出情感分类结果（好评或差评）。
  - 使用 pipeline 简化预测流程，支持 GPU 加速。
3. 关键步骤
- 数据预处理：
  - 确保数据质量，过滤无效数据。
  - 合理划分训练集和测试集，避免数据泄露。
- 模型选择：
  - 使用 hfl/chinese-macbert-large 作为预训练模型，适合中文文本分类任务。
- 训练优化：
  - 使用 adafactor 优化器，适合大规模模型训练。
  - 冻结 BERT 模型的参数，只训练分类头部分，减少计算开销。
  - 设置梯度累加（gradient_accumulation_steps）和梯度检查点（gradient_checkpointing），优化显存使用。
- 评估与保存：
  - 使用 accuracy 和 f1 作为评估指标，确保模型性能。
  - 在每个 epoch 结束后保存模型，并加载最优模型用于预测。
4. 优化策略
- 梯度累加：通过 gradient_accumulation_steps 减少显存占用，适合在小批量数据上训练大规模模型。
- 梯度检查点：通过 gradient_checkpointing 进一步优化显存使用，适合显存有限的设备。
- 参数冻结：冻结 BERT 模型的参数，只训练分类头部分，加快训练速度并减少过拟合风险。
- 优化器选择：使用 adafactor 优化器，适合大规模模型的训练，减少显存占用。
5. 未来改进方向
- 数据增强：
  - 对训练数据进行增强（如同义词替换、随机删除等），提高模型的泛化能力。
- 超参数调优：
  - 对学习率、批量大小、训练轮数等超参数进行调优，进一步提升模型性能。
- 模型微调：
  - 解冻部分 BERT 层的参数，进行更精细的微调，可能提升模型的表现。
- 更大规模的数据集：
  - 使用更大规模的中文情感分析数据集进行训练，提高模型的泛化能力。
- 多任务学习：
  - 结合其他相关任务（如情感强度预测）进行多任务学习，提升模型的鲁棒性。
- 模型压缩与加速：
  - 使用模型剪枝、量化或蒸馏技术，压缩模型大小并加速推理过程。
6. 总结
- 任务完成情况：
  - 成功实现了中文酒店评论的情感分类任务，能够准确区分“好评”和“差评”。
  - 通过优化训练策略（如梯度累加、参数冻结等），在有限资源下高效完成了模型训练。
- 模型性能：
  - 使用 accuracy 和 f1 作为评估指标，模型在测试集上表现良好。
  - 通过加载最优模型，确保了预测结果的准确性。
- 扩展性：
  - 代码结构清晰，易于扩展和修改，可以适配其他文本分类任务或数据集。
具体代码

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# 加载数据集
if os.path.exists("./ChnSentiCorp_htl_all_saved.csv"):
    dataset = load_dataset("csv", data_files="./ChnSentiCorp_htl_all.csv", split="train")
else :
    dataset = load_dataset("dirtycomputer/ChnSentiCorp_htl_all")
    dataset.to_csv("./ChnSentiCorp_htl_all_saved.csv")
dataset = dataset.filter(lambda x: x["review"] is not None and x["review"] != "")

#划分数据集
datasets = dataset.train_test_split(test_size=0.1)

tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-macbert-large")

def process_function(examples):
    reviews = examples["review"]
    
    # 使用 tokenizer 处理文本
    tokenized_examples = tokenizer(reviews, max_length=32, truncation=True, padding="max_length")
    tokenized_examples["labels"] = examples["label"]
    return tokenized_examples
tokenized_datasets = datasets.map(process_function, batched=True, remove_columns=datasets["train"].column_names)

model = AutoModelForSequenceClassification.from_pretrained("hfl/chinese-macbert-large")


import evaluate
# 在线加载 accuracy 指标
# acc_metric = evaluate.load("accuracy")
# 在线加载 f1 指标
# f1_metric = evaluate.load("f1")


# 经常会网络不太好，也可以使用本地加载的方式
acc_metric = evaluate.load("./metric_accuracy.py")
f1_metirc = evaluate.load("./metric_f1.py")

def eval_metric(eval_predict):
    predictions, labels = eval_predict
    predictions = predictions.argmax(axis=-1)
    acc = acc_metric.compute(predictions=predictions, references=labels)
    f1 = f1_metirc.compute(predictions=predictions, references=labels)
    acc.update(f1)
    return acc
    
    
# 创建TrainingArguments
train_args = TrainingArguments(output_dir="./checkpoints",      # 输出文件夹
                               per_device_train_batch_size=2,   # 训练时的batch_size
                               gradient_accumulation_steps=32,  # *** 梯度累加 ***
                               gradient_checkpointing=True,     # *** 梯度检查点 ***
                               optim="adafactor",               # *** adafactor优化器 *** 
                               per_device_eval_batch_size=4,    # 验证时的batch_size
                               num_train_epochs=1,              # 训练轮数
                               logging_steps=10,                # log 打印的频率
                               evaluation_strategy="epoch",     # 评估策略
                               save_strategy="epoch",           # 保存策略
                               save_total_limit=3,              # 最大保存数
                               learning_rate=2e-5,              # 学习率
                               weight_decay=0.001,              # weight_decay
                               metric_for_best_model="f1",      # 设定评估指标
                               load_best_model_at_end=True
                              )     # 训练完成后加载最优模型
                              
                              
                              
# 创建Trainer
from transformers import DataCollatorWithPadding

# *** 参数冻结 *** 
for name, param in model.bert.named_parameters():
    param.requires_grad = False

trainer = Trainer(model=model, 
                  args=train_args, 
                  tokenizer=tokenizer,
                  train_dataset=tokenized_datasets["train"], 
                  eval_dataset=tokenized_datasets["test"], 
                  data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
                  compute_metrics=eval_metric)

# 模型训练
trainer.train()

# 模型评估
trainer.evaluate(tokenized_datasets["test"])

# 模型预测
trainer.predict(tokenized_datasets["test"])
sen = "我觉得这家酒店不错，饭很好吃！"
id2_label = {0: "差评！", 1: "好评！"}
model.eval()
with torch.inference_mode():
    inputs = tokenizer(sen, return_tensors="pt")
    inputs = {k: v.cuda() for k, v in inputs.items()}
    logits = model(**inputs).logits
    pred = torch.argmax(logits, dim=-1)
    print(f"输入：{sen}\n模型预测结果:{id2_label.get(pred.item())}")
from transformers import pipeline

model.config.id2label = id2_label
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0)
pipe(sen)
metric_accuracy.py
metric_f1.py
实体命名识别
ner.ipynb
seqeval_metric.py
ner.py
1. 相关包及解释
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset


这段代码使用了几个重要的Python库来处理自然语言处理（NLP）任务。下面是对每个包及其作用的解释：

1. **`transformers`**:
   - **`AutoTokenizer`**: 这是一个用于自动加载预训练分词器的类。分词器负责将原始文本转换为模型可以理解的数字形式（如token IDs）。`AutoTokenizer`可以根据模型名称自动选择合适的分词器。
   - **`AutoModelForSequenceClassification`**: 这是一个用于自动加载预训练模型的类，特别适用于序列分类任务（如情感分析、文本分类等）。它会根据模型名称自动选择适合的模型架构。
   - **`Trainer`**: 这是一个高级API，用于简化模型的训练和评估过程。`Trainer`类封装了训练循环、评估、保存模型等功能，使得训练过程更加简洁。
   - **`TrainingArguments`**: 这是一个用于定义训练参数的类。你可以通过它设置学习率、批次大小、训练轮数等超参数。

2. **`datasets`**:
   - **`load_dataset`**: 这是一个用于加载数据集的函数。`datasets`库提供了许多常用的数据集，并且支持从本地文件或远程URL加载数据。`load_dataset`函数可以方便地加载这些数据集，并且通常返回一个`Dataset`对象，可以直接用于训练和评估。

### 代码的大致流程：
1. **加载数据集**：使用`load_dataset`函数加载数据集。
2. **加载分词器**：使用`AutoTokenizer`加载与预训练模型对应的分词器。
3. **加载模型**：使用`AutoModelForSequenceClassification`加载预训练模型。
4. **设置训练参数**：使用`TrainingArguments`定义训练过程中的超参数。
5. **训练模型**：使用`Trainer`类进行模型训练和评估。

这些库的组合使得构建和训练一个NLP模型变得非常简单和高效。
具体代码
import evaluate
from datasets import load_dataset,DatasetDict
from transformers import AutoTokenizer, AutoModelForTokenClassification, TrainingArguments, Trainer, DataCollatorForTokenClassification
import numpy as np
import os
if os.path.exists("./data/ner_data"):
    ner_datasets = DatasetDict.load_from_disk("./data/peoples_daily_ner")
else:
    # os.makedirs("./data/ner_data")
    ner_datasets = load_dataset("peoples_daily_ner",cache_dir="./data",trust_remote_code=True)

label_list = ner_datasets["train"].features["ner_tags"].feature.names
tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-macbert-base")
# 借助word_ids 实现标签映射
def process_function(examples):
    tokenized_exmaples = tokenizer(examples["tokens"], max_length=128, truncation=True, is_split_into_words=True)
    labels = []
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_exmaples.word_ids(batch_index=i)
        label_ids = []
        for word_id in word_ids:
            if word_id is None:
                label_ids.append(-100)
            else:
                label_ids.append(label[word_id])
        labels.append(label_ids)
    tokenized_exmaples["labels"] = labels
    return tokenized_exmaples
tokenized_datasets = ner_datasets.map(process_function, batched=True)
# 对于所有的非二分类任务，切记要指定num_labels，否则就会device错误
model = AutoModelForTokenClassification.from_pretrained("hfl/chinese-macbert-base", num_labels=len(label_list))
# 从网络加载 seqeval 评估指标
seqeval = evaluate.load("seqeval_metric.py")

def eval_metric(pred):
    predictions, labels = pred
    predictions = np.argmax(predictions, axis=-1)

    # 将id转换为原始的字符串类型的标签
    true_predictions = [
        [label_list[p] for p, l in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels) 
    ]

    true_labels = [
        [label_list[l] for p, l in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels) 
    ]

    result = seqeval.compute(predictions=true_predictions, references=true_labels, mode="strict", scheme="IOB2")

    return {
        "f1": result["overall_f1"]
    }
# 配置训练参数
args = TrainingArguments(
    output_dir="models_for_ner",
    per_device_train_batch_size=64,
    per_device_eval_batch_size=128,
    eval_strategy="epoch",
    save_strategy="epoch",
    metric_for_best_model="f1",
    load_best_model_at_end=True,
    logging_steps=50,
    num_train_epochs=1
)
# 创建训练器
trainer = Trainer(
    model=model,
    args=args,
    tokenizer=tokenizer,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    compute_metrics=eval_metric,
    data_collator=DataCollatorForTokenClassification(tokenizer=tokenizer)
)
# 模型训练
trainer.train()

trainer.evaluate(eval_dataset=tokenized_datasets["test"])

from transformers import pipeline
model.config.id2label = {idx: label for idx, label in enumerate(label_list)}
# 如果模型是基于GPU训练的，那么推理时要指定device
# 对于NER任务，可以指定aggregation_strategy为simple，得到具体的实体的结果，而不是token的结果
ner_pipe = pipeline("token-classification", model=model, tokenizer=tokenizer, device=0, aggregation_strategy="simple")
res = ner_pipe("小明在北京上班")
# 根据start和end取实际的结果
ner_result = {}
x = "小明在北京上班"
for r in res:
    if r["entity_group"] not in ner_result:
        ner_result[r["entity_group"]] = []
    ner_result[r["entity_group"]].append(x[r["start"]: r["end"]])

print(ner_result)


模型训练优化方法
RLHF
参考：
https://huggingface.co/blog/zh/rlhf
PPO
在强化学习（Reinforcement Learning, RL）中，**PPO（Proximal Policy Optimization，近端策略优化）** 是一种高效的策略优化算法，广泛应用于强化学习任务中。PPO 在强化学习与人类反馈（RLHF, Reinforcement Learning from Human Feedback）中也扮演了重要角色，尤其是在训练大型语言模型（如 ChatGPT 等）时。

---

1. PPO 的基本概念
PPO 是一种基于策略梯度的强化学习算法，旨在通过优化策略来最大化累积奖励，同时避免更新步长过大导致训练不稳定的问题。它通过限制策略更新的范围，确保新策略不会偏离旧策略太远，从而实现更稳定的训练。

PPO 的核心思想是：
- 限制策略更新幅度：通过引入一个“信任区域”（trust region），防止策略更新过于激进。
- 高效采样和更新：相比其他方法（如 TRPO，Trust Region Policy Optimization），PPO 更加简单且易于实现，同时性能优异。

---

2. PPO 的数学公式
PPO 使用目标函数来优化策略参数 \(\theta\)，其目标函数的形式如下：

(1) 原始目标函数
$$L^{CLIP}(\theta) = \mathbb{E}_t \left[ \min \left( r_t(\theta) A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t \right) \right]$$

其中：
- $$r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}$$是新策略与旧策略的概率比值。
- $$A_t$$ 是优势函数（Advantage Function），衡量某个动作相对于平均表现的好坏。
- $$\epsilon$$ 是一个超参数（通常取值为 0.1~0.2），用于限制概率比值的变化范围。
- $$\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)$$ 是对 $$r_t(\theta)$$ 的裁剪操作，确保其变化范围在 $$[1-\epsilon, 1+\epsilon]$$ 内。

(2) 目标函数的作用
- 当 \(r_t(\theta) A_t\) 超过裁剪范围时，使用裁剪后的值，从而避免策略更新过于激进。
- 这种裁剪机制有效地限制了策略更新的幅度，使得训练更加稳定。

---

3. PPO 在 RLHF 中的应用
在 RLHF 中，PPO 被用来根据人类反馈优化模型的行为。以下是 PPO 在 RLHF 中的主要应用步骤：

(1) 收集人类反馈
- 让人类对模型生成的多个候选输出进行评分或排序。
- 根据评分或排序结果，构建一个奖励模型（Reward Model），用于估计人类对模型输出的偏好。

(2) 定义奖励信号
- 使用奖励模型为每个生成的输出分配一个奖励值 \(R\)。
- 奖励值反映了该输出的质量或符合人类偏好的程度。

(3) 使用 PPO 优化策略
- 将语言模型视为策略 \(\pi_\theta\)，其参数为 \(\theta\)。
- 使用 PPO 算法优化策略参数 \(\theta\)，以最大化奖励信号 \(R\)。
- 在每一轮训练中：
  - 从当前策略 \(\pi_\theta\) 中采样一批数据。
  - 计算奖励值 \(R\) 和优势函数 \(A_t\)。
  - 使用 PPO 的目标函数更新策略参数。

(4) 限制策略更新
- 在更新过程中，PPO 的裁剪机制确保新策略不会偏离旧策略太远，从而避免模型性能突然下降。

---

4. PPO 的优点
- 稳定性：通过裁剪机制限制策略更新幅度，避免训练过程中的剧烈波动。
- 高效性：相比其他方法（如 TRPO），PPO 实现简单，计算效率高。
- 通用性：适用于连续动作空间和离散动作空间的任务。

---

5. 总结
在 RLHF 中，PPO 是一种关键的强化学习算法，用于根据人类反馈优化语言模型的行为。通过结合奖励模型和 PPO 的策略优化能力，可以有效地训练出符合人类偏好的高质量语言模型。



参考：
https://www.bilibili.com/video/BV12bP2e5EDh?t=2574.2

高效微调
BitFit
参考
BitFit介绍 - 知乎
BitFit论文原文

- 基本概念： BitFit是一种稀疏微调方法，其中仅修改模型（或其子集）的bias项。
- 代码源码:
主要代码就这一段
for name, param in model.named_parameters():
    if "bias" not in name:
        param.requires_grad = False
BitFit.py
seqeval_metric.py
import evaluate
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, TrainingArguments, Trainer, DataCollatorForTokenClassification
from datasets import DatasetDict
ner_datasets = DatasetDict.load_from_disk("ner_data")

label_list = ner_datasets["train"].features["ner_tags"].feature.names

tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-macbert-base")
tokenizer(ner_datasets["train"][0]["tokens"], is_split_into_words=True)   # 对于已经做好tokenize的数据，要指定is_split_into_words参数为True

# 借助word_ids 实现标签映射
def process_function(examples):
    tokenized_exmaples = tokenizer(examples["tokens"], max_length=128, truncation=True, is_split_into_words=True)
    labels = []
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_exmaples.word_ids(batch_index=i)
        label_ids = []
        for word_id in word_ids:
            if word_id is None:
                label_ids.append(-100)
            else:
                label_ids.append(label[word_id])
        labels.append(label_ids)
    tokenized_exmaples["labels"] = labels
    return tokenized_exmaples

tokenized_datasets = ner_datasets.map(process_function, batched=True)
# 对于所有的非二分类任务，切记要指定num_labels，否则就会device错误
model = AutoModelForTokenClassification.from_pretrained("hfl/chinese-macbert-base", num_labels=len(label_list))

# %%
sum(param.numel() for param in model.parameters())

# %%
# bitfit
# 选择模型参数里面的所有bias部分

num_param = 0
for name, param in model.named_parameters():
    if "bias" not in name:
        param.requires_grad = False
    else:
        num_param += param.numel()
print(num_param)
# %%
# 这里方便大家加载，替换成了本地的加载方式，无需额外下载
seqeval = evaluate.load("seqeval_metric.py")
# %%
import numpy as np

def eval_metric(pred):
    predictions, labels = pred
    predictions = np.argmax(predictions, axis=-1)

    # 将id转换为原始的字符串类型的标签
    true_predictions = [
        [label_list[p] for p, l in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels) 
    ]

    true_labels = [
        [label_list[l] for p, l in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels) 
    ]

    result = seqeval.compute(predictions=true_predictions, references=true_labels, mode="strict", scheme="IOB2")

    return {
        "f1": result["overall_f1"]
    }
    

# %% [markdown]
# ## Step6 配置训练参数

# %%
args = TrainingArguments(
    output_dir="models_for_ner",
    per_device_train_batch_size=64,
    per_device_eval_batch_size=128,
    eval_strategy="epoch",
    save_strategy="epoch",
    metric_for_best_model="f1",
    load_best_model_at_end=True,
    logging_steps=50,
    num_train_epochs=1
)

# %% [markdown]
# ## Step7 创建训练器

# %%
trainer = Trainer(
    model=model,
    args=args,
    tokenizer=tokenizer,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    compute_metrics=eval_metric,
    data_collator=DataCollatorForTokenClassification(tokenizer=tokenizer)
)

# %% [markdown]
# ## Step8 模型训练

# %%
trainer.train()

# %%
trainer.evaluate(eval_dataset=tokenized_datasets["test"])

# %% [markdown]
# ## Step9 模型预测

# %%
from transformers import pipeline

# %%
# 使用pipeline进行推理，要指定id2label
model.config.id2label = {idx: label for idx, label in enumerate(label_list)}
model.config

# %%
# 如果模型是基于GPU训练的，那么推理时要指定device
# 对于NER任务，可以指定aggregation_strategy为simple，得到具体的实体的结果，而不是token的结果
ner_pipe = pipeline("token-classification", model=model, tokenizer=tokenizer, device=0, aggregation_strategy="simple")

# %%
res = ner_pipe("小明在北京上班")
res

# %%
# 根据start和end取实际的结果
ner_result = {}
x = "小明在北京上班"
for r in res:
    if r["entity_group"] not in ner_result:
        ner_result[r["entity_group"]] = []
    ner_result[r["entity_group"]].append(x[r["start"]: r["end"]])

ner_result

# %%

# %%


Prompt Tuning
参考：
Prompt-Tuning、P-Tuning和Prefix-Tuning高效微调
huggingface - prompt-Tuning

主要代码：


model = AutoModelForCausalLM.from_pretrained("./bloom-1b4-zh")
# 上面和其他训练任务一样，包括分词器，数据处理这些
...

from peft import PromptTuningConfig, get_peft_model, TaskType, PromptTuningInit

# Soft Prompt
# config = PromptTuningConfig(task_type=TaskType.CAUSAL_LM, num_virtual_tokens=10)
# config
# Hard Prompt
config = PromptTuningConfig(task_type=TaskType.CAUSAL_LM,
                            prompt_tuning_init=PromptTuningInit.TEXT,
                            prompt_tuning_init_text="下面是一段人与机器人的对话。",
                            num_virtual_tokens=len(tokenizer("下面是一段人与机器人的对话。")["input_ids"]),
                            tokenizer_name_or_path="Langboat/bloom-1b4-zh")
model = get_peft_model(model, config)
# 打印可训练参数数量
model.print_trainable_parameters()

....
# 下面和其他训练任务一样
简介： Prompt-Tuning 高效微调只会训练新增的Prompt的表示层，模型的其余参数全部固定；
        新增的 Prompt 内容可以分为 Hard Prompt 和 Soft Prompt 两类；
        Soft prompt 通常指的是一种较为宽泛或模糊的提示，允许模型在生成结果时有更大的自由度，通常用于启发模型进行创造性的生成；
        Hard prompt 是一种更为具体和明确的提示，要求模型按照给定的信息生成精确的结果，通常用于需要模型提供准确答案的任务；
        Soft Prompt 在 peft 中一般是随机初始化prompt的文本内容，而 Hard prompt 则一般需要设置具体的提示文本内容；
[图片]
Prompt-Tuning（提示微调）是自然语言处理（NLP）领域中一种用于调整预训练语言模型的技术，以下从其定义、原理、优势、应用场景等方面进行详细介绍：
定义
Prompt-Tuning是一种在预训练语言模型基础上，通过设计和优化输入提示（prompt）来引导模型生成特定任务输出的方法，它不需要对模型的主体结构进行大规模修改或重新训练，而是通过调整输入的提示信息来适配不同的任务或领域。
原理
- 利用预训练模型的知识：预训练语言模型在大规模数据上进行训练，已经学习到了丰富的语言知识和模式。Prompt-Tuning就是基于这些已有的知识，通过巧妙设计提示，让模型能够将这些知识应用到具体的任务中。
- 提示的构建与嵌入：将精心设计的提示文本与原始输入文本进行组合或嵌入，形成新的输入。提示文本通常包含与任务相关的关键词、引导语句或特定的格式，以引导模型生成符合任务要求的输出。例如，在情感分类任务中，提示可能是“请判断以下文本表达的情感是积极还是消极：[原始文本]”。
- 微调过程：在将带有提示的输入提供给模型后，通过微调（fine-tuning）技术，对模型的一些参数进行小幅度调整，以使模型更好地适应特定任务。微调过程通常使用任务相关的标注数据，通过最小化损失函数来更新模型参数，让模型学会根据提示和输入生成正确的输出。
优势
- 高效性：相比传统的对整个模型进行重新训练的方法，Prompt-Tuning只需要调整少量参数，大大减少了计算资源和时间成本，能够快速适应新任务或新领域。
- 灵活性：可以根据不同的任务和需求，灵活设计各种提示，无需修改模型的底层结构，就能让模型适用于多种自然语言处理任务，如文本分类、问答、生成等。
- 数据利用效率高：在标注数据有限的情况下，Prompt-Tuning能够充分利用预训练模型的先验知识，通过合理的提示设计，更好地利用少量标注数据进行微调，提高模型在特定任务上的性能。
应用场景
- 文本分类任务：如新闻分类、情感分类等。通过设计合适的提示，让模型能够准确判断文本所属的类别。
- 问答任务：可以将问题和相关的上下文与提示相结合，引导模型生成准确的答案。例如在智能客服中，通过提示让模型根据知识库回答用户的问题。
- 文本生成任务：如故事生成、对话生成等。利用提示提供故事的主题、开头或特定的情节要求，让模型生成符合要求的文本内容。
- 信息抽取任务：设计提示来引导模型从文本中抽取特定的信息，如实体、关系等。例如从新闻报道中抽取人物、事件、时间等关键信息。
与其他技术的比较
- 与Fine-Tuning的比较：Fine-Tuning是对整个模型或大部分模型参数进行调整，而Prompt-Tuning主要是通过调整提示和少量与提示相关的参数来适配任务。Fine-Tuning通常需要更多的计算资源和数据，而Prompt-Tuning在效率和灵活性上更具优势，尤其是在低资源场景下表现更好。
- 与Prompt Engineering的比较：Prompt Engineering侧重于设计各种有效的提示来引导模型输出，更关注提示的设计技巧和策略。而Prompt-Tuning不仅包括提示设计，还涉及到对模型参数的微调过程，是一种更系统的利用提示来优化模型性能的方法。

P-Tuning
核心代码
# 上面和其他训练一样，不再解释
....
from peft import PromptEncoderConfig, TaskType, get_peft_model, PromptEncoderReparameterizationType

config = PromptEncoderConfig(task_type=TaskType.CAUSAL_LM, num_virtual_tokens=10,
                             encoder_reparameterization_type=PromptEncoderReparameterizationType.MLP,
                             encoder_dropout=0.1, encoder_num_layers=5, encoder_hidden_size=1024)
model = get_peft_model(model, config)
....
# 上面和其他训练一样，不再解释
简介：
 P-Tuning 是在 Prompt-Tuning的基础上，通过新增 LSTM 或 MLP 编码模块来加速模型的收敛；
[图片]

Prefix-Tuning
主要代码：
...
from peft import PrefixTuningConfig, get_peft_model, TaskType
config = PrefixTuningConfig(task_type=TaskType.CAUSAL_LM, num_virtual_tokens=10, prefix_projection=True)
model = get_peft_model(model, config)
...
简介：
     Prefix-Tuning 会把可训练参数嵌入到整个模型中，即前缀；
        Prefix-Tuning 将多个 prompt vectors 放在每个 multi-head attention 的 key 矩阵和 value 矩阵之前；
[图片]
Lora
主要代码
# 前面代码一样
......
from peft import LoraConfig, TaskType, get_peft_model
config = LoraConfig(task_type=TaskType.CAUSAL_LM, target_modules=".*\.1.*query_key_value", modules_to_save=["word_embeddings"])
model = get_peft_model(model, config)
args = TrainingArguments(
    output_dir="./chatbot",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    logging_steps=10,
    num_train_epochs=1
)
trainer = Trainer(
    model=model,
    args=args,
    tokenizer=tokenizer,
    train_dataset=tokenized_ds,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True),
)
# 模型去训练微调
trainer.train()
# 模型合并
p_model = PeftModel.from_pretrained(model, model_id="./chatbot/checkpoint-500/")
merge_model = p_model.merge_and_unload()

.......
#后面代码一样
简介：
LoRA 的核心思想
只调整模型的一小部分，而不是整个模型 。
具体来说：
- 大模型的参数矩阵是非常大的，比如一个矩阵可能有 1000x1000 个参数。
- LoRA 假设：在微调时，模型的变化其实可以用一个低秩矩阵 来近似表示。
  - “低秩”是什么意思呢？就是这个矩阵可以用两个更小的矩阵相乘来代替。比如，原来 1000x1000 的矩阵，可以用 1000x4 和 4x1000 的两个小矩阵代替。
  - 这样做的好处是：只需要训练这两个小矩阵，而不用动原来的 1000x1000 大矩阵。

---
LoRA 的工作流程
1. 冻结原模型 ：保持大模型的原始参数不变，不进行任何修改。
2. 添加低秩矩阵 ：在模型的关键部分（比如注意力机制中的权重矩阵）旁边，插入两个小矩阵。
3. 训练小矩阵 ：只训练这两个小矩阵，而不是整个模型。
4. 推理时合并 ：在实际使用时，可以将小矩阵和原矩阵结合起来，恢复成一个完整的模型。主要就是 $W_new = W+\deltaW = W + A·B$ 

---
LoRA 的优点
- 节省存储空间 ：只需要保存小矩阵，而不是整个模型。
- 节省计算资源 ：只训练小矩阵，比训练整个模型快得多。
- 灵活性高 ：可以为不同的任务训练不同的小矩阵，而不需要重新加载整个模型。
[图片]
参考
https://zhuanlan.zhihu.com/p/639229126

QLora
QLora([3])，本质上其就是Lora。只是对基座模型做了四比特量化，在此基础之上训练Lora的适配模型，只需要原来四分之一的显存。24G的显存，就可以精调33B的基座。据说其精心设计的FP4量化方法下，基座模型的效果损失很小，很是牛逼。另，QLora建议对所有的matrix multiplication都做低秩适配。
[图片]
ia3
[图片]

[图片]


....
from peft import IA3Config, TaskType, get_peft_model
config = IA3Config(task_type=TaskType.CAUSAL_LM)
model = get_peft_model(model, config)
....
# 后面和Lora一样，需要合并模型
Peft 微调自定义模型
暂时无法在飞书文档外展示此内容
主要代码：
# 自定义网络
net1 = nn.Sequential(
    nn.Linear(10, 10),
    nn.ReLU(),
    nn.Linear(10, 2)
)
# 查看网络有哪些参数
for name, param in net1.named_parameters():
    print(name)
#>>>0.weight
#>>>0.bias
#>>>2.weight
#>>>2.bias

# 配置Lora调整什么参数
config = LoraConfig(target_modules=["0"])

# 加载模型
model1 = get_peft_model(net1, config)
。。。
# 后面代码和其他一样
Peft 还有多适配器加载和切换以及禁用适配器的功能，可以查看完整代码

参考：
https://www.bilibili.com/video/BV1YH4y1o7rg?t=122.6
模型量化
半精度训练
主要难度在于构造Tokenizer，把自己的数据构造成目标模型的input格式


使用LLama2模型
[图片]
[图片]
llama2tokenizer 有点不一样，对齐要设置成right，如果使用默认的left可能会在loss上面出问题
有时候llama2 训练会报错，需要开启 model.enable_input_require_grads()


参考：
https://www.bilibili.com/video/BV1CB4y1R78v
https://www.bilibili.com/video/BV1U94y157NN

使用chatGLM3模型

暂时无法在飞书文档外展示此内容
暂时无法在飞书文档外展示此内容

4bit量化与QLoRA
[图片]
[图片]

参考：
https://www.bilibili.com/video/BV1aw411M7Cv


TensorRT框架
参考：
https://blog.csdn.net/kunhe0512/article/details/137065234
分布式训练
1. 可能会遇到导入apex包错误的问题，进入Transformers库里注释掉就行了
2. 可能会遇到导入config.json保存， 需要使用BertTokenizer和BertForSequenceClassification加载
[图片]

[图片]
参考：
https://www.bilibili.com/video/BV1cK4y1z7Mv?t=816.9

DataParallel


[图片]
[图片]
参考
https://www.bilibili.com/video/BV1qN4y1n7iG
Distributed DataParallel

[图片]
[图片]
[图片]

参考：
https://www.bilibili.com/video/BV1wS421w7ug?t=18.1

Accelerate库
[图片]
ref：
https://www.bilibili.com/video/BV12Z421t74R?t=1700.6

Deepspeed
[图片]
[图片]
[图片]
[图片]
[图片]
[图片]
[图片]


Megatron

大模型接口调用开发框架
Langchain
[图片]


ref：
Bili 教程
Langchain官网介绍

Dify.AI
[图片]
Ref:
https://blog.csdn.net/qq_44696532/article/details/135766356
开源项目
Qwen - chat
模型部署
1. 下载源码    项目地址：https://github.com/QwenLM/Qwen

git clone https://github.com/QwenLM/Qwen.git
2. 配置环境   
  - 虚拟环境
  - 安装相关的库
pip install -r requirements.txt    
3.  去modelspace或者github下面模型文件
[图片]
git lfs install  # 首先需要确保git lfs已经安装，安装方式：apt-get install git-lfs
git clone https://www.modelscope.cn/qwen/Qwen-1_8B-Chat.git


4. 修改web_demo.py中的模型文件地址，然后运行  python web_demo.py
[图片]

注意，可能碰到问题：
[图片]
这个问题是由于安装的库不对导致的
模型微调
1. 找到对应的数据集
这里使用的是法律的数据集：https://modelscope.cn/datasets/Robin021/DISC-Law-SFT/files
[图片]
2. 在Qwen的文件里面新建一个Data文件夹
[图片]
3. 使用脚本把数据重新处理
import json
json_data = []
with open('DISC-Law-SFT-Triplet-released.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        json_data.append(json.loads(line))

template = []

for idx, data in enumerate(json_data):
    conversation = [
        {
            "from": "user",
            "value": data['input']
        },
        {
            "from": "assistant",
            "value": data['output']
        }
    ]
    template.append({
                     "id":f"identity_{idx}",
                     "conversations": conversation
                     })
    
print(len(template))
print(json.dumps(template[2], indent=2, ensure_ascii=False))
output_file = 'DISC-train-data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(template, f, indent=2, ensure_ascii=False)
print(f"Data saved to {output_file}")
[图片]
4. 安装模型训练用的依赖
pip install "peft<0.8.0" deepspeed
注意：可能会安装失败（一般是在Windows系统里面或者没有GPU）
  1. 缺失cpuinfo ： pip install py-cpuinfo
  2. aio.lib 缺失   参考：https://blog.csdn.net/dalaomanzou/article/details/137188431
set DS_BUILD_AIO=0
set DS_BUILD_EVOFORMER_ATTN=0
set DS_BUILD_OPS=0
set DS_BUILD_SPARSE_ATTN=0
pip install deepspeed==0.3.16  # 注意版本，新版本不支持了
[图片]
如果还是会出现问题，就换环境吧
5. 修改微调文件  finetune\finetune_lora_single_gpu.sh 中的MODEL和DATA变量
[图片]
6. 运行 bash  finetune\finetune_lora_single_gpu.sh 就可以开始微调了（这个微调就必须要硬件设备达到，达不到硬件设备是跑不起来的）
[图片]
7. 微调好之后的模型会存储在项目文件夹下的output_qwen文件夹下面，会按照epoch次数存储多个检查点文件夹
[图片]
8. 下一步需要把训练好的lora模型和原始模型合并，这里我写了一个用于合并的代码
# 导入PEFT库中的AutoPeftModelForCausalLM类，用于加载和合并模型
from peft import AutoPeftModelForCausalLM

# 设置adapter模型的路径
path_to_adapter = "/openbayes/home/20250121-Qwen/Qwen-main/output_qwen/checkpoint-1000"
# 设置合并后模型的保存路径
new_model_path = "/openbayes/home/20250121-Qwen/Qwen-main/law_model-chat"  # load model

# 加载adapter模型，设置device_map为auto自动分配设备，允许使用远程代码，并设置为评估模式
model = AutoPeftModelForCausalLM.from_pretrained(path_to_adapter, device_map="auto",trust_remote_code=True).eval()
# 合并adapter和基础模型
merged_model = model.merge_and_unload()

# 保存合并后的模型，设置最大分片大小为2048MB，使用安全序列化
merged_model.save_pretrained(new_model_path,max_shard_size="2048MB",safe_serialization=True)

# 保存分词器
# 导入AutoTokenizer用于处理分词
from transformers import AutoTokenizer
# 从adapter模型路径加载分词器，允许使用远程代码
tokenizer = AutoTokenizer.from_pretrained(path_to_adapter,trust_remote_code=True)
# 将分词器保存到新模型路径
tokenizer.save_pretrained(new_model_path)
创建merge_model.py,运行代码
[图片]
9. 然后修改推理模型进行推理
[图片]
还是和之前一样，运行python web_demo.py

- 在这个过程中我遇到了一个问题，发现是transformers-stream-generator库的问题，在微调的时候我安装的这个库和推理的时候这个库不一致
[图片]



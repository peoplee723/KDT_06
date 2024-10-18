#####
from collections import Counter
import torch.nn as nn
from typing import Literal
import torch.nn.functional as F

def vectorize(vocab, DF, tokenizer):
    '''
    단어사전을 통해 문장을 수치화하는 함수

    '''
    vector_list=[]
  
    for t in DF:
        token_lists=tokenizer.morphs(t)
        vector_token=[vocab[token] if token in vocab else vocab['<UNK>'] for token in token_lists]
        vector_list.append(vector_token)

    return vector_list

class textCLF(nn.Module):
    def __init__(self, n_vocab, hidden_dim, embedding_dim, n_layers,
                 model_type: Literal['lstm', 'rnn'], dropout=0.5, bidirectional=True):
        super().__init__()

        # 임베딩 층
        # num-> 단어사전의 크기
        self.embedding= nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=embedding_dim,
            padding_idx=0
        )
        if model_type =='rnn':
            self.model=nn.RNN(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True
            )
        elif model_type =='lstm':
            self.model= nn.LSTM(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True
            )
        # 양방향 여부
        if bidirectional:
            self.classifier= nn.Linear(hidden_dim*2, 3)
        else:
            self.classifier= nn.Linear(hidden_dim, 3)
        self.dropout=nn.Dropout(dropout)

    #포워딩
    def forward(self, input):
        embeddings= self.embedding(input)
        output,_= self.model(embeddings)
        last_output=output[:,-1,:]
        last_output=self.dropout(last_output)
        logits=self.classifier(last_output)
        return logits
    

def vectorize2(vocab, DF, tokenizer):
    '''
    단어사전을 통해 문장을 수치화하는 함수

    '''
    vector_list=[]
  
    for t in DF:
        token_lists=tokenizer.morphs(t)
        vector_token=[vocab[token] if token in vocab else vocab['<UNK>'] for token in token_lists]
        vector_list.extend(vector_token)

    return vector_list


def padding2(length, text):
    pad_texts=[]
    # for text in textList:
    #         # 선택 길이> 문장길이 일때
    if length>len(text):
                                        # 남은 텍스트 길이만큼 0으로 채우기
        text=text+[0]*(length-len(text))
    else: # 선택 길이< 문장 길이 일때
        text=text[:length]              # 선택 길이만큼 슬라이싱
    pad_texts.append(text)
    return pad_texts

def predict_mcf2(model, data, result):
    dataTS=data.reshape(1,-1) #torch.FloatTensor(data).reshape(1,-1)
    pre_val=model(dataTS)
    pre_val=F.softmax(pre_val, dim=1)
    num=pre_val.argmax(dim=1)
    print(f'{result[num]}: {max(pre_val[0].detach()):.4f}')
    return f'{result[num]}: {max(pre_val[0].detach()):.4f}'
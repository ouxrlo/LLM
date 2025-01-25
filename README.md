# LLM

## Transformer 모델

## ⭐ 개요

#### 2017년 Vaswani et al.의 논문 "Attention is All You Need"에서 소개됨.
#### 기존의 RNN과 LSTM의 한계를 극복한 모델로, NLP 및 다양한 AI 분야에 혁신을 가져옴.

## ⭐구성 요소

#### 인코더(Encoder) 입력 시퀀스를 처리하여 고차원 표현을 생성.
#### 디코더(Decoder): 인코더에서 생성된 표현을 기반으로 출력 시퀀스를 생성.

## ⭐ Self-Attention
#### 입력 시퀀스 내 각 단어가 다른 단어들과 관계를 맺으며 중요한 정보를 추출.
#### Q(Query), K(Key), V(Value)**를 사용하여 단어 간의 관계를 계산.

### ⭐ Multi-Head Attention
#### 여러 개의 Self-Attention을 동시에 계산하여 정보를 다양하게 추출.

## ⭐ Positional Encoding
#### 순차적인 계산 없이 단어의 순서를 인식하기 위해 입력에 위치 정보를 추가.

## ⭐ 장점
* 병렬 처리: RNN보다 빠르고 효율적.
* 긴 거리 의존성 학습: 긴 문맥도 잘 처리.
* 확장성: 모델 크기를 확장하여 성능을 향상시킬 수 있음.**

## ⭐ 응용 분야
* NLP: 기계 번역, 텍스트 생성, 문서 분류 등.
* 이미지 처리: Vision Transformer (ViT)로 이미지 분류에 적용.
* 음성 처리: 음성 인식 및 생성에 사용.**

## ⭐ 대표적인 Transformer 모델들
* BERT: 양방향 문맥 이해 모델.
* GPT: 텍스트 생성 모델.
* T5: 다양한 NLP 작업을 처리할 수 있는 모델.**

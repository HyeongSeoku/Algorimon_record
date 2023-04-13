# 10610 - 30

## Description

1. 끝자리는 무조건 0. 즉,0이 하나 이상 있어야 함 . 없으면 => -1 출력
2. 모든 수들을 더해서 3으로 나눌수 있으면 3의 배수가 될 수 있음

---

## 속도 개선

![image](https://user-images.githubusercontent.com/48541850/231233665-205e4f82-ced9-4ba4-bda0-392430e231a4.png)

속도 개선에 있어서 결정적인 역할을 했던 부분은, sorting을 하지 않아도되는 케이스.

즉, 이미 답에서 벗어나는 케이스에 대해서는 sort를 진행하지 않아야 속도 개선을 할 수 있다

---

![image](https://user-images.githubusercontent.com/48541850/231234170-3944d343-7a90-4da2-8268-2f26cd668210.png)

위와 아래 제출의 차이는

#### 위 [84ms]

```py
# ...중략
num_list = list(map(int,read().rstrip()))
if sum(num_list)%3 == 0 and 0 in num_list:
    num_list.sort(reverse=True)
    print("".join(map(str,num_list)))
```

#### 아래 [64ms]

```py
# ...중략
num_list = list(read().rstrip())
if sum(map(int,num_list))%3 == 0 and '0' in num_list:
    num_list.sort(reverse=True)
    print("".join(num_list))
```

# 사다리

수식 한 번에 구할 수 있을 줄 알고 삼각형에 관해 아는 성질을 모조리 대입해봤으나 실패함.

피타고라스의 정리 / 삼각형의 닮음을 이용해 아래와 같은 수식을 구할 수 있음.

![Triangle](https://user-images.githubusercontent.com/33550065/234631179-262bc3d7-b95b-4d91-b363-38b415712740.jpg)

c로 쪼개진 삼각형 안의 두 삼각형들은 닮음이므로

-   $\alpha = cw / q$
-   $\beta = cw / p$

이고, $w$는

$$
w\newline
= \alpha + \beta\newline
= cw / q + cw / p\newline
$$

이므로

$c / p + c / q = 1$이고,\
이를 정리하면 $c = pq / (p + q)$이다.

-   $c = pq / (p + q)$
-   $p = \sqrt{x^2-w^2}$
-   $q = \sqrt{y^2-w^2}$

고로 위 세 식을 통해 범위를 좁혀가며 $w$의 값을 구할 수 있다.

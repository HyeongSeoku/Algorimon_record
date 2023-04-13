
import java.util.*;

/*
입력 받은 정보를 강연일이 짧고 비용이 높은 순으로 우선순위 큐에 담는다
우선순위 큐에서 꺼내면서 수업일수 보다 작은 강연의 값을 더해준다.

놓친부분
- 해당일 안에 처리하면돼서 처리일이 낮은순이 아니라 점수가 높은순으로 정렬을 해야함
- 최대한 늦게 일을 처리하는 과정 필요

ex)
    4
    10 2
    20 2
    30 3
    40 3
    정답 90
 */


class Baejoon2109Time implements Comparable<Baejoon2109Time> {
    private int p;
    private int d;


    public Baejoon2109Time(String[] info) {
        this.p = Integer.parseInt(info[0]);
        this.d = Integer.parseInt(info[1]);
    }

    public int getP() {
        return this.p;
    }

    public int getD() {
        return d;
    }

    @Override
    public int compareTo(Baejoon2109Time time) {
        if (this.getD() != time.getD()) {
            if (this.getD() < time.getD()) {
                return -1;
            } else {
                return 1;
            }
        }
        if (this.getP() > time.getP()) {
            return -1;
        } else {
            return 1;
        }
    }

    @Override
    public String toString() {
        return "Baejoon2109Time [getP : " + getP() + ", getD=" + getD();
    }
}


public class Main {


    public static void main(String[] args) {

        int result = 0;
        int sumCnt = 0;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();  // 버퍼 비우기

        PriorityQueue<Baejoon2109Time> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            pq.add(new Baejoon2109Time(sc.nextLine().split(" ")));
        }

        while (!pq.isEmpty()) {
            Baejoon2109Time time = pq.poll();
            //System.out.println(time.toString());
            if (time.getD() > sumCnt) {
                result += time.getP();
                sumCnt++;
                //System.out.println("갱신" + result);
            }
        }

        System.out.println(result);


    }


    // 배열 프린트 함수
    public static void arrPrint(int[][] matrix) {
        System.out.println("-------------------------");
        for (int i = 0; i < matrix.length; i++) {
            System.out.println(Arrays.toString(matrix[i]));
        }


    }


}







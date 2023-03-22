import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine(); // 버퍼 비우기

        int result = 0;
        int weight = 9;

        HashMap<Character, Integer> alphMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String tempStr = sc.nextLine();
            int power = -1;

            // 입력 받은값들 채워넣기
            for (int j = tempStr.length()-1; j >= 0; j--) {
                alphMap.put(tempStr.charAt(j), alphMap.getOrDefault(tempStr.charAt(j), 0) + power);
                power *= 10;
            }
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>();

        // 정렬하기
        for (Character key : alphMap.keySet()) {
            heap.add(alphMap.get(key));
        }

        // 나온순서대로 순서대로 곱해주기
        while (!heap.isEmpty()) {
            result += -heap.poll() * weight--;
        }

        System.out.println(result);

    }
}
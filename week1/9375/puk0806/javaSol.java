import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {

            int m = sc.nextInt();
            if (m == 0) {
                System.out.println("0");
                continue;
            }

            int result = 1;
            HashMap<String, Integer> clothesMap = new HashMap<>();
            sc.nextLine(); // 버퍼 비우기
            for (int j = 0; j < m; j++) {

                String[] clothesInfo = sc.nextLine().split(" ");
                clothesMap.put(clothesInfo[1], clothesMap.getOrDefault(clothesInfo[1], 0) + 1);
            }

            for (String key : clothesMap.keySet()) {
                int tempInt = clothesMap.get(key);
                result *= tempInt + 1;
            }
            System.out.println(result - 1);
        }

    }
}
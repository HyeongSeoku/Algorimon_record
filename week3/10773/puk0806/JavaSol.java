import java.util.*;
/**
Stack에 0이 아니면 넣어주고 0일 경우에 Stack에서 꺼내준다.
 */


public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = 0;

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            int m = sc.nextInt();
            if (m == 0) {
                stack.pop();
            } else {
                stack.add(m);
            }
        }

        while (!stack.isEmpty()) {
            result += stack.pop();
        }

        System.out.println(result);

    }
}







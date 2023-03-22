import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String num = sc.nextLine();
        int changecnt = 0;

        // 변화한 수 체크하기 
        for (int i = 1; i < num.length(); i++) {
            if (num.charAt(i - 1) != num.charAt(i)) ++changecnt;
        }

        // 변화한 수 나누고 올림처리
        System.out.println((int) Math.ceil((double) changecnt / 2));
    }
}
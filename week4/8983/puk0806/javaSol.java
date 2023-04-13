

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/*
풀이 :
- 모든 동물들을 x축이 가장 가까운 사로를 확인하며 사냥 가능한 동물의 수를 파악함
*/

public class Main {

    public static void main(String[] args) throws IOException {

        int result = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] MNL = br.readLine().split(" ");
        int m = Integer.parseInt(MNL[0]);
        int n = Integer.parseInt(MNL[1]);
        int l = Integer.parseInt(MNL[2]);

        int[] shotList = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(shotList);

        String[] animalInfo;
        for (int i = 0; i < n; i++) {
            animalInfo = br.readLine().split(" ");
            int absNum = searchApproxIdxAbs(shotList, Integer.parseInt(animalInfo[0]));
            if (l >= absNum + Integer.parseInt(animalInfo[1])) {
                result += 1;
            }

        }

        System.out.println(result);


    }

    public static int searchApproxIdxAbs(int[] numList, int target) {

        int start = 0;
        int end = numList.length - 1;


        while (start <= end) {
            int mid = (start + end) / 2;
            // 찾은 경우 중간점 인덱스 반환
            if (numList[mid] == target) {
                // return mid;
                return 0;
            } else if (numList[mid] > target) end = mid - 1;
            else start = mid + 1;
        }


        if (start < 0) start = 0;
        if (end < 0) end = 0;
        if (start >= numList.length) start = numList.length - 1;
        if (end >= numList.length) end = numList.length - 1;

        return Math.abs(numList[start] - target) > Math.abs(numList[end] - target) ? Math.abs(numList[end] - target) : Math.abs(numList[start] - target);
        // return Math.abs(numList[start] - target) > Math.abs(numList[end] - target) ? end : start;

    }


}







import java.util.*;

/*
아이디어
5번만 슬라이딩 가능하니 4방향 4*4*4*4*4 모두 진행해도 1024번 바께 안돼서 완전 탐색해도 괜찮다고 생각함

주의 사항
똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.

풀의
모든 슬라이드 경우의 수를 진행한다.
슬라이드 진행후 가장 최대값을 확인하며 갱신해준다.
*/

public class Main {


    public static int n;
    public static int[][] blockMatrix;
    public static void main(String[] args) {

        int result = 0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        blockMatrix = new int[n][n];

        sc.nextLine();
        // 배열 입력받기
        for (int i = 0; i < n; i++) {
            blockMatrix[i] = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        // 5번만 실행하니 4*4*4*4*4 해도 1024 바께 안돼서 완전 탐색 진행
        for (int i1 = 0; i1 < 4; i1++) {
            int[][] tempMatrix1 = deepClone(blockMatrix);
            slideMatrix(i1, tempMatrix1);
            for (int i2 = 0; i2 < 4; i2++) {
                int[][] tempMatrix2 = deepClone(tempMatrix1);
                slideMatrix(i2, tempMatrix2);
                for (int i3 = 0; i3 < 4; i3++) {
                    int[][] tempMatrix3 = deepClone(tempMatrix2);
                    slideMatrix(i3, tempMatrix3);
                    for (int i4 = 0; i4 < 4; i4++) {
                        int[][] tempMatrix4 = deepClone(tempMatrix3);
                        slideMatrix(i4, tempMatrix4);
                        for (int i5 = 0; i5 < 4; i5++) {
                            int[][] tempMatrix5 = deepClone(tempMatrix4);
                            int tempMaxNum = slideMatrix(i5, tempMatrix5);
                            if (result < tempMaxNum) {
                                result = tempMaxNum;
                            }
                        }
                    }
                }
            }
        }


        System.out.println(result);

    }

    // 블록 슬라이딩 시키기
    public static int slideMatrix(int type, int[][] matrix) {

        int maxNum = 0;

        // 주의 조건 : 움직이는 방향쪽이 먼저 합처진다. 처리안함
        // 상
        if (type == 0) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int z = j + 1; z < n; z++) {
                        if (matrix[z][i] == 0) continue;

                        if (matrix[j][i] == 0) {
                            matrix[j][i] = matrix[z][i];
                            matrix[z][i] = 0;
                        } else {
                            if (matrix[j][i] == matrix[z][i]) {
                                matrix[j][i] += matrix[z][i];
                                matrix[z][i] = 0;
                            }
                            break;
                        }
                    }
                    if (maxNum < matrix[j][i]) maxNum = matrix[j][i];
                }
            }
        }
        // 하
        if (type == 1) {
            for (int i = 0; i < n; i++) {
                for (int j = n - 1; j > 0; j--) {
                    for (int z = j - 1; z >= 0; z--) {
                        if (matrix[z][i] == 0) continue;

                        if (matrix[j][i] == 0) {
                            matrix[j][i] = matrix[z][i];
                            matrix[z][i] = 0;
                        } else {
                            if (matrix[j][i] == matrix[z][i]) {
                                matrix[j][i] += matrix[z][i];
                                matrix[z][i] = 0;
                            }
                            break;
                        }

                    }
                    if (maxNum < matrix[j][i]) maxNum = matrix[j][i];
                }

            }

        }

        // 좌
        if (type == 2) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int z = j + 1; z < n; z++) {
                        if (matrix[i][z] == 0) continue;

                        if (matrix[i][j] == 0) {
                            matrix[i][j] = matrix[i][z];
                            matrix[i][z] = 0;
                        } else {
                            if (matrix[i][j] == matrix[i][z]) {
                                matrix[i][j] += matrix[i][z];
                                matrix[i][z] = 0;
                            }
                            break;
                        }


                    }
                    if (maxNum < matrix[i][j]) maxNum = matrix[i][j];
                }

            }
        }

        // 우
        if (type == 3) {
            for (int i = 0; i < n; i++) {
                for (int j = n - 1; j > 0; j--) {
                    for (int z = j - 1; z >= 0; z--) {

                        if (matrix[i][z] == 0) continue;

                        if (matrix[i][j] == 0) {

                            matrix[i][j] = matrix[i][z];
                            matrix[i][z] = 0;
                        } else {
                            if (matrix[i][j] == matrix[i][z]) {
                                matrix[i][j] += matrix[i][z];
                                matrix[i][z] = 0;
                            }
                            break;
                        }
                    }
                    if (maxNum < matrix[i][j]) maxNum = matrix[i][j];
                }
            }
        }

        return maxNum;

    }


    // 깊은 복사 하기 위한 함수
    public static int[][] deepClone(int[][] matrix) {
        int[][] cloneArr = new int[n][];
        for (int i = 0; i < n; i++) {
            cloneArr[i] = matrix[i].clone();
        }
        return cloneArr;
    }


}







import java.util.*;


public class Main {

    public static int n;
    public static int[][] blockMatrix;

    // 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

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

        // 5번만 실행하니 20*20*4*4*4*4*4 해도 400000번 바께 안돼서 완전 탐색 진행
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
                            if(result<tempMaxNum) {
                                result=tempMaxNum;
                                System.out.println("i1 : "+i1+"  i2 : "+i2+"   i3 : "+i3+"   i4 : "+i4+"  i5 : "+i5);
                                arrPrint(tempMatrix5);
                            };
                        }
                    }
                }
            }
        }


        System.out.println(result);

    }

    // 블록 슬라이딩 시키기
    public static int slideMatrix(int type, int[][] matrix) {
        int nx = dx[type];
        int ny = dy[type];
        int maxNum = 0;


        // 주의 조건 : 움직이는 방향쪽이 먼저 합처진다. 처리안함@!@!@
        // 코드 정리는 나중에
        // 상
        if (type == 0) {
            for (int i = 0; i < n; i++) {
                for (int j = n - 1; j > 0; j--) {
                    if (maxNum < matrix[j][i]) maxNum = matrix[j][i];

                    if(matrix[j + nx][i + ny] ==0){
                        matrix[j + nx][i + ny] = matrix[j][i];
                        matrix[j][i]=0;
                    }else if (matrix[j][i] == matrix[j + nx][i + ny]) {
                        matrix[j + nx][i + ny] *= 2;
                        matrix[j][i] = 0;
                        if (maxNum < matrix[j + nx][i + ny]) maxNum = matrix[j + nx][i + ny];
                        j--;
                    }
                }

            }
        }
        // 하
        if (type == 1) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n - 1; j++) {
                    if (maxNum < matrix[j][i]) maxNum = matrix[j][i];


                    if(matrix[j + nx][i + ny] ==0){
                        matrix[j + nx][i + ny] = matrix[j][i];
                        matrix[j][i]=0;
                    }else if (matrix[j][i] == matrix[j + nx][i + ny]) {
                        matrix[j + nx][i + ny] *= 2;
                        matrix[j][i] = 0;
                        if (maxNum < matrix[j + nx][i + ny]) maxNum = matrix[j + nx][i + ny];
                        j++;
                    }
                }
            }

        }

        // 좌
        if (type == 2) {
            for (int i = 0; i < n; i++) {
                for (int j = n - 1; j > 0; j--) {
                    if (maxNum < matrix[i][j]) maxNum = matrix[i][j];

                    if(matrix[i + nx][j + ny] ==0){
                        matrix[i + nx][j + ny] = matrix[i][j];
                        matrix[i][j]=0;
                    }else if (matrix[i][j] == matrix[i + nx][j + ny]) {
                        matrix[i + nx][j + ny] *= 2;
                        matrix[i][j] = 0;
                        if (maxNum < matrix[i + nx][j+ny]) maxNum = matrix[i + nx][j+ny];
                        j--;
                    }
                }
            }
        }

        // 우
        if (type == 3) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n - 1; j++) {
                    if (maxNum < matrix[i][j]) maxNum = matrix[i][j];

                    if(matrix[i + nx][j + ny] ==0){
                        matrix[i + nx][j + ny] = matrix[i][j];
                        matrix[i][j]=0;
                    }else if (matrix[i][j] == matrix[i + nx][j + ny]) {
                        matrix[i + nx][j + ny] *= 2;
                        matrix[i][j] = 0;
                        if (maxNum < matrix[i + nx][j+ny]) maxNum = matrix[i + nx][j+ny];
                        j++;
                    }
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


    // 배열 프린트 함수
    public static void arrPrint(int[][] matrix) {
        System.out.println("-------------------------");
        for (int i = 0; i < matrix.length; i++) {
            System.out.println(Arrays.toString(matrix[i]));
        }

    }


}







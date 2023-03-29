import java.util.*;


class Baejoon14502Node {

    private int x;
    private int y;


    public Baejoon14502Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }

}

public class Main {

    public static int n, m;
    public static int[][] labaMatrix;

    // 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    public static int dx[] = {-1, 1, 0, 0};
    public static int dy[] = {0, 0, -1, 1};


    public static int bfs(int[][] matrix) {
        Queue<Baejoon14502Node> q = new LinkedList<>();

        int minusCnt = 0;   // 안전지대가 아닌곳

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 바이러스 수
                if (matrix[i][j] == 2) {
                    q.offer(new Baejoon14502Node(i, j));
                    minusCnt++;
                } else if (matrix[i][j] == 1) { // 벽의 수
                    minusCnt++;
                }
            }
        }

        while (!q.isEmpty()) {
            Baejoon14502Node node = q.poll();
            int x = node.getX();
            int y = node.getY();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 공간을 벗어난 경우 무시
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                // 빈 방일 경우 오염시킴
                if (matrix[nx][ny] == 0) {
                    matrix[nx][ny] = 2;
                    minusCnt++;
                    q.offer(new Baejoon14502Node(nx, ny));
                }
            }
        }
        return n * m - minusCnt;

    }


    public static void main(String[] args) {

        int result = 0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        labaMatrix = new int[n][];

        sc.nextLine();
        // 배열 입력받기
        for (int i = 0; i < n; i++) {
            labaMatrix[i] = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        // 최대 64*64*64 백만번이 안돼서 완전 탐색해도 괜찮다고 생각
        // 3개의 기둥을 꼭 안세워도된다고 생각햇는데 문제에 3개의기둥을 세워야 한다고함
        
        int maxIndex = n * m;
//        int[][] tempMatrix = deepClone(labaMatrix);
//        int bfsResult = bfs(tempMatrix);
//        if (result < bfsResult) result = bfsResult;

        for (int i = 0; i < maxIndex; i++) {
            if (labaMatrix[i / m][i % m] != 0) continue;

//            tempMatrix = deepClone(labaMatrix);
//            tempMatrix[i / m][i % m] = 1;
//            bfsResult = bfs(tempMatrix);
//            if (result < bfsResult) result = bfsResult;

            for (int j = i + 1; j < maxIndex; j++) {
                if (labaMatrix[j / m][j % m] != 0) continue;

//                tempMatrix = deepClone(labaMatrix);
//                tempMatrix[i / m][i % m] = 1;
//                tempMatrix[j / m][j % m] = 1;
//
//                bfsResult = bfs(tempMatrix);
//                if (result < bfsResult) result = bfsResult;

                for (int z = j + 1; z < maxIndex; z++) {
                    if (labaMatrix[z / m][z % m] != 0) continue;

                    int [][] tempMatrix = deepClone(labaMatrix);
                    tempMatrix[i / m][i % m] = 1;
                    tempMatrix[j / m][j % m] = 1;
                    tempMatrix[z / m][z % m] = 1;

                    int bfsResult = bfs(tempMatrix);
                    if (result < bfsResult) result = bfsResult;


                }
            }
        }

        System.out.println(result);

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







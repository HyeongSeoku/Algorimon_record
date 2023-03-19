import java.util.*;


class Node {

    private int x;
    private int y;


    public Node(int x, int y) {
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
    public static int[][] tomatoInfoGraph;

    // 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    public static int dx[] = {-1, 1, 0, 0};
    public static int dy[] = {0, 0, -1, 1};


    public static void bfs() {
        Queue<Node> q = new LinkedList<>();

        // 익어 있는 토마토들 넣어주기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tomatoInfoGraph[i][j] == 1) {
                    q.offer(new Node(i, j));
                }
            }
        }


        while (!q.isEmpty()) {

            Node node = q.poll();
            int x = node.getX();
            int y = node.getY();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 공간을 벗어난 경우 무시
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                // 토마토가 없을 경우 무시
                if (tomatoInfoGraph[nx][ny] == -1) continue;
                // 익지 않았거나, 더 짧은 경과일이경우 실행
                if (tomatoInfoGraph[nx][ny] == 0 || tomatoInfoGraph[nx][ny] > tomatoInfoGraph[x][y] + 1) {
                    tomatoInfoGraph[nx][ny] = tomatoInfoGraph[x][y] + 1;
                    q.offer(new Node(nx, ny));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        m = sc.nextInt();
        n = sc.nextInt();

        sc.nextLine();

        tomatoInfoGraph = new int[n][];


        // 입력 받기
        for (int i = 0; i < n; i++) {
            String[] tempTomatoInfos = sc.nextLine().split(" ");
            tomatoInfoGraph[i] = Arrays.stream(tempTomatoInfos).mapToInt(Integer::parseInt).toArray();
        }

        
        bfs();

        boolean falseFlag = false;
        int maxDay = -1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tomatoInfoGraph[i][j] == 0) {
                    falseFlag = true;
                    break;
                }
                if (maxDay < tomatoInfoGraph[i][j]) {
                    maxDay = tomatoInfoGraph[i][j];
                }
            }
            // 안익은게 존재 할때
            if (falseFlag) {
                break;
            }
        }

        if (falseFlag) {
            System.out.println("-1");
        } else {
            System.out.println(maxDay - 1);
        }

    }
}
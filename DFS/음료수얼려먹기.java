package me.shinsunyoung;

import java.io.*;
import java.util.*;

public class 음료수얼려먹기 {
    static int n, m;
    static int[][] map;          // 0: 빈칸(미방문), 1: 벽 또는 방문완료
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    // 반복문 DFS (스택)
    static void dfs(int sx, int sy) {
        Deque<int[]> st = new ArrayDeque<>();

        map[sx][sy] = 1;             // 시작점 방문 표시
        st.push(new int[]{sx, sy});

        while (!st.isEmpty()) {
            int[] cur = st.pop();
            int x = cur[0], y = cur[1];

            // 4방향 탐색
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                // 경계 체크
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                // 벽이거나 이미 방문한 곳
                if (map[nx][ny] == 1) continue;

                map[nx][ny] = 1;         // 방문 표시
                st.push(new int[]{nx, ny});
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];

        // 입력: 0/1 문자열 n줄
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = row.charAt(j) - '0';
            }
        }

        int comp = 0; // 연결된 0 덩어리 개수
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {    // 빈칸(미방문) 발견 시
                    dfs(i, j);
                    comp++;
                }
            }
        }

        System.out.println(comp);
    }
}
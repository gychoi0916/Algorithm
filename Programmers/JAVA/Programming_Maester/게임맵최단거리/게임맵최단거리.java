// 시간 효율성 테스트  통과 못하는 중 ... 


import java.util.LinkedList;
import java.util.Queue;
class Solution {
    class Location {
        int row;

        int col;  
        int distance; 
        public Location(int row,int col,int distance) {
            this.row =row;
            this.col = col;
     

    }
                     
    private int bfs(int[][] maps, Location start) {
        int[][] directs = {{1,0},{0,1},{-1,0},{0,-1}};
        int n = maps.length;
        int m = maps[0]

        q.off er(start);
    
        while(!q.is pty()) {   
            Location tmp = q.poll();
            int  r =  tmp.row, c=tmp.col, d =tmp.distance;
            maps[r][c] = 0 ; 
            for(int[] dir  :  directs) {
                in t dr = r + dir[0];  
                int dc = c+d i r[1];
                if(dr == n-1 && dc == m-1) {
                     return d+1;    
                } 
                if(0 <= dr && dr < n && 0<=dc &&  dc <   m){
                    if(maps[dr][dc] == 1) {
                        q.offer(new Location(dr,dc,d+1));
                    }
                }
            }
     

        return -1;
    }

        int answer = 0;  
        
        Location start = new Location(0,0,1);
        answer = bfs(maps, start);
        return answer;
    }
}
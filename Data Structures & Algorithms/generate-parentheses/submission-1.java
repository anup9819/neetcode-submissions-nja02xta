class Solution {
    public List<String> generateParenthesis(int n) {
     List<String> res = new ArrayList<>();
     StringBuilder ds = new StringBuilder();

     solution(ds, n, n, res);

     return res;   
    }

    public void solution(StringBuilder ds, int open , int closed, List<String> res){
        // if(open < 0 || closed < 0) return;
        if(open == 0 && closed == 0){
            res.add(ds.toString());
            return;
        }
        if(open > 0){
            ds.append('(');
            solution(ds, open - 1, closed, res);
            ds.deleteCharAt(ds.length() - 1);
        }
        if(open < closed){
            ds.append(')');
            solution(ds, open, closed - 1, res);
            ds.deleteCharAt(ds.length() - 1);
        }
    }
}

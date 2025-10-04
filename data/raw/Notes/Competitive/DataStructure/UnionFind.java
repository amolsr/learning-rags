class UnionFind{
        int[] parent;
        UnionFind(int n){
            parent = new int[n];
            for(int i = 0 ; i < n ; i++){
                parent[i] = i;
            }
        }
        
        public int getAbsoluteParent(int i){
            if(parent[i]==i){
                return i;
            }
            parent[i] = getAbsoluteParent(parent[i]);
            return parent[i];
        }
        
        public void unify(int i , int j){
            int parentI = getAbsoluteParent(i);
            int parentJ = getAbsoluteParent(j);
            if(parentI!=parentJ){
                parent[parentJ] = parentI;                
            }
        }
    }

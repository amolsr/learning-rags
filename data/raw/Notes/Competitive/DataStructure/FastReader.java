	//Fast IO class
  class FastReader {
        BufferedReader br; 
        StringTokenizer st; 
        public FastReader() {
        	boolean env=System.getProperty("ONLINE_JUDGE") != null;
        	if(!env) {
        		try {
					br=new BufferedReader(new FileReader("src\\input.txt"));
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				}
        	}
        	else br = new BufferedReader(new InputStreamReader(System.in)); 
        } 
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine()); 
                } 
                catch (IOException  e) {
                    e.printStackTrace(); 
                } 
            } 
            return st.nextToken(); 
        } 
        int nextInt() {
            return Integer.parseInt(next()); 
        } 
        long nextLong() {
            return Long.parseLong(next()); 
        } 
        double nextDouble() {
            return Double.parseDouble(next()); 
        } 
        String nextLine() {
            String str = ""; 
            try {
                str = br.readLine(); 
            } 
            catch (IOException e) {
                e.printStackTrace(); 
            } 
            return str; 
        } 
    }

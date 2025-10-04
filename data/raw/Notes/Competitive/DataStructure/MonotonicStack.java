public static class MonotonicStack {
        Stack<Integer> stack;
        HashMap<Integer,Integer> nextGreaterElementMap;
        
        public MonotonicStack(int[] arr) {
            int length = arr.length;

            stack = new Stack<>();
            nextGreaterElementMap = new HashMap<>();
            
            for(int i=0;i<length;i++) {
                while(!stack.isEmpty() && arr[i]> stack.peek()) {
                    nextGreaterElementMap.put(stack.pop(),arr[i]);    
                } 
                    stack.push(arr[i]);     
            }
            
        }
        
        public int getNextGreaterElement(int lookup) {
           return nextGreaterElementMap.containsKey(lookup)?
               nextGreaterElementMap.get(lookup):-1;
        }
}

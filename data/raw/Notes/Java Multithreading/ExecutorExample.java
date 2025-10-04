import java.util.concurrent.*;

class Producer implements Runnable {
    private final BlockingQueue<Integer> queue;

    public Producer(BlockingQueue<Integer> queue) {
        this.queue = queue;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 10; i++) { // smaller loop for demo
                queue.put(i);  // safe insert
                System.out.println(Thread.currentThread().getName() + " Produced: " + i);
                Thread.sleep(100); // simulate work
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

class Consumer implements Runnable {
    private final BlockingQueue<Integer> queue;

    public Consumer(BlockingQueue<Integer> queue) {
        this.queue = queue;
    }

    @Override
    public void run() {
        try {
            while (true) {
                Integer item = queue.take();  // waits if empty
                System.out.println(Thread.currentThread().getName() + " Consumed: " + item);
                Thread.sleep(150); // simulate work
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

public class ExecutorExample {
    public static void main(String[] args) {
        BlockingQueue<Integer> queue = new LinkedBlockingQueue<>(5); // capacity = 5

        // Create a thread pool
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // Submit multiple producers and consumers
        executor.submit(new Producer(queue));
        executor.submit(new Producer(queue));
        executor.submit(new Consumer(queue));
        executor.submit(new Consumer(queue));

        // Allow tasks to run for a while, then shutdown
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        executor.shutdownNow(); // stop all tasks
    }
}

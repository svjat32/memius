package memius.com.memius40;

import java.util.concurrent.ExecutionException;

/**
 * Created by lexay on 18.11.2017.
 */

public interface OnTaskCompleted {
    void onTaskCompleted() throws ExecutionException, InterruptedException;
}

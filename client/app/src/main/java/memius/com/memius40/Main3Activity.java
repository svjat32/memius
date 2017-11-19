package memius.com.memius40;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.widget.ImageView;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

public class Main3Activity extends AppCompatActivity implements OnTaskCompleted {
    GetMemeTask task;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        GetMemeTask memeTesak = new GetMemeTask(this);
        memeTesak.execute("");
        task = memeTesak;
    }
    @Override
    public void onTaskComleted() throws ExecutionException, InterruptedException {
        JSONObject result = task.get();
        String res ="";
        try {
            res = result.getJSONObject("Container").getString("Meme");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        res = res.substring(2,res.length()-1);
        byte[] decodedString = Base64.decode(res, Base64.DEFAULT);
        Bitmap bitMap = BitmapFactory.decodeByteArray(decodedString, 0, decodedString.length);
        ImageView imageView;
        imageView = (ImageView) findViewById(R.id.imageView);
        imageView.setImageBitmap(bitMap);
    }
}

package memius.com.memius40;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.os.Bundle;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;



import com.mashape.unirest.http.*;
import org.json.*;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        JSONObject answer = new RegistrationTask().execute("");

        setContentView(R.layout.activity_main);
        Button button3;
        button3 = (Button) findViewById (R.id.button3);

    }
    public void clickButton3(View view){
        setContentView(R.layout.activity_registration);
    }
}


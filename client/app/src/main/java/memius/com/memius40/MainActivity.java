package memius.com.memius40;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.os.Bundle;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.TextView;


import com.mashape.unirest.http.*;
import org.json.*;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

import java.util.concurrent.ExecutionException;

public class MainActivity extends AppCompatActivity implements OnTaskCompleted{
    LoginTask task;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //RegistrationTask regTesak = new RegistrationTask(this);
        //regTesak.execute("");
        //task = regTesak;
        setContentView(R.layout.activity_main);
//        Button button3;
//        button3 = (Button) findViewById (R.id.button3);

    }
    public void clickButton3(View view){

        Intent intent = new Intent(this,Main2Activity.class);
        startActivity(intent);
    }
    public void clickButton4(View view){
        EditText login;
        login = (EditText)findViewById (R.id.editText3);
        EditText password;
        password = (EditText)findViewById (R.id.editText4);
        LoginTask logTesak = new LoginTask(this,login,password);
        logTesak.execute("");
        task = logTesak;
    }

    @Override
    public void onTaskCompleted() throws ExecutionException, InterruptedException {
        JSONObject result = task.get();
        TextView text;
        text = (TextView)findViewById (R.id.textView5);
        //text.setText("loh");
        String res = "Failure";
//        TextView textView2;
//        textView2 = (TextView) findViewById(R.id.textView11);
        try {
            res = result.getString("Status");
            text.setText(res);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        if(res.equals("Success")){
            try {
                GlobalVars.sessionID = result.getJSONObject("Container").getString("SessionId");
            } catch (JSONException e) {
                e.printStackTrace();
            }
            Intent intent = new Intent(this,Main3Activity.class);
            startActivity(intent);
        }
        else{
            text.setText("Wrong password or login");
        }
    }
}


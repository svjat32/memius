package memius.com.memius40;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

public class Main2Activity extends AppCompatActivity implements OnTaskCompleted {

    RegistrationTask task;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
//        RegistrationTask regTesak = new RegistrationTask(   this);
//        regTesak.execute("");
//        task = regTesak;


    }
        public void clickButton(View view){

        EditText login;
        login = (EditText)findViewById (R.id.editText6);
        EditText password1;
        password1 = (EditText)findViewById (R.id.editText7);
        EditText password2;
        password2 = (EditText)findViewById (R.id.editText8);


        String p1=password1.getText().toString();
        String p2=password2.getText().toString();
        if (p1.equals(p2)){

            RegistrationTask regTesak = new RegistrationTask(this,login,password1);
            regTesak.execute("");
            task = regTesak;

        }
        else{
            TextView text;
            text = (TextView)findViewById (R.id.textView11);
            text.setText("Wrong password or login");
        }
    }
    @Override
    public void onTaskComleted() throws ExecutionException, InterruptedException {
        JSONObject result = task.get();
        String res = "Failure";
//        TextView textView2;
//        textView2 = (TextView) findViewById(R.id.textView11);
        try {
            res = result.getString("Status");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        if(res.equals("Success")){
            Intent intent = new Intent(this,Main3Activity.class);
            startActivity(intent);
        }
        else{
            TextView text;
            text = (TextView)findViewById (R.id.textView11);
            text.setText("Wrong password or login");
        }
    }
}

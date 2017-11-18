package memius.com.memius40;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import com.mashape.unirest.http.*;
import org.json.*;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

//        try {
//            String url = "http://91.225.131.175:8000/cgi-bin/reg.py";
//            HttpResponse<String> jsonResponse = Unirest.post(url)
//                    .header("content-type", "application/x-www-form-urlencoded")
//                    .body("Username=" + "user" + "&Password=" + "pass" + "&E-mail=" + "email")
//                    .asString();
//
//            String status = jsonResponse.toString();
//            //String status = jsonResponse.getBody().getObject().getString("Status");
//            System.out.println(status);
//        }
//        catch(Exception e) {
//            System.out.println("Error: " + e.toString());
//        }
        new RegistrationTask().execute("");

        setContentView(R.layout.activity_main);
    }
}
